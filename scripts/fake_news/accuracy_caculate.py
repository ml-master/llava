# 提取答案，计算准确率
import json
import os

def calculate_ACC(model, data_set):
    print('=================================================')
    # 读取模型预测的llava的答案
    if model == 'origin':
        model_data_path = 'path/to/origin_data/'+ 'answer_'+data_set+'.jsonl'
    else:
        model_data_path = 'path/to/finetue_data/'+ 'answer_'+data_set+'.jsonl'
    llava_answer = []
    with open(model_data_path, 'r') as file:
        for line in file:
            # 将每一行的JSON字符串转换为字典
            data = json.loads(line)
            # 从字典中提取text字段的值，并添加到列表中
            llava_answer.append(data['text'])


    # 读取数据的真实标签
    tag_data_path = 'path/to/tag_data/'+data_set+'.json'
    with open(tag_data_path,'r') as file:
        data_tag = json.load(file)
    
    # 处理模型预测的llava的答案
    tag = []
    for value in data_tag:
        if value['origin_label'] == "fake":  # 0代表假新闻，1代表真新闻
            tag.append('0')
        else:
            tag.append('1')

    # 确保新闻的数量的相等
    assert len(llava_answer) == len(tag), "新闻的数量不相等"

    print(data_set+'集中'+"新闻的总数量为: " + str(len(llava_answer)))
    num_fake = 0
    num_legitimate = 0
    for i in range (len(tag)):
        if tag[i] == '0':
            num_fake = num_fake + 1
        else:
            num_legitimate = num_legitimate + 1
    assert num_fake + num_legitimate == len(tag), "数据标签有误"
    print("真新闻数量 : " + str(num_legitimate))
    print("假新闻数量 : " + str(num_fake))
    

    num = 0  # 用于计算整体准确率

    num_legitimate_predict = 0 #真实新闻中的预测为真实新闻的个数
    num_fake_predict = 0  #假新闻中预测为假新闻的个数

    for i in range (len(llava_answer)):
        if llava_answer[i] == tag[i]: # 计算整体的准确率
            num = num + 1
        if tag[i] == '1' and llava_answer[i] == '1': # 计算真实新闻中的准确率
            num_legitimate_predict += 1
        if tag[i] == '0' and llava_answer[i] == '0' :  # 计算虚假新闻中的准确率
            num_fake_predict += 1

    # print("total predict: " + str(num))
    # print("fake news predict: " + str(num_fake_predict))
    # print("legitimate predict: " + str(num_legitimate_predict))
    # print("=============================================")

    print(model+'模型在'+data_set+'集中,'+"总体准确率为：" + str(num / len(llava_answer)))
    print(model+'模型在'+data_set+'集中,'+"真实新闻预测准确率为：" + str(num_legitimate_predict / num_legitimate))
    print(model+'模型在'+data_set+'集中,'+"虚假新闻预测准确率为：" + str(num_fake_predict / num_fake))


def main():
   
    data_set = ['train', 'test']
    #使用微调之前的llava模型
    calculate_ACC('origin', 'train')
    calculate_ACC('origin', 'test')

    #使用微调之后的模型
    calculate_ACC('finetune', 'train')
    calculate_ACC('finetune', 'test')

if __name__ == '__main__':
    main()

