# Module 5 — Reflection

**Team name**: _______________
**Branch**: `module-05/<team-name>`
**Submitted**: before Module 6 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

The game-service now has two models for the same data: SQLite for writes, Redis for reads. They store the same games in two different shapes.

**Why go through the trouble of maintaining two representations of the same data?**

Think about what kind of queries each model is optimised for, and what would happen if you tried to use the write model for high-traffic read operations.

> *Your answer:*
We maintain two representations because the system has two different needs. SQLite is better as the source of truth: it stores the full game data and is safer for writes. Redis is better for fast reads, especially for small summaries that could be requested very often.If every high-traffic read used SQLite, the write model could become overloaded and slower. The Redis summary is simpler and faster because it only contains the data needed for display, not the full authoritative record.


---

## 2. Your choice

The logging-service checks GDPR consent before recording any activity. If a user has not opted in, the log is silently dropped.

**What does this consent check force you to accept about your data?** It is incomplete by design — some activities will never be recorded.

From a system design perspective: where is the right place to enforce this rule — in the logging-service, in the activity-service, or at the gateway? Why?

> *Your answer:*
The consent check forces me to accept that the logs are intentionally incomplete. If the user did not give consent, the system must not store their activity, even if that means losing useful analytics or debugging information. I think the right place to enforce this rule is the logging-service. The gateway should only route requests, and the activity-service should only publish activity events.The logging-service owns the decision about what it is legally allowed to store, so it should check consent before writing logs.


---

## 3. The tradeoff

With CQRS, your write model and read model can drift out of sync — a game is updated in SQLite but the Redis projection still shows the old data.

**In what scenario does this inconsistency matter to the user? In what scenario is it completely acceptable?**

Is there a class of applications where eventual consistency is never acceptable? What are they?

> *Your answer:*
This inconsistency matters if the user sees wrong important information, for example if a game title or platform was changed but the summary still shows the old version. It could confuse the user because different endpoints show different data. It is acceptable when the data is not critical, like a cached game summary or a cover image that updates a few seconds later. In that case, faster reads are worth the small delay. Eventual consistency is not acceptable for systems where wrong or stale data can cause real damage, for example banking, payments, medical records, or legal/identity systems. In those cases, the user must see accurate data immediately.

---

*Keep this file. You will refer back to it during the oral presentation.*
