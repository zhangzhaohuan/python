#!/usr/bin/python3
 
dict1 = {'Name': 'Runoob', 'Age': {'name':'zhangzhoahuan'}, 'Class': [1,2,3]}
 
dict2 = dict1.copy()
print ("新复制的字典为 : ",dict2)

print('------fromkeys--------')
keys = ('name', 'age', 'sex')
dict3 = dict.fromkeys(keys, 10)
print ("新的字典为 : %s" %  str(dict3))

 
print('------dirct.keys()--------')
dict4 = {'Name': 'Runoob', 'Age': 7}
print( dict4.keys())
print(list(dict4.keys()))


print('------dirct.update(dict2)--------')
dict5 = {'Name': 'Runoob', 'Age': 7}
dict6 = {'Age': 8 }
dict5.update(dict6)
print ("更新字典 dict5 : ", dict5)


print('------dirct.pop()--------')
dict7= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_val1=dict7.pop('name','123')
pop_val2=dict7.pop('names','456')
print(pop_val1)
print(pop_val2)
print(dict7)

print('------dirct.popitem()--------')
dict8= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=dict8.popitem()
print(pop_obj)
print(dict8)