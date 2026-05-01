# Genlabs_Tiktok

Operational Git repository for GenLabs TikTok / GenLabs AI Learning work.

## Repo rule

This workspace is intentionally locked to:

```text
https://github.com/xGujju/Genlabs_Tiktok.git
```

Aion should only inspect, update, commit, and push this Git repository unless Sway explicitly overrides the rule.

## Daily auto-push

A daily automation commits and pushes uncommitted files from this repo once per day.

Script:

```text
scripts/daily_auto_push.sh
```

Behavior:

- verifies the working directory is `/home/clawd/Genlabs_Tiktok`
- verifies `origin` is exactly `https://github.com/xGujju/Genlabs_Tiktok.git`
- authenticates with the GitHub token stored in `~/.hermes/.env`
- stages all local changes with `git add -A`
- skips clean days with no changes
- commits with a timestamped message
- pushes to `main`

Logs are written outside the repo at:

```text
~/.hermes/logs/genlabs_tiktok_daily_push.log
```
