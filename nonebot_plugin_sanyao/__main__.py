import base64

from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot_plugin_sanyao.util.main import calculate_and_visualize_gua,parse_input

sanyaopaipan = on_command("三爻", rule=to_me(), aliases={"三爻排盘", "三爻易"}, priority=10, block=True)

@sanyaopaipan.handle()
async def handle_function(args: Message = CommandArg()):
    # 提取参数纯文本作为地名，并判断是否有效
    if location := args.extract_plain_text():
        xx=calculate_and_visualize_gua(parse_input(location))
        await sanyaopaipan.finish(MessageSegment.image(base64.b64decode(xx)))
    else:
        await sanyaopaipan.finish("请输入参数 如/三爻 101")
