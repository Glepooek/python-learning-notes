import json

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print(json_str)

python_dic = json.loads(json_str)
print(python_dic)

# 读取文件中的数据
with open('json_example.json', 'r', encoding='utf-8') as file:
    data1 = json.load(file)
    print(data1.__class__)

# 将数据写入文件
# with open('json_example.json', 'w', encoding='utf-8') as file:
#     data1 = json.dump(data1, file)
#     print(data1)
