import pandas as pd
import numpy as np
from  scipy.stats import chi2_contingency

"""label=0 为train label=1 test"""

"""对tumor_size 进行卡方检验"""
csv_path_0 = r'D:\data_process\tongji\test_train\train\train_numeric_feature(2).csv'
csv_0 = pd.read_csv(csv_path_0)
csv_path_1 = r'D:\data_process\tongji\test_train\test\test_numeric_feature(2).csv'
csv_1 = pd.read_csv(csv_path_1)



def tumor_size_kafang(name):
    label_0_tumor_size = np.array(list(csv_0.loc[:, name]))
    lab1e_0_num_1 = 0
    label_0_num_2 = 0
    label_0_num_3 = 0
    lab1e_0_num_4 = 0
    label_0_num_5 = 0
    label_0_num_6 = 0
    lab1e_0_num_7 = 0
    label_0_num_8 = 0
    label_0_num_9 = 0
    lab1e_0_num_10 = 0
    lab1e_0_num_11 = 0
    lab1e_0_num_12 = 0
    number_label_0 = len(csv_0.loc[:, name])
    number_label_1 = len(csv_1.loc[:, name])
    for value in list(label_0_tumor_size):
        if value == 2:
            label_0_num_2 += 1
        elif value == 1:
            lab1e_0_num_1 += 1
        elif value == 3:
            label_0_num_3 += 1
        elif value == 4:
            lab1e_0_num_4 += 1
        elif value == 4:
            lab1e_0_num_4 += 1
        elif value == 5:
            label_0_num_5 += 1
        elif value == 6:
            label_0_num_6 += 1
        elif value == 7:
            lab1e_0_num_7 += 1
        elif value == 8:
            label_0_num_8 += 1
        elif value == 9:
            label_0_num_9 += 1
        elif value == 10:
            lab1e_0_num_10 += 1
        elif value == 11:
            lab1e_0_num_11 += 1
        elif value == 12:
            lab1e_0_num_12 += 1
        else:
            pass
    label_1_tumor_size = np.array(list(csv_1.loc[:, name]))
    lab1e_1_num_1 = 0
    label_1_num_2 = 0
    label_1_num_3 = 0
    lab1e_1_num_4 = 0
    label_1_num_5 = 0
    label_1_num_6 = 0
    lab1e_1_num_7 = 0
    label_1_num_8 = 0
    label_1_num_9 = 0
    lab1e_1_num_10 = 0
    lab1e_1_num_11 = 0
    lab1e_1_num_12 = 0
    for value in list(label_1_tumor_size):
        if value == 2:
            label_1_num_2 += 1
        elif value == 1:
            lab1e_1_num_1 += 1
        elif value == 3:
            label_1_num_3 += 1
        elif value == 4:
            lab1e_1_num_4 += 1
        elif value == 4:
            lab1e_1_num_4 += 1
        elif value == 5:
            label_1_num_5 += 1
        elif value == 6:
            label_1_num_6 += 1
        elif value == 7:
            lab1e_1_num_7 += 1
        elif value == 8:
            label_1_num_8 += 1
        elif value == 9:
            label_1_num_9 += 1
        elif value == 10:
            lab1e_1_num_10 += 1
        elif value == 11:
            lab1e_1_num_11 += 1
        elif value == 12:
            lab1e_1_num_12 += 1
        else:
            pass

    print("train中数据的比例问题：")
    print("train的总个数：", number_label_0)
    print("train中", name, "为1占有的比例：", '%.2f%%' %  ((lab1e_0_num_1 / number_label_0)*100))
    print("个数为：", lab1e_0_num_1)
    print("train中", name, "为2占有的比例：",'%.2f%%' %  (( label_0_num_2 / number_label_0)*100))
    print("个数为：", label_0_num_2)
    print("train中", name, "为3占有的比例：", '%.2f%%' %  ((label_0_num_3 / number_label_0)*100))
    print("个数为：", label_0_num_3)
    print("train中", name, "为3占有的比例：",'%.2f%%' %  (( lab1e_0_num_4 / number_label_0)*100))
    print("个数为：", lab1e_0_num_4)
    print("train中", name, "为1占有的比例：", '%.2f%%' %  ((label_0_num_5 / number_label_0)*100))
    print("个数为：", label_0_num_5)
    print("train中", name, "为2占有的比例：", '%.2f%%' %  ((label_0_num_6 / number_label_0)*100))
    print("个数为：", label_0_num_6)
    print("train中", name, "为3占有的比例：", '%.2f%%' %  ((lab1e_0_num_7 / number_label_0)*100))
    print("个数为：", lab1e_0_num_7)
    print("train中", name, "为1占有的比例：",'%.2f%%' %  (( label_1_num_8 / number_label_0)*100))
    print("个数为：", label_1_num_8)
    print("train中", name, "为2占有的比例：", '%.2f%%' %  ((label_0_num_9 / number_label_0)*100))
    print("个数为：", label_0_num_9)
    print("train中", name, "为3占有的比例：", '%.2f%%' %  ((lab1e_0_num_10 / number_label_0)*100))
    print("个数为：", lab1e_0_num_10)

    print("test中数据的比例问题：")
    print("test的总个数：", number_label_0)
    print("test中", name, "为1占有的比例：", '%.2f%%' %  ((lab1e_1_num_1 / number_label_0)*100))
    print("个数为：", lab1e_0_num_1)
    print("test中", name, "为2占有的比例：", '%.2f%%' %  ((label_1_num_2 / number_label_0)*100))
    print("个数为：", label_0_num_2)
    print("test中", name, "为3占有的比例：", '%.2f%%' %  ((label_1_num_3 / number_label_0)*100))
    print("个数为：", label_0_num_3)
    print("test中", name, "为3占有的比例：", '%.2f%%' %  ((lab1e_1_num_4 / number_label_0)*100))
    print("个数为：", lab1e_0_num_4)
    print("test中", name, "为1占有的比例：", '%.2f%%' %  ((label_1_num_5 / number_label_0)*100))
    print("个数为：", label_0_num_5)
    print("test中", name, "为2占有的比例：", '%.2f%%' %  ((label_1_num_6 / number_label_0)*100))
    print("个数为：", label_0_num_6)
    print("test中", name, "为3占有的比例：", '%.2f%%' %  ((lab1e_1_num_7 / number_label_0)*100))
    print("个数为：", lab1e_0_num_7)
    print("test中", name, "为1占有的比例：", '%.2f%%' %  ((label_1_num_8 / number_label_0)*100))
    print("个数为：", label_1_num_8)
    print("test中", name, "为2占有的比例：", '%.2f%%' %  ((label_1_num_9 / number_label_0)*100))
    print("个数为：", label_0_num_9)
    print("test中", name, "为3占有的比例：", '%.2f%%' %  ((lab1e_1_num_10 / number_label_0)*100))
    print("个数为：", lab1e_0_num_10)

    kf_data = np.array(
        [[  lab1e_0_num_1,label_0_num_2 ,label_0_num_3,lab1e_0_num_4,label_0_num_5,label_0_num_6,lab1e_0_num_7,label_0_num_8,label_0_num_9,lab1e_0_num_10,lab1e_0_num_11,lab1e_0_num_12 ], [ lab1e_1_num_1,label_1_num_2,label_1_num_3,lab1e_1_num_4,label_1_num_5,label_1_num_6,lab1e_1_num_7,label_1_num_8,label_1_num_9,lab1e_1_num_10, lab1e_1_num_11, lab1e_1_num_12]])
    kf = chi2_contingency(kf_data)
    print(name, "卡方分布的结果：")
    print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s' % kf)

name = "tumor_size"
tumor_size_kafang(name)