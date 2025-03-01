from  nonebot_plugin_sanyao.util.sanyaoyi import GuaCalculator
from  nonebot_plugin_sanyao.util.sanyaoyi import format_results
from  nonebot_plugin_sanyao.util.sanyaoyi import create_gua_plot



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

calculate_and_visualize_gua([9, 8, 0])