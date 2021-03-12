my_dict = {'name': 'isaac', 'age': 18, 'gender': '男', 1: 'float'}

# for循环直接遍历字典, 遍历的字典的key值
# for i in my_dict:
#     print('key：', i, '   value:', my_dict[i])

# 字典.keys() 获取字典中所有的key值， 得到类型是dict_keys, 该类型具有的特点是
# 1. 可以使用list() 进行类型转换，即将器转换为列表类型
# 2. 可以使用for循环进行遍历

result = my_dict.keys()
print(result, type(result))
for key in result:
    print(key)
    print(my_dict[key])




