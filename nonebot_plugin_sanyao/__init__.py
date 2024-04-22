from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="三爻易数",
    description="三爻易数排盘",
    usage="",
    type="application",
    homepage="https://github.com/afterow/nonebot-plugin-sanyao",
    config=Config,
    supported_adapters=None,
)