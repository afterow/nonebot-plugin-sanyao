class GuaCalculator:
    def __init__(self):
        self.bagua = {
            "乾": [[1, 1, 1], 1],
            "兑": [[0, 1, 1], 2],
            "离": [[1, 0, 1], 3],
            "震": [[0, 0, 1], 4],
            "巽": [[1, 1, 0], 5],
            "坎": [[0, 1, 0], 6],
            "艮": [[1, 0, 0], 7],
            "坤": [[0, 0, 0], 8]
        }
        self.biggua = [
            ["乾为天", "天泽履", "天火同人", "天雷无妄", "天风姤", "天水讼", "天山遁", "天地否"],
            ["泽天夬", "兑为泽", "泽火革", "泽雷随", "泽风大过", "泽水困", "泽山咸", "泽地萃"],
            ["火天大有", "火泽睽", "离为火", "火雷噬嗑", "火风鼎", "火水未济", "火山旅", "火地晋"],
            ["雷天大壮", "雷泽归妹", "雷火丰", "震为雷", "雷风恒", "雷水解", "雷山小过", "雷地豫"],
            ["风天小畜", "风泽中孚", "风火家人", "风雷益", "巽为风", "风水涣", "风山渐", "风地观"],
            ["水天需", "水泽节", "水火既济", "水雷屯", "水风井", "坎为水", "坎为水", "水山蹇", "水地比"],
            ["山天大蓄", "山泽损", "山火贲", "山雷颐", "山风蛊", "山水蒙", "艮为山", "山地剥"],
            ["地天泰", "地泽临", "地火明夷", "地雷复", "地风升", "地水师", "地山谦", "坤为地"]
        ]

    def _find_gua_by_value(self, target_value: list) -> list or None:
        """根据卦象值查找对应的卦名和索引"""
        for key, value in self.bagua.items():
            if value[0] == target_value:
                return [key, value[0], value[1]]
        return None

    def _get_palace(self, shanggua_index: int, xiagua_index: int) -> str:
        """根据上下卦索引获取宫位"""
        gua_name = self.biggua[shanggua_index - 1][xiagua_index - 1]
        return gua_name[-2:] if len(gua_name) >= 4 else gua_name[-1]

    def calculate_element_changes(self, input_list: list) -> list:
        """
        计算本卦、变卦、互卦和各个宫位。

        Args:
            input_list (list): 包含三个数字的列表，用于表示初始卦象。

        Returns:
            list: 包含计算结果的列表，包括宫位、本卦、变卦、互卦等信息。
        """
        # 将输入列表转换为二进制表示
        binary_list = [1 if x % 2 else 0 for x in input_list]

        # 1. 计算本卦
        original_gua = self._find_gua_by_value(binary_list)
        if not original_gua:
            return ["本卦未找到"]
        original_gua_name, _, original_gua_index = original_gua

        # 2. 计算变卦
        yao_index = sum(binary_list) % 3  # 确定要变的爻位
        changed_list = binary_list[:]  # 创建一个 binary_list 的副本
        changed_list[yao_index] = 1 if changed_list[yao_index] == 0 else 0  # 改变爻位
        changed_gua = self._find_gua_by_value(changed_list)
        if not changed_gua:
            return ["变卦未找到"]
        changed_gua_name, _, changed_gua_index = changed_gua

        # 3. 计算互卦
        # 合并原始和变更后的列表
        combined_list = binary_list + changed_list
        # 提取互卦
        inter_gua_1 = self._find_gua_by_value(combined_list[1:4])
        inter_gua_2 = self._find_gua_by_value(combined_list[2:5])

        if not inter_gua_1 or not inter_gua_2:
            return ["互卦未找到"]

        inter_gua_name_1, _, inter_gua_index_1 = inter_gua_1
        inter_gua_name_2, _, inter_gua_index_2 = inter_gua_2

        # 4. 计算各个宫位
        palaces = [
            self._get_palace(changed_gua_index, inter_gua_index_2),  # 子宫
            self._get_palace(original_gua_index, inter_gua_index_1),  # 丑宫
            self._get_palace(changed_gua_index, inter_gua_index_1),  # 寅宫
            self._get_palace(inter_gua_index_2, inter_gua_index_1),  # 卯宫
            self._get_palace(changed_gua_index, original_gua_index),  # 辰宫
            self._get_palace(inter_gua_index_2, original_gua_index),  # 巳宫
            self._get_palace(inter_gua_index_1, original_gua_index),  # 午宫
            self._get_palace(inter_gua_index_2, changed_gua_index),  # 未宫
            self._get_palace(inter_gua_index_1, changed_gua_index),  # 申宫
            self._get_palace(original_gua_index, changed_gua_index),  # 酉宫
            self._get_palace(inter_gua_index_1, inter_gua_index_2),  # 戌宫
            self._get_palace(original_gua_index, inter_gua_index_2)  # 亥宫
        ]

        # 5. 返回结果
        return palaces + [
            original_gua_name,  # 本卦
            changed_gua_name,  # 变卦
            inter_gua_name_1,  # 互卦1
            inter_gua_name_2  # 互卦2
        ]
