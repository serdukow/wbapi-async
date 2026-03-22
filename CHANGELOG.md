# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0b1] - 2026-03-22

### Added

- Domain-specific module structure (`products/`, `analytics/`, `orders_fbs/`, etc.)
- Flat re-exports for backward compatibility (`from wbapi_async.types import AnyType`)
- `py.typed` marker for PEP 561 type checker support
- `__version__` attribute via `importlib.metadata`
- Public exports for `WbAPIError` and `TokenValidationError`
- GitHub Actions lint workflow with ruff autofix on PRs
- Pull request template
- CHANGELOG.md and CONTRIBUTING.md
- PyPI classifiers: `Framework :: AsyncIO`, `Framework :: Pydantic :: 2`, `Typing :: Typed`

### Changed

- Version bumped to `0.1.0b1` (beta)
- Development status classifier: `Pre-Alpha` -> `Beta`
- Ruff line-length increased to 110 for generated import paths
- Enum names now use path-based disambiguation (e.g. `SortBlocked`, `SortShadowed`)
- Enum members use values as defaults in API method signatures

## [0.0.8] - 2026-03-10

### Added

- Auto-generated API methods, types, and tests from Wildberries OpenAPI specs
- 280+ API methods covering all 13 WB API domains
- Auto-pagination for list endpoints
- Rate limiting per method with `aiolimiter`
- Automatic retry on HTTP 429
- JWT token validation (structure, required fields, expiry)
- Unofficial method support with `@unofficial` decorator
- Mocked API infrastructure for testing
- CI/CD: test matrix (Python 3.11-3.13), PyPI release workflow
- Pre-commit hooks (ruff, prettier, gitlint)

### Changed

- Dropped Python 3.10 support
- Added PATCH HTTP method support

[0.1.0b1]: https://github.com/serdukow/wbapi-async/compare/v0.0.8...HEAD
[0.0.8]: https://github.com/serdukow/wbapi-async/releases/tag/v0.0.8
