# ── Prospera SYSTEM HEADER (ADR-0032/SBOM) ──
# 性質:engineering ｜設計:Kevin 架構 ｜執行:AI 工具(claude.ai+Claude Code)
# 驗證:無機制驗證 ｜IP:創造性歸 Kevin(發明人), AI 為執行工具 (ADR-0032)
import pytest, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from monitoring_hook import trigger_monitoring

_LOG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "execution_log.jsonl")

def test_trigger_monitoring():
    trigger_monitoring({"test": True})
    assert os.path.exists(_LOG)

def test_monitoring_entry_valid():
    trigger_monitoring({"action": "test"})
    with open(_LOG, encoding="utf-8") as f:
        lines = f.readlines()
    entry = json.loads(lines[-1].strip())
    assert "timestamp" in entry
