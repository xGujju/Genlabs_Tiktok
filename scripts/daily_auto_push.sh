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

# Pull only if the remote branch exists and the worktree is clean.
# This job's purpose is to preserve uncommitted work, so never fail just because local changes exist.
if git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  if git diff --quiet && git diff --cached --quiet; then
    git pull --rebase origin "$BRANCH"
  else
    echo "Local changes exist before pull; skipping pre-pull and will push after commit."
  fi
fi

# Export current generated GenLabs carousel assets and durable learning notes into this repo
# before staging, so files generated outside the repo are not missed by the daily push.
python3 - <<'PY'
from pathlib import Path
import shutil, time, re

repo = Path('/home/clawd/Genlabs_Tiktok')
src_car = Path.home() / '.hermes' / 'ai_signal_radar' / 'carousels'
assets = repo / 'assets' / 'carousels'
learn = repo / 'docs' / 'learnings'
assets.mkdir(parents=True, exist_ok=True)
learn.mkdir(parents=True, exist_ok=True)

if src_car.exists():
    for p in src_car.rglob('*'):
        if not p.is_file() or p.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp', '.json', '.md', '.html'}:
            continue
        dst = assets / p.relative_to(src_car)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst)

vault = Path.home() / 'Documents' / 'Obsidian Vault' / 'Aion OS'
selected = []
for rel in [
    'Projects/genlabs-ai-learning-state.md',
    'Projects/genlabs-thai-ai-media-engine.md',
    'Projects/genlabs-thai-ai-media-engine-plan.md',
    '02 - Decision Log.md',
    '07 - Open Loops.md',
    'SOPs/genlabs-ai-carousel-production-process.md',
    'SOPs/genlabs-ai-learning-self-improvement-system.md',
    'SOPs/genlabs-thai-ai-media-loop.md',
]:
    p = vault / rel
    if p.exists():
        selected.append(p)
lab = vault / 'Aion Learning Lab'
if lab.exists():
    selected.extend([p for p in lab.rglob('*.md') if p.is_file()])

for p in selected:
    rel = p.relative_to(vault)
    safe_rel = Path(*[part.replace(' ', '_') for part in rel.parts])
    dst = learn / safe_rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, dst)

# Redact transient URL token query params and obvious API keys in exported text files.
for p in repo.rglob('*'):
    if not p.is_file() or '.git' in p.parts or p.suffix.lower() not in {'.json', '.md', '.html', '.txt'}:
        continue
    try:
        s = p.read_text(errors='ignore')
    except Exception:
        continue
    orig = s
    s = re.sub(r'(?i)([?&]token=)[A-Za-z0-9_\-.%]+', r'\1REDACTED', s)
    s = re.sub(r'(?i)(token=)[A-Za-z0-9_\-.%]+', r'\1REDACTED', s)
    s = re.sub(r'gh[pousr]_[A-Za-z0-9_]{20,}', 'GITHUB_TOKEN_REDACTED', s)
    s = re.sub(r'sk-[A-Za-z0-9_-]{20,}', 'OPENAI_KEY_REDACTED', s)
    if s != orig:
        p.write_text(s)

image_count = sum(1 for p in assets.rglob('*') if p.is_file() and p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp'})
manifest_count = sum(1 for p in assets.rglob('*') if p.is_file() and p.name == 'manifest.json')
learning_count = sum(1 for p in learn.rglob('*.md'))
carousel_dirs = []
for d in sorted([x for x in assets.iterdir() if x.is_dir()]):
    imgs = sum(1 for p in d.glob('slide-*') if p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp'})
    if imgs:
        carousel_dirs.append((d.name, imgs))
(repo / 'docs').mkdir(parents=True, exist_ok=True)
(repo / 'docs' / 'asset-and-learning-index.md').write_text(
    '# GenLabs Asset + Learning Index\n\n'
    f'Updated: {time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())}\n\n'
    f'- Carousel image assets copied: {image_count}\n'
    f'- Carousel manifests copied: {manifest_count}\n'
    f'- Learning/operations notes copied: {learning_count}\n\n'
    '## Carousel folders\n\n'
    + '\n'.join(f'- `{name}` — {imgs} image(s)' for name, imgs in carousel_dirs)
    + '\n\n## Source policy\n\nGenerated images are exported from `~/.hermes/ai_signal_radar/carousels`. Durable GenLabs learnings are exported from Obsidian `Aion OS` notes. Secrets and environment files are intentionally excluded.\n'
)
print(f'Exported assets: images={image_count} manifests={manifest_count} learning_notes={learning_count}')
PY

git add -A

if git diff --cached --quiet; then
  echo "No uncommitted changes to push."
  echo "===== $(date -u '+%Y-%m-%dT%H:%M:%SZ') daily auto-push end ====="
  exit 0
fi

COMMIT_MSG="chore: daily auto-sync $(date -u '+%Y-%m-%d %H:%M UTC')"
git commit -m "$COMMIT_MSG"
if ! git push origin "HEAD:$BRANCH"; then
  echo "Initial push failed; rebasing on origin/$BRANCH then retrying."
  git pull --rebase origin "$BRANCH"
  git push origin "HEAD:$BRANCH"
fi

echo "Pushed commit: $COMMIT_MSG"
echo "===== $(date -u '+%Y-%m-%dT%H:%M:%SZ') daily auto-push end ====="
