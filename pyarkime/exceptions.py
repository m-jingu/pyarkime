"""Custom exception classes for pyarkime."""


class ArkimeError(Exception):
    """Base exception for all pyarkime errors."""

    pass


class ArkimeAPIError(ArkimeError):
    """Exception raised for API-related errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response_body: str | None = None,
    ) -> None:
        """Initialize API error.

        Args:
            message: Error message
            status_code: HTTP status code if available
            response_body: Response body if available
        """
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class ArkimeAuthError(ArkimeAPIError):
    """Exception raised for authentication errors."""

    pass


class ArkimeConnectionError(ArkimeError):
    """Exception raised for connection errors."""

    pass


class ArkimeNotFoundError(ArkimeAPIError):
    """Exception raised when a resource is not found."""

    pass


class ArkimeValidationError(ArkimeError):
    """Exception raised for validation errors."""

    pass

