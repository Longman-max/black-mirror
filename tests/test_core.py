import pytest
from black_mirror.core import BlackMirror
from black_mirror.collectors import Collector

def test_plugin_loading():
    bm = BlackMirror()
    assert "email" in bm.collectors
    assert "username" in bm.collectors
    assert "domain" in bm.collectors
    assert "phone" in bm.collectors

def test_lookup_structure():
    bm = BlackMirror()
    result = bm.lookup("email", "test@example.com")
    
    assert "query_type" in result
    assert "query_value" in result
    assert "timestamp" in result
    assert "sources" in result
    assert result["query_type"] == "email"
    assert result["query_value"] == "test@example.com"

def test_lookup_execution():
    bm = BlackMirror()
    result = bm.lookup("email", "test@example.com")
    
    # Check if email_basic collector ran
    assert "email_basic" in result["sources"]
    assert result["sources"]["email_basic"]["status"] == "success"
