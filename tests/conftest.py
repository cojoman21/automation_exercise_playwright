import re
import uuid

import pytest
from playwright.sync_api import Page, Playwright

from api_clients.product_client import ProductClient
from api_clients.user_client import UserClient


# API
@pytest.fixture()
def user_client(page: Page):
    return UserClient(page)


@pytest.fixture()
def temp_user_client(user_client: UserClient, random_user):
    user_client.create_user(random_user)
    yield user_client
    user_client.delete_user(random_user)


@pytest.fixture()
def product_client(page: Page):
    return ProductClient(page)


# Browser_context_args
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


# data-qa ID
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


# Random user data - erased after each test
@pytest.fixture(scope="function")
def random_user(faker):
    unique_id = str(uuid.uuid4())[:5]
    email = f"test_{unique_id}_{faker.email()}"

    return {
        "name": faker.name(),
        "title": True,
        "email": email,
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
        "upload_path": "./upload_test.txt",
        "download_path": "./download/invoice.txt",
    }


# Random user data - valid for the whole session (multiple tests)
@pytest.fixture(scope="session")
def session_user(_session_faker):
    return {
        "name": _session_faker.name(),
        "title": True,
        "email": _session_faker.email(),
        "password": _session_faker.password(length=12),
        "day": str(_session_faker.random_int(min=1, max=28)),
        "month": str(_session_faker.random_int(min=1, max=12)),
        "year": str(_session_faker.random_int(min=1970, max=2000)),
        "newsletter": True,
        "offers": True,
        "first_name": _session_faker.first_name(),
        "last_name": _session_faker.last_name(),
        "company": _session_faker.company(),
        "address": _session_faker.street_address(),
        "address2": _session_faker.secondary_address(),
        "country": _session_faker.random_element(
            elements=("India", "United States", "Canada", "Australia")
        ),
        "state": _session_faker.state(),
        "city": _session_faker.city(),
        "zipcode": _session_faker.zipcode(),
        "mobile_number": _session_faker.phone_number(),
        "card_number": _session_faker.credit_card_number(),
        "card_cvc": _session_faker.credit_card_security_code(),
        "card_month": str(_session_faker.random_int(min=1, max=12)),
        "card_year": str(_session_faker.random_int(min=2027, max=2031)),
        "subject": "Test subject",
        "message": "Test message",
        "review_message": "I give this products a rating of 5/5. Really helped me.",
        "upload_path": "./upload_test.txt",
        "download_path": "./download/invoice.txt",
    }
