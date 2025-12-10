# pyarkime

Python client library for Arkime API v3.x-5.x

**Docs:** https://m-jingu.github.io/pyarkime/  

## Installation

```bash
pip install pyarkime
```

## Quick Start

### Synchronous Usage

```python
from pyarkime import ArkimeClient

# Initialize client
client = ArkimeClient(
    base_url="https://arkime.example.com",
    username="your_username",
    password="your_password"
)

# Search sessions
sessions = client.sessions.search(expression="ip.src == 192.168.1.1")
print(f"Found {len(sessions)} sessions")
```

### Asynchronous Usage

```python
import asyncio
from pyarkime import AsyncArkimeClient

async def main():
    # Initialize async client
    client = AsyncArkimeClient(
        base_url="https://arkime.example.com",
        username="your_username",
        password="your_password"
    )
    
    # Search sessions
    sessions = await client.sessions.search(expression="ip.src == 192.168.1.1")
    print(f"Found {len(sessions)} sessions")
    
    # Close client
    await client.close()

asyncio.run(main())
```

## API Endpoints

This library supports all Arkime API v3.x-5.x endpoints:

- **Sessions**: Search, retrieve, and manage sessions
- **Hunt**: Create and manage packet search jobs
- **Views**: Create and manage database views
- **Stats**: Get statistics and health information
- **Crons**: Manage periodic queries
- **Shortcuts**: Create and manage shortcuts
- **Fields**: List available fields
- **Files**: List files
- **Elasticsearch**: Manage ES indices, tasks, shards, and admin operations
- And many more...

## Documentation

Online documentation: https://m-jingu.github.io/pyarkime/  

See [examples](examples/) for more usage examples.

## Requirements

- Python 3.11+
- httpx
- pydantic
