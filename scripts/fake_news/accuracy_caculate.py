# 提取答案，计算准确率
import json

# 读取llava的答案
llava_answer = []
with open('Path/to/answer.jsonl', 'r') as file:
    for line in file:
        # 将每一行的JSON字符串转换为字典
        data = json.loads(line)
        # 从字典中提取text字段的值，并添加到列表中
        llava_answer.append(data['text'])


# 读取原数据标签
with open('Path/to/test.json','r') as file:
    data_tag = json.load(file)
   
# 读取标签
tag = []
for value in data_tag:
    if value['origin_label'] == "fake":
        tag.append('0')
    else:
        tag.append('1')

# 使用断言来确保两个列表的长度相等
assert len(llava_answer) == len(tag), "两个列表的长度不相等"

#打印前20个看看
print(llava_answer[:20])
print(tag[:20])

print("新闻的数量为: " + str(len(llava_answer)))
num_fake = 0
num_legitimate = 0
for i in range (len(tag)):
    if tag[i] == '0':
        num_fake = num_fake + 1
    else:
        num_legitimate = num_legitimate + 1
# 断言真实新闻数量 + 虚假新闻数量 = 新闻总数量
assert num_fake + num_legitimate == len(tag), "数据标签有误"
print("fake news : " + str(num_fake))
print("legitimate : " + str(num_legitimate))

num = 0
for i in range (len(llava_answer)):
    if llava_answer[i] == tag[i]:
        num = num + 1


print("准确率为：" + str(num / len(llava_answer)))
