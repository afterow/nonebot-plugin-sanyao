from  nonebot_plugin_sanyao.util.sanyaoyi import GuaCalculator
from  nonebot_plugin_sanyao.util.sanyaoyi import format_results
from  nonebot_plugin_sanyao.util.sanyaoyi import create_gua_plot
import re

def parse_input(input_str):
    """
    解析输入字符串，将其转换为包含三个整数的列表。

    Args:
        input_str:  输入的字符串，可以是 "111", "222", "333", "1,1,1", "2,2,2", 或其他类似格式。

    Returns:
        包含三个整数的列表。如果输入字符串无法解析为包含三个整数的列表，则返回 None。
        例如:
        parse_input("111") == [1, 1, 1]
        parse_input("222") == [2, 2, 2]
        parse_input("1,1,1") == [1, 1, 1]
        parse_input("2,2,2") == [2, 2, 2]
        parse_input("abc") == None
        parse_input("1,2") == None
    """
    # 尝试解析 "111" 或 "222" 这种格式
    if len(input_str) == 3 and input_str.isdigit():
        return [int(input_str[0]), int(input_str[1]), int(input_str[2])]

    # 尝试解析 "1,1,1" 这种格式
    parts = re.split(r"[,，]", input_str)  # 使用正则表达式同时匹配逗号和中文逗号
    if len(parts) == 3:
        try:
            nums = [int(part.strip()) for part in parts] #strip()去除空格
            return nums
        except ValueError:
            return None  # 转换为整数失败

    return None  # 无法解析

def calculate_and_visualize_gua(input_data):
  """
  计算卦象变化并可视化结果。

  Args:
    input_data: 一个包含三个元素的列表，代表卦象的输入数据。
                 例如: [9, 8, 0]

  Returns:
    None。该函数会直接生成并显示卦象图。
  """

  calculator = GuaCalculator()  # 实例化 GuaCalculator 类，假设该类已定义

  results = calculator.calculate_element_changes(input_data)  # 调用计算方法

  formatted_results = format_results(results)  # 格式化计算结果，假设 format_results 函数已定义

  xx=create_gua_plot(formatted_results)  # 创建卦象图，假设 create_gua_plot 函数已定义
  return xx

