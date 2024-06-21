import json
import random
# 将原始数据打乱，并且分为训练集和测试集,8 : 2



# 读取数据
with open('path/to/gossipcop_v3-1_style_based_fake.json', 'r') as file:
    data = json.load(file)

# 检查数据类型
if isinstance(data, dict):
    # 获取字典的值，转换为列表
    items = list(data.values())
    random.shuffle(items)  # 打乱列表
elif isinstance(data, list):
    items = data
    random.shuffle(items)
else:
    raise TypeError("Unsupported data type")

# 分割数据
split_index = int(len(items) * 0.8)
train_data = items[:split_index]
test_data = items[split_index:]

# 写入文件
with open('path/to/train.json', 'w') as file:
    json.dump(train_data, file, indent=4)
with open('path/to/test.json', 'w') as file:
    json.dump(test_data, file, indent=4)

print("Data has been split into train.json and test.json.")