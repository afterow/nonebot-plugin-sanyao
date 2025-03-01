import base64
import io

import matplotlib.pyplot as plt
import matplotlib as mpl
from  nonebot_plugin_sanyao.util.paipan import GuaCalculator
from  nonebot_plugin_sanyao.util.format_results import format_results
import datetime
import cnlunar

def get_formatted_lunar_info():
    """
    获取当前时间的农历和八字信息，并返回指定格式的字符串。

    Returns:
        tuple: 包含日期字符串（ISO 格式）、农历日期字符串和八字字符串的元组。
    """
    now = datetime.datetime.now()
    lunar_obj = cnlunar.Lunar(now, godType='8char')

    date_str_iso = now.isoformat()
    readable_format_us = now.strftime("%Y-%m-%d %H:%M:%S.") + str(now.microsecond)

    lunar_date_str = f"农历{lunar_obj.lunarYearCn}{lunar_obj.year8Char}[{lunar_obj.chineseYearZodiac}]年{lunar_obj.lunarMonthCn}{lunar_obj.lunarDayCn}"
    bazi_str = " ".join([lunar_obj.year8Char, lunar_obj.month8Char, lunar_obj.day8Char, lunar_obj.twohour8Char])

    return readable_format_us, lunar_date_str, bazi_str

def create_gua_plot(formatted_results):
    """
    创建并保存包含农历信息和卦象的图像。

    Args:
        formatted_results (str): 格式化后的卦象结果字符串。
    """
    plt.style.use('fast')
    mpl.rcParams['font.family'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False



    readable_format, lunar_date_str, bazi_str = get_formatted_lunar_info()
    text_data = [readable_format, lunar_date_str, bazi_str, formatted_results]

    fig, axes = plt.subplots(5, 4, figsize=(6, 8), gridspec_kw={'wspace': 0, 'hspace': 0})

    # 移除第一行的后三个子图
    for j in range(1, 4):
        fig.delaxes(axes[0, j])

    # 设置第一行的第一个子图
    axes[0, 0].set_position([0.1, 0.60, 0.8, 0.3])
    axes[0, 0].text(0.5, 0.5, '\n'.join(text_data[:3]), ha='center', va='center', fontsize=14)
    axes[0, 0].axis('off')  # 关闭边框

    # 处理卦象数据
    all_items = [item.strip().replace('"', '') for line in formatted_results.split(",\n") for item in line.split(",")]
    all_items = all_items[::-1]  # 反转顺序
    for i in range(0, len(all_items), 4):
        all_items[i:i+4] = all_items[i:i+4][::-1]  # 每4个一组反转

    # 设置表格格子
    cell_width = 0.225  # 每个格子的宽度
    cell_height = 0.175  # 每个格子的高度
    x_start = 0.1  # 起始x坐标
    y_start = 0.60 - cell_height * 4  # 起始y坐标

    for i in range(1, 5):  # 遍历行
        for j in range(4):  # 遍历列
            ax = axes[i, j]
            ax.set_position([x_start + j * cell_width, y_start + (i - 1) * cell_height, cell_width, cell_height])
            ax.text(0.5, 0.5, all_items.pop(0), ha='center', va='center', fontsize=12)
            ax.set_xticks([])
            ax.set_yticks([])
            for spine in ax.spines.values():  # 设置边框线宽
                spine.set_linewidth(1.5)

    # 保存图像
     # 将图形保存到内存中的文件流
    try:
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png", dpi=150, bbox_inches="tight")
        buffer.seek(0)  # important: reset buffer position to the beginning

        # Convert file stream to base64
        base64_str = base64.b64encode(buffer.read()).decode('utf-8')

        # 关闭图形
        plt.close(fig)

        return base64_str
    except Exception as e:
        print(f"生成 Base64 编码时出错: {e}")
        return None