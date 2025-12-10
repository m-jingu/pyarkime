"""Main client classes for Arkime API."""

from typing import TYPE_CHECKING, Any

import httpx

from pyarkime.auth import create_auth
from pyarkime.exceptions import ArkimeConnectionError

if TYPE_CHECKING:
    from pyarkime.api import (
        crons,
        histories,
        hunt,
        fields,
        files,
        valueactions,
        fieldactions,
        upload,
        buildquery,
        sessions,
        spiview,
        unique,
        delete,
        shortcuts,
        eshealth,
        stats,
        esindices,
        estasks,
        esadmin,
        esshards,
        esrecovery,
        parliament,
        views,
    )


class BaseClient:
    """Base client class with common functionality."""

    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        timeout: float = 30.0,
        verify: bool = True,
    ) -> None:
        """Initialize base client.

        Args:
            base_url: Base URL of Arkime instance (e.g., "https://arkime.example.com")
            username: Username for digest authentication
            password: Password for digest authentication
            timeout: Request timeout in seconds
            verify: Whether to verify SSL certificates
        """
        # Ensure base_url doesn't end with /
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.timeout = timeout
        self.verify = verify

        # Create auth instance
        self._auth = create_auth(username, password)

        # API endpoint modules will be initialized in subclasses
        self._api_modules: dict[str, Any] = {}


