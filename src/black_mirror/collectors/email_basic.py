from typing import Dict, Any
from black_mirror.collectors import Collector

class EmailBasicCollector(Collector):
    @property
    def name(self) -> str:
        return "email_basic"

    @property
    def supported_types(self) -> list[str]:
        return ["email"]

    def run(self, query: str) -> Dict[str, Any]:
        # In a real scenario, this would query an API or scrape a site.
        # For now, we perform basic validation and domain extraction.
        if "@" not in query:
            return {"valid": False, "reason": "Missing @ symbol"}
        
        user, domain = query.split("@", 1)
        return {
            "valid": True,
            "user": user,
            "domain": domain,
            "is_disposable": domain in ["tempmail.com", "10minutemail.com"] # Example list
        }
