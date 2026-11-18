import logging
from pathlib import Path

import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"
AUTH_URL = f"{BASE_URL}/auth"
CARS_URL = f"{BASE_URL}/cars"
LOG_FILE = Path(__file__).resolve().parent.parent / "test_search.log"

logger = logging.getLogger("cars_api_tests")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


class TestCarsAPI:

    @pytest.fixture(scope="class")
    def authenticated_session(self):
        session = requests.Session()

        response = session.post(
            AUTH_URL,
            auth=HTTPBasicAuth("test_user", "test_pass")
        )

        logger.info("POST %s | status: %s", AUTH_URL, response.status_code)

        assert response.status_code == 200, (
            f"Authentication failed: {response.status_code}, {response.text}"
        )

        access_token = response.json().get("access_token")
        assert access_token, "Response does not contain access_token"

        session.headers.update({
            "Authorization": f"Bearer {access_token}"
        })

        logger.info("Authentication successful; access token received.")
        yield session

        session.close()
        logger.info("Session closed.")

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("year", 10),
            ("engine_volume", 3),
            ("brand", 7),
            (None, 5),
            ("price", 10),
        ]
    )
    def test_search_cars(self, authenticated_session, sort_by, limit):
        params = {"limit": limit}
        if sort_by is not None:
            params["sort_by"] = sort_by

        logger.info(
            "GET %s | sort_by=%s | limit=%s",
            CARS_URL, sort_by, limit
        )

        response = authenticated_session.get(CARS_URL, params=params)
        logger.info("Response status: %s", response.status_code)

        assert response.status_code == 200, (
            f"Search failed: {response.status_code}, {response.text}"
        )

        cars = response.json()
        assert isinstance(cars, list), "Response should be a JSON list"
        assert len(cars) <= limit, (
            f"Expected at most {limit} cars, received {len(cars)}"
        )

        sort_field = sort_by if sort_by else "brand"
        actual_values = [car[sort_field] for car in cars]
        assert actual_values == sorted(actual_values), (
            f"Cars are not sorted by {sort_field}"
        )

        logger.info(
            "Test passed: %s cars returned, sorted by %s.",
            len(cars), sort_field
        )
