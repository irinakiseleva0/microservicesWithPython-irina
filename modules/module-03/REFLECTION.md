# Module 3 — Reflection

**Team name**: _______________
**Branch**: `module-03/<team-name>`
**Submitted**: before Module 4 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

All client requests now go through the gateway. No client ever calls a service directly.

**Why does that single entry point exist? What would the client's life look like without it?**

Think about what the client would need to know and manage if it talked to each service on its own port.

> *Your answer:*
The gateway makes things much simpler for the client because the frontend only needs to know one address instead of keeping track of multiple services and ports. Without it, the client would need to know where user-service, game-service, and activity-service are running, which feels messy and hard to maintain. If I changed a service port or moved it somewhere else, I would also have to update the client. With the gateway, all that routing logic stays in one place.

---

## 2. Your choice

The activity-service makes two outbound calls: one to validate the user (with retry logic), one to fetch game data (with a null fallback if it fails).

**Why are these two calls treated differently? Why does one retry and the other just give up gracefully?**

What is the consequence for the user in each case if the downstream service is unavailable?

> *Your answer:*
I treated these calls differently because they don’t have the same importance. Validating the user is required because it would be a data integrity problem if activities were created for users that don’t actually exist. That’s why retrying makes sense in case the user-service is temporarily unavailable. Fetching game data feels more like extra information rather than something required for the activity itself. If game-service is down, the user should still be able to create the activity instead of being blocked by a non-critical dependency. Returning "game": null felt like the better user experience.
---

## 3. The tradeoff

Every time a client creates an activity, three services are involved synchronously. They all have to be running, healthy, and fast.

**What is the systemic risk of chaining synchronous calls like this?**

What happens to the user experience if the slowest service in the chain takes 3 seconds to respond?

> *Your answer:*
The risk with synchronous service chaining is that the whole request becomes dependent on every service being available and responsive at the same time. Even if my activity-service works perfectly, a slow or failing dependency can still make the whole request feel broken. If the slowest service takes 3 seconds, the user will feel that delay directly, and if multiple services are slow, the waiting time adds up quickly. In a real application, this would make the system feel unreliable even if only one service has performance issues.
---

*Keep this file. You will refer back to it during the oral presentation.*
