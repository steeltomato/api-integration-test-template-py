import typed_settings as ts


@ts.settings
class Config:
    env: str
    baseurl: str
    tenant: str


# Central reference to the test app config state
config = ts.load(
    cls=Config,
    appname="apitest",
    config_files=[ts.find("config/default.toml")],
)
