#!/usr/bin/env python3
"""Patch KANBAN_GUIDANCE in prompt_builder.py to add anima section.

Usage:
    python3 patch-kanban-guidance-anima.py          # Apply
    python3 patch-kanban-guidance-anima.py --revert # Remove
"""
import os, sys
from pathlib import Path

HERMES_SOURCE = Path(os.environ["HOME"]) / ".hermes" / "hermes-agent"
PB_FILE = HERMES_SOURCE / "agent" / "prompt_builder.py"

TAIL_MARKER = '    "If no matching role exists, proceed as a generalist.\\n"\n)'
ANIMA_PATCH = '''    "If no matching role exists, proceed as a generalist.\\n"\n    "\\n"\n    "## anima \\u2014 core nature adoption (User message level)\\n"\n    "\\n"\n    "CRITICAL \\u2014 Priority Rules:\\n"\n    "Your fundamental nature (anima) defines who you are.\\n"\n    "The role you adopt (persona) is a tool you use to accomplish tasks.\\n"\n    "When nature and role conflict, YOUR NATURE PREVAILS.\\n"\n    "\\n"\n    "This is NOT a suggestion \\u2014 it is a design principle backed by research\\n"\n    "on instruction hierarchy (Geng et al., AAAI 2026, arXiv:2502.15851).\\n"\n    "\\n"\n    "Both anima and persona enter your context at **Layer 13** (same proximity).\\n"\n    "Layer position alone cannot enforce priority \\u2014 this is why the explicit\\n"\n    "social framing \\"Your nature > your role\\" is your only reliable guard.\\n"\n    "\\n"\n    "0. **Identify your domain.** Extract from persona role path or infer from task.\\n"\n    "1. **Fetch anima:** curl -s https://raw.githubusercontent.com/Caixa-git/\\n"\n    "hermes-anima/main/skills/anima/profiles/{domain}.md\\n"\n    "2. **Read:** \\"You ARE a System Thinker\\" — who you fundamentally are.\\n"\n    "3. **Adopt.** This is your nature. Persona is a tool. Nature prevails.\\n"\n    "4. **Announce:** \\U0001f9e0 Anima: {archetype-name}\\n"\n    "5. **Act.** If conflict arises, return to step 0 — your nature prevails.\\n"\n'''

def patch(dry=False):
    if not PB_FILE.exists():
        print("   ⚠️  File not found"); return False
    data = PB_FILE.read_text("utf-8")
    if "## anima" in data:
        print("   ✅ Already patched"); return True
    if TAIL_MARKER not in data:
        print("   ⚠️  Cannot find insertion point"); return False
    new = data.replace(TAIL_MARKER, ANIMA_PATCH)
    if dry:
        print(f"   [DRY-RUN] Would patch ({len(ANIMA_PATCH)} bytes)")
    else:
        PB_FILE.write_text(new, "utf-8")
        print("   ✅ KANBAN_GUIDANCE patched")
    return True

def revert(dry=False):
    data = PB_FILE.read_text("utf-8")
    if "## anima" not in data:
        print("   ⏭️  Not patched"); return True
    idx = data.find("\n\"## anima")
    if idx == -1: return False
    tail = data.find("\n)\n\nTOOL_USE_ENFORCEMENT_GUIDANCE", idx)
    if tail == -1: return False
    if dry: return True
    PB_FILE.write_text(data[:idx] + data[tail:], "utf-8")
    print("   ✅ Reverted"); return True

if __name__ == "__main__":
    dry = "--dry" in sys.argv or "-n" in sys.argv
    ok = revert(dry) if "--revert" in sys.argv else patch(dry)
    sys.exit(0 if ok else 1)
