# 字典 dict 定义使用 {} 定义， 是由键值对（key - value）
# 变量 = {key1：value1，key2：value2，...}  一个key1：value1 键值对是一个元素
# 字典的key 可以是 字符串类型和数字类型（int float）， 不能是列表
# value值可以是任何类型

# 1. 定义空字典
my_dict = {}
my_dict1 = dict()
print(my_dict, type(my_dict))
print(my_dict1, type(my_dict1))

# 2. 定义带数据的字典
my_dict2 = {'name': 'isaac', 'age': 18, 'like': ['学习', '购物', '游戏'], 1: [2, 5, 8]}
print(my_dict2)

# 3. 访问value 值， 在字典中没有下标的概念， 使用key值访问对应的value 值
# 18
print(my_dict2['age'])
# '购物'
print(my_dict2['like'][1])

# 如果key值不存在
# print(my_dict2['gender']) 代码报错，key值不存在
# 字典.get 如果key值不存在，不会报错，返回值是None
print(my_dict2.get('gemder'))

# my_dict2.get(key, 数据值) 如果可以存在，返回key 对应的value值 如果key不存在，返回书写的数据值
print(my_dict2.get('gender', '男'))
print(my_dict2.get('age', 1))

print(len(my_dict2)) # 4
