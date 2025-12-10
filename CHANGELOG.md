# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-12-10

### Added
- Initial release of pyarkime
- Support for Arkime API v3.x-5.x endpoints
- Synchronous (`ArkimeClient`) and asynchronous (`AsyncArkimeClient`) client interfaces
- Comprehensive type hints with Python 3.11+ support
- Pydantic models for request/response validation
- Digest authentication support
- TLS certificate verification control (`verify` parameter)
- Comprehensive error handling with custom exception classes:
  - `ArkimeError`: Base exception class
  - `ArkimeAPIError`: API-related errors
  - `ArkimeAuthError`: Authentication errors
  - `ArkimeNotFoundError`: Resource not found errors
  - `ArkimeConnectionError`: Connection errors

### API Endpoints Supported
- **Sessions**: Search, retrieve, and manage sessions
- **Hunt**: Create and manage packet search jobs
- **Views**: Create and manage database views
- **Stats**: Get statistics and health information
- **Crons**: Manage periodic queries
- **Histories**: Access search history
- **Shortcuts**: Create and manage shortcuts
- **Fields**: List available fields
- **Files**: List files
- **ESHealth**: Elasticsearch health information
- **BuildQuery**: Build query expressions
- **SPIView**: SPI view data
- **Unique**: Get unique field values
- **ValueActions**: Field value actions
- **FieldActions**: Field actions
- **Upload**: File upload functionality
- **ESIndices**: Elasticsearch indices management
- **ESTasks**: Elasticsearch tasks management
- **ESAdmin**: Elasticsearch admin operations
- **ESShards**: Elasticsearch shards information
- **ESRecovery**: Elasticsearch recovery information
- **Parliament**: Parliament data
- **Delete**: Delete operations

### Documentation
- README with quick start examples
- Full API documentation in `docs/` directory
- Usage examples in `examples/` directory
- Type stubs (`.py.typed` marker file)

### Development
- Test suite with pytest
- Code formatting with black
- Linting with ruff
- Type checking with mypy
- Import sorting with isort

