# Misuse Signals

Use this file to pressure-test a SOLID recommendation before proposing it.

- SRP used to split one cohesive workflow into too many files
- OCP interpreted as "never touch existing code"
- LSP ignored while subclass behavior quietly changes semantics
- ISP implemented as many trivial interfaces with no real consumer focus
- DIP used to hide direct dependencies that were already clear
- Test mocking pressure alone driving architecture
- Interfaces mirroring implementations one-to-one without independent value
- Refactors increasing concept count faster than understanding
