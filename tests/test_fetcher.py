# tests/test_fetcher.py
from weather_fetcher import WeatherFetcher


class DummyResp:
def raise_for_status(self): pass
def json(self):
return {'main': {'temp': 70, 'humidity': 40}, 'weather': [{'description': 'clear sky'}]}


def test_fetch_city(monkeypatch):
def fake_get(url, params, timeout):
return DummyResp()
monkeypatch.setattr('requests.get', fake_get)
wf = WeatherFetcher('fakekey')
out = wf.fetch_city('Nowhere')
assert out['temperature_f'] == 70
assert out['humidity'] == 40