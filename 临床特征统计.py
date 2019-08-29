import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import ttest_ind, levene
from  scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

"""计算771数据的文件路径"""
csv_path_0 = r'D:\data_process\tongji\clinical\771_0.csv'
csv_0 = pd.read_csv(csv_path_0)
csv_path_1 = r'D:\data_process\tongji\clinical\771_1.csv'
csv_1 = pd.read_csv(csv_path_1)

def Age():

    Age_0 = np.array(list(csv_0.loc[:, "Age"]))
    Age_1 = np.array(list(csv_1.loc[:, "Age"]))

    pd_csv = pd.DataFrame({'label_0': csv_0.loc[:, "Age"],
                           'label_1': csv_1.loc[:, "Age"]}
                          )
    pd_csv.plot.hist(bins=30)
    plt.xlabel("value")
    plt.title("data_graph")
    plt.show()
    mean_age_1 = np.mean(Age_1)
    mean_age_0 = np.mean(Age_0)
    var_age_1 = np.var(Age_1)
    var_age_0 = np.var(Age_0)
    std_age_1 = np.std(Age_1)
    std_age_0 = np.std(Age_0)

    print("######################################################")
    print("Age_result:")
    print("lable=0；", mean_age_0, "±", std_age_0)
    print("lable=1；", mean_age_1, "±", std_age_1)
    print("label=0, 正态性检验，若p大于0.05则是正态性的:")
    norm_test_0 = stats.kstest(Age_0, 'norm', (mean_age_0, std_age_0))  # 正太性检验，若p大于0.5则是正太性的
    print(norm_test_0)
    print("label=1, 正态性检验，若p大于0.05则是正态性的:")
    norm_test_1 = stats.kstest(Age_1, 'norm', (mean_age_1, std_age_1))  # 正太性检验，若p大于0.5则是正太性的
    print(norm_test_1)
    print("方差齐性检验, 若p大于0.05则方差是齐性的:")
    print(levene(Age_0, Age_1)) # 方差齐性检验
    print("方差齐性下的独立样本t检验:")
    print(ttest_ind(Age_0, Age_1))  # 方差齐性下的独立样本t检验
    print("t 检验是检查两组数据的均值差异大小的检验方法，其零假设是均值之间差是0，p很小，我们将拒绝零假设")
    u_statistic, pVal = stats.mannwhitneyu(Age_0, Age_1)
    print("u检验的结果：")
    print("u_statistic =", u_statistic, "   p_value =", pVal)
    print("######################################################\n")
Age()

"""卡方检验"""

def Mstage_CEA_CA199(name):
    number_la_0 = len(csv_0.loc[:,name])
    number_la_1 = len(csv_1.loc[:,name])
    la_0_name = np.array(list(csv_0.loc[:, name]))
    la_0_number_1 = 0
    la_0_number_0 = 0
    for value in list(la_0_name):
        if value == 0:
            la_0_number_0 += 1
        elif value == 1:
            la_0_number_1 += 1
        else:
            pass
    la_1_name = np.array(list(csv_1.loc[:, name]))
    la_1_number_1 = 0
    la_1_number_0 = 0
    for value in list(la_1_name):
        if value == 0:
            la_1_number_0 += 1
        elif value == 1:
            la_1_number_1 += 1
        else:
            pass
    kf_data = np.array([[la_0_number_0, la_1_number_0], [la_0_number_1, la_1_number_1]])
    kf = chi2_contingency(kf_data)
    print("######################################################")
    print("数据的比例问题：")
    print("label=0的总个数：", number_la_0)
    print("label=0中",name,"为0占有的比例：", '%.2f%%' % ((la_0_number_0/number_la_0) * 100))
    print("个数为",la_0_number_0)
    print("label=0中", name, "为1占有的比例：", '%.2f%%' % ((la_0_number_1 / number_la_0) * 100))
    print("个数为",la_0_number_1)
    print("label=1的总个数：", number_la_1)
    print("label=1中", name, "为0占有的比例：", '%.2f%%' % ((la_1_number_0 / number_la_1) * 100))
    print("个数为",la_1_number_0)
    print("label=1中", name, "为1占有的比例：", '%.2f%%' % ((la_1_number_1 / number_la_1) * 100))
    print("个数为",la_1_number_1)
    print(name, "卡方分布的结果：")
    print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s' % kf)
    print("######################################################\n")
name = "CEA"
Mstage_CEA_CA199(name)
name = "Mstage"
Mstage_CEA_CA199(name)
name = "CA199"
Mstage_CEA_CA199(name)


