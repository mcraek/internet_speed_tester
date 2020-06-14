from internet_speed_tester.web_scraping_functions.read_site import wait, get_download_speed, get_upload_speed
import pytest
from unittest.mock import Mock

# Setup arguments to pass to function

args = {'log': False, 'verbose': False}
log = "log"

# Setup mocked registry connection
# start_browser fixture handles all registry functions with ZoomFactor value
# for both setup and teardown

mocked_reg_connection = Mock()


@pytest.mark.usefixtures("start_browser")
class TestReadSite:

    def test_wait(self):

        # Validate wait is able to verify the site has finished loading
        # If this test fails, subsequent ones will fail as well

        site_loaded = wait(args, log, self.driver, mocked_reg_connection)
        assert site_loaded

    def test_get_download_speed(self):

        # Validate get_download_speed can pull value from site and convert
        # it to MB/s. Must be a float that's returned. Otherwise an error
        # has occurred

        download_speed = get_download_speed(args, log, self.driver, mocked_reg_connection)

        assert isinstance(download_speed, float)

    def test_get_upload_speed(self):

        # Validate get_upload_speed can pull value and convert it to MB/s

        upload_speed = get_upload_speed(args, log, self.driver, mocked_reg_connection)

        assert isinstance(upload_speed, float)
