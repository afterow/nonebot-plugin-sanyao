import pytest
import nonebot
# 导入适配器
from nonebot.adapters.console import Adapter as ConsoleAdapter

@pytest.fixture(scope="session", autouse=True)
async def after_nonebot_init(after_nonebot_init: None):
    # 加载适配器
    driver = nonebot.get_driver()
    driver.register_adapter(ConsoleAdapter)

    # 加载插件
    nonebot.load_from_toml("../../../pyproject.toml")