from nonebot.plugin import PluginMetadata

from .config import Config
from . import __main__

__version__ = "0.2.4"
__plugin_meta__ = PluginMetadata(
    name="三爻易数",
    description="三爻易数排盘",
    usage="",
    type="application",
    homepage="https://github.com/afterow/nonebot-plugin-sanyao",
    config=Config,
    supported_adapters=None,
)
