from apiritif import http
from apitest.config import Config


class BaseClient:
    def __init__(self, config: Config):
        self.api = http.target(
            address=config.baseurl,
            additional_headers={"Content-Type": "application/json", "Accept": "application/json"},
            use_cookies=False,
            keep_alive=False,
            auto_assert_ok=False,
        )
