from hokodream_analytics.instagram_client import fetch_instagram_media
from unittest.mock import Mock

page_1 = {
    "data": [
        {"id": "1", "media_type": "VIDEO", "timestamp": "2026-01-01T10:00:00+0000"},
        {"id": "2", "media_type": "VIDEO", "timestamp": "2026-01-02T10:00:00+0000"},
        {"id": "3", "media_type": "IMAGE", "timestamp": "2026-01-03T10:00:00+0000"},
    ],
    "paging": {"next": "https://graph.instagram.com/page2"},
}

page_2 = {
    "data": [
        {"id": "4", "media_type": "VIDEO", "timestamp": "2026-01-04T10:00:00+0000"},
        {
            "id": "5",
            "media_type": "CAROUSEL_ALBUM",
            "timestamp": "2026-01-05T10:00:00+0000",
        },
    ],
    "paging": {},
}


def test_pagination(monkeypatch):
    reponse_1 = Mock()
    reponse_1.json.return_value = page_1
    reponse_2 = Mock()
    reponse_2.json.return_value = page_2
