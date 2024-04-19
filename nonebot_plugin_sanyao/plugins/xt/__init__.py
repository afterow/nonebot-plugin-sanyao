from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot_plugin_sanyao.plugins.xt.sanyao import print_lunar_info_and_bazi

weather = on_command("三爻", rule=to_me(), aliases={"排盘", "三爻易"}, priority=10, block=True)

@weather.handle()
async def handle_function(args: Message = CommandArg()):
    # 提取参数纯文本作为地名，并判断是否有效
    if location := args.extract_plain_text():
        xx=print_lunar_info_and_bazi(location)
        await weather.finish(xx)
    else:
        await weather.finish("请输入参数 如/三爻 101")