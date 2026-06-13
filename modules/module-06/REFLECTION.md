# Module 6 — Reflection

**Team name**: _______________
**Branch**: `module-06/<team-name>`
**Submitted**: before Module 7 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

The gateway now validates every JWT before forwarding a request. Individual services no longer need to check identity themselves.

**What does centralising authentication at the gateway buy you?** What would the alternative look like — if every service validated tokens on its own?

Think about what happens when you need to rotate the secret key, or add a new service to the system.

> *Your answer:*
Centralising authentication at the gateway makes the system easier to control. I only need one main place to reject missing or invalid tokens before the request reaches internal services. If every service checked tokens separately, I would have to repeat the same logic many times, and every new service could become a security risk if I forgot to add validation. It also makes changes easier. For example, if the secret key changes, it is simpler to update the gateway than to update many services one by one.

---

## 2. Your choice

When activity-service calls user-service internally, it uses a Machine-to-Machine (M2M) token — not a user's token.

**Why can't it just reuse the user's token that arrived in the original request?**

What would break, or what door would you accidentally leave open, if services passed user tokens between themselves?

> *Your answer:*
The activity-service should not reuse a user's token because it is not really acting as that user. It is another service doing an internal system call. If services pass user tokens around, the token can travel too far and give services more access than they should have. An M2M token is clearer: it says "this request comes from a service", not from a normal user. That makes the permissions easier to separate and safer.

---

## 3. The tradeoff

The gateway and the auth-service share the same `SECRET_KEY` to verify tokens without making a network call on every request.

**What is the security risk of sharing this key?** What happens if it leaks?

And what would the alternative look like — verifying tokens by calling auth-service on every request instead? What does that cost you?

> *Your answer:*
The risk is that the shared secret key becomes very powerful. If it leaks, someone could create fake valid tokens and pretend to be any user or role. That would be a serious security problem. The alternative is to call auth-service on every request to verify the token. That is safer in some ways because the key is not shared everywhere, but it makes the system slower and more dependent on auth-service. If auth-service is down, then the whole system may stop accepting requests.

---

*Keep this file. You will refer back to it during the oral presentation.*
