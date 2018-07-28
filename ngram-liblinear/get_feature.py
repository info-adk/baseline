# coding:utf-8

from sklearn.utils import shuffle
from sklearn.datasets import dump_svmlight_file
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
import os

feature_dir = "/home/iiip/Info/capsnet/n-gram/data/feature(1,3).txt"
ngram = CountVectorizer(ngram_range=(1,3))

def metrics_result(actual,predict):
    accuracy = round(metrics.accuracy_score(actual,predict),3)
    return accuracy

def get_dataset():
    corpus = []
    label_list = []
    datadir = "/home/iiip/Info/capsnet/data/20_newsgroups_new"
    for labelname in os.listdir(datadir):
        labeldir = os.path.join(datadir,labelname)
        for textname in os.listdir(labeldir):
            text = os.path.join(labeldir,textname)
            with open(text,"r") as f:
                content = f.read()
                corpus.append(content)
            label_list.append(labelname)
    data = ngram.fit_transform(corpus)
    return data,label_list

data,label_list = get_dataset()

def get_label(label_list):
    label_list = label_list
    label = []
    label2index = {}
    index = 0
    datadir = "/home/iiip/Info/capsnet/data/20_newsgroups_new"
    for labelname in os.listdir(datadir):
        label2index[labelname] = index
        index+=1
    for i in label_list:
        label.append(label2index[i])
    return label

label = get_label(label_list)
data,label = shuffle(data,label)
print(ngram.ngram_range)
dump_svmlight_file(data,label,feature_dir)

