# ML Mentor — AI/ML Engineering Tutor Agent

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/LLM-Groq%20%7C%20Gemini%20%7C%20Ollama-FF6F00" alt="LLM"/>
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License"/>
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs"/>
</p>

<p align="center">
  <b>A personal AI tutor that teaches AI/ML engineering step by step — lessons, exercises, quizzes, projects, code review, and interview prep.</b>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-api-reference">API</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## Overview

**ML Mentor** is an AI-powered learning agent that acts like a personal tutor for AI and Machine Learning engineering.

Instead of just answering questions, it **teaches**:

- Builds a personalized learning roadmap
- Teaches one topic at a time with examples
- Gives coding exercises and quizzes
- Reviews your code politely
- Tracks your progress and weak areas
- Prepares you for interviews and projects

It ships with a **FastAPI backend** and a **zero-dependency chat frontend** that works in two modes:

| Mode | When | Behavior |
|---|---|---|
| **LIVE** | Backend running | Real LLM replies via Groq / Gemini / Ollama |
| **DEMO** | Backend offline | Built-in offline brain for testing the UI |

---

## Features

### AI Tutor Agent
- Personalized onboarding (level, Python skill, math comfort, daily time, goal)
- Adaptive roadmap generation (8-week plans, custom pacing)
- Structured lessons: explanation, example, key terms, code, practice
- Quiz generation with scoring and weak-area feedback
- Project recommendations matched to skill level
- Polite, educational code review
- Interview preparation mode

### Frontend Chat UI
- Real-time chat with typing indicator and streaming-style replies
- Markdown rendering with copyable code blocks
- Roadmap sidebar with animated progress tracking
- Daily streak counter
- Quick-action prompt chips
- Chat history persisted in localStorage
- Fully responsive — works on mobile

### Developer Experience
- Clean modular FastAPI structure
- OpenAI-compatible LLM client (swap providers via .env only)
- JSON-file memory (zero database setup) — SQLite upgrade path included
- Auto-generated API docs at /docs
- CORS-ready for browser use

---

## Architecture

```
Student --> message --> Frontend UI (HTML/CSS/JS)
    |
    v
POST /chat --> FastAPI Backend
    |
    v
Agent Service
    |-- loads Profile + Progress from JSON Memory
    |-- builds Prompt (system rules + context + curriculum)
    |-- calls LLM Client (OpenAI-compatible API)
    |-- saves updated progress
    |
    v
LLM Provider (Groq / Gemini / OpenAI / Ollama)
    |
    v
Reply --> Frontend UI --> Student
```

**Request flow:**

1. Student sends a message from the chat UI
2. FastAPI receives `POST /chat`
3. Agent loads the user's profile and progress
4. Prompt builder combines system rules + user context + curriculum
5. LLM generates a teaching response
6. Chat history and progress are saved
7. UI renders the reply and updates the roadmap sidebar

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11+, FastAPI, Uvicorn, Pydantic |
| LLM Client | httpx (OpenAI-compatible API) |
| Storage | JSON files (SQLite-ready) |
| Frontend | Vanilla HTML / CSS / JavaScript (no build step) |
| Fonts | Space Grotesk, IBM Plex Sans, IBM Plex Mono |
| LLM Providers | Groq, Google Gemini, OpenAI, Ollama (local) |

---

## Project Structure

```
ai_ml_mentor/
|
|-- app/
|   |-- __init__.py
|   |-- main.py            # FastAPI app + CORS
|   |-- config.py          # Settings & environment variables
|   |-- schemas.py         # Pydantic models
|   |-- prompts.py         # System prompt & context builder
|   |-- curriculum.py      # AI/ML learning modules
|   |-- memory.py          # JSON-based user storage
|   |-- llm.py             # OpenAI-compatible LLM client
|   |-- agent.py           # Core agent logic
|   |
|   +-- routers/
|       |-- __init__.py
|       |-- chat.py        # POST /chat
|       +-- progress.py    # GET/POST profile & progress
|
|-- data/
|   +-- users/             # Per-user JSON files (auto-created)
|
|-- frontend/
|   +-- index.html         # Chat UI (open in browser)
|
|-- tests/
|   +-- test_agent.py
|
|-- cli.py                 # Optional terminal chat mode
|-- run.py                 # uvicorn launcher
|-- requirements.txt
|-- .env.example
|-- .gitignore
|-- LICENSE
+-- README.md
```

---

## Quick Start

### 1. Prerequisites

- Python 3.11 or newer — python.org
- An LLM API key (free options below) or Ollama for fully local use

