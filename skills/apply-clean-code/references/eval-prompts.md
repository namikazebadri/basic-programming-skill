# Eval Prompts

Use this file to test whether the skill makes an agent more practical and readability-focused.

A good answer should:

- identify the main readability problem
- prefer the smallest effective cleanup
- explain how comprehension improves
- avoid over-refactoring
- mention test impact when implementation is requested

1. This function works, but no one can tell what `data`, `process`, and `result` mean. How should it be cleaned up first?
2. A 60-line function mixes validation, database writes, logging, and response formatting. What should be extracted, and what should stay together?
3. There are comments above every block explaining obvious code. Should we keep them or change the code itself?
4. A refactor proposal splits one readable function into eight tiny helpers. Is that actually cleaner?
5. A Kotlin use case has nested `if` chains around validation. How would you make the happy path clearer?
6. A Go service has repeated error handling that hides the core flow. What cleanup would improve readability without changing behavior?
7. A patch renames twenty files but barely changes comprehension. Should this be considered a clean-code improvement?
8. A teammate wants to remove duplication, but the duplicated blocks are not actually the same business rule. Should they still be merged?
9. How would you review a PR that is "technically fine" but exhausting to read?
10. Refactor this code to be easier for a new teammate to follow, but avoid broad rewrites.
