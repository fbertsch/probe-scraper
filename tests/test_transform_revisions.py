import probe_scraper.transform_revisions as transform
from datetime import datetime
import pytest


@pytest.fixture
def channels():
    return ['nightly', 'beta']


@pytest.fixture
def revision_dates(channels):
    return {
        channel: {
            "node_id_1": {
                "version": "50",
                "date": datetime(2018, 1, 1, 10, 11, 12)
            },
            "node_id_2": {
                "version": "51",
                "date": datetime(2018, 2, 2, 10, 11, 12)
            },
            "node_id_3": {
                "version": "52",
                "date": datetime(2018, 3, 3, 10, 11, 12)
            },
            "node_id_4": {
                "version": "52",
                "date": datetime(2018, 1, 1, 1, 1, 1)
            },
        } for channel in channels 
    }


def test_get_latest_per_channel(revision_dates, channels):
    expected = {c: {'50': 'node_id_1', '51': 'node_id_2', '52': 'node_id_3'} for c in channels}
    assert transform.get_latest_revision_per_channel_version(revision_dates) == expected
