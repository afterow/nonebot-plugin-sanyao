from datetime import datetime

import cnlunar
import pytest
from nonebug import App
from nonebot.adapters.console import User, Message, MessageEvent


@pytest.mark.asyncio
async def test_weather(app: App):
    from nonebot_plugin_sanyao.__main__ import sanyaopaipan

    event = MessageEvent(
        time=datetime.now(),
        self_id="test",
        message=Message("/三爻 111"),  # 修改为三爻 111
        user=User(id="user"),
    )
    today = datetime.now()
    a = cnlunar.Lunar(today, godType='8char', year8Char='beginningOfSpring')
    a1=(a.year8Char[0] + a.month8Char[0] + a.day8Char[0] + a.twohour8Char[0])
    a2=(a.year8Char[1] + a.month8Char[1] + a.day8Char[1] + a.twohour8Char[1])
    cxk="""{a1}
{a2}
本卦：乾之兑
互卦：巽之离
错卦：坤之艮
综卦：巽之乾
    """.format(a1=a1, a2=a2)
    async with app.test_matcher(sanyaopaipan) as ctx:
        bot = ctx.create_bot()
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, cxk, result=None, bot=bot)
        ctx.should_finished(sanyaopaipan)

