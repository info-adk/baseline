# coding:utf-8

from sklearn import metrics
from liblinearutil import svm_read_problem,predict,problem,parameter,train

feature_dir = "/home/iiip/Info/capsnet_baseline/n-gram/data/feature(1,1).txt"

def metrics_result(actual, predict):
    accuracy = round(metrics.accuracy_score(actual, predict), 3)
    precision = round(metrics.precision_score(actual, predict,average="weighted"), 3)
    recall = round(metrics.recall_score(actual, predict,average="weighted"), 3)
    return accuracy,precision,recall


def main():
    if __name__ == "__main__":
        y, x = svm_read_problem(feature_dir, return_scipy = True)
        # train:test = 7:3
        train_X = x[:14000]
        train_y = y[:14000]
        test_X = x[14000:]
        test_y = y[14000:]

        prob = problem(train_y,train_X)
        param = parameter("-c 1 -s 2")
        model = train(prob,param)
        p_labs, p_acc, p_vals = predict(test_y, test_X, model)
        accuracy, precision, recall = metrics_result(test_y,p_labs)
        print
        print "accuracy: ",accuracy
        print "precision: ",precision
        print "recall: ",recall

main()
