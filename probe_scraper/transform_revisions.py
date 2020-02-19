# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from collections import defaultdict
from itertools import groupby


def transform(revision_data):
    results = defaultdict(dict)
    for channel, nodes in revision_data.items():
        for node_id, details in nodes.items():
            results[channel][node_id] = {
                'version': details.get('version'),
                'date': details.get('date')
            }

    return results


def get_latest_revision_per_channel_version(revisions):
    return {
        channel: {
            k: max(list(g), key=lambda x: x[1]['date'])[0]
            for k, g in groupby(revisions[channel].items(), key=lambda x: x[1]['version'])
        } for channel in revisions
    }