def Grade_Histotype(name):
    lable_0_Grade = np.array(list(csv_0.loc[:,name]))
    lab1e_0_num_1 = 0
    lable_0_num_2 = 0
    lable_0_num_3 = 0
    number_label_0 = len(csv_0.loc[:, name])
    number_label_1 = len(csv_1.loc[:, name])
    for value in list(lable_0_Grade):
        if value == 2:
            lable_0_num_2 += 1
        elif value == 1:
            lab1e_0_num_1 += 1
        elif value == 3:
            lable_0_num_3 += 1
        else:
            pass
    lable_1_Grade = np.array(list(csv_1.loc[:,name]))
    lab1e_1_num_1 = 0
    lable_1_num_2 = 0
    lable_1_num_3 = 0
    for value in list(lable_1_Grade):
        if value == 2:
            lable_1_num_2 += 1
        elif value == 1:
            lab1e_1_num_1 += 1
        elif value == 3:
            lable_1_num_3 += 1
        else:
            pass
    # print(lable_0_number_2)
    # print(lab1e_0_number_1)
    # print(lable_1_number_2)
    # print(lab1e_1_number_1)
    print("######################################################")
    print("数据的比例问题：")
    print("label=0的总个数：", number_label_0)
    print("label=0中",name,"为1占有的比例：", '%.2f%%' % ((lab1e_0_num_1 / number_label_0) * 100))
    print("个数为：",lab1e_0_num_1)
    print("label=0中",name,"为2占有的比例：", '%.2f%%' % ((lable_0_num_2 / number_label_0) * 100))
    print("个数为：", lable_0_num_2)
    print("label=0中",name,"为3占有的比例：", '%.2f%%' % ((lable_0_num_3 / number_label_0) * 100))
    print("个数为：", lable_0_num_3)
    print("label=1的总个数：", number_label_1)
    print("label=1中",name,"为1占有的比例：", '%.2f%%' % ((lab1e_1_num_1 / number_label_1) * 100))
    print("个数为：", lab1e_1_num_1)
    print("label=1中",name,"为2占有的比例：", '%.2f%%' % ((lable_1_num_2 / number_label_1) * 100))
    print("个数为：", lable_1_num_2)
    print("label=1中",name,"为3占有的比例：", '%.2f%%' % ((lable_1_num_3 / number_label_1) * 100))
    print("个数为：", lable_1_num_3)
    kf_data = np.array([[lable_0_num_2, lab1e_0_num_1, lable_0_num_3], [lable_1_num_2, lab1e_1_num_1, lable_1_num_3]])
    kf = chi2_contingency(kf_data)
    print(name,"卡方分布的结果：")
    print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s' % kf)
    print("######################################################\n")
name = "Grade"
Grade_Histotype(name)
name = "Histotype"
Grade_Histotype(name)


def Sex_Location_Histotype(name):
    lab_0_name = np.array(list(csv_0.loc[:,name]))
    lab_0_number_1 = 0
    lab_0_number_2 = 0
    number_lab_0 = len(csv_0.loc[:, name])
    number_lab_1 = len(csv_1.loc[:, name])
    for value in list(lab_0_name):
        if value == 2:
            lab_0_number_2 += 1
        elif value == 1:
            lab_0_number_1 += 1
        else:
            pass
    lab_1_name = np.array(list(csv_1.loc[:,name]))
    lab_1_number_1 = 0
    lab_1_number_2 = 0
    for value in list(lab_1_name):
        if value == 2:
            lab_1_number_2 += 1
        elif value == 1:
            lab_1_number_1 += 1
        else:
            pass
    print("######################################################")
    print("数据的比例问题：")
    print("label=0的总个数：", number_lab_0)
    print("label=0中", name, "为1占有的比例：", '%.2f%%' % ((lab_0_number_1 / number_lab_0) * 100))
    print("个数为：",lab_0_number_1)
    print("label=0中", name, "为2占有的比例：", '%.2f%%' % ((lab_0_number_2 / number_lab_0) * 100))
    print("个数为：", lab_0_number_2)
    print("label=1的总个数：", number_lab_1)
    print("label=1中", name, "为1占有的比例：", '%.2f%%' % ((lab_1_number_1 / number_lab_1) * 100))
    print("个数为：", lab_1_number_1)
    print("label=1中", name, "为2占有的比例：", '%.2f%%' % ((lab_1_number_2 / number_lab_1) * 100))
    print("个数为：", lab_1_number_2)
    kf_data = np.array([[lab_0_number_2, lab_0_number_1], [lab_1_number_2, lab_1_number_1]])
    kf = chi2_contingency(kf_data)
    print(name,"卡方分布的结果：")
    print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s' % kf)
    print("######################################################\n")
name = "Sex"
Sex_Location_Histotype(name)
name = "Location"
Sex_Location_Histotype(name)
