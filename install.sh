#!/usr/bin/env bash
set -euo pipefail

# 🧠 hermes-anima — install anima core nature skill for Hermes Agent
#
# Usage: bash install.sh [--dry-run] [--help]

DRY_RUN=false
for arg in "$@"; do
    case "$arg" in
        --dry-run|-n) DRY_RUN=true ;;
        --help|-h)
            echo "Usage: bash install.sh [--dry-run] [--help]"
            echo ""
            echo "Installs the anima skill to ~/.hermes/skills/anima/"
            echo "and patches KANBAN_GUIDANCE with anima section."
            echo ""
            echo "Repository: https://github.com/Caixa-git/hermes-anima"
            exit 0
            ;;
    esac
done

maybe() { [ "$DRY_RUN" = true ] && echo "   [DRY-RUN] Would $*" || "$@"; }

echo ""
echo "🧠 Installing Hermes Anima..."
echo ""

ANIMA_DIR="${HOME}/.hermes/skills/anima"
ANIMA_PROFILES="${ANIMA_DIR}/profiles"
HERMES_SOURCE="${HOME}/.hermes/hermes-agent"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PB_FILE="${HERMES_SOURCE}/agent/prompt_builder.py"

# Step 1: Create anima skill directory
maybe mkdir -p "$ANIMA_PROFILES"
[ "$DRY_RUN" = false ] && mkdir -p "$ANIMA_PROFILES" 2>/dev/null || true

# Step 2: Copy SKILL.md and profiles
if [ "$DRY_RUN" = true ]; then
    echo "   [DRY-RUN] Would copy SKILL.md and 15 profiles to ${ANIMA_DIR}/"
else
    cp "${SCRIPT_DIR}/skills/anima/SKILL.md" "${ANIMA_DIR}/SKILL.md"
    cp "${SCRIPT_DIR}/skills/anima/profiles/"*.md "${ANIMA_PROFILES}/"
    echo "   ✅ SKILL.md and 15 profiles installed"
fi

# Step 3: Patch KANBAN_GUIDANCE with anima section
if [ -f "$PB_FILE" ]; then
    if grep -q "core nature adoption" "$PB_FILE" 2>/dev/null; then
        echo "   ✅ anima section already in KANBAN_GUIDANCE"
    else
        if [ "$DRY_RUN" = true ]; then
            echo "   [DRY-RUN] Would patch KANBAN_GUIDANCE with anima section"
        else
            python3 "${SCRIPT_DIR}/scripts/patch-kanban-guidance-anima.py"
            echo "   ✅ KANBAN_GUIDANCE patched with anima section"
        fi
    fi
else
    echo "   ⚠️  prompt_builder.py not found — install Hermes Agent first"
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "Usage:"
echo "  hermes kanban create 'Build auth API' --skill anima"
echo "  hermes kanban create 'Design dashboard' --skill persona --skill anima"
