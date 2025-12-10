"""Async usage example for pyarkime."""

import asyncio

from pyarkime import AsyncArkimeClient


async def main() -> None:
    """Async usage example."""
    # Initialize async client
    client = AsyncArkimeClient(
        base_url="https://arkime.example.com",
        username="your_username",
        password="your_password",
        verify=True,  # Set to False for self-signed certificates
    )

    try:
        # Search sessions
        results = await client.sessions.search(expression="ip.src == 192.168.1.1")
        print(f"Found {len(results.get('data', []))} sessions")

        # Get stats
        stats = await client.stats.get_stats()
        print(f"Stats: {stats}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())

