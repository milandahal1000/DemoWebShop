"""
Global configuration loader for Demo Web Shop automation.
Loads settings from environment variables and .env file.
"""
import os
import shutil
from pathlib import Path
from dotenv import load_dotenv

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file
load_dotenv(dotenv_path=BASE_DIR / ".env")

# Base URL
BASE_URL = os.getenv("DEMO_BASE_URL", "https://demowebshop.tricentis.com/").strip()
if not BASE_URL.endswith("/"):
    BASE_URL += "/"

# User Credentials
DEMO_EMAIL = os.getenv("DEMO_EMAIL", "").strip()
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD", "").strip()

# Browser binary discovery
_env_browser = os.getenv("BROWSER_BINARY", "").strip()
if _env_browser and os.path.exists(_env_browser):
    BROWSER_BINARY = _env_browser
else:
    # Auto-detect brave, google-chrome, or chromium on PATH
    BROWSER_BINARY = (
        shutil.which("brave")
        or shutil.which("brave-browser")
        or shutil.which("google-chrome")
        or shutil.which("chromium-browser")
        or shutil.which("chromium")
    )

# Timeout settings (seconds)
EXPLICIT_WAIT = 10
IMPLICIT_WAIT = 0  # Rely on explicit waits per QA best practices
PAGE_LOAD_TIMEOUT = 30
