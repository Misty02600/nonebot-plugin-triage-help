def test_config_can_be_instantiated():
    from nonebot_plugin_triage_help.config import Config

    assert Config().model_dump() == {}
