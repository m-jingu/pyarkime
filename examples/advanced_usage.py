"""Advanced usage example for pyarkime."""

from pyarkime import ArkimeClient
from pyarkime.models import ArkimeQuery, Shortcut, ArkimeView


def main() -> None:
    """Advanced usage example."""
    client = ArkimeClient(
        base_url="https://arkime.example.com",
        username="your_username",
        password="your_password",
    )

    try:
        # Create a periodic query (cron)
        query = ArkimeQuery(
            name="Daily IP Check",
            query="ip.src == 192.168.1.1",
            action="tag",
            tags=["suspicious"],
            enabled=True,
        )
        created_query = client.crons.create(query)
        print(f"Created query: {created_query}")

        # Create a shortcut
        shortcut = Shortcut(
            name="My Shortcut",
            expression="ip.src == 192.168.1.1",
        )
        created_shortcut = client.shortcuts.create(shortcut)
        print(f"Created shortcut: {created_shortcut}")

        # Create a view
        view = ArkimeView(
            name="My View",
            expression="ip.src == 192.168.1.1",
        )
        created_view = client.views.create(view)
        print(f"Created view: {created_view}")

        # Search with pagination
        results = client.sessions.search(
            expression="ip.src == 192.168.1.1",
            start=0,
            length=100,
            order_field="firstPacket",
            desc=True,
        )
        print(f"Found {len(results.get('data', []))} sessions")

    finally:
        client.close()


if __name__ == "__main__":
    main()

