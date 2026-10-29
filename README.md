# speech-to-graph

> **Clean-Room Open-Source Implementation**  
> *Target Architecture Archetype:* Granola / Otter Autonomous Audio Transcription & Semantic Action Extractor  
> *Author:* Ayush Kandwal ([@Sunzzx](https://github.com/Sunzzx)) | License: MIT

---

## ⚡ Overview
`speech-to-graph` is a 100% clean-room, independently authored open-source implementation providing:
- Local-first semantic meeting notes and structured action-item extractor compiling raw timestamps into a directed task DAG with zero third-party cloud dependencies.
- Zero external runtime dependencies.
- Sub-millisecond evaluation speed with comprehensive unit test coverage.

## 🚀 Quickstart
```bash
python3 -m unittest discover tests
```

## 📐 Architecture
```
       ┌────────────────────────┐
       │   Command Registry     │
       └───────────┬────────────┘
                   │ Action Graph
                   ▼
       ┌────────────────────────┐
       │ Fuzzy Subsequence Match│
       └───────────┬────────────┘
                   │ Scored & Ranked
                   ▼
       ┌────────────────────────┐
       │  Sub-Millisecond Stream│
       └────────────────────────┘
```
