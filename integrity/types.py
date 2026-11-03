"""Data objects keep raw extraction separate from normalized scoring tokens."""

from dataclasses import dataclass, field


@dataclass
class Unit:
    text: str
    location: dict


@dataclass
class Token:
    value: str
    unit: int
    start: int
    end: int


@dataclass
class Document:
    document_id: str
    kind: str
    sha256: str = ""
    status: str = "ok"
    units: list[Unit] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    tokens: list[Token] = field(default_factory=list)
    excluded: dict[int, str] = field(default_factory=dict)


@dataclass
class Window:
    document_id: str
    token_ids: list[int]
    text: str
    model_tokens: int
    role: str = "chunk"
    normalized_text: str = ""
