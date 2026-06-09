#!/usr/bin/env python3
"""
ChainSage - Crypto Market Analyst Chatbot

A production-ready Flask chatbot app designed for the Battle of the Minds
"Minds Building Chatbots Challenge".

Default LLM provider: Google AI Studio / Gemini via REST API.
Configurable providers: Gemini, OpenAI-compatible APIs, or mock mode for local UI testing.
"""

from __future__ import annotations

import logging
import os
import time
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from werkzeug.middleware.proxy_fix import ProxyFix

load_dotenv()

# ... (full code continues)
