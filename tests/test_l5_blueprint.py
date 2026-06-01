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
