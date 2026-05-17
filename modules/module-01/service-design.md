# Module 1 — Service Decomposition

## Task 1 — Bounded Contexts

| Bounded Context | Responsibilities | Owned Entities | Team |
|---|---|---|---|
| Auth | Authentication and JWT token management | UserCredentials, Session, Token | Platform |
| User Profile | Managing user profile information | UserProfile | User Team |
| Game Library | Managing available games and user collections | Game, UserGameLibrary | Game Team |
| Activity | Tracking user actions in the platform | ActivityEvent | Activity Team |
| Notification | Sending notifications asynchronously | Notification | Communication Team |
| Logging | Audit logging with GDPR compliance | LogEntry, ConsentRecord | Compliance Team |

## Task 2 — Service Contracts

### gateway → auth-service
Trigger: User login or token validation  
Protocol: REST  
Payload: `{ email, password }` or `{ token }`

### gateway → user-service
Trigger: User updates profile  
Protocol: REST  
Payload: `{ user_id, display_name, bio }`

### activity-service → logging-service
Trigger: Activity event created  
Protocol: RabbitMQ (async)  
Payload: `{ activity_id, user_id, action, timestamp }`

### activity-service → notification-service
Trigger: User action requiring notification  
Protocol: RabbitMQ (async)  
Payload: `{ recipient_id, message }`

## Task 3 — Service Map

```text
Client
  |
Gateway
  |
  +--> auth-service
  +--> user-service
  +--> game-service
  +--> activity-service
           |
      RabbitMQ
       /     \
logging-service  notification-service
```