import re

import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.fixture(scope="session", autouse=True)
def set_selectors(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-qa")


# this blocks ads
@pytest.fixture(autouse=True)
def block_ads(page):
    ad_patterns = [
        re.compile(r".*googlesyndication\.com.*"),
        re.compile(r".*googleadservices\.com.*"),
        re.compile(r".*google-analytics\.com.*"),
        re.compile(r".*adservice\.google.*"),
        re.compile(r".*google\.com/ads.*"),
    ]

    def handle_route(route):
        if any(pattern.match(route.request.url) for pattern in ad_patterns):
            route.abort()
        else:
            route.continue_()

    page.route("**/*", handle_route)
    # page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())


@pytest.fixture(scope="function")
def random_user(faker):
    return {
        "name": faker.name(),
        "title": True,
        "email": faker.email(),
        "password": faker.password(length=12),
        "day": str(faker.random_int(min=1, max=28)),
        "month": str(faker.random_int(min=1, max=12)),
        "year": str(faker.random_int(min=1970, max=2000)),
        "newsletter": True,
        "offers": True,
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "company": faker.company(),
        "address": faker.street_address(),
        "address2": faker.secondary_address(),
        "country": faker.random_element(
            elements=("India", "United States", "Canada", "Australia")
        ),
        "state": faker.state(),
        "city": faker.city(),
        "zipcode": faker.zipcode(),
        "mobile_number": faker.phone_number(),
        "card_number": faker.credit_card_number(),
        "card_cvc": faker.credit_card_security_code(),
        "card_month": str(faker.random_int(min=1, max=12)),
        "card_year": str(faker.random_int(min=2027, max=2031)),
        "subject": "Test subject",
        "message": "Test message",
        "review_message": "I give this products a rating of 5/5. Really helped me.",
        "path": "./upload_test.txt",
    }


@pytest.fixture(scope="session")
def session_user(faker):
    return {
        "name": faker.name(),
        "title": True,
        "email": faker.email(),
        "password": faker.password(length=12),
        "day": str(faker.random_int(min=1, max=28)),
        "month": str(faker.random_int(min=1, max=12)),
        "year": str(faker.random_int(min=1970, max=2000)),
        "newsletter": True,
        "offers": True,
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "company": faker.company(),
        "address": faker.street_address(),
        "address2": faker.secondary_address(),
        "country": faker.random_element(
            elements=("India", "United States", "Canada", "Australia")
        ),
        "state": faker.state(),
        "city": faker.city(),
        "zipcode": faker.zipcode(),
        "mobile_number": faker.phone_number(),
        "card_number": faker.credit_card_number(),
        "card_cvc": faker.credit_card_security_code(),
        "card_month": str(faker.random_int(min=1, max=12)),
        "card_year": str(faker.random_int(min=2027, max=2031)),
        "subject": "Test subject",
        "message": "Test message",
        "review_message": "I give this products a rating of 5/5. Really helped me.",
        "path": "./upload_test.txt",
    }
