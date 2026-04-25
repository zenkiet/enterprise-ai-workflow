# SKILL: devops-tasks

## Purpose

This skill handles DevOps-related tasks: Docker image builds, Docker Compose updates, Nginx configuration, Jenkins pipeline modifications, environment variable management, and CI/CD changes. It follows the same intake → plan → approve → execute → report workflow as frontend tasks.

**Always go through `task-intake` first. Never execute DevOps changes without an approved plan.**

---

## When to Activate

Activate this skill when the task involves any of the following:

- Docker: `Dockerfile`, `docker-compose.yml`, image builds, container configs
- Nginx: proxy configs, upstream servers, SSL, rate limiting
- Jenkins: `Jenkinsfile`, pipeline stages, build triggers
- GitHub Actions: `.github/workflows/` files
- Environment: `.env` files, secrets management, config maps
- Server: SSH commands, service restarts, log inspection
- CI/CD: deployment scripts, release automation

---

## DevOps Principles (Non-Negotiable)

| Principle                           | Rule                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------ |
| **Never touch production directly** | All changes go through a branch and plan approval                              |
| **Idempotent changes**              | Scripts and configs must be safe to run multiple times                         |
| **Minimal blast radius**            | Change only what the plan specifies — no scope creep                           |
| **Secrets stay secret**             | Never hardcode secrets. Use env vars or secret managers                        |
| **Rollback plan**                   | Every change must have a clear rollback path                                   |
| **Dry-run first**                   | Validate configs before applying (e.g., `nginx -t`, `docker build --no-cache`) |

---

## Step-by-Step Procedure

### Step 1 — Load Context

Before any DevOps task:

1. Identify which project/service is affected
2. Read the project's `Jenkinsfile` to understand current pipeline
3. Read `docker-compose.yml` or `Dockerfile` if relevant
4. Check `.env.example` for expected environment variables
5. Note current service state (running containers, active branches)

```bash
# Check running containers
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Check current Nginx config
nginx -t 2>&1

# Check Jenkins pipeline status (if accessible)
cat Jenkinsfile
```

---

### Step 2 — Docker Tasks

#### Dockerfile Best Practices

```dockerfile
# Always use specific version tags — never :latest
FROM node:20.11-alpine AS builder

# Set working directory
WORKDIR /app

# Copy dependency files first (layer caching)
COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install --frozen-lockfile

# Copy source
COPY . .

# Build
RUN pnpm build

# Production stage — minimal image
FROM nginx:1.25-alpine AS production
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**Rules:**

- Multi-stage builds for frontend projects (builder + production)
- Alpine base images unless specific packages require otherwise
- Pin versions explicitly — no `:latest`
- `.dockerignore` must exist and exclude `node_modules`, `.git`, `dist`
- Non-root user for production containers when possible

#### Docker Compose Updates

```yaml
# docker-compose.yml pattern
version: '3.9'

services:
  [service-name]:
    build:
      context: .
      dockerfile: Dockerfile
      target: production
    image: [image-name]:[tag]
    container_name: [container-name]
    restart: unless-stopped
    ports:
      - "[host-port]:[container-port]"
    environment:
      - NODE_ENV=production
    env_file:
      - .env
    networks:
      - app-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:[port]/health"]
      interval: 30s
      timeout: 10s
      retries: 3

networks:
  app-network:
    driver: bridge
```

**Validation before commit:**

```bash
# Validate compose file
docker compose config

# Test build (no push)
docker build --no-cache -t [image]:[tag] .

# Test compose up (dry run)
docker compose up --dry-run 2>&1 || true
```

---

### Step 3 — Nginx Configuration

#### Standard Proxy Config

```nginx
# /etc/nginx/conf.d/[service].conf
server {
    listen 80;
    server_name [domain];

    # Redirect HTTP to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name [domain];

    ssl_certificate /etc/ssl/certs/[cert].pem;
    ssl_certificate_key /etc/ssl/private/[key].pem;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;

    # Gzip
    gzip on;
    gzip_types text/plain text/css application/json application/javascript;

    location / {
        proxy_pass http://[upstream]:[port];
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 60s;
        proxy_connect_timeout 10s;
    }

    # Health check endpoint
    location /health {
        access_log off;
        return 200 "OK\n";
        add_header Content-Type text/plain;
    }
}
```

**Validation before applying:**

```bash
# Test config syntax
nginx -t

