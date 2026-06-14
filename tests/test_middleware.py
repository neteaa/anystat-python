

from unittest.mock import MagicMock

from anystat.aiogram._models.models import MessageEvent
from anystat.aiogram.middleware import AnystatMiddleware
import pytest


@pytest.fixture
def anystat():
	mock = MagicMock()
	mock.track_start = True
	mock.track_messages = True
	mock.auto_identify = True
	return mock

@pytest.fixture
def middleware(anystat):
	return AnystatMiddleware(anystat)

def test_identify_user(middleware):
	"""Проверка авто индетификации пользователя."""
	mock_user = MagicMock()
	mock_user.id = 52
	mock_user.username = "test_username"
	mock_user.first_name = "test_first_name"
	mock_user.last_name = None
	mock_user.language_code = "en"
	mock_user.is_premium = False

	data = {"event_from_user": mock_user}
	result = middleware._identify(data)

	assert result.user_id == 52
	assert result.username == "test_username"

def test_regular_get_message(middleware):
	"""Проверка определения события обычного сообщения."""
	mock_message = MagicMock()
	mock_message.text = "test"
	mock_message.from_user.id = 52
	mock_message.message_id = 123

	result = middleware._get_message_event(mock_message, received_at=10, duration=230)

	assert isinstance(result, MessageEvent)
	assert result.user_id == 52
	assert result.duration == 230