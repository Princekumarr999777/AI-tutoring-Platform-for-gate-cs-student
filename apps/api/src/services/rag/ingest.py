from dataclasses import dataclass
@dataclass(frozen=True)
class Chunk:
    text: str
    source: str
    page: int
    subject: str
def chunk_text(text: str, source: str, subject: str, size: int = 900, overlap: int = 120) -> list[Chunk]:
    if size <= overlap or overlap < 0: raise ValueError("size must exceed overlap")
    clean = " ".join(text.split())
    return [Chunk(clean[i:i+size], source, 1, subject) for i in range(0, len(clean), size-overlap) if clean[i:i+size]]
