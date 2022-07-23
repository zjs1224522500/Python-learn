# 导入正则表达式模块
import re
import sys

# 含有数字的字符串（可以看到有小数和整数）
# string = "#$1.23，zimu3，520.1314, 300"
string = sys.argv[1]

# 获取所有数字
# print(re.findall(r"\d+",string))

# 获取所有数值（包含小数一起识别匹配）
nums = re.findall(r"\d+\.?\d*", string)
print(*nums, sep="\n")

