import importlib
import pkgutil
import inspect
import time
from typing import Dict, List, Type, Any
from black_mirror.collectors import Collector
from black_mirror.utils import get_logger, format_result
import black_mirror.collectors

logger = get_logger(__name__)

class BlackMirror:
    def __init__(self):
        self.collectors: Dict[str, List[Collector]] = {}
        self._load_collectors()

    def _load_collectors(self):
        """Dynamically discovers and loads collector plugins."""
        package = black_mirror.collectors
        path = package.__path__
        prefix = package.__name__ + "."

        for _, name, _ in pkgutil.iter_modules(path, prefix):
            try:
                module = importlib.import_module(name)
                for _, obj in inspect.getmembers(module):
                    if (inspect.isclass(obj) and 
                        issubclass(obj, Collector) and 
                        obj is not Collector):
                        
                        collector_instance = obj()
                        for query_type in collector_instance.supported_types:
                            if query_type not in self.collectors:
                                self.collectors[query_type] = []
                            self.collectors[query_type].append(collector_instance)
                        
                        logger.debug(f"Loaded collector: {collector_instance.name}")
            except Exception as e:
                logger.error(f"Failed to load module {name}: {e}")

    def lookup(self, query_type: str, query_value: str) -> Dict[str, Any]:
        """
        Runs all relevant collectors for the given query type and value.
        """
        if query_type not in self.collectors:
            logger.warning(f"No collectors found for type: {query_type}")
            return format_result(query_type, query_value, {})

        results = {}
        for collector in self.collectors[query_type]:
            try:
                logger.info(f"Running {collector.name} for {query_value}")
                start_time = time.time()
                data = collector.run(query_value)
                duration = time.time() - start_time
                
                results[collector.name] = {
                    "status": "success",
                    "data": data,
                    "duration_seconds": duration
                }
            except Exception as e:
                logger.error(f"Collector {collector.name} failed: {e}")
                results[collector.name] = {
                    "status": "error",
                    "error": str(e)
                }

        return format_result(query_type, query_value, results)