class ArkimeClient(BaseClient):
    """Synchronous client for Arkime API."""

    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        timeout: float = 30.0,
        verify: bool = True,
    ) -> None:
        """Initialize synchronous Arkime client.

        Args:
            base_url: Base URL of Arkime instance
            username: Username for digest authentication
            password: Password for digest authentication
            timeout: Request timeout in seconds
            verify: Whether to verify SSL certificates
        """
        super().__init__(base_url, username, password, timeout, verify)

        # Create synchronous httpx client
        self._client = httpx.Client(
            base_url=self.base_url,
            auth=self._auth,
            timeout=self.timeout,
            verify=self.verify,
        )

        # Initialize API modules (will be imported when needed)
        self._init_api_modules()

    def _init_api_modules(self) -> None:
        """Initialize API endpoint modules.

        Modules are imported lazily to avoid circular imports.
        """
        # This will be populated as modules are imported
        pass

    def __enter__(self) -> "ArkimeClient":
        """Context manager entry."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    @property
    def sessions(self) -> "sessions.SessionsAPI":
        """Access sessions API."""
        from pyarkime.api import sessions

        if "sessions" not in self._api_modules:
            self._api_modules["sessions"] = sessions.SessionsAPI(self._client)
        return self._api_modules["sessions"]

    @property
    def hunt(self) -> "hunt.HuntAPI":
        """Access hunt API."""
        from pyarkime.api import hunt

        if "hunt" not in self._api_modules:
            self._api_modules["hunt"] = hunt.HuntAPI(self._client)
        return self._api_modules["hunt"]

    @property
    def views(self) -> "views.ViewsAPI":
        """Access views API."""
        from pyarkime.api import views

        if "views" not in self._api_modules:
            self._api_modules["views"] = views.ViewsAPI(self._client)
        return self._api_modules["views"]

    @property
    def stats(self) -> "stats.StatsAPI":
        """Access stats API."""
        from pyarkime.api import stats

        if "stats" not in self._api_modules:
            self._api_modules["stats"] = stats.StatsAPI(self._client)
        return self._api_modules["stats"]

    @property
    def crons(self) -> "crons.CronsAPI":
        """Access crons API."""
        from pyarkime.api import crons

        if "crons" not in self._api_modules:
            self._api_modules["crons"] = crons.CronsAPI(self._client)
        return self._api_modules["crons"]

    @property
    def histories(self) -> "histories.HistoriesAPI":
        """Access histories API."""
        from pyarkime.api import histories

        if "histories" not in self._api_modules:
            self._api_modules["histories"] = histories.HistoriesAPI(self._client)
        return self._api_modules["histories"]

    @property
    def shortcuts(self) -> "shortcuts.ShortcutsAPI":
        """Access shortcuts API."""
        from pyarkime.api import shortcuts

        if "shortcuts" not in self._api_modules:
            self._api_modules["shortcuts"] = shortcuts.ShortcutsAPI(self._client)
        return self._api_modules["shortcuts"]

    @property
    def fields(self) -> "fields.FieldsAPI":
        """Access fields API."""
        from pyarkime.api import fields

        if "fields" not in self._api_modules:
            self._api_modules["fields"] = fields.FieldsAPI(self._client)
        return self._api_modules["fields"]

    @property
    def files(self) -> "files.FilesAPI":
        """Access files API."""
        from pyarkime.api import files

        if "files" not in self._api_modules:
            self._api_modules["files"] = files.FilesAPI(self._client)
        return self._api_modules["files"]

    @property
    def delete(self) -> "delete.DeleteAPI":
        """Access delete API."""
        from pyarkime.api import delete

        if "delete" not in self._api_modules:
            self._api_modules["delete"] = delete.DeleteAPI(self._client)
        return self._api_modules["delete"]

    @property
    def eshealth(self) -> "eshealth.ESHealthAPI":
        """Access eshealth API."""
        from pyarkime.api import eshealth

        if "eshealth" not in self._api_modules:
            self._api_modules["eshealth"] = eshealth.ESHealthAPI(self._client)
        return self._api_modules["eshealth"]

    @property
    def buildquery(self) -> "buildquery.BuildQueryAPI":
        """Access buildquery API."""
        from pyarkime.api import buildquery

        if "buildquery" not in self._api_modules:
            self._api_modules["buildquery"] = buildquery.BuildQueryAPI(self._client)
        return self._api_modules["buildquery"]

    @property
    def spiview(self) -> "spiview.SPIViewAPI":
        """Access spiview API."""
        from pyarkime.api import spiview

        if "spiview" not in self._api_modules:
            self._api_modules["spiview"] = spiview.SPIViewAPI(self._client)
        return self._api_modules["spiview"]

    @property
    def unique(self) -> "unique.UniqueAPI":
        """Access unique API."""
        from pyarkime.api import unique

        if "unique" not in self._api_modules:
            self._api_modules["unique"] = unique.UniqueAPI(self._client)
        return self._api_modules["unique"]

    @property
    def valueactions(self) -> "valueactions.ValueActionsAPI":
        """Access valueactions API."""
        from pyarkime.api import valueactions

        if "valueactions" not in self._api_modules:
            self._api_modules["valueactions"] = valueactions.ValueActionsAPI(self._client)
        return self._api_modules["valueactions"]

    @property
    def fieldactions(self) -> "fieldactions.FieldActionsAPI":
        """Access fieldactions API."""
        from pyarkime.api import fieldactions

        if "fieldactions" not in self._api_modules:
            self._api_modules["fieldactions"] = fieldactions.FieldActionsAPI(self._client)
        return self._api_modules["fieldactions"]

    @property
    def upload(self) -> "upload.UploadAPI":
        """Access upload API."""
        from pyarkime.api import upload

        if "upload" not in self._api_modules:
            self._api_modules["upload"] = upload.UploadAPI(self._client)
        return self._api_modules["upload"]

    @property
    def esindices(self) -> "esindices.ESIndicesAPI":
        """Access esindices API."""
        from pyarkime.api import esindices

        if "esindices" not in self._api_modules:
            self._api_modules["esindices"] = esindices.ESIndicesAPI(self._client)
        return self._api_modules["esindices"]

    @property
    def estasks(self) -> "estasks.ESTasksAPI":
        """Access estasks API."""
        from pyarkime.api import estasks

        if "estasks" not in self._api_modules:
            self._api_modules["estasks"] = estasks.ESTasksAPI(self._client)
        return self._api_modules["estasks"]

    @property
    def esadmin(self) -> "esadmin.ESAdminAPI":
        """Access esadmin API."""
        from pyarkime.api import esadmin

        if "esadmin" not in self._api_modules:
            self._api_modules["esadmin"] = esadmin.ESAdminAPI(self._client)
        return self._api_modules["esadmin"]

    @property
    def esshards(self) -> "esshards.ESShardsAPI":
        """Access esshards API."""
        from pyarkime.api import esshards

        if "esshards" not in self._api_modules:
            self._api_modules["esshards"] = esshards.ESShardsAPI(self._client)
        return self._api_modules["esshards"]

    @property
    def esrecovery(self) -> "esrecovery.ESRecoveryAPI":
        """Access esrecovery API."""
        from pyarkime.api import esrecovery

        if "esrecovery" not in self._api_modules:
            self._api_modules["esrecovery"] = esrecovery.ESRecoveryAPI(self._client)
        return self._api_modules["esrecovery"]

    @property
    def parliament(self) -> "parliament.ParliamentAPI":
        """Access parliament API."""
        from pyarkime.api import parliament

        if "parliament" not in self._api_modules:
            self._api_modules["parliament"] = parliament.ParliamentAPI(self._client)
        return self._api_modules["parliament"]


class AsyncArkimeClient(BaseClient):
    """Asynchronous client for Arkime API."""

    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        timeout: float = 30.0,
        verify: bool = True,
    ) -> None:
        """Initialize asynchronous Arkime client.

        Args:
            base_url: Base URL of Arkime instance
            username: Username for digest authentication
            password: Password for digest authentication
            timeout: Request timeout in seconds
            verify: Whether to verify SSL certificates
        """
        super().__init__(base_url, username, password, timeout, verify)

        # Create asynchronous httpx client
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            auth=self._auth,
            timeout=self.timeout,
            verify=self.verify,
        )

        # Initialize API modules
        self._init_api_modules()

    def _init_api_modules(self) -> None:
        """Initialize API endpoint modules."""
        pass

    async def __aenter__(self) -> "AsyncArkimeClient":
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    @property
    def sessions(self) -> "sessions.AsyncSessionsAPI":
        """Access sessions API."""
        from pyarkime.api import sessions

        if "sessions" not in self._api_modules:
            self._api_modules["sessions"] = sessions.AsyncSessionsAPI(self._client)
        return self._api_modules["sessions"]

    @property
    def hunt(self) -> "hunt.AsyncHuntAPI":
        """Access hunt API."""
        from pyarkime.api import hunt

        if "hunt" not in self._api_modules:
            self._api_modules["hunt"] = hunt.AsyncHuntAPI(self._client)
        return self._api_modules["hunt"]

    @property
    def views(self) -> "views.AsyncViewsAPI":
        """Access views API."""
        from pyarkime.api import views

        if "views" not in self._api_modules:
            self._api_modules["views"] = views.AsyncViewsAPI(self._client)
        return self._api_modules["views"]

    @property
    def stats(self) -> "stats.AsyncStatsAPI":
        """Access stats API."""
        from pyarkime.api import stats

        if "stats" not in self._api_modules:
            self._api_modules["stats"] = stats.AsyncStatsAPI(self._client)
        return self._api_modules["stats"]

    @property
    def crons(self) -> "crons.AsyncCronsAPI":
        """Access crons API."""
        from pyarkime.api import crons

        if "crons" not in self._api_modules:
            self._api_modules["crons"] = crons.AsyncCronsAPI(self._client)
        return self._api_modules["crons"]

    @property
    def histories(self) -> "histories.AsyncHistoriesAPI":
        """Access histories API."""
        from pyarkime.api import histories

        if "histories" not in self._api_modules:
            self._api_modules["histories"] = histories.AsyncHistoriesAPI(self._client)
        return self._api_modules["histories"]

    @property
    def shortcuts(self) -> "shortcuts.AsyncShortcutsAPI":
        """Access shortcuts API."""
        from pyarkime.api import shortcuts

        if "shortcuts" not in self._api_modules:
            self._api_modules["shortcuts"] = shortcuts.AsyncShortcutsAPI(self._client)
        return self._api_modules["shortcuts"]

    @property
    def fields(self) -> "fields.AsyncFieldsAPI":
        """Access fields API."""
        from pyarkime.api import fields

        if "fields" not in self._api_modules:
            self._api_modules["fields"] = fields.AsyncFieldsAPI(self._client)
        return self._api_modules["fields"]

    @property
    def files(self) -> "files.AsyncFilesAPI":
        """Access files API."""
        from pyarkime.api import files

        if "files" not in self._api_modules:
            self._api_modules["files"] = files.AsyncFilesAPI(self._client)
        return self._api_modules["files"]

    @property
    def delete(self) -> "delete.AsyncDeleteAPI":
        """Access delete API."""
        from pyarkime.api import delete

        if "delete" not in self._api_modules:
            self._api_modules["delete"] = delete.AsyncDeleteAPI(self._client)
        return self._api_modules["delete"]

    @property
    def eshealth(self) -> "eshealth.AsyncESHealthAPI":
        """Access eshealth API."""
        from pyarkime.api import eshealth

        if "eshealth" not in self._api_modules:
            self._api_modules["eshealth"] = eshealth.AsyncESHealthAPI(self._client)
        return self._api_modules["eshealth"]

    @property
    def buildquery(self) -> "buildquery.AsyncBuildQueryAPI":
        """Access buildquery API."""
        from pyarkime.api import buildquery

        if "buildquery" not in self._api_modules:
            self._api_modules["buildquery"] = buildquery.AsyncBuildQueryAPI(self._client)
        return self._api_modules["buildquery"]

    @property
    def spiview(self) -> "spiview.AsyncSPIViewAPI":
        """Access spiview API."""
        from pyarkime.api import spiview

        if "spiview" not in self._api_modules:
            self._api_modules["spiview"] = spiview.AsyncSPIViewAPI(self._client)
        return self._api_modules["spiview"]

    @property
    def unique(self) -> "unique.AsyncUniqueAPI":
        """Access unique API."""
        from pyarkime.api import unique

        if "unique" not in self._api_modules:
            self._api_modules["unique"] = unique.AsyncUniqueAPI(self._client)
        return self._api_modules["unique"]

    @property
    def valueactions(self) -> "valueactions.AsyncValueActionsAPI":
        """Access valueactions API."""
        from pyarkime.api import valueactions

        if "valueactions" not in self._api_modules:
            self._api_modules["valueactions"] = valueactions.AsyncValueActionsAPI(self._client)
        return self._api_modules["valueactions"]

    @property
    def fieldactions(self) -> "fieldactions.AsyncFieldActionsAPI":
        """Access fieldactions API."""
        from pyarkime.api import fieldactions

        if "fieldactions" not in self._api_modules:
            self._api_modules["fieldactions"] = fieldactions.AsyncFieldActionsAPI(self._client)
        return self._api_modules["fieldactions"]

    @property
    def upload(self) -> "upload.AsyncUploadAPI":
        """Access upload API."""
        from pyarkime.api import upload

        if "upload" not in self._api_modules:
            self._api_modules["upload"] = upload.AsyncUploadAPI(self._client)
        return self._api_modules["upload"]

    @property
    def esindices(self) -> "esindices.AsyncESIndicesAPI":
        """Access esindices API."""
        from pyarkime.api import esindices

        if "esindices" not in self._api_modules:
            self._api_modules["esindices"] = esindices.AsyncESIndicesAPI(self._client)
        return self._api_modules["esindices"]

    @property
    def estasks(self) -> "estasks.AsyncESTasksAPI":
        """Access estasks API."""
        from pyarkime.api import estasks

        if "estasks" not in self._api_modules:
            self._api_modules["estasks"] = estasks.AsyncESTasksAPI(self._client)
        return self._api_modules["estasks"]

    @property
    def esadmin(self) -> "esadmin.AsyncESAdminAPI":
        """Access esadmin API."""
        from pyarkime.api import esadmin

        if "esadmin" not in self._api_modules:
            self._api_modules["esadmin"] = esadmin.AsyncESAdminAPI(self._client)
        return self._api_modules["esadmin"]

    @property
    def esshards(self) -> "esshards.AsyncESShardsAPI":
        """Access esshards API."""
        from pyarkime.api import esshards

        if "esshards" not in self._api_modules:
            self._api_modules["esshards"] = esshards.AsyncESShardsAPI(self._client)
        return self._api_modules["esshards"]

    @property
    def esrecovery(self) -> "esrecovery.AsyncESRecoveryAPI":
        """Access esrecovery API."""
        from pyarkime.api import esrecovery

        if "esrecovery" not in self._api_modules:
            self._api_modules["esrecovery"] = esrecovery.AsyncESRecoveryAPI(self._client)
        return self._api_modules["esrecovery"]

    @property
    def parliament(self) -> "parliament.AsyncParliamentAPI":
        """Access parliament API."""
        from pyarkime.api import parliament

        if "parliament" not in self._api_modules:
            self._api_modules["parliament"] = parliament.AsyncParliamentAPI(self._client)
        return self._api_modules["parliament"]

