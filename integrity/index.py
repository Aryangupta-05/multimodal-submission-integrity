"""Normalized dense vectors and exact NumPy Flat inner-product search."""

from hashlib import sha256
from pathlib import Path

import numpy as np


class Embedder:
    def __init__(self, config):
        import torch
        from sentence_transformers import SentenceTransformer

        torch.set_num_threads(config["cpu_threads"])
        torch.manual_seed(0)
        self.model = SentenceTransformer(
            config["embedding_model_path"], device="cpu", local_files_only=True
        )
        self.tokenizer = self.model.tokenizer
        self.batch_size = config["embedding_batch_size"]
        self.cache = Path(config["cache_dir"]) / "embeddings"
        self.cache.mkdir(parents=True, exist_ok=True)
        self.cache_namespace = config["embedding_revision"]

    def encode(self, windows):
        if not windows:
            return np.empty((0, 384), dtype=np.float32)
        vectors, missing, positions = [None] * len(windows), [], []
        inputs = [w.normalized_text or w.text for w in windows]
        keys = [sha256((self.cache_namespace + "\n" + s).encode()).hexdigest() for s in inputs]
        for i, key in enumerate(keys):
            path = self.cache / f"{key}.npy"
            if path.exists():
                vectors[i] = np.load(path, allow_pickle=False)
            else:
                positions.append(i)
                missing.append(inputs[i])
        if missing:
            encoded = self.model.encode(
                missing,
                batch_size=self.batch_size,
                normalize_embeddings=True,
                convert_to_numpy=True,
                show_progress_bar=False,
            )
            for i, vec in zip(positions, encoded):
                vectors[i] = vec.astype(np.float32)
                np.save(self.cache / f"{keys[i]}.npy", vectors[i], allow_pickle=False)
        return np.stack(vectors)


def cosine_matrix(vectors):
    return np.clip(vectors @ vectors.T, -1, 1)
