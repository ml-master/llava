# 本文件用于测试微调后的llava模型，生成模型的输入数据集，存储在Path/to/finetune/quesion.jsonl中
# gossipcop-1202546208_top_img.png 这张图片打不开,使用spcae.png代替
import json


# 读取数据文件
with open('Path/to/test.json', 'r') as file:
    data = json.load(file)

# 准备写入quesion.jsonl文件
with open('Path/to/finetune/quesion.jsonl', 'w') as file:
    question_id = 0
    for value in data:
        # 根据has_top_img决定image字段
        if value['has_top_img'] == 1:
            image_file = value['origin_id']+"_top_img.png"
        else:
            image_file = "space.png"
        if image_file == "gossipcop-1202546208_top_img.png":
            image_file = "space.png"
        
        # 构建每条记录
        record = {
            "question_id": question_id,
            "image": image_file,
            "text": "I will tell you a piece of news, and you need to determine whether this news is true or false. The news is as follows:"+value['origin_text'] + "You need to judge whether this news is true or false. You only need to answer with 0 or 1, where 0 represents false and 1 represents true.",
            "category": "conv"
        }
        
        # 写入文件，每条记录一行
        json.dump(record, file)
        file.write('\n')  # 每个JSON对象后添加换行符
        question_id += 1

print("quesion.jsonl文件已生成")
