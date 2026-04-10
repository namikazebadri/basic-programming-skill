# Before And After Examples

Use this file when the user wants concrete examples of focused SOLID refactors.

## Narrow An Interface

### Before

```go
type UserStore interface {
    Save(User) error
    Delete(string) error
    Find(string) (User, error)
    Count() (int, error)
}
```

### After

```go
type UserFinder interface {
    Find(string) (User, error)
}
```

Why this is better:

- Consumers depend only on what they use.
- ISP is applied without inventing a framework.

## Separate A Responsibility

### Before

```kotlin
class InvoiceService(
    private val repo: InvoiceRepository,
    private val email: EmailClient,
) {
    fun send(invoice: Invoice) {
        validate(invoice)
        repo.save(invoice)
        email.send(invoice.customerEmail)
    }
}
```

### After

```kotlin
class InvoiceSaver(private val repo: InvoiceRepository) {
    fun save(invoice: Invoice) {
        validate(invoice)
        repo.save(invoice)
    }
}

class InvoiceNotifier(private val email: EmailClient) {
    fun send(invoice: Invoice) {
        email.send(invoice.customerEmail)
    }
}
```

Why this is better:

- Persistence and notification stop changing for the same reason.
- SRP improves ownership without a large rewrite.
