#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
DEST_DIR="$HERMES_HOME/skills/enterprise-ai-workflow"

mkdir -p "$DEST_DIR"

install_skill() {
  local name="$1"
  local description="$2"
  local src="$ROOT_DIR/skills/$name/SKILL.md"
  local dest="$DEST_DIR/$name"

  if [[ ! -f "$src" ]]; then
    echo "Missing skill source: $src" >&2
    return 1
  fi

  mkdir -p "$dest"

  if head -n 1 "$src" | grep -q '^---$'; then
    cp "$src" "$dest/SKILL.md"
  else
    {
      echo "---"
      echo "name: $name"
      echo "description: $description"
      echo "version: 1.0.0"
      echo "category: enterprise-ai-workflow"
      echo "---"
      echo
      cat "$src"
    } > "$dest/SKILL.md"
  fi

  echo "Installed skill: $name -> $dest/SKILL.md"
}

install_skill "task-intake" "Requirement intake, clarification, plan generation, and approval workflow for ZenAgent engineering tasks."
install_skill "guideline" "Pre-flight and execution checkpoints for minimal, surgical, goal-driven agent work."
install_skill "angular-scaffold" "Angular Smart/Dumb component scaffold workflow following Blogic Systems frontend standards."
install_skill "git-workflow" "Branch, commit, push, and report workflow for approved ZenAgent changes."
install_skill "devops-tasks" "Docker, Jenkins, Nginx, GitHub Actions, and infrastructure task workflow with rollback planning."

echo
echo "Done. Verify with: hermes skills list | grep -E 'task-intake|angular-scaffold|git-workflow|devops-tasks|guideline'"
