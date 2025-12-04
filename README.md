# Rule-Based Chatbot (Python) — Local Ollama qwen2.5-coder:0.5b

A lightweight rule-based chatbot written in Python that runs a local Ollama model (qwen2.5-coder:0.5b) for generation. The bot uses deterministic, rule-based priorities to select or craft responses and falls back to the local Ollama model when rules don't apply.

This README explains how to set up a Python virtual environment, install dependencies, pull and run the Ollama model locally, configure rules, and run the chatbot.

---

## Features

- Deterministic rule-matching engine (keyword, regex, and priority-based rules)
- Local model fallback using Ollama's qwen2.5-coder:0.5b
- Simple JSON-based rule configuration for easy extension
- Console-mode demo to interact with the chatbot locally
- Easy to adapt to a web or messaging UI

---

## Table of contents

- Overview
- Prerequisites
- Install Ollama & pull model
- Setup Python virtualenv & dependencies
- Rules configuration
- Example usage (console)
- How it works
- Extending & best practices
- Troubleshooting
- Security & privacy

---

## Overview

This project uses explicit rules to answer user queries. Rules are matched in order of priority. If no rule matches, the chatbot sends the user prompt (optionally augmented with context) to a locally running Ollama instance using the model qwen2.5-coder:0.5b and returns the model's response.

---

## Prerequisites

- Python 3.8+
- Virtualenv (or venv)
- Ollama installed and able to run locally (see below)
- Network access to localhost (Ollama runs a local server typically on port 11434)

---

## Install Ollama & pull model

1. Install Ollama following official instructions: https://ollama.ai
   - macOS: Homebrew or installer
   - Linux / Windows: See official downloads and install steps on Ollama website

2. Pull the model you need locally:
   ```
   ollama pull qwen2.5-coder:0.5b
   ```

3. Ensure Ollama daemon/server is running. The Ollama CLI typically starts a local service automatically; alternatively:
   ```
   ollama serve
   ```
   The REST API is available on http://localhost:11434 by default.

If you need more details, consult Ollama docs: https://docs.ollama.ai

---

## Setup Python virtualenv & dependencies

1. Create and activate a virtual environment:
   - macOS / Linux:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

2. Create a minimal `requirements.txt`:
   ```
   requests
   python-dotenv
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

---
