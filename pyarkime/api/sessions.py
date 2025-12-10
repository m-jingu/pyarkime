"""Sessions API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/sessions-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class SessionsAPI(BaseAPI):
    """Sessions API endpoint.

    Provides methods for searching and managing sessions.
    """

    def search(
        self,
        expression: str | None = None,
        date: int | None = None,
        start_time: int | None = None,
        stop_time: int | None = None,
        start: int | None = None,
        length: int | None = None,
        fields: str | None = None,
        order_field: str | None = None,
        desc: bool | None = None,
        facets: int | None = None,
        bounding: str | None = None,
        view: str | None = None,
        strict: bool | None = None,
        segments: str | None = None,
        cluster: str | None = None,
        map: bool | None = None,
        format: str | None = None,
        fields_format: str | None = None,
        line: bool | None = None,
        ts_format: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Search sessions.

        POST/GET - /api/sessions

        Args:
            expression: Search expression
            date: Date in milliseconds since Unix epoch
            start_time: Start time in milliseconds since Unix epoch
            stop_time: Stop time in milliseconds since Unix epoch
            start: Start offset for pagination
            length: Number of results to return
            fields: Comma-separated list of fields to return
            order_field: Field to sort by
            desc: Sort in descending order
            facets: Number of facets to return
            bounding: Bounding box for map view
            view: View name to apply
            strict: Use strict query mode
            segments: Segment specification
            cluster: Cluster name
            map: Return map data
            format: Response format
            fields_format: Fields format
            line: Return line format
            ts_format: Timestamp format
            **kwargs: Additional parameters

        Returns:
            Search results
        """
        # Convert milliseconds to seconds for startTime/stopTime
        # Arkime API expects seconds (10 digits), not milliseconds (13 digits)
        start_time_seconds = (
            start_time // 1000 if start_time is not None and start_time > 10000000000 else start_time
        )
        stop_time_seconds = (
            stop_time // 1000 if stop_time is not None and stop_time > 10000000000 else stop_time
        )

        params = self._prepare_params(
            expression=expression,
            date=date,
            startTime=start_time_seconds,
            stopTime=stop_time_seconds,
            start=start,
            length=length,
            fields=fields,
            orderField=order_field,
            desc=desc,
            facets=facets,
            bounding=bounding,
            view=view,
            strict=strict,
            segments=segments,
            cluster=cluster,
            map=map,
            format=format,
            fieldsFormat=fields_format,
            line=line,
            tsFormat=ts_format,
            **kwargs,
        )
        response = self._client.get("/api/sessions", params=params)
        return self._handle_response(response)

    def search_csv(
        self,
        expression: str | None = None,
        date: int | None = None,
        start_time: int | None = None,
        stop_time: int | None = None,
        fields: str | None = None,
        **kwargs: Any,
    ) -> str:
        """Search sessions and return CSV.

        POST/GET - /api/sessions/csv OR /api/sessions.csv

        Args:
            expression: Search expression
            date: Date in milliseconds since Unix epoch
            start_time: Start time in milliseconds since Unix epoch
            stop_time: Stop time in milliseconds since Unix epoch
            fields: Comma-separated list of fields to return
            **kwargs: Additional parameters

        Returns:
            CSV string
        """
        # Convert milliseconds to seconds for startTime/stopTime
        # Arkime API expects seconds (10 digits), not milliseconds (13 digits)
        start_time_seconds = (
            start_time // 1000 if start_time is not None and start_time > 10000000000 else start_time
        )
        stop_time_seconds = (
            stop_time // 1000 if stop_time is not None and stop_time > 10000000000 else stop_time
        )

        params = self._prepare_params(
            expression=expression,
            date=date,
            startTime=start_time_seconds,
            stopTime=stop_time_seconds,
            fields=fields,
            **kwargs,
        )
        response = self._client.get("/api/sessions/csv", params=params)
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"]
        return str(result)

    def get_detail(
        self, node_name: str, session_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Get session detail.

        GET - /api/session/:nodeName/:id/detail

        Args:
            node_name: Node name
            session_id: Session ID
            **kwargs: Additional parameters

        Returns:
            Session detail
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(
            f"/api/session/{node_name}/{session_id}/detail", params=params
        )
        return self._handle_response(response)

    def get_packets(
        self, node_name: str, session_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Get session packets.

        GET - /api/session/:nodeName/:id/packets

        Args:
            node_name: Node name
            session_id: Session ID
            **kwargs: Additional parameters

        Returns:
            Session packets
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(
            f"/api/session/{node_name}/{session_id}/packets", params=params
        )
        return self._handle_response(response)

    def get_body(
        self,
        node_name: str,
        session_id: str,
        body_type: str,
        body_num: int,
        body_name: str,
        **kwargs: Any,
    ) -> bytes:
        """Get session body.

        GET - /api/session/:nodeName/:id/body/:bodyType/:bodyNum/:bodyName

        Args:
            node_name: Node name
            session_id: Session ID
            body_type: Body type
            body_num: Body number
            body_name: Body name
            **kwargs: Additional parameters

        Returns:
            Body content as bytes
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(
            f"/api/session/{node_name}/{session_id}/body/{body_type}/{body_num}/{body_name}",
            params=params,
        )
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"].encode() if isinstance(result["content"], str) else result["content"]
        return b""

    def get_body_png(
        self,
        node_name: str,
        session_id: str,
        body_type: str,
        body_num: int,
        body_name: str,
        **kwargs: Any,
    ) -> bytes:
        """Get session body as PNG.

        GET - /api/session/:nodeName/:id/bodypng/:bodyType/:bodyNum/:bodyName

        Args:
            node_name: Node name
            session_id: Session ID
            body_type: Body type
            body_num: Body number
            body_name: Body name
            **kwargs: Additional parameters

        Returns:
            PNG image as bytes
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(
            f"/api/session/{node_name}/{session_id}/bodypng/{body_type}/{body_num}/{body_name}",
            params=params,
        )
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"].encode() if isinstance(result["content"], str) else result["content"]
        return b""

    def add_tags(self, ids: list[str], tags: list[str], **kwargs: Any) -> dict[str, Any]:
        """Add tags to sessions.

        POST - /api/sessions/addtags

        Args:
            ids: List of session IDs (format: "nodeName:sessionId")
            tags: List of tags to add
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(ids=ids, tags=tags, **kwargs)
        response = self._client.post("/api/sessions/addtags", json=params)
        return self._handle_response(response)

    def remove_tags(
        self, ids: list[str], tags: list[str], **kwargs: Any
    ) -> dict[str, Any]:
        """Remove tags from sessions.

        POST - /api/sessions/removetags

        Args:
            ids: List of session IDs (format: "nodeName:sessionId")
            tags: List of tags to remove
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(ids=ids, tags=tags, **kwargs)
        response = self._client.post("/api/sessions/removetags", json=params)
        return self._handle_response(response)

    def get_pcap(
        self, ids: list[str], **kwargs: Any
    ) -> bytes:
        """Download PCAP for sessions.

        POST - /api/sessions/pcap

        Args:
            ids: List of session IDs (format: "nodeName:sessionId")
            **kwargs: Additional parameters

        Returns:
            PCAP file as bytes
        """
        params = self._prepare_params(ids=ids, **kwargs)
        response = self._client.post("/api/sessions/pcap", json=params)
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"].encode() if isinstance(result["content"], str) else result["content"]
        return b""

    def get_pcapng(
        self, ids: list[str], **kwargs: Any
    ) -> bytes:
        """Download PCAPNG for sessions.

        POST - /api/sessions/pcapng

        Args:
            ids: List of session IDs (format: "nodeName:sessionId")
            **kwargs: Additional parameters

        Returns:
            PCAPNG file as bytes
        """
        params = self._prepare_params(ids=ids, **kwargs)
        response = self._client.post("/api/sessions/pcapng", json=params)
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"].encode() if isinstance(result["content"], str) else result["content"]
        return b""

    def get_entire_pcap(
        self, node_name: str, session_id: str, **kwargs: Any
    ) -> bytes:
        """Download entire PCAP for session.

        GET - /api/session/entire/:nodeName/:id/pcap

        Args:
            node_name: Node name
            session_id: Session ID
            **kwargs: Additional parameters

        Returns:
            PCAP file as bytes
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(
            f"/api/session/entire/{node_name}/{session_id}/pcap", params=params
        )
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"].encode() if isinstance(result["content"], str) else result["content"]
        return b""

    def get_raw_png(
        self, node_name: str, session_id: str, **kwargs: Any
    ) -> bytes:
        """Get raw session PNG.

        GET - /api/session/raw/:nodeName/:id/png

        Args:
            node_name: Node name
            session_id: Session ID
            **kwargs: Additional parameters

        Returns:
            PNG image as bytes
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(
            f"/api/session/raw/{node_name}/{session_id}/png", params=params
        )
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"].encode() if isinstance(result["content"], str) else result["content"]
        return b""

    def get_raw(
        self, node_name: str, session_id: str, **kwargs: Any
    ) -> bytes:
        """Get raw session data.

        GET - /api/session/raw/:nodeName/:id

        Args:
            node_name: Node name
            session_id: Session ID
            **kwargs: Additional parameters

        Returns:
            Raw data as bytes
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(
            f"/api/session/raw/{node_name}/{session_id}", params=params
        )
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"].encode() if isinstance(result["content"], str) else result["content"]
        return b""

    def search_by_bodyhash(
        self, hash_value: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Search sessions by body hash.

        GET - /api/sessions/bodyhash/:hash

        Args:
            hash_value: Body hash value
            **kwargs: Additional parameters

        Returns:
            Search results
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(
            f"/api/sessions/bodyhash/{hash_value}", params=params
        )
        return self._handle_response(response)

    def get_session_bodyhash(
        self, node_name: str, session_id: str, hash_value: str, **kwargs: Any
    ) -> bytes:
        """Get session body by hash.

        GET - /api/session/:nodeName/:id/bodyhash/:hash

        Args:
            node_name: Node name
            session_id: Session ID
            hash_value: Body hash value
            **kwargs: Additional parameters

        Returns:
            Body content as bytes
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(
            f"/api/session/{node_name}/{session_id}/bodyhash/{hash_value}",
            params=params,
        )
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"].encode() if isinstance(result["content"], str) else result["content"]
        return b""


class AsyncSessionsAPI(BaseAPI):
    """Async Sessions API endpoint."""

    async def search(
        self,
        expression: str | None = None,
        date: int | None = None,
        start_time: int | None = None,
        stop_time: int | None = None,
        start: int | None = None,
        length: int | None = None,
        fields: str | None = None,
        order_field: str | None = None,
        desc: bool | None = None,
        facets: int | None = None,
        bounding: str | None = None,
        view: str | None = None,
        strict: bool | None = None,
        segments: str | None = None,
        cluster: str | None = None,
        map: bool | None = None,
        format: str | None = None,
        fields_format: str | None = None,
        line: bool | None = None,
        ts_format: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Search sessions (async)."""
        start_time_seconds = (
            start_time // 1000 if start_time is not None and start_time > 10000000000 else start_time
        )
        stop_time_seconds = (
            stop_time // 1000 if stop_time is not None and stop_time > 10000000000 else stop_time
        )

        params = self._prepare_params(
            expression=expression,
            date=date,
            startTime=start_time_seconds,
            stopTime=stop_time_seconds,
            start=start,
            length=length,
            fields=fields,
            orderField=order_field,
            desc=desc,
            facets=facets,
            bounding=bounding,
            view=view,
            strict=strict,
            segments=segments,
            cluster=cluster,
            map=map,
            format=format,
            fieldsFormat=fields_format,
            line=line,
            tsFormat=ts_format,
            **kwargs,
        )
        response = await self._client.get("/api/sessions", params=params)
        return self._handle_response(response)

    async def search_csv(
        self,
        expression: str | None = None,
        date: int | None = None,
        start_time: int | None = None,
        stop_time: int | None = None,
        fields: str | None = None,
        **kwargs: Any,
    ) -> str:
        """Search sessions and return CSV (async)."""
        # Convert milliseconds to seconds for startTime/stopTime
        # Arkime API expects seconds (10 digits), not milliseconds (13 digits)
        start_time_seconds = (
            start_time // 1000 if start_time is not None and start_time > 10000000000 else start_time
        )
        stop_time_seconds = (
            stop_time // 1000 if stop_time is not None and stop_time > 10000000000 else stop_time
        )

        params = self._prepare_params(
            expression=expression,
            date=date,
            startTime=start_time_seconds,
            stopTime=stop_time_seconds,
            fields=fields,
            **kwargs,
        )
        response = await self._client.get("/api/sessions/csv", params=params)
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"]
        return str(result)

    async def get_detail(
        self, node_name: str, session_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Get session detail (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get(
            f"/api/session/{node_name}/{session_id}/detail", params=params
        )
        return self._handle_response(response)

    async def get_packets(
        self, node_name: str, session_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Get session packets (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get(
            f"/api/session/{node_name}/{session_id}/packets", params=params
        )
        return self._handle_response(response)

    async def add_tags(
        self, ids: list[str], tags: list[str], **kwargs: Any
    ) -> dict[str, Any]:
        """Add tags to sessions (async)."""
        params = self._prepare_params(ids=ids, tags=tags, **kwargs)
        response = await self._client.post("/api/sessions/addtags", json=params)
        return self._handle_response(response)

    async def remove_tags(
        self, ids: list[str], tags: list[str], **kwargs: Any
    ) -> dict[str, Any]:
        """Remove tags from sessions (async)."""
        params = self._prepare_params(ids=ids, tags=tags, **kwargs)
        response = await self._client.post("/api/sessions/removetags", json=params)
        return self._handle_response(response)

    async def get_pcap(self, ids: list[str], **kwargs: Any) -> bytes:
        """Download PCAP for sessions (async)."""
        params = self._prepare_params(ids=ids, **kwargs)
        response = await self._client.post("/api/sessions/pcap", json=params)
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"].encode() if isinstance(result["content"], str) else result["content"]
        return b""

    async def get_pcapng(self, ids: list[str], **kwargs: Any) -> bytes:
        """Download PCAPNG for sessions (async)."""
        params = self._prepare_params(ids=ids, **kwargs)
        response = await self._client.post("/api/sessions/pcapng", json=params)
        result = self._handle_response(response)
        if isinstance(result, dict) and "content" in result:
            return result["content"].encode() if isinstance(result["content"], str) else result["content"]
        return b""

