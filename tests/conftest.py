from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


_ORIGINAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep tests isolated by resetting in-memory data before each test."""
    activities.clear()
    activities.update(deepcopy(_ORIGINAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(deepcopy(_ORIGINAL_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)
