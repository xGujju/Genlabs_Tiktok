#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/home/clawd/Genlabs_Tiktok"
EXPECTED_REMOTE="https://github.com/xGujju/Genlabs_Tiktok.git"
BRANCH="main"
LOG_DIR="$HOME/.hermes/logs"
LOG_FILE="$LOG_DIR/genlabs_tiktok_daily_push.log"
ENV_FILE="$HOME/.hermes/.env"

mkdir -p "$LOG_DIR"
exec >>"$LOG_FILE" 2>&1

echo "===== $(date -u '+%Y-%m-%dT%H:%M:%SZ') daily auto-push start ====="

export PATH="$HOME/.local/bin:$PATH"

if [[ ! -d "$REPO_DIR/.git" ]]; then
  echo "ERROR: repo not found at $REPO_DIR"
  exit 1
fi

cd "$REPO_DIR"

REMOTE_URL="$(git remote get-url origin 2>/dev/null || true)"
if [[ "$REMOTE_URL" != "$EXPECTED_REMOTE" ]]; then
  echo "ERROR: refusing to run; origin is '$REMOTE_URL', expected '$EXPECTED_REMOTE'"
  exit 1
fi

# Load only the GitHub token safely from ~/.hermes/.env. Do not source the whole file.
if [[ -f "$ENV_FILE" ]]; then
  TOKEN="$(python3 - <<'PY'
from pathlib import Path
import re
p = Path.home() / '.hermes' / '.env'
text = p.read_text() if p.exists() else ''
for key in ('GITHUB_TOKEN', 'GH_TOKEN'):
    m = re.search(rf'^{key}=(.*)$', text, re.M)
    if m:
        v = m.group(1).strip()
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
            v = v[1:-1]
        print(v)
        break
PY
)"
else
  TOKEN=""
fi

if [[ -n "${TOKEN:-}" ]]; then
  export GITHUB_TOKEN="$TOKEN"
  export GH_TOKEN="$TOKEN"
fi

if command -v gh >/dev/null 2>&1; then
  gh auth status >/dev/null 2>&1 || {
    if [[ -z "${GITHUB_TOKEN:-}" ]]; then
      echo "ERROR: gh not authenticated and no GITHUB_TOKEN/GH_TOKEN found"
      exit 1
    fi
    printf '%s' "$GITHUB_TOKEN" | gh auth login --with-token
  }
  gh auth setup-git >/dev/null 2>&1 || true
fi

# Local identity only for this repo.
git config user.name "Aion"
git config user.email "aion@users.noreply.github.com"

# Make sure branch exists locally.
if ! git rev-parse --verify "$BRANCH" >/dev/null 2>&1; then
  git checkout -B "$BRANCH"
else
  git checkout "$BRANCH"
fi

# Pull only if the remote branch exists.
if git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  git pull --rebase origin "$BRANCH"
fi

git add -A

if git diff --cached --quiet; then
  echo "No uncommitted changes to push."
  echo "===== $(date -u '+%Y-%m-%dT%H:%M:%SZ') daily auto-push end ====="
  exit 0
fi

COMMIT_MSG="chore: daily auto-sync $(date -u '+%Y-%m-%d %H:%M UTC')"
git commit -m "$COMMIT_MSG"
git push origin "HEAD:$BRANCH"

echo "Pushed commit: $COMMIT_MSG"
echo "===== $(date -u '+%Y-%m-%dT%H:%M:%SZ') daily auto-push end ====="
