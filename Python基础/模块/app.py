import converters  # 导入体重转换模块
import utils  # 导入寻找最大的数字模块
from converters import lbs_to_kg  # 导入模块的方法

k_to_l = converters.kg_to_lbs(70)
print(k_to_l)
l_to_k = lbs_to_kg(120)
print(l_to_k)

numbers = [10, 3, 6, 2, 20]
max_number = utils.find_max(numbers)
print(max_number)
