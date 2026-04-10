# Eval Prompts

Use this file to test whether the smell-review skill finds high-value issues instead of generic nits.

1. Review this service for the most important maintainability smells and order them by severity.
2. This handler works, but every new feature touches three branches and two helper files. What smell is most expensive here?
3. A refactor adds many wrappers and helper layers. Is this improved design or abstraction drift?
4. A class changes for logging rules, validation rules, and persistence changes. Which smell matters first?
5. A function looks short, but its side effects are hidden and order-dependent. How should that be reviewed?
6. Review this PR and tell me whether the biggest problem is readability, design drift, or duplicated business logic.
