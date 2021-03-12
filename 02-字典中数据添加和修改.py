# 字典中添加和修改数据， 使用key值进行添加和修改
# 字典[key] = 数据值； 如果key值存在，就是修改，如果key值不存在，就是添加
my_dict = {'name':'isaac'}
print(my_dict)
my_dict['age'] = 18 # key值不存在，添加
print(my_dict)

my_dict['age'] = 19 # key值已经存在，就是修改数据
print(my_dict)

# 注意点 key值 int的 1 和float 的1.0 代表一个数据
my_dict[1] = 'int'
print(my_dict)
my_dict[1.0] = 'float'
print(my_dict)
