from .config import config as conf


def pytest_report_header(config, startdir):
    return ["Api Integration Test Results"]


def pytest_configure(config):
    if conf is None:
        assert "Failed to load configuration"
    pass
