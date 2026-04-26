# Hermes Skill Migration

The canonical workflow skills live in the repository root under `skills/`.

Run:

```bash
./scripts/setup-hermes.sh
```

This installs/updates the skills into:

```text
~/.hermes/skills/enterprise-ai-workflow/
```

## Skill mapping

| Source | Hermes skill name |
| --- | --- |
| `skills/task-intake/SKILL.md` | `task-intake` |
| `skills/guideline/SKILL.md` | `guideline` |
| `skills/angular-scaffold/SKILL.md` | `angular-scaffold` |
| `skills/git-workflow/SKILL.md` | `git-workflow` |
| `skills/devops-tasks/SKILL.md` | `devops-tasks` |

## Load examples

```bash
hermes --skills task-intake,guideline
hermes --skills angular-scaffold,git-workflow
hermes --skills devops-tasks,git-workflow
```
