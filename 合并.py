import pandas as pd
import csv
from wordcloud import WordCloud
import jieba
from PIL import Image  # 安装词云的时候一起装上的
import numpy as np # 安装词云的时候一起装上的
import os



def concat(path1,path2):

    df1 = pd.read_csv("sizhouliu的收藏夹.csv")
    df2 = pd.read_csv("合并数据.csv")
    df3 = pd.concat([df1,df2])
    print(df3)
    df3.to_csv("合并数据.csv")


stopwords = set()
content = [line.strip() for line in open('../cn_stopwords.txt', 'r', encoding="utf-8").readlines()]
stopwords.update(content)

def readComment():
    with open("刘思洲的历史记录.csv", 'r', encoding="utf-8") as file:
        csvRead = csv.reader(file) #加载文件数据
        print(csvRead)
        return [item[1] for item in csvRead] #这是一个列表生成式


def generateWordCloud():
    commentlist = readComment() #获取影评内容
    finalComment = ""
    for comment in commentlist:
        finalComment += comment
    counts = {}  # 通过键值对的形式存储词语及其出现的次数
    words = jieba.lcut(finalComment)
    for word in words:
        if len(word) == 1:  # 单个词语不计算在内
            continue
        else:
            counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序
    alldata = []
    for i in range(100):
        word, count = items[i]
        alldata.append(items[i])
        print("{0:<5}{1:>5}".format(word, count))
    print(alldata)
    df = pd.DataFrame(alldata)
    df.to_csv("特征值3.csv",encoding="gbk")

generateWordCloud()