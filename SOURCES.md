# Primary references and model provenance

- [all-MiniLM-L6-v2 model card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2): public Sentence-Transformers model, 384-dimensional representations, 256-piece default context, Apache-2.0 license. Runtime is pinned to `c9745ed1d9f207416be6d2e6f8de32d1f16199bf`, not a moving branch.
- [faster-whisper project](https://github.com/SYSTRAN/faster-whisper): CTranslate2-based Whisper inference, CPU int8, word timestamps and VAD integration. The installed library is 1.2.1.
- [OpenAI Whisper](https://github.com/openai/whisper): original open speech recognition model. This project uses the English tiny conversion from [Systran/faster-whisper-tiny.en](https://huggingface.co/Systran/faster-whisper-tiny.en), pinned to `0d3d19a32d3338f10357c0889762bd8d64bbdeba`.

These sources describe the models/tools, not the accuracy of this implementation. The repository's own measured evidence is in `evaluation/` and `reports/`. No third-party benchmark has been presented as this project's measured performance.

Synthetic sample and reference prose is authored locally with Codex assistance and dedicated under CC0-1.0. The local external reference URL identifies its actual committed source location in the private repository; it is not a claim of retrieving an independently published web article.
