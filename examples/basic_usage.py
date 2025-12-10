"""Basic usage example for pyarkime."""

from pyarkime import ArkimeClient


def main() -> None:
    """Basic usage example."""
    # Initialize client
    client = ArkimeClient(
        base_url="https://arkime.example.com",
        username="your_username",
        password="your_password",
        verify=True,  # Set to False for self-signed certificates
    )

    try:
        # Search sessions
        results = client.sessions.search(expression="ip.src == 192.168.1.1")
        print(f"Found {len(results.get('data', []))} sessions")

        # Get stats
        stats = client.stats.get_stats()
        print(f"Stats: {stats}")

    finally:
        client.close()


if __name__ == "__main__":
    main()

