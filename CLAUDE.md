# CLAUDE.md — Prospera governance contract

**Authority**: ccktaiwan
**Schema**: prospera-os/DIRECTORY_SCHEMA.json
**Skills**: prospera-infra-ci/skills/SKILL-CORE.md
**Canonical source**: system_index.yaml v3.0

---

## EXECUTION MODEL

When working in any Prospera repo:
- NEVER produce manual scripts for the human to run
- ALWAYS use Claude Code to directly create files, run git, move directories
- If a task needs a decision → ask ccktaiwan ONE question, then execute
- The human judges. Claude Code executes.

---

## This repo

**Repo**: prospera-blueprint-esg
**Status**: ACTIVE
**Tier**: L3 (Blueprint)
**Ring**: Ring 3 — Blueprints

**Contract**:
- INPUT: Carbon data + ISO 14064 submission
- OUTPUT: ESG compliance score + GBCT token record

**Purpose**: ESG/carbon compliance framework, ISO 14064, 4-pass audit
