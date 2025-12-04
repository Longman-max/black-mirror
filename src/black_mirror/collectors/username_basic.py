from typing import Dict, Any
from black_mirror.collectors import Collector

class UsernameBasicCollector(Collector):
    @property
    def name(self) -> str:
        return "username_basic"

    @property
    def supported_types(self) -> list[str]:
        return ["username"]

    def run(self, query: str) -> Dict[str, Any]:
        # Placeholder for username availability check across platforms
        return {
            "length": len(query),
            "alphanumeric": query.isalnum(),
            "platforms_checked": ["twitter", "github", "instagram"], # Mock
            "exists_on": [] # Mock
        }