### 2. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai_ml_mentor.git
cd ai_ml_mentor
```

### 3. Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment

```bash
cp .env.example .env
```

Edit `.env` with your provider details (see next section).

### 6. Run the backend

```bash
python run.py
# or
uvicorn app.main:app --reload
```

Backend runs at **http://127.0.0.1:8000** — API docs at **http://127.0.0.1:8000/docs**

### 7. Open the frontend

Open `frontend/index.html` in your browser.

The status badge turns LIVE when connected to the backend.

---

## LLM Provider Setup

The LLM client is **OpenAI-compatible**, so switching providers only requires changing `.env`.

| Provider | Cost | `LLM_API_URL` | Example `MODEL_NAME` |
|---|---|---|---|
| **Groq** (recommended) | Free tier | `https://api.groq.com/openai/v1/chat/completions` | `llama-3.3-70b-versatile` |
| Google Gemini | Free tier | `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions` | `gemini-2.0-flash` |
| OpenAI | Paid | `https://api.openai.com/v1/chat/completions` | `gpt-4o-mini` |
| Ollama (local) | Free, offline | `http://localhost:11434/v1/chat/completions` | `llama3.2` |

### Example `.env` (Groq — recommended)

```env
LLM_API_KEY=gsk_your_key_here
LLM_API_URL=https://api.groq.com/openai/v1/chat/completions
MODEL_NAME=llama-3.3-70b-versatile
```

Get a free Groq key: console.groq.com -> API Keys -> Create.

Fully offline with Ollama: install from ollama.com, then `ollama run llama3.2`. No API key needed.

---

## API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/chat` | Send a message to the tutor |
| `GET` | `/progress/{user_id}` | Get learning progress |
| `GET` | `/profile/{user_id}` | Get user profile |
| `POST` | `/profile/{user_id}` | Update user profile |

### Example: POST /chat

**Request**

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id": "ali", "message": "Teach me Python variables"}'
```

**Response**

```json
{
  "user_id": "ali",
  "reply": "### Python basics · variables\n\nA variable is a name that points to a value...",
  "progress": {
    "completed_topics": [],
    "weak_areas": [],
    "current_topic": "Python basics",
    "next_topic": "Python basics",
    "chat_history": []
  }
}
```

Interactive docs are available at `http://127.0.0.1:8000/docs`.

---

## Example Conversation

```
Student:  I want to learn AI/ML from zero.
Mentor:   Great! First — what is your Python level: No, Basic, or Good?
Student:  Basic.
Mentor:   Perfect. Here is your 8-week roadmap...
          Shall we start with Python basics today?
Student:  Yes.
Mentor:   ### Variables
          A variable is a name that points to a value...
          Quick check: after x = 5 then x = x + 2, what is x?
```

---

## How the Agent Works

The agent's behavior is controlled by a structured system prompt (`app/prompts.py`) that enforces:

- **Teaching-first behavior** — guides instead of giving away answers
- **One topic at a time** — prevents overwhelming the learner
- **Adaptive difficulty** — adjusts to the student's answers
- **Progress awareness** — completed topics and weak areas are injected into every prompt
- **Curriculum grounding** — a built-in 6-module AI/ML syllabus keeps lessons on track

User state is stored per user in `data/users/{user_id}.json`:

```json
{
  "profile": {
    "level": "beginner",
    "python_level": "basic",
    "goal": "job"
  },
  "progress": {
    "completed_topics": ["Python basics"],
    "weak_areas": ["statistics"],
    "next_topic": "Pandas & NumPy"
  }
}
```

---

## Roadmap

- [x] Core chat agent with teaching prompt
- [x] JSON-based memory & progress tracking
- [x] Chat UI with roadmap sidebar
- [x] Multi-provider LLM support (Groq / Gemini / OpenAI / Ollama)
- [x] Demo mode (offline brain)
- [ ] SQLite / PostgreSQL storage
- [ ] User authentication (JWT)
- [ ] Streaming responses (SSE)
- [ ] RAG with vector database (textbooks & notes)
- [ ] Sandboxed code execution for exercises
- [ ] Progress dashboard with charts
- [ ] Teacher / school mode
- [ ] Docker deployment & cloud hosting

---

## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Badge stuck on DEMO | Backend unreachable | Run `python run.py`; check `CONFIG.API_URL` in `index.html` |
| CORS error in console | Missing middleware | Add `CORSMiddleware` in `app/main.py` (included by default) |
| `401 Unauthorized` | Bad API key | Re-copy key into `.env`, no extra spaces |
| `Model not found` | Wrong model name | Check your provider's model list; update `MODEL_NAME` |
| Ollama connection refused | Ollama not running | Start Ollama; verify with `ollama list` |
| `ModuleNotFoundError` | Venv not active | Activate venv, then `pip install -r requirements.txt` |

---

## Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing`
3. **Commit** your changes: `git commit -m "Add amazing feature"`
4. **Push** to the branch: `git push origin feature/amazing`
5. **Open** a Pull Request

Please keep the teaching prompt student-friendly and add tests for new endpoints.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Groq — ultra-fast free LLM inference
- Meta Llama — open-weight models
- FastAPI — modern Python web framework
- Google Fonts — Space Grotesk & IBM Plex families

---

<p align="center">
  Built for learners, by a learner. <b>Keep learning.</b>
</p>
