import pytest
from black_mirror.collectors.email_basic import EmailBasicCollector
from black_mirror.collectors.username_basic import UsernameBasicCollector
from black_mirror.collectors.domain_basic import DomainBasicCollector
from black_mirror.collectors.phone_basic import PhoneBasicCollector

def test_email_collector():
    collector = EmailBasicCollector()
    result = collector.run("user@example.com")
    assert result["valid"] is True
    assert result["user"] == "user"
    assert result["domain"] == "example.com"

    result_invalid = collector.run("invalid-email")
    assert result_invalid["valid"] is False

def test_username_collector():
    collector = UsernameBasicCollector()
    result = collector.run("testuser")
    assert result["length"] == 8
    assert result["alphanumeric"] is True

def test_domain_collector():
    collector = DomainBasicCollector()
    # We can't easily test network calls without mocking, but we can test the structure
    # For now, let's just run it and ensure it doesn't crash.
    # In a real test, we would mock socket.gethostbyname
    try:
        result = collector.run("example.com")
        assert "resolves" in result
    except Exception:
        pytest.fail("Domain collector raised an exception")

def test_phone_collector():
    collector = PhoneBasicCollector()
    # Test US Number
    result = collector.run("+1-555-010-0123") # Example valid-ish format
    # Note: 555-01xx are reserved for fiction, so might be invalid in strict check, 
    # but let's try a known valid format or just check keys.
    # Actually, let's use a real-looking dummy: +1 650 253 0000 (Google)
    result = collector.run("+16502530000")
    assert result["valid"] is True
    assert result["region_code"] == "US"
    
    # Test Togo Number (User's request)
    result_togo = collector.run("+22890016077")
    assert result_togo["region_code"] == "TG"
    assert result_togo["country"] == "Togo"
