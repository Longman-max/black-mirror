import requests
from typing import Dict, Any
from black_mirror.collectors import Collector

class UsernameSocialCollector(Collector):
    @property
    def name(self) -> str:
        return "username_social"

    @property
    def supported_types(self) -> list[str]:
        return ["username"]

    def run(self, query: str) -> Dict[str, Any]:
        results = {}
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; BlackMirror/0.1; +https://github.com/yourusername/black-mirror)"
        }
        
        sites = {
            "github": f"https://github.com/{query}",
            "reddit": f"https://www.reddit.com/user/{query}/about.json"
        }

        for site, url in sites.items():
            try:
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code == 200:
                    results[site] = {"exists": True, "url": url}
                elif response.status_code == 404:
                    results[site] = {"exists": False}
                else:
                    results[site] = {"exists": False, "status_code": response.status_code}
            except requests.RequestException as e:
                results[site] = {"error": str(e)}
        
        return results
