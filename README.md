# Black Mirror

**Weapons-grade cool OSINT toolkit.**

Black Mirror is a modular, extensible OSINT + enrichment engine designed to collect, analyze, and structure public data. It is built to integrate cleanly with scam detection systems.

> [!NOTE]
> This project was inspired by one of my favorite TV shows, **Black Mirror**.

## Features

- **Modular Architecture**: Plugin-based system for easy extension.
- **Unified Output**: Structured, deterministic JSON output for all queries.
- **CLI Tool**: Powerful command-line interface for quick lookups.
- **Collectors**:
  - Email (Basic validation, disposable check)
  - Username (Basic format check)
  - Domain (Resolution check)
  - Phone (Parsing)

## Installation

```bash
git clone https://github.com/Longman-max/black-mirror.git
cd black-mirror
pip install -e .
```

## Usage

### CLI

```bash
# Email Lookup
python -m black_mirror lookup --type email --value target@example.com

# Domain Lookup
python -m black_mirror lookup --type domain --value example.com

# Username Lookup
python -m black_mirror lookup --type username --value targetuser

# Phone Lookup
python -m black_mirror lookup --type phone --value +1234567890
```

### Python API

```python
from black_mirror.core import BlackMirror

bm = BlackMirror()
result = bm.lookup("email", "target@example.com")
print(result)
```

## Output Format

```json
{
  "query_type": "email",
  "query_value": "target@example.com",
  "timestamp": 1701712345.678,
  "sources": {
    "email_basic": {
      "status": "success",
      "data": {
        "valid": true,
        "user": "target",
        "domain": "example.com",
        "is_disposable": false
      },
      "duration_seconds": 0.0001
    }
  }
}
```

## Development

### Running Tests

```bash
pytest
```

### Adding a Collector

1. Create a new file in `src/black_mirror/collectors/`.
2. Inherit from `black_mirror.collectors.Collector`.
3. Implement `name`, `supported_types`, and `run`.

```python
from typing import Dict, Any
from black_mirror.collectors import Collector

class MyCollector(Collector):
    @property
    def name(self) -> str:
        return "my_collector"

    @property
    def supported_types(self) -> list[str]:
        return ["email"]

    def run(self, query: str) -> Dict[str, Any]:
        return {"data": "found"}
```

## License

MIT
