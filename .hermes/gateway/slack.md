# Slack Gateway Setup for Hermes

Use this when ZenAgent should operate in Slack.

## 1. Configure secrets

Add these to `~/.hermes/.env`:

```bash
SLACK_BOT_TOKEN=replace_me
SLACK_APP_TOKEN=replace_me
SLACK_OWNER_USER_ID=U...
```

## 2. Run setup

```bash
hermes gateway setup
hermes gateway run
```

For a background service:

```bash
hermes gateway install
hermes gateway start
hermes gateway status
```

## 3. Workspace behavior

The Slack workflow should follow `.agent/AGENTS.md` and `.agent/WORKFLOWS.md`:

- Intake tasks in a thread.
- Ask one grouped clarification message.
- Create `plan.md` and wait for approval.
- Execute only after approval keywords.
- Report branch, files, summary, and next steps.

## 4. Safety

Never post secrets or private internal content to shared channels. Use DMs for main-session memory and sensitive context.
