import logging
import json
import time
from typing import Any, Dict, Optional

def setup_logging(verbose: bool = False) -> None:
    """Configures the logging for the application."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def get_logger(name: str) -> logging.Logger:
    """Returns a logger instance with the given name."""
    return logging.getLogger(name)

def format_result(
    query_type: str,
    query_value: str,
    sources: Dict[str, Any],
    timestamp: Optional[float] = None
) -> Dict[str, Any]:
    """
    Formats the final result into a standardized dictionary.
    
    Args:
        query_type: The type of query (email, username, etc.)
        query_value: The value queried.
        sources: A dictionary of results from different collectors.
        timestamp: Optional timestamp. Defaults to current time.
        
    Returns:
        A dictionary representing the enriched report.
    """
    if timestamp is None:
        timestamp = time.time()
        
    return {
        "query_type": query_type,
        "query_value": query_value,
        "timestamp": timestamp,
        "sources": sources
    }
