import os

data = []
with open("sample", "rt") as fd:
    for line in fd:
        line = line.rstrip()
        gt, pred = line.split(",")
        if gt == "TRUE":
            gt = True
        else:
            gt = False

        data.append((gt, int(pred)))

fp = tp = tn = 0
min_fp = len(data)
min_th = 0
min_acc = 0

for th in range(0, 100):
    for gt, pred in data:
        if pred >= th and gt:
            tp += 1
        elif pred < th and not gt:
            tn += 1
        elif pred >= th and not gt:
            fp += 1


    acc = ((tp + tn) / len(data)) * 100.0
    if acc >= 65.0:
        if fp < min_fp:
            min_fp = fp
            min_th = th
            min_acc = acc

    tp = tn = fp = 0

print("acc:", min_acc, "th:", min_th, "fp:", min_fp)
