import json
import uuid


# 读取数据文件
with open('path/to/train.json', 'r') as file:
    data_a = json.load(file)

# 创建一个空列表来存储最终的fineTuneData.json格式数据
fineTuneData = []

# 遍历a.json中的数据并转换格式
for key, value in data_a.items():
    if value['has_top_img'] == 1:
        img_path = value['origin_id'] + '_top_img.png'
    else:
        img_path = "space.png"
    # gossipcop-1202546208_top_img.png 这张图片打不开,使用spcae.png代替
    if img_path == "gossipcop-1202546208_top_img.png":
        img_path = "space.png"
    
    if value['origin_label'] == "fake":
        label = '0'
    else:
        label = '1'

    new_entry = {
        "id": value['origin_id'],  
        "image": img_path,
        "conversations": [
            {
                "from": "human",
                "value": "<image>\n"+"I will tell you a piece of news, and you need to determine whether this news is true or false. The news is as follows:"+ value['origin_text']+"You need to judge whether this news is true or false. You only need to answer with 0 or 1, where 0 represents false and 1 represents true."
            },
            {
                "from": "gpt",
                "value": label
            }
        ]
    }
    fineTuneData.append(new_entry)

# 将转换后的数据写入b.json文件
with open('path/to/fineTuneData.json', 'w') as f:
    json.dump(fineTuneData, f, indent=4)

print("fineTuneData.json文件已生成")












