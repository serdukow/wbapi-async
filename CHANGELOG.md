# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0](https://github.com/serdukow/wbapi-async/compare/v0.3.2...v0.4.0) (2026-04-16)


### Features

* fallback to URL-based naming for duplicate GET method summaries ([9cff9c4](https://github.com/serdukow/wbapi-async/commit/9cff9c4e7c37a23185550d813b75a8d64a590dc8))
* fallback to URL-based naming for duplicate GET method summaries ([e1ec3b6](https://github.com/serdukow/wbapi-async/commit/e1ec3b6bf73ece41996b0cd8b3d79f4f7c51d1a2))

## [0.3.2](https://github.com/serdukow/wbapi-async/compare/v0.3.1...v0.3.2) (2026-04-16)


### Bug Fixes

* remove enums, fix camelCase conversion, always emit aliases, fix empty JSON body ([b5b87ca](https://github.com/serdukow/wbapi-async/commit/b5b87cab3ed4abd03600b5b325ea6a71c1eedbff))
* remove enums, fix camelCase conversion, always emit aliases, fix… ([9348303](https://github.com/serdukow/wbapi-async/commit/934830371ebe8be45e28d138c444a556f71b0823))

## [0.3.0](https://github.com/serdukow/wbapi-async/compare/v0.2.3...v0.3.0) (2026-04-16)


### Features

* add typed models for promotion stats and product data ([3b4281a](https://github.com/serdukow/wbapi-async/commit/3b4281a5b9db57faf994b5cc5645cdb4c6e6f87a))


### Bug Fixes

* add typed models for promotion stats and product data ([47f5b8e](https://github.com/serdukow/wbapi-async/commit/47f5b8e3194068cf363f02e2203388ad9551d7ee))

## [0.2.3](https://github.com/serdukow/wbapi-async/compare/v0.2.2...v0.2.3) (2026-04-16)


### Bug Fixes

* **codegen:** fix nested type imports, circular imports, and test moc… ([638c88f](https://github.com/serdukow/wbapi-async/commit/638c88f3d3c3558908c974e7a9b7c0b4544e2b73))
* **codegen:** fix nested type imports, circular imports, and test mock quality ([d677904](https://github.com/serdukow/wbapi-async/commit/d677904cd8c70b3661c9dd88a215f7729fcc5590))

## [0.2.1](https://github.com/serdukow/wbapi-async/compare/v0.2.0...v0.2.1) (2026-04-15)


### Bug Fixes

* **analytics:** add request params to product_data method ([4b13005](https://github.com/serdukow/wbapi-async/commit/4b13005cc8c7895cdf3ce326011ad0765154a545))
* **analytics:** add request params to product_data method ([b7a0161](https://github.com/serdukow/wbapi-async/commit/b7a0161ff82e5dc635f097979bfb9208194070ce))

## [0.2.0](https://github.com/serdukow/wbapi-async/compare/v0.1.0...v0.2.0) (2026-04-14)


### Features

* **codegen:** add source links to methods in PR body ([0710d2c](https://github.com/serdukow/wbapi-async/commit/0710d2c408f602f5415e02fd182fa823a406c425))
* **reports:** add GetGoodsReturn method and GoodsReturnItem type ([ce4f531](https://github.com/serdukow/wbapi-async/commit/ce4f531b543f8a234dab84ef3750ae2d7a02674e))
* **reports:** add GetGoodsReturn method and GoodsReturnItem type ([cc19462](https://github.com/serdukow/wbapi-async/commit/cc194621e532e31c84a784ca79be54c99603f096))

## [0.1.0](https://github.com/serdukow/wbapi-async/compare/v0.0.6...v0.1.0) (2026-03-23)


### Features

* add 40+ new WB API methods for products and warehouses ([504b48a](https://github.com/serdukow/wbapi-async/commit/504b48ad9c169a27a7d976b1d84c3ce0d64191a1))
* add PATCH method support and refactor product cards API ([b3382eb](https://github.com/serdukow/wbapi-async/commit/b3382eb46b684722cbe7e068d9d9b15e58313882))
* reorganize source into domain-specific module subdirectories ([82617aa](https://github.com/serdukow/wbapi-async/commit/82617aab10a7ff6b9f3a236cbaa1d6080ad781ae))
* replace auto-pagination with explicit paginate() utility ([03da7ad](https://github.com/serdukow/wbapi-async/commit/03da7addf40775500adcc627b1d09b5221f0c44b))


### Bug Fixes

* preserve original error when response body is not JSON ([ca2bf59](https://github.com/serdukow/wbapi-async/commit/ca2bf5954a9ff903b1cbb08e9c6ba4a107c5cd1b))
* rename builtins, required params have no default in api.py ([6f41595](https://github.com/serdukow/wbapi-async/commit/6f41595908d27db1e5134be67296e415f679de5a))


### Documentation

* add AGENTS.md with project guidelines, symlink CLAUDE.md to it ([b436ec0](https://github.com/serdukow/wbapi-async/commit/b436ec01c88b83f4b89419128e1b2de737680a87))
* add mkdocs-material documentation with gh-pages deploy ([dd1349d](https://github.com/serdukow/wbapi-async/commit/dd1349d659e6b0461801d7db1ff2f7f6ba810d66))
* add note about auto-generated API methods from OpenAPI specs ([28906dd](https://github.com/serdukow/wbapi-async/commit/28906dda4aff10736abfa0e1197222770a044ea9))
* add uv sync --all-extras command to AGENTS.md ([3a23d28](https://github.com/serdukow/wbapi-async/commit/3a23d28e227a92815042f9f08d4ae7cf3492e778))
* simplify README and link docs/index.md to README ([df57f60](https://github.com/serdukow/wbapi-async/commit/df57f60890f5144006098bca800c63fb73530d40))
* update AGENTS.md with pagination API and structure changes ([25ea154](https://github.com/serdukow/wbapi-async/commit/25ea1547fa16752500f5c4641cd6e3301bef1064))
* update codegen description to reflect event-driven updates ([b6cdb67](https://github.com/serdukow/wbapi-async/commit/b6cdb67bdf762d654efb3ded238f0dc4bff0d57d))
* update codegen link to include wb api reference ([96352d2](https://github.com/serdukow/wbapi-async/commit/96352d233bf120bdb94d052d7c2f52bb511d23cf))

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
