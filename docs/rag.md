# Retrieval augmented generation

```mermaid
flowchart LR
 Upload --> Validate[PDF/DOCX, 10 MB cap]
 Validate --> Extract --> Chunk --> Embed --> PG[(pgvector)]
 Question --> Hybrid[Lexical + semantic search]
 PG --> Hybrid --> Rerank --> LLM --> Answer[Cited answer]
```
Metadata includes document_id, source_uri, page, subject, chunk_index, content_hash, embedding_model and created_at. Ingest extracts, chunks with overlap, embeds and persists. Retrieval fuses vector and keyword matches, reranks, then cites source links. Provider-backed indexing is an extension point.
