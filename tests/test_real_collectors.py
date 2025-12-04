import pytest
from unittest.mock import patch, MagicMock
from black_mirror.collectors.email_gravatar import EmailGravatarCollector
from black_mirror.collectors.username_social import UsernameSocialCollector

def test_gravatar_collector_exists():
    collector = EmailGravatarCollector()
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        result = collector.run("test@example.com")
        assert result["exists"] is True
        assert "profile_url" in result

def test_gravatar_collector_not_exists():
    collector = EmailGravatarCollector()
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        result = collector.run("test@example.com")
        assert result["exists"] is False

def test_social_collector():
    collector = UsernameSocialCollector()
    with patch('requests.get') as mock_get:
        def side_effect(url, **kwargs):
            mock_resp = MagicMock()
            if "github" in url:
                mock_resp.status_code = 200
            else:
                mock_resp.status_code = 404
            return mock_resp
        
        mock_get.side_effect = side_effect
        
        result = collector.run("testuser")
        assert result["github"]["exists"] is True
        assert result["reddit"]["exists"] is False
