# 使用llava进行假新闻检测
llava(Large Language and Vision Assistant)是一个大语言模型，支持多模态数据集进行任务微调，本研究利用假新闻检测的数据集对llava进行微调，提高假新闻检测的准确率。
本次实验使用RTX3090显卡，base模型使用: liuhaotian/llava-v1.5-7b

## 安装
1. 克隆仓库
```bash
git clone https://github.com/haotian-liu/LLaVA.git
cd LLaVA
```
2. 安装必要的package
```Shell
conda create -n llava python=3.10 -y
conda activate llava
pip install --upgrade pip  # enable PEP 660 support
pip install -e .
```
3. 为了训练安装额外的包
```
pip install -e ".[train]"
pip install flash-attn --no-build-isolation
```
4. 下载权重（liuhaotian/llava-v1.5-7b):https://huggingface.co/liuhaotian/llava-v1.5-7b

## 数据预处理
打乱原始数据，按照8:2的比例将数据分为训练集和测试集
```Shell
python ./scripts/fake_news/data-classification.py
```
## 不微调，直接利用llava模型自带的推理能力进行假新闻检测
```Shell
python ./llava/eval/model_vqa.py \
    --model-path path/to/llava-v1.5-7b \
    --question-file \
    path/to/quesion.jsonl \
    --image-folder \
    path/to/style_img \
    --answers-file \
    path/to/answer.jsonl
```
## 使用rola微调llava
1.在训练集上微调
```Shell
sh ./scripts/v1_5/finetune_task_lora.sh
```
2.融合rola的权重与base-model
```Shell
python ./scripts/merge_lora_weights.py  \
    --model-path path/to/llava-v1.5-7b-task-lora \
    --model-base path/to/llava-v1.5-7b \
    --save-model-path path/to/merge_model
```
## 实验结果


