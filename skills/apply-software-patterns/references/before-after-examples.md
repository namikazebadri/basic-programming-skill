# Before And After Examples

Use this file when the user wants concrete examples of how code can become clearer with or without a pattern.

## Strategy Versus Growing Conditionals

### Before

```ts
function calculateShipping(method: string, weight: number) {
  if (method === "standard") {
    return weight * 1.2;
  }
  if (method === "express") {
    return weight * 2.4 + 10;
  }
  if (method === "pickup") {
    return 0;
  }
  throw new Error("unknown method");
}
```

### After

```ts
type ShippingPolicy = (weight: number) => number;

const shippingPolicies: Record<string, ShippingPolicy> = {
  standard: (weight) => weight * 1.2,
  express: (weight) => weight * 2.4 + 10,
  pickup: () => 0,
};

function calculateShipping(method: string, weight: number) {
  const policy = shippingPolicies[method];
  if (!policy) throw new Error("unknown method");
  return policy(weight);
}
```

Why this is better:

- Variation is isolated without introducing heavy class structure.
- The main flow reads directly.
- Adding a new policy is local and testable.

## Reject Strategy When The Conditional Is Still Small

### Before

```py
def normalize(role: str) -> str:
    if role == "admin":
        return "ADMIN"
    return "USER"
```

### After

```py
def normalize_role(role: str) -> str:
    return "ADMIN" if role == "admin" else "USER"
```

Why this is better:

- The simpler refactor improves naming without adding indirection.
- A full pattern would be ceremony with no real payoff.

## Adapter Around An External Dependency

### Before

```go
func SendWelcomeEmail(client *thirdparty.Client, user User) error {
    payload := map[string]any{
        "recipient": user.Email,
        "template":  "welcome-v2",
    }
    return client.Dispatch(payload)
}
```

### After

```go
type Mailer interface {
    SendWelcome(email string) error
}

type ThirdPartyMailer struct {
    client *thirdparty.Client
}

func (m ThirdPartyMailer) SendWelcome(email string) error {
    return m.client.Dispatch(map[string]any{
        "recipient": email,
        "template":  "welcome-v2",
    })
}
```

Why this is better:

- The business call site depends on intent, not SDK shape.
- Only the unstable boundary is wrapped.

## Repository Boundary For Leaking Persistence

### Before

```java
public OrderSummary loadOrderSummary(long orderId) {
    var row = jdbc.queryForMap("select * from orders where id = ?", orderId);
    if ("PAID".equals(row.get("status"))) {
        return new OrderSummary(orderId, true);
    }
    return new OrderSummary(orderId, false);
}
```

### After

```java
public interface OrderRepository {
    OrderRecord findById(long orderId);
}

public OrderSummary loadOrderSummary(long orderId) {
    OrderRecord order = orderRepository.findById(orderId);
    return new OrderSummary(order.id(), order.isPaid());
}
```

Why this is better:

- Persistence concerns stop leaking into business logic.
- The use case reads in domain terms.

## Modular Monolith Before Microservices

### Before

```text
One large app with packages importing each other freely.
Teams propose microservices because the codebase feels tangled.
```

### After

```text
One deployable app, but modules have explicit boundaries:
- billing
- catalog
- checkout

Cross-module calls go through clear interfaces or application services.
```

Why this is better:

- Structural clarity improves before operational complexity is added.
- It tests whether the real issue is boundaries, not deployment shape.

## Fluent Interface Only When It Helps

### Before

```ts
const query = new UserQueryBuilder();
query.filterActive();
query.sortByName();
query.limit(20);
return query.run();
```

### After

```ts
return userQuery()
  .active()
  .sortedByName()
  .limit(20)
  .run();
```

Why this is better:

- The chain reads as one intention.
- If mutation or side effects became hidden, plain functions would be better.
