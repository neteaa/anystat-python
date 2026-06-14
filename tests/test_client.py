from __future__ import annotations

import pytest
from anystat import AnystatError, Anystat


def test_requires_api_key(monkeypatch):
	"""Если ключа нет -> ошибка."""
	monkeypatch.delenv("ANYSTAT_API_KEY", raising=False)
	with pytest.raises(AnystatError):
		Anystat()


def test_api_key_from_env(monkeypatch):
	"""Ключ из переменной окружения."""
	monkeypatch.setenv("ANYSTAT_API_KEY", "TEST_API_KEY")
	anystat = Anystat()
	assert anystat.api_key == "TEST_API_KEY"

def test_api_key_from_init():
	"""Ключ передают при создании."""
	anystat = Anystat(api_key="TEST_API_KEY")
	assert anystat.api_key == "TEST_API_KEY"
	
