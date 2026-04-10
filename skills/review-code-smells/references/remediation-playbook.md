# Remediation Playbook

Use this file when translating smells into practical next steps.

- For long functions: rename values, flatten the flow, then extract one responsibility at a time.
- For shotgun surgery: centralize one repeated decision or responsibility boundary.
- For feature envy: move the logic closer to the data it truly depends on.
- For primitive obsession: introduce one well-named type or helper where domain meaning is lost.
- For hidden side effects: make mutation and I/O explicit in names or boundaries.
- For abstraction drift: inline or remove one layer that adds no explanatory value.

Stop when comprehension materially improves. Do not keep refactoring just because more cleanup is possible.
