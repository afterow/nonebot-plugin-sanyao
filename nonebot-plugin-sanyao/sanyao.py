import datetime
import cnlunar

bagua = {
    "乾": [[1, 1, 1], 1],
    "兑": [[0, 1, 1], 2],
    "离": [[1, 0, 1], 3],
    "震": [[0, 0, 1], 4],
    "巽": [[1, 1, 0], 5],
    "坎": [[0, 1, 0], 6],
    "艮": [[1, 0, 0], 7],
    "坤": [[0, 0, 0], 8]

}

big_gua = [
    ["乾为天", "天泽履", "天火同人", "天雷无妄", "天风姤", "天水讼", "天山遁", "天地否"],
    ["泽天夬", "兑为泽", "泽火革", "泽雷随", "泽风大过", "泽水困", "泽山咸", "泽地萃"],
    ["火天大有", "火泽睽", "离为火", "火雷噬嗑", "火风鼎", "火水未济", "火山旅", "火地晋"],
    ["雷天大壮", "雷泽归妹", "雷火丰", "震为雷", "雷风恒", "雷水解", "雷山小过", "雷地豫"],
    ["风天小畜", "风泽中孚", "风火家人", "风雷益", "巽为风", "风水涣", "风山渐", "风地观"],
    ["水天需", "水泽节", "水火既济", "水雷屯", "水风井", "坎为水", "水山蹇", "水地比"],
    ["山天大蓄", "山泽损", "山火贲", "山雷姬", "山风蛊", "山水蒙", "艮为山", "山地剥"],
    ["地天泰", "地泽临", "地火明夷", "地雷复", "地风升", "地水师", "地山谦", "坤为地"]
]


def get_parity(numbers):
    # 定义一个空列表用于存储结果
    result = []
    # 将输入的数字转换为整数并判断奇偶性
    for num in numbers:
        num = int(num)
        if num % 2 == 0:  # 如果是偶数
            result.append(0)
        else:  # 如果是奇数
            result.append(1)
    return result  # 不要忘记返回结果列表


# 卦象得到卦名
def find_key_by_value(bagua_dict, target_value):
    for key, value in bagua_dict.items():
        if value[0] == target_value:
            return key, value  # 如果找到，返回键
    return '没有找到'  # 如果循环结束还没有找到，返回没有找到


def toggle_element(target_value):
    # 创建临时列表
    tmp_list = list(target_value)

    # 获取本卦
    man_gua = find_key_by_value(bagua, tmp_list)

    # 计算列表中所有元素的和
    total_sum = sum(tmp_list)

    # 计算变爻位置（Python索引从0开始，无需减1）
    yaobian = total_sum % 3

    # 切换变爻位置上的元素
    tmp_list[yaobian] = 0 if tmp_list[yaobian] == 1 else 1

    # 创建合并列表
    flattened_list = target_value + tmp_list
    # 获取变卦、互卦、错卦和综卦
    Bian_gua = find_key_by_value(bagua, tmp_list)
    hu_ben = find_key_by_value(bagua, flattened_list[1:4])
    hu_bian = find_key_by_value(bagua, flattened_list[2:5])

    # 创建补码列表
    result_tmp_list = [1 if value == 0 else 0 for value in flattened_list]

    # 获取错卦
    cuo_ben = find_key_by_value(bagua, result_tmp_list[0:3])
    cuo_bian = find_key_by_value(bagua, result_tmp_list[3:6])

    # 创建反向列表并获取综卦
    reverse_tmp_list = flattened_list[::-1]
    zong_ben = find_key_by_value(bagua, reverse_tmp_list[0:3])
    zong_bian = find_key_by_value(bagua, reverse_tmp_list[3:6])

    # 打印卦的名称和相关信息
    A1 = ("本卦：{}之{}".format(man_gua[0], Bian_gua[0]))
    A2 = ("互卦：{}之{}".format(hu_ben[0], hu_bian[0]))
    A3 = ("错卦：{}之{}".format(cuo_ben[0], cuo_bian[0]))  # 修正了变量名
    A4 = ("综卦：{}之{}".format(zong_ben[0], zong_bian[0]))  # 修正了变量名
    xx = f"{A1}\n{A2}\n{A3}\n{A4}"
    return xx


# 获取当前日期的上一个和下一个节气
def get_previous_and_next_solar_terms(current_date, solar_terms_dict):
    # 初始化上一个和下一个节气的名称和日期
    previous_term = None
    next_term = None
    previous_date = None
    next_date = None

    # 遍历节气字典，找到当前日期所在的节气以及上一个和下一个节气
    for term, (month, day) in solar_terms_dict.items():
        if current_date.month > month or (current_date.month == month and current_date.day >= day):
            next_term = term
            next_date = (current_date.year, month, day)
        else:
            if previous_term is None:
                previous_term = term
                previous_date = (current_date.year, month, day)

    # 如果当前日期在第一个节气之前，则没有上一个节气
    if previous_term is None:
        previous_term = None
        previous_date = None

    # 如果当前日期在最后一个节气之后，则下一个节气是下一年的第一个节气
    if next_term is None:
        next_year = current_date.year + 1
        for term, (month, day) in solar_terms_dict.items():
            next_term = term
            next_date = (next_year, month, day)
            break

    # 将日期从元组转换为字符串格式
    previous_date_str = "{},{},{}".format(previous_date[0], previous_date[1],
                                          previous_date[2]) if previous_date else None
    next_date_str = "{},{},{}".format(next_date[0], next_date[1], next_date[2])

    return (previous_term, previous_date_str), (next_term, next_date_str)


# 打印结果
# 日期
def print_lunar_info_and_bazi(nums_list):
    # 获取今天的日期和时间
    today = datetime.datetime.now()
    # 将今天的日期和时间转换为农历日期
    a = cnlunar.Lunar(today, godType='8char', year8Char='beginningOfSpring')
    # 计算上一个和下一个节气
    previous_and_next_terms = get_previous_and_next_solar_terms(today, a.thisYearSolarTermsDic)
    bengua = find_key_by_value(bagua, get_parity(nums_list))
    biangua = bengua
    # 日期
    # print(a.lunarSeason, str(a.date)[0:19])
    # print(previous_and_next_terms[1][0], previous_and_next_terms[1][1], "到", previous_and_next_terms[0][0],
    #       previous_and_next_terms[0][1])
    #
    # # 农历月份和日期
    # print(a.lunarMonthCn, a.lunarDayCn)
    #
    # # 今日八字
    # print(a.year8Char[0] + a.month8Char[0] + a.day8Char[0] + a.twohour8Char[0])
    # print(a.year8Char[1] + a.month8Char[1] + a.day8Char[1] + a.twohour8Char[1])

    # 目标值并切换元素
    target_value = biangua[1][0]
    cc = toggle_element(target_value)
    return cc
