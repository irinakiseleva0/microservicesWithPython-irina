# Module 2 — Reflection

**Team name**: **irina**
**Branch**: `module-02/irina`
**Submitted**: before Module 3 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You built a service with distinct layers: models, schemas, repository, service, and routes — each with a single responsibility.

**Why not just put everything in one file and call it done?**

Think about what happens six months later when someone new joins the team, or when you need to swap SQLite for PostgreSQL. What does the layered structure protect you from?

> *Your answer:*
I think putting everything in one file would be faster at the beginning, but it would become confusing very quickly. When I was building the game service, separating routes, schemas, repository, and service helped me understand where each part belongs. If someone joins later, they do not have to read one huge file and guess what is API logic and what is database logic. It also makes changes safer, for example if we replace SQLite with PostgreSQL, most of the changes should stay close to the database/repository part.
---

## 2. Your choice

Each service owns its data exclusively — no other service is allowed to touch its database directly.

**Pick one entity your service owns (e.g. `User`, `Game`). What would go wrong if another service could write to that table directly?**

Give a concrete scenario, not a general principle.

> *Your answer:*
My service owns the `Game` entity. If another service could write directly to the games table, it could create games with missing or wrong fields, for example a game without a title or with a platform name written in a different format. Then the game-service API could return broken or inconsistent data even though the bug came from another service. I prefer that other services ask game-service through its API, so the game-service stays responsible for validating and protecting its own data.

---

## 3. The tradeoff

You now have models, schemas, a repository, a service, and routes — five layers for what is essentially a CRUD service.

**For a system this small, what is the cost of all this structure?**

And at what point does the complexity start to pay off? Where is the tipping point?

> *Your answer:*
For a small CRUD service, the cost is that there are many files for something simple. Sometimes it feels like I am jumping between five layers just to add one endpoint. But I think it starts to pay off when the service grows beyond basic CRUD, or when more people work on the same code. At that point, the structure helps avoid messy code and makes it easier to change one part without breaking everything.
---

*Keep this file. You will refer back to it during the oral presentation.*
