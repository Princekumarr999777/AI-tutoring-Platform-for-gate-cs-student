# API
FastAPI serves OpenAPI at `/openapi.json` and interactive docs at `/docs`.
```sh
curl localhost:8000/health
curl -X POST localhost:8000/api/v1/auth/register -H 'Content-Type: application/json' -d '{"email":"learner@example.com","password":"secure-password-123"}'
curl -X POST localhost:8000/api/v1/auth/login -H 'Content-Type: application/json' -d '{"email":"learner@example.com","password":"secure-password-123"}'
curl localhost:8000/api/v1/auth/me -H 'Authorization: Bearer ACCESS_TOKEN'
```
Register, login, refresh and protected me endpoints use JSON; errors include `detail`; responses receive `X-Request-ID`.
