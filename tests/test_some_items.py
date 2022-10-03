#  Copyright (c) 2022 https://reportportal.io .
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License
import time

import pytest

from reportportal_client.helpers import timestamp
from test_launch import START_TIME

@pytest.mark.order(2)
def test_item_1(report_portal_client):
    report_portal_client.start_launch(
        "Multi node join",
        timestamp(),
        rerun=True

    )

    parent_suite_uuid = report_portal_client.start_test_item(
        "First suite", START_TIME, "SUITE", "A common parent suite",
    )

    time.sleep(1)

    item_uuid = report_portal_client.start_test_item(
        "Item 1", START_TIME, "STEP", "A test step",
        parent_item_id=parent_suite_uuid
    )

    report_portal_client.finish_test_item(item_uuid, timestamp(), "PASSED")
    report_portal_client.finish_test_item(parent_suite_uuid, timestamp())

    report_portal_client.finish_launch(timestamp())
    time.sleep(1)


@pytest.mark.order(3)
def test_item_2(report_portal_client):
    item_time = timestamp()
    report_portal_client.start_launch(
        "Multi node join",
        item_time,
        rerun=True

    )

    parent_suite_uuid = report_portal_client.start_test_item(
        "First suite", item_time, "SUITE", "A common parent suite",
    )

    time.sleep(1)

    item_uuid = report_portal_client.start_test_item(
        "Item 2", item_time, "STEP", "A test step",
        parent_item_id=parent_suite_uuid
    )

    report_portal_client.log(timestamp(), "A test log message", "INFO",
                             item_id=item_uuid)

    report_portal_client.finish_test_item(item_uuid, timestamp(), "PASSED")
    report_portal_client.finish_test_item(parent_suite_uuid, timestamp())

    report_portal_client.finish_launch(timestamp())


@pytest.mark.order(4)
def test_item_3(report_portal_client):
    report_portal_client.start_launch(
        "Multi node join",
        START_TIME,
        rerun=True

    )

    parent_suite_uuid = report_portal_client.start_test_item(
        "Second suite", int(START_TIME) + 10, "SUITE", "A common parent suite",
    )

    time.sleep(1)

    item_uuid = report_portal_client.start_test_item(
        "Item 3", timestamp(), "STEP", "A test step",
        parent_item_id=parent_suite_uuid
    )

    report_portal_client.log(timestamp(), "A test log message", "INFO",
                             item_id=item_uuid)

    report_portal_client.finish_test_item(item_uuid, timestamp(), "PASSED")
    report_portal_client.finish_test_item(parent_suite_uuid, timestamp())

    report_portal_client.finish_launch(timestamp())