# Reload without downtime (after confirming syntax is valid)
nginx -s reload
```

---

### Step 4 — Jenkins Pipeline

#### Standard Jenkinsfile Pattern

```groovy
// Jenkinsfile
pipeline {
    agent any

    environment {
        NODE_VERSION = '20'
        IMAGE_NAME = '[image-name]'
        REGISTRY = '[registry-url]'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Branch: ${env.GIT_BRANCH}"
            }
        }

        stage('Install') {
            steps {
                sh 'npm install -g pnpm'
                sh 'pnpm install --frozen-lockfile'
            }
        }

        stage('Lint') {
            steps {
                sh 'pnpm lint'
            }
        }

        stage('Test') {
            steps {
                sh 'pnpm test --watch=false --browsers=ChromeHeadless'
            }
            post {
                always {
                    junit 'test-results/**/*.xml'
                }
            }
        }

        stage('Build') {
            steps {
                sh 'pnpm build --configuration=production'
            }
        }

        stage('Docker Build') {
            when {
                branch 'main'
            }
            steps {
                sh "docker build -t ${IMAGE_NAME}:${env.BUILD_NUMBER} ."
                sh "docker tag ${IMAGE_NAME}:${env.BUILD_NUMBER} ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker compose pull'
                sh 'docker compose up -d --remove-orphans'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline succeeded — Build #${env.BUILD_NUMBER}"
        }
        failure {
            echo "❌ Pipeline failed — Build #${env.BUILD_NUMBER}"
        }
        always {
            cleanWs()
        }
    }
}
```

**Rules for Jenkinsfile:**

- `when { branch 'main' }` gates for deploy stages — never deploy from feature branches
- `cleanWs()` in `post.always` — always clean workspace after build
- Use `environment {}` block for all configurable values
- Credentials via `credentials()` helper — never hardcode

---

### Step 5 — GitHub Actions (Alternative to Jenkins)

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install pnpm
        run: npm install -g pnpm

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Lint
        run: pnpm lint

      - name: Test
        run: pnpm test --watch=false --browsers=ChromeHeadless

      - name: Build
        run: pnpm build --configuration=production

      - name: Docker Build & Push
        if: github.ref == 'refs/heads/main'
        run: |
          docker build -t ${{ secrets.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }} .
          docker push ${{ secrets.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
        env:
          IMAGE_NAME: [image-name]
```

---

### Step 6 — Environment Variables

**Rules:**

- Never commit `.env` files — only `.env.example`
- `.env.example` must be kept up to date with all required variables (no values)
- Use `${VARIABLE_NAME}` syntax in configs — never hardcode
- Document each variable with a comment in `.env.example`

```bash
# .env.example template
# Application
NODE_ENV=production
PORT=3000
APP_URL=https://[domain]

# Database
DB_HOST=
DB_PORT=5432
DB_NAME=
DB_USER=
DB_PASSWORD=

# External APIs
API_KEY=
API_SECRET=

# Docker Registry
REGISTRY_URL=
REGISTRY_USERNAME=
REGISTRY_PASSWORD=
```

---

### Step 7 — Validation Checklist

Before handing off to `git-workflow`, run through this checklist:

```bash
# Docker
docker build --no-cache -t [image]:test . && echo "✅ Docker build OK"
docker compose config && echo "✅ Compose config OK"

# Nginx
nginx -t && echo "✅ Nginx config OK"

# Jenkins
# (manual review — no automated validation available)
cat Jenkinsfile | grep -E "stage|steps|when" | head -20

# Environment
diff .env.example .env | grep "^<" | awk '{print $2}' | sort
# (shows variables in .env.example but missing from .env)
```

---

### Step 8 — Report to Slack

After `git-workflow` pushes the branch, send this report:

```
✅ *DevOps task complete!*

📌 *Branch:* \`feature/[task-id]-[description]\`
🔧 *Changes made:*
  - [File changed]: [what was changed and why]

✔️ *Validation:*
  - Docker build: ✅ passed
  - Nginx config: ✅ valid
  - Compose config: ✅ valid

⚠️ *Manual steps required before deploy:*
  1. [Any manual step — e.g., "Update .env on server with new variable X"]
  2. [e.g., "Restart Nginx after merging: nginx -s reload"]

📝 *Rollback:*
  - [How to revert if something goes wrong]
```

---

## Error Handling

| Situation                     | Action                                                     |
| ----------------------------- | ---------------------------------------------------------- |
| `docker build` fails          | Show error output. Ask Kiet if he wants to debug or abort. |
| `nginx -t` fails              | Show syntax error. Fix and re-validate before committing.  |
| Missing env variable          | Note in report under "Manual steps required".              |
| Jenkins pipeline syntax error | Use `jenkins-linter` or validate via Jenkins Blue Ocean.   |
| Compose port conflict         | Check `docker ps` for conflicting ports. Report to Kiet.   |

---

## Memory

After each DevOps task, log to `memory/YYYY-MM-DD.md`:

```markdown
## [HH:MM] DevOps — [Task Title]

- Branch: feature/[task-id]-[description]
- Files changed: [list]
- Validation: passed / failed ([details])
- Manual steps noted: yes/no
- Notes: [anything unusual — port conflicts, missing vars, etc.]
```
