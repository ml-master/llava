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
