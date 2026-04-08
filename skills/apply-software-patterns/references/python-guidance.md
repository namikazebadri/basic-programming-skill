# Python Guidance

Use this file when the codebase is in Python.

## General Notes

- Prefer simple modules, functions, and dataclasses before class-heavy pattern translations.
- Keep dependency flow explicit; avoid hidden globals and module-level singletons for business logic.
- Use context managers for scope-based resource cleanup whenever possible.
- Keep framework layers thin in Django, FastAPI, or Flask applications so business rules remain testable.

## Pattern Notes

- Strategy often maps cleanly to callables, dictionaries of functions, or small protocol-based objects.
- Adapter works well as a wrapper around external clients, requests sessions, or ORM-specific APIs.
- Repository can be useful, but avoid building a second ORM on top of an ORM.
- Pipeline and function composition are often natural in Python if naming stays clear.
- Dispose-style abstractions are less valuable when `with` blocks already solve lifecycle safely.

## Review Reminders

- Check whether "OO purity" is adding more classes than clarity.
- Check whether duck typing is helping readability or making contracts too implicit.
- Check whether exception and resource-handling paths remain obvious.
