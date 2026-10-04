# Architecture and scalability

```mermaid
flowchart LR
 Client --> LB[Cloud load balancer]
 LB --> API[Stateless FastAPI replicas]
 API --> PG[(PostgreSQL + pgvector)]
 API --> Redis[(Redis cache/broker)]
 Redis --> Worker[Autoscaled Celery pool]
 API --> AI[Provider interfaces]
```
Scale from 100 to 100,000 users with horizontal stateless API replicas, pooled DB connections/read replicas, managed or sharded Redis, and queue-depth worker autoscaling. Batch model calls, cache embeddings, and enforce model quotas. pgvector works for early millions; benchmark and consider Milvus above roughly 10M vectors behind the VectorStore interface.
