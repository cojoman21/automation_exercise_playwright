# Automation Exercise - Playwright Framework


### This project covers testing the UI and API test cases for [automationexercise.com](https://automationexercise.com).

## Features
- **UI Testing**: Complete coverage using [Playwright](https://playwright.dev/python/docs/intro) Page Object Model (POM)
- **API Testing**: REST API validation using Playwright's `APIRequestContext` ([docs](https://playwright.dev/python/docs/api/class-apirequestcontext))
- **Hybrid Cleanup**: Using API calls to ensure a clean state before/after UI tests #TODO
- **Data Generation**: Dynamic test data using `pytest-faker` ([docs](https://faker.readthedocs.io/en/master/))
- **CI/CD**: Fully integrated with GitHub Actions ([docs](https://docs.github.com/en/actions))
- **Containerization**: Dockerized environment for consistent execution ([docker](https://docs.docker.com/))
- **Reports generation**: Using [pytest-html](https://pytest-html.readthedocs.io/en/latest/) and [pytest-md-report](https://pypi.org/project/pytest-md-report/)


## 🐳 How to run using Docker
The easiest way to run the entire suite is using Docker. This ensures all browser dependencies and Python environments are perfectly configured.

The Docker image can be found at this [link](https://hub.docker.com/r/cojoman1/automation_exercise_playwright-playwright-tests)

### 1. Open a powershell window and run:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
docker pull cojoman1/automation_exercise_playwright-playwright-tests:latest
```
### 2. Run the image using:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
docker run cojoman1/automation_exercise_playwright-playwright-tests:latest
```

## 🐱 How to run using GitHub

### 1. Open a powershell window and download the project using:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
git clone https://github.com/cojoman21/ #TODO
```

#### Alternatively you can manually download the repository from this [link](#TODO)

### 2. Navigate into the root project directory

<h5 a><strong><code>powershell</code></strong></h5>

```sh
cd #TODO
```

### 3️⃣ Initialize the project

<h5 a><strong><code>powershell</code></strong></h5>


```sh
uv sync --frozen
```

This uses `uv.lock` to re-create the virtual environment with all the requirements for this project.

## Running the tests: 

### 1. Running a single test:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest project/tests/test_case_01.py
```

### 2. Running the whole test suite:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest
```

### 3. Running the test suite with reports:

The reports will be available at ```root/test-results/```. Make sure the path exists before running the command.

```sh
mkdir test-results
```

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest --md-report --md-report-output test-results/report.md --md-report-color never --html=test-results/report.html --self-contained-html
```

## Project structure:

- `root/project/data`: some custom data for test that require stable data (not randomly generated)
- `root/project/download`: used as download path for test that require it
- `root/project/pages`: this contains the POMs
  - `/components/`: smaller sections that appear in multiple places on the website
- `root/project/test-result`: test results are stored in here (check[ Running the test suite with reports](#3-running-the-test-suite-with-reports))