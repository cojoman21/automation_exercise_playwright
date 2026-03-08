# Automation Exercise - Playwright Framework


> This project covers testing the UI and API test cases for [automationexercise.com](https://automationexercise.com).

## Features
- **UI Testing**: Complete coverage using [Playwright](https://playwright.dev/python/docs/intro) Page Object Model (POM)
- **API Testing**: REST API validation using Playwright's `APIRequestContext` ([docs](https://playwright.dev/python/docs/api/class-apirequestcontext))
- **Cleanup**: Using API calls to ensure a clean state before/after UI tests
- **Test Data Generation**: Dynamic test data using `pytest-faker` ([docs](https://faker.readthedocs.io/en/master/))
- **CI/CD**: Fully integrated with GitHub Actions ([docs](https://docs.github.com/en/actions))
- **Containerization**: Dockerized environment for consistent execution ([docker](https://docs.docker.com/))
- **Reports generation**: Using [pytest-html](https://pytest-html.readthedocs.io/en/latest/) and [pytest-md-report](https://pypi.org/project/pytest-md-report/)


## How to run using Docker (easiest way)

> The Docker image can be found at this [link](https://hub.docker.com/r/cojoman1/automation_exercise_playwright-playwright-tests)

### 1. Open a powershell window and run:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
docker pull cojoman1/automation_exercise_playwright-playwright-tests
```
### 2. Run the image using:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
docker run cojoman1/automation_exercise_playwright-playwright-tests
```

## How to run locally

### 1. Open a powershell window and download the project using:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
git clone https://github.com/cojoman21/automation_exercise_playwright.git
```

#### Alternatively you can manually download the repository from this [link](https://github.com/cojoman21/automation_exercise_playwright)

### 2. Navigate into the root project directory

<h5 a><strong><code>powershell</code></strong></h5>

```sh
cd automation_exercise_playwright
```

### 3. Initialize the project

<h5 a><strong><code>powershell</code></strong></h5>


```sh
uv sync --frozen
```

> This uses `uv.lock` to recreate the virtual environment using the exact dependency versions from the lockfile.

### 4. Running the tests: 

### 4.1. Running a single test:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest tests/tests_UI/test_case_01_register.py
```

### 4.2. Running the whole test suite:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest
```

### 4.3. Running the test suite with reports:

The reports will be available at `root/test-results/`. Create the path using:

```sh
mkdir test-results
```

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest --md-report --md-report-output test-results/report.md --md-report-color never --html=test-results/report.html --self-contained-html
```
