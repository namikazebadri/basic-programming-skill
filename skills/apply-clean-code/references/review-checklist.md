# Review Checklist

Use this file when reviewing a patch or planning an incremental clean-code refactor.

- Can a new teammate tell what the code is trying to do?
- Are names specific enough to reveal intent?
- Does each function stay focused on one meaningful responsibility?
- Is the main flow visible without bouncing through too many helpers?
- Are comments still necessary, or should the code be clarified instead?
- Are business rules separated from plumbing where it matters?
- Are side effects and dependencies explicit?
- Did the refactor improve readability without adding unnecessary churn?
- Are tests protecting the changed behavior?
