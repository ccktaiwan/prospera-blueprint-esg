# AGENTS.md — prospera-blueprint-esg
# Version: 1.0 | 2026-05-30
# Governance Reference: prospera-constitution-governance v3.0
# Pipeline Reference: prospera-infra-ci v3.5

## 1. REPO IDENTITY
Repo: ccktaiwan/prospera-blueprint-esg
Ring: Ring 3 — Blueprints
Role: ESG 治理藍圖、評分框架設計、企業永續標準定義

## 2. AGENT RULES

### PERMIT
- 讀取 ESG 標準文件
- 生成評分建議（draft）
- 輸出藍圖規格文件

### ESCALATE
- 修改評分維度定義 → J2
- 新增監管對應（MAS/SEC）→ J2

### BLOCK
- 核准 ESG 評分（AI 只能 draft）
- 修改 Ring 2 Standards 定義

## 3. Decision Engine
Q1 Should / Q2 Can / Q3 Fit / Q4 Profit
任一 BLOCK → 整體 BLOCK
任一 ESCALATE → 觸發對應 J點

## 4. J 點
J1 技術確認 / J2 品質審閱 / J3 架構決策

# Version: 1.0 | 2026-05-30
# Human-Reviewed: pending
