"""Type definitions for pyarkime."""
from __future__ import annotations

from typing import Any, Literal

# Baseline date range options
BaselineDate = Literal[
    "1x",
    "2x",
    "4x",
    "6x",
    "8x",
    "10x",
    1,
    6,
    24,
    48,
    72,
    168,
    336,
    720,
    1440,
    4380,
    8760,
]

# Baseline visibility options
BaselineVis = Literal["all", "actual", "actualold", "new", "old"]

# Sort direction
SortDirection = Literal["asc", "desc"]

# Detail format options
DetailFormat = Literal["last", "natural", "ascii", "utf-8", "hex"]

# Show timestamps options
ShowTimestamps = Literal["last", "true", "false"]

# Theme options
Theme = str  # Can be a predefined theme name or custom color codes

# Manual query option
ManualQuery = bool

# Timeline data filters
TimelineDataFilter = Literal[
    "network.packets",
    "network.bytes",
    "totDataBytes",
]

# JSON response type
JSONResponse = dict[str, Any]

# List response type
ListResponse = list[dict[str, Any]]

