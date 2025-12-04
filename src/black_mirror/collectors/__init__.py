from abc import ABC, abstractmethod
from typing import Dict, Any

class Collector(ABC):
    """
    Abstract base class for all data collectors.
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the unique name of the collector."""
        pass

    @property
    @abstractmethod
    def supported_types(self) -> list[str]:
        """Returns a list of query types this collector supports (e.g., ['email', 'username'])."""
        pass

    @abstractmethod
    def run(self, query: str) -> Dict[str, Any]:
        """
        Executes the collection logic.
        
        Args:
            query: The value to search for.
            
        Returns:
            A dictionary containing the collected data.
        """
        pass
