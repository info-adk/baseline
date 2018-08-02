# coding:utf-8

from sklearn.utils import shuffle
from sklearn.datasets import dump_svmlight_file
from sklearn.feature_extraction.text import CountVectorizer
import os

feature_file = "/home/iiip/Info/capsnet_baseline/n-gram/data/feature(1,3).txt"
ngram = CountVectorizer(ngram_range=(1, 3))


# data是ngram表示特征的sparse matrix
# label_list是每篇文档所属类别
def get_dataset():
    corpus = []
    label_list = []
    datadir = "/home/iiip/Info/capsnet/data/20_newsgroups_new"
    for labelname in os.liostdir(datadir):
        labeldir = os.path.join(datadir, labelname)
        for textname in os.listdir(labeldir):
            text = os.path.join(labeldir, textname)
            with open(text, "r") as f:
                content = f.read()
                corpus.append(content)
            label_list.append(labelname)
    data = ngram.fit_transform(corpus)
    return data, label_list


# 将每篇文章所属类别转换成integer,即label_list -> lable
def get_label(label_list):
    label_list = label_list
    label = []
    label2index = {}
    index = 0
    datadir = "/home/iiip/Info/capsnet/data/20_newsgroups_new"
    for labelname in os.listdir(datadir):
        label2index[labelname] = index
        index += 1
    for i in label_list:
        label.append(label2index[i])
    return label


def main():
    if __name__ == "__main__":
        data, label_list = get_dataset()
        label = get_label(label_list)
        data, label = shuffle(data, label)  # 打乱数据
        print(ngram.ngram_range)
        dump_svmlight_file(data, label, feature_file)  # 将数据转换成libsvm格式并保存本地


main()
