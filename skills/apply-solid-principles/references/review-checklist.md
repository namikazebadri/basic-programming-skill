# Review Checklist

Use this file when reviewing SOLID-oriented design changes.

- Is the main design pressure clear?
- Does one unit change for unrelated reasons?
- Are extension points justified by actual change patterns?
- Can implementations safely substitute for their contracts?
- Are interfaces consumer-shaped rather than broad?
- Are dependencies explicit and pointed in the right direction?
- Did the refactor improve maintainability without harming readability?
- Are tests protecting the changed seam?
