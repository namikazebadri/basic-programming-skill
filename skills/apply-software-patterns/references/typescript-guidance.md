# TypeScript Guidance

Use this file when the codebase is in TypeScript or JavaScript with strong type structure.

## General Notes

- Prefer explicit module boundaries and named exports over sprawling utility files.
- Use functions and plain objects first; introduce classes only when lifecycle, invariants, or behavior grouping genuinely benefit.
- Keep framework details out of domain logic, especially in React, Next.js, NestJS, or Express applications.
- Prefer narrow interfaces and discriminated unions over overly abstract base classes.

## Pattern Notes

- Strategy often fits function maps, discriminated unions, or narrow interfaces.
- Adapter usually works best as a thin wrapper around SDKs, browser APIs, or framework services.
- Builder can fit complex object creation, but plain object factories are often enough.
- Fluent interfaces are acceptable for query builders or DSL-like APIs if side effects remain obvious.
- Repository can help when ORM or API client details leak into use cases.

## Review Reminders

- Check whether types clarify architecture or merely create ceremony.
- Check whether async flow is readable with `Promise` chains, `async/await`, or queues.
- Check whether dependency injection frameworks are hiding too much.
