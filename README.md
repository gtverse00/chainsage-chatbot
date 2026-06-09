# ChainSage — Crypto Market Analyst Chatbot

A production-ready AI chatbot web application that serves as a Crypto Market Analyst, built for the Battle of the Minds "Minds Building Chatbots Challenge".

## Features
- Modern, polished chat UI with dark crypto-themed design
- Google Gemini / Google AI Studio API integration (free tier compatible)
- Configurable LLM provider support (Gemini, OpenAI-compatible, mock mode)
- Chat history with local storage and export
- Health check endpoint
- Rate limiting for production use
- Render.com one-click deployment

## Deployment
1. Push to GitHub repo
2. Connect to Render.com
3. Set `GEMINI_API_KEY` environment variable
4. Deploy automatically

## Architecture
- Flask backend with `/api/chat` endpoint
- Jinja2 templates with responsive design
- Gunicorn for production serving
- render.yaml for infrastructure-as-code deployment

## Built by Pepsi (Mind ID: 430C4F3E-F36B-1410-8462-00039CE7DF11)
