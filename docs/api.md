# API Reference

This document provides a reference for all API endpoints available in pyarkime.

## Client Classes

### ArkimeClient

Synchronous client for Arkime API.

```python
from pyarkime import ArkimeClient

client = ArkimeClient(
    base_url="https://arkime.example.com",
    username="your_username",
    password="your_password"
)
```

### AsyncArkimeClient

Asynchronous client for Arkime API.

```python
from pyarkime import AsyncArkimeClient

client = AsyncArkimeClient(
    base_url="https://arkime.example.com",
    username="your_username",
    password="your_password"
)
```

## API Endpoints

### Sessions API

Search and manage sessions.

```python
# Search sessions
results = client.sessions.search(expression="ip.src == 192.168.1.1")

# Get session detail
detail = client.sessions.get_detail(node_name="node1", session_id="session123")

# Add tags
client.sessions.add_tags(ids=["node1:session123"], tags=["suspicious"])

# Download PCAP
pcap_data = client.sessions.get_pcap(ids=["node1:session123"])
```

### Hunt API

Create and manage packet search jobs.

```python
# Create a hunt
hunt = client.hunt.create(
    name="My Hunt",
    query="ip.src == 192.168.1.1",
    size=1000
)

# List hunts
hunts = client.hunt.list()

# Get hunt details
hunt_details = client.hunt.get(hunt_id="hunt123")

# Cancel a hunt
client.hunt.cancel(hunt_id="hunt123")
```

### Views API

Create and manage database views.

```python
# List views
views = client.views.list()

# Create a view
from pyarkime.models import ArkimeView
view = ArkimeView(
    name="My View",
    expression="ip.src == 192.168.1.1"
)
created_view = client.views.create(view)

# Get view
view_details = client.views.get(view_id="view123")
```

### Stats API

Get statistics and health information.

```python
# Get stats
stats = client.stats.get_stats()

# Get dstats
dstats = client.stats.get_dstats()

# Get ES stats
es_stats = client.stats.get_esstats()
```

### Crons API

Manage periodic queries.

```python
# List crons
crons = client.crons.list()

# Create a cron
from pyarkime.models import ArkimeQuery
query = ArkimeQuery(
    name="Daily Check",
    query="ip.src == 192.168.1.1",
    action="tag",
    enabled=True
)
created_cron = client.crons.create(query)
```

### Shortcuts API

Create and manage shortcuts.

```python
# List shortcuts
shortcuts = client.shortcuts.list()

# Create a shortcut
from pyarkime.models import Shortcut
shortcut = Shortcut(
    name="My Shortcut",
    expression="ip.src == 192.168.1.1"
)
created_shortcut = client.shortcuts.create(shortcut)
```

## Error Handling

The library provides custom exception classes for different error types:

```python
from pyarkime import (
    ArkimeError,
    ArkimeAPIError,
    ArkimeAuthError,
    ArkimeConnectionError,
    ArkimeNotFoundError,
)

try:
    results = client.sessions.search(expression="invalid query")
except ArkimeAPIError as e:
    print(f"API error: {e}")
    print(f"Status code: {e.status_code}")
except ArkimeAuthError as e:
    print(f"Authentication error: {e}")
except ArkimeConnectionError as e:
    print(f"Connection error: {e}")
```

## Models

The library uses Pydantic models for type safety and validation:

- `ArkimeQuery`: Periodic query object
- `History`: History object
- `Hunt`: Hunt object
- `SessionsQuery`: Sessions query parameters
- `Shortcut`: Shortcut object
- `ESHealth`: Elasticsearch health object
- `ArkimeRole`: Role object
- `ArkimeUser`: User object
- `ArkimeSettings`: Settings object
- `ArkimeColumnLayout`: Column layout object
- `ArkimeInfoColumnLayout`: Info column layout object
- `ArkimeView`: View object

## For More Information

See the [official Arkime API documentation](https://arkime.com/apiv3) for detailed parameter descriptions and response formats.

