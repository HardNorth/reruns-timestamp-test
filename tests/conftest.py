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
import pytest

from reportportal_client.client import RPClient


def pytest_addoption(parser):
    """Pytest hook that defines list of CLI arguments

    :param parser: pytest specific argument
    :return: void
    """
    parser.addini(name='rp_uuid',
                  help='Report Portal API secret key')
    parser.addini(name='rp_endpoint',
                  help='Report Portal API endpoint')
    parser.addini(name='rp_project',
                  help='Report Portal project')


@pytest.fixture(scope='function')
def report_portal_client(request):
    rp_client = RPClient(request.config.getini('rp_endpoint'),
                         request.config.getini('rp_project'),
                         request.config.getini('rp_uuid'),
                         log_batch_size=1)
    rp_client.start()
    return rp_client
