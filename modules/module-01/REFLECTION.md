## YOU NEED TO COMMIT THIS FILE BEFORE MOVING ON TO THE NEXT MODULE ! 🚨

**feel free to delete this comment**

# Module 1 — Reflection

**Team name**:**irina**
**Branch**: `module-01/irina`
**Submitted**: before Module 2 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You started from a painful monolith. Now you're splitting it into separate services.

**What concrete problem does that split solve: and for whom?**

Think about it from three angles: the developer who has to change code, the team that has to deploy it, and the user who has to live with its failures. You don't need to cover all three, pick the one that felt most real to you today.

> _Your answer:_
For me, the biggest reason to split the monolith is maintainability. In one large application, even a small change can affect unrelated parts of the system, which makes development stressful and slow. If I only need to update user profiles, I should not have to worry about notifications or logging logic breaking. From the user perspective, this also makes the system more reliable, because if one service has a problem, the whole platform does not necessarily go down.


---

## 2. Your choice

Look at your service map. Every arrow between two services is a decision someone made.

**Pick one boundary, one place where you decided service A should not be part of service B. Explain why that line exists.**

What would break, slow down, or become harder to manage if you merged those two services back together?

> _Your answer:_
One decision I made was keeping the activity service separate from the logging service. At first they sounded similar because both deal with events, but I realized they actually have different responsibilities. Activity is part of the product logic, like tracking what the user does in the app, while logging is more about audit records, traceability, and compliance requirements like GDPR. If they were combined, the service would become harder to maintain because product features and compliance logic would be mixed together.


---

## 3. The tradeoff

Microservices solve the monolith's problems. But they create new ones.

**Name one thing that was simpler in the monolith and is now harder in your distributed design.**

No need to solve it: just name it honestly. This is exactly the tension the rest of the course is about.

> _Your answer:_
One thing that was definitely simpler in the monolith is communication between components. Everything could directly call functions in the same codebase, and data access was straightforward. In a microservice architecture, even simple actions may require REST calls or asynchronous messaging, which means dealing with network failures, debugging distributed flows, and keeping services in sync.
---

_Keep this file. You will refer back to it during the oral presentation._
