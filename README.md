# Automation Exercise - Playwright Framework
[![Playwright Tests](https://github.com)](https://github.com)

A professional End-to-End (E2E) testing framework covering UI and API test cases for [automationexercise.com](https://automationexercise.com).

## 🚀 Features
- **UI Testing**: Complete coverage using Playwright Page Object Model (POM).
- **API Testing**: REST API validation using Playwright's `APIRequestContext`.
- **Hybrid Cleanup**: Using API calls to ensure a clean state before/after UI tests.
- **Data Generation**: Dynamic test data using `pytest-faker`.
- **CI/CD**: Fully integrated with GitHub Actions.
- **Containerization**: Dockerized environment for consistent execution.

## 🐳 How to Run (Docker)
The easiest way to run the entire suite is using Docker. This ensures all browser dependencies and Python environments are perfectly configured.

1. **Build the image:**
   ```bash
   docker build -t playwright-tests
   docker run --rm playwright-tests

   
This project is configured to capture Playwright Traces on failure. This allows for deep inspection of network logs, console output, and DOM snapshots at the exact moment of a failure.
To view a trace:
Go to the Actions tab in this repository.
Select a failed workflow run.
Scroll down to Artifacts and download playwright-traces.
Drag and drop the downloaded zip file into trace.playwright.dev.
🛠️ Local Setup (Without Docker)
If you prefer to run tests locally:

    pip install -r requirements.txt
    playwright install --with-deps
    pytest project/tests
