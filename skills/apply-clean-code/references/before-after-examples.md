# Before And After Examples

Use this file when the user wants concrete examples of code becoming cleaner without unnecessary abstraction.

## Better Naming And Flow

### Before

```go
func Process(items []Item) []Item {
    result := []Item{}
    for _, x := range items {
        if x.Active {
            result = append(result, x)
        }
    }
    return result
}
```

### After

```go
func FilterActiveItems(items []Item) []Item {
    activeItems := make([]Item, 0, len(items))
    for _, item := range items {
        if item.Active {
            activeItems = append(activeItems, item)
        }
    }
    return activeItems
}
```

Why this is better:

- The function name reveals intent.
- Variable names reduce mental translation.
- The flow stays simple and direct.

## Flatten Nested Validation

### Before

```kotlin
fun createUser(req: CreateUserRequest): User {
    if (req.email != null) {
        if (req.password != null) {
            if (req.password.length >= 8) {
                return userService.create(req.email, req.password)
            }
        }
    }
    throw IllegalArgumentException("invalid request")
}
```

### After

```kotlin
fun createUser(req: CreateUserRequest): User {
    val email = req.email ?: throw IllegalArgumentException("email is required")
    val password = req.password ?: throw IllegalArgumentException("password is required")
    require(password.length >= 8) { "password is too short" }

    return userService.create(email, password)
}
```

Why this is better:

- The happy path is obvious.
- Validation is explicit and local.
- Nesting no longer hides the main behavior.

## Replace Comment With Clearer Code

### Before

```python
def total(items):
    # sum only paid items
    amount = 0
    for i in items:
        if i.status == "paid":
            amount += i.price
    return amount
```

### After

```python
def total_paid_amount(items):
    total_amount = 0
    for item in items:
        if item.status == "paid":
            total_amount += item.price
    return total_amount
```

Why this is better:

- The name replaces the comment.
- The function reads in domain terms.

## Extract Responsibility Without Over-Splitting

### Before

```ts
function submitOrder(order: Order) {
  validate(order);
  const total = calculateTotal(order);
  console.log("submitting", total);
  return http.post("/orders", { ...order, total });
}
```

### After

```ts
function submitOrder(order: Order) {
  validate(order);
  const payload = buildOrderPayload(order);
  console.log("submitting", payload.total);
  return http.post("/orders", payload);
}

function buildOrderPayload(order: Order) {
  return {
    ...order,
    total: calculateTotal(order),
  };
}
```

Why this is better:

- The top-level function keeps a clearer story.
- Extraction supports the reader instead of hiding the flow.
