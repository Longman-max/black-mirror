import hashlib
import requests
from typing import Dict, Any
from black_mirror.collectors import Collector

class EmailGravatarCollector(Collector):
    @property
    def name(self) -> str:
        return "email_gravatar"

    @property
    def supported_types(self) -> list[str]:
        return ["email"]

    def run(self, query: str) -> Dict[str, Any]:
        email_hash = hashlib.md5(query.lower().strip().encode('utf-8')).hexdigest()
        url = f"https://www.gravatar.com/avatar/{email_hash}?d=404"
        
        try:
            response = requests.get(url, timeout=5)
            exists = response.status_code == 200
            return {
                "exists": exists,
                "profile_url": f"https://www.gravatar.com/{email_hash}" if exists else None,
                "avatar_url": url if exists else None
            }
        except requests.RequestException as e:
            return {
                "error": str(e),
                "exists": False
            }
