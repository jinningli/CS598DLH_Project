from matplotlib import pyplot as plt
import numpy as np


train_loss = []
train_accuracy = []
train_f1score = []
train_recall = []
train_precision = []

with open("train.txt", "r") as fin:
    for line in fin:
        splts = line.strip().split(" ")
        train_loss.append(float(splts[0]))
        train_accuracy.append(float(splts[1]))
        train_f1score.append(float(splts[2]))
        train_recall.append(float(splts[3]))
        train_precision.append(float(splts[4]))

val_loss = []
val_accuracy = []
val_f1score = []
val_recall = []
val_precision = []

with open("val.txt", "r") as fin:
    for line in fin:
        splts = line.strip().split(" ")
        val_loss.append(float(splts[0]))
        val_accuracy.append(float(splts[1]))
        val_f1score.append(float(splts[2]))
        val_recall.append(float(splts[3]))
        val_precision.append(float(splts[4]))

def smooth(ls):
    len_ls = len(ls)
    ls = [ls[0], ls[0], ls[0]] + ls + [ls[-1], ls[-1], ls[-1]]
    new_ls = []
    for i in range(3, 3 + len_ls):
        new_ls.append(np.average([ls[i-2], ls[i-1], ls[i], ls[i+1], ls[i+2]]))
    return new_ls

print("F1 Acc Prec")
print(max(val_f1score), max(val_accuracy), max(val_precision))

plt.plot(smooth(train_loss), label="Train loss")
plt.plot(smooth(val_loss), label="Validation Loss")
plt.plot(smooth(train_f1score), label="Train F1-score")
plt.plot(smooth(val_f1score), label="Validation F1-score")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
# plt.show()
plt.savefig("loss.pdf")