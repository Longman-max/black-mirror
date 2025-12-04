from typing import Dict, Any
from black_mirror.collectors import Collector
import socket
from urllib.parse import urlparse

class DomainBasicCollector(Collector):
    @property
    def name(self) -> str:
        return "domain_basic"

    @property
    def supported_types(self) -> list[str]:
        return ["domain"]

    def run(self, query: str) -> Dict[str, Any]:
        # Clean up the query to get just the hostname
        if "://" not in query:
            # If no protocol, urlparse might not parse hostname correctly if it thinks it's a path
            # But for "example.com", urlparse("example.com").path == "example.com"
            # So we can just prepend http:// to make it robust
            target = query
        else:
            parsed = urlparse(query)
            target = parsed.netloc or parsed.path # Fallback if something weird happens

        # Remove any trailing slash or path if user typed "example.com/foo" without protocol
        if "/" in target:
            target = target.split("/")[0]

        try:
            ip = socket.gethostbyname(target)
            return {
                "resolves": True,
                "hostname": target,
                "ip": ip
            }
        except socket.gaierror:
            return {
                "resolves": False,
                "hostname": target,
                "error": "Could not resolve domain"
            }
