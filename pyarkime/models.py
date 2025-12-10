"""Pydantic models for Arkime API request/response types."""
from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ArkimeQuery(BaseModel):
    """Periodic query (cron) object.

    See: https://arkime.com/apiv3#ArkimeQuery-Type
    """

    name: str
    query: str
    action: str
    notifier: str | None = None
    tags: list[str] | None = None
    users: list[str] | None = None
    roles: list[str] | None = None
    enabled: bool = True
    created: int | None = None  # milliseconds since Unix epoch
    last_run: int | None = None  # milliseconds since Unix epoch
    last_run_status: str | None = None
    last_run_count: int | None = None
    last_run_error: str | None = None


class History(BaseModel):
    """History (user client request) object.

    See: https://arkime.com/apiv3#History-Type
    """

    id: str
    user: str
    expression: str
    created: int  # milliseconds since Unix epoch
    api: str
    query: dict[str, Any] | None = None
    response_time: int | None = None  # milliseconds
    records_returned: int | None = None
    records_filtered: int | None = None


class Hunt(BaseModel):
    """Hunt (packet search job) object.

    See: https://arkime.com/apiv3#Hunt-Type
    """

    id: str
    name: str
    query: str
    size: int
    search_type: str
    status: str
    created: int  # milliseconds since Unix epoch
    started: int | None = None  # milliseconds since Unix epoch
    completed: int | None = None  # milliseconds since Unix epoch
    errors: list[str] | None = None
    notifier: str | None = None
    users: list[str] | None = None
    roles: list[str] | None = None
    user: str | None = None


class SessionsQuery(BaseModel):
    """Sessions query parameters.

    See: https://arkime.com/apiv3#SessionsQuery-Parameter-List

    Note: This model includes common parameters. Additional parameters
    may be passed as keyword arguments and will be included in the request.
    """

    expression: str | None = None
    date: int | None = None  # milliseconds since Unix epoch
    start_time: int | None = None  # milliseconds since Unix epoch
    stop_time: int | None = None  # milliseconds since Unix epoch
    start: int | None = None
    length: int | None = None
    fields: str | None = None
    order_field: str | None = None
    desc: bool | None = None
    facets: int | None = None
    bounding: str | None = None
    view: str | None = None
    strict: bool | None = None
    segments: str | None = None
    cluster: str | None = None
    map: bool | None = None
    format: str | None = None
    fields_format: str | None = None
    line: bool | None = None
    ts_format: str | None = None

    class Config:
        extra = "allow"  # Allow additional parameters not defined in the model


class Shortcut(BaseModel):
    """Shortcut object.

    See: https://arkime.com/apiv3#Shortcut-Type
    """

    id: str | None = None
    name: str
    expression: str
    user: str | None = None
    users: list[str] | None = None
    roles: list[str] | None = None


class ESHealth(BaseModel):
    """Elasticsearch health object.

    See: https://arkime.com/apiv3#ESHealth-Type
    """

    status: str
    cluster_name: str
    number_of_nodes: int
    number_of_data_nodes: int
    active_primary_shards: int
    active_shards: int
    relocating_shards: int
    initializing_shards: int
    unassigned_shards: int
    delayed_unassigned_shards: int
    number_of_pending_tasks: int
    number_of_in_flight_fetch: int
    task_max_waiting_in_queue_millis: int
    active_shards_percent_as_number: float


class ArkimeRole(BaseModel):
    """Arkime role object.

    See: https://arkime.com/apiv3#ArkimeRole-Type
    """

    id: str
    name: str
    description: str | None = None
    users: list[str] | None = None
    permissions: list[str] | None = None


class ArkimeSettings(BaseModel):
    """Arkime settings object.

    See: https://arkime.com/apiv3#ArkimeSettings-Type
    """

    timezone: str = "local"
    detail_format: str = "last"
    show_timestamps: str = "last"
    sort_column: str = "firstPacket"
    sort_direction: str = "desc"
    spi_graph: str = "node"
    conn_src_field: str = "source.ip"
    conn_dst_field: str = "ip.dst:port"
    num_packets: str = "last"
    theme: str = "default-theme"
    manual_query: bool = False
    timeline_data_filters: list[str] = Field(
        default_factory=lambda: ["network.packets", "network.bytes", "totDataBytes"]
    )
    hide_tags: str = '""'
    logo: str | None = None


class ArkimeColumnLayout(BaseModel):
    """Sessions table column layout.

    See: https://arkime.com/apiv3#ArkimeColumnLayout-Type
    """

    name: str
    order: list[list[str]] = Field(
        default_factory=lambda: [["firstPacket", "desc"]]
    )
    visible_headers: list[str] = Field(
        default_factory=lambda: [
            "firstPacket",
            "lastPacket",
            "src",
            "source.port",
            "dst",
            "destination.port",
            "network.packets",
            "dbby",
            "node",
        ]
    )


class ArkimeInfoColumnLayout(BaseModel):
    """Sessions info column layout.

    See: https://arkime.com/apiv3#ArkimeInfoColumnLayout-Type
    """

    name: str
    fields: list[str] = Field(
        default_factory=lambda: [
            "firstPacket",
            "lastPacket",
            "src",
            "source.port",
            "dst",
            "destination.port",
            "network.packets",
            "dbby",
            "node",
        ]
    )


class ArkimeView(BaseModel):
    """Database view object.

    See: https://arkime.com/apiv3#ArkimeView-Type
    """

    name: str
    expression: str
    sessions_col_config: dict[str, Any] | None = None
    user: str | None = None
    users: list[str] | None = None
    roles: list[str] | None = None
    edit_roles: list[str] | None = None


class ArkimeUser(BaseModel):
    """Arkime user object.

    See: https://arkime.com/apiv3#ArkimeUser-Type
    """

    user_id: str
    user_name: str
    enabled: bool = True
    web_enabled: bool = True
    header_auth_enabled: bool = False
    email_search: bool = False
    remove_enabled: bool = False
    packet_search: bool = True
    hide_stats: bool = False
    hide_files: bool = False
    hide_pcap: bool = False
    disable_pcap_download: bool = False
    expression: str | None = None
    settings: ArkimeSettings | None = None
    notifiers: dict[str, Any] | None = None
    column_configs: dict[str, Any] | None = None
    spiview_field_configs: dict[str, Any] | None = None
    table_states: dict[str, Any] | None = None
    welcome_msg_num: int = 0
    last_used: int | None = None  # milliseconds since Unix epoch
    time_limit: int | None = None
    roles: list[str] | None = None
    role_assigners: list[str] | None = None

