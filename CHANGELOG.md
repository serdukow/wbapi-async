# Changelog

## [1.1.0](https://github.com/serdukow/wbapi-async/compare/v1.0.3...v1.1.0) (2026-08-26)


### Features

* preserve unknown API fields as extras on WBModel ([38ee9d8](https://github.com/serdukow/wbapi-async/commit/38ee9d8724b74e074ce8afdcb752f8bb2b41e641))
* preserve unknown API fields as extras on WBModel ([f898f45](https://github.com/serdukow/wbapi-async/commit/f898f4549cd7991651d7d53e8b1ce4056a37d537))

## [1.0.3](https://github.com/serdukow/wbapi-async/compare/v1.0.2...v1.0.3) (2026-08-26)


### Bug Fixes

* detect pagination behind allOf and stop rounding the coverage badge ([8971b97](https://github.com/serdukow/wbapi-async/commit/8971b97de2602e44555362ac21b5c6bd779402c9))

## [1.0.2](https://github.com/serdukow/wbapi-async/compare/v1.0.1...v1.0.2) (2026-08-26)


### Bug Fixes

* **codegen:** merge allOf branches and follow refs for descriptions ([099cb7c](https://github.com/serdukow/wbapi-async/commit/099cb7c178054814dff76469a8bd66c231233c6f))
* **codegen:** resolve response refs and type file downloads ([65e8b8e](https://github.com/serdukow/wbapi-async/commit/65e8b8ed82a78f986e1ce93aced8cc001ff4c024))

## [1.0.1](https://github.com/serdukow/wbapi-async/compare/v1.0.0...v1.0.1) (2026-08-25)


### Bug Fixes

* **ci:** check the built commit belongs to main, not the reverse ([6c6a60c](https://github.com/serdukow/wbapi-async/commit/6c6a60ca556b9065ba890a82fe14dd667671a8fa))
* **ci:** check the built commit belongs to main, not the reverse ([d4b1b1c](https://github.com/serdukow/wbapi-async/commit/d4b1b1ce13fe36b78fd1c0a5d94745d792084416))
* **ci:** dispatch the PyPI workflow instead of calling it ([f7c9138](https://github.com/serdukow/wbapi-async/commit/f7c9138359cf652c18176d89659badcf4df09084))
* **ci:** dispatch the PyPI workflow instead of calling it ([8057040](https://github.com/serdukow/wbapi-async/commit/8057040a46cb3f0eb89fca6f987af89abcec75d5))
* **codegen:** follow schemas deep enough to type them ([e34701b](https://github.com/serdukow/wbapi-async/commit/e34701b293512239e942121909a1f51fb6dee15f))
* **codegen:** follow schemas deep enough to type them ([d29fadb](https://github.com/serdukow/wbapi-async/commit/d29fadb4df1fa9a373e3e793d9dcc99cf73cba86))

## [1.0.0](https://github.com/serdukow/wbapi-async/compare/v1.0.0...v1.0.0) (2026-08-25)


### Features

* **codegen:** carry spec defaults into method signatures ([cee7cf7](https://github.com/serdukow/wbapi-async/commit/cee7cf7901d83ee2d02e81bdabb381b6fcce9132))
* **codegen:** name methods by action instead of URL path ([5df6631](https://github.com/serdukow/wbapi-async/commit/5df6631fd4ff39908859ec833e886d60890960a3))


### Bug Fixes

* **ci:** watch the real section paths and test before generating ([8b0cb7f](https://github.com/serdukow/wbapi-async/commit/8b0cb7fa40e557bd48d69ed11e5279b771d94a6c))
* **codegen:** read the sustained rate, not the burst columns ([93f3ce5](https://github.com/serdukow/wbapi-async/commit/93f3ce532556fc9c286ed7d165e5fa718ff23ca6))
* **deps:** upgrade the lockfile off a vulnerable idna ([a40671d](https://github.com/serdukow/wbapi-async/commit/a40671dd593118cad2d741515c44a30acbd85986))
* handle non-ASCII names, irregular plurals, and edge cases in codegen ([1440caf](https://github.com/serdukow/wbapi-async/commit/1440caf87f279d8cf3bb64f7390f070576e23e87))
* **session:** give each endpoint its own rate limiter ([c4933c3](https://github.com/serdukow/wbapi-async/commit/c4933c33ba58a8f67a4fd8bd99875028730cb536))
* **test:** open the live client per test, not per module ([50a2c69](https://github.com/serdukow/wbapi-async/commit/50a2c69c94f05e3871dabe3b1200a4e63ec4a35a))


### Changes

* **codegen:** drop the content segment from method names ([127c830](https://github.com/serdukow/wbapi-async/commit/127c830d9a99187e38a0884d5a35d6f3aaff4481))
* move sections into the package root ([5c8a8f7](https://github.com/serdukow/wbapi-async/commit/5c8a8f7774ca3867bc3c68a697649b6b46e9cc90))
* shorten method names and redo the 1.0.0rc2 release ([fd46650](https://github.com/serdukow/wbapi-async/commit/fd466507eb00287054964354f26383badd38d0a5))
* **smoke_check:** read sections from the SECTIONS registry ([c57a087](https://github.com/serdukow/wbapi-async/commit/c57a08727ff6c9ffbefb8f88a36c247477f110a8))
