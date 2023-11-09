#####################################################
# Analyzing Data
#####################################################

import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, ttest_ind


pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

dataframe_control = pd.read_excel("datasets/ab_testing.xlsx" , sheet_name="Control Group")
dataframe_test = pd.read_excel("datasets/ab_testing.xlsx" , sheet_name="Test Group")

df_control = dataframe_control.copy()
df_test = dataframe_test.copy()


def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head())
    print("##################### Tail #####################")
    print(dataframe.tail())
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df_control)
check_df(df_test)


df_control["group"] = "control"
df_test["group"] = "test"

df = pd.concat([df_control,df_test], axis=0,ignore_index=False)
df.head()
df.tail()


#####################################################
# Defining the Hypothesis of an A/B Test
#####################################################

# Define the Hypothesis.

# H0: M1 = M2 (There is no difference in purchase averages between the control and test groups.)
# H1: M1 != M2 (There is a difference in purchase averages between the control and test groups.)

# Analyze purchase averages for the control and test groups.
df.groupby("group").agg({"Purchase": "mean"})



#####################################################
# Performing the Hypothesis Test
#####################################################
# Before conducting the hypothesis test, perform assumption checks. These include the Normality Assumption and Homogeneity of Variance.

# Test the Normality Assumption for the control and test groups separately using the Purchase variable.
# Normality Assumption:
# H0: The normal distribution assumption is satisfied.
# H1: The normal distribution assumption is not satisfied.
# p < 0.05 Reject H0
# p > 0.05 Fail to reject H0
# Determine whether the normality assumption is satisfied for the control and test groups based on the test results.
# Interpret the obtained p-values.


test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.5891
# Fail to reject H0. The values of the control group satisfy the normal distribution assumption.


test_stat, pvalue = levene(df.loc[df["group"] == "control", "Purchase"],
                           df.loc[df["group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.1083
# Fail to reject H0. The values of the control and test groups satisfy the assumption of homogeneity of variances.
# Variances are homogeneous.

# Based on the results of the Normality Assumption and Homogeneity of Variance, choose the appropriate test.
# Since the assumptions are met, an independent two-sample t-test (parametric test) is conducted.
# H0: M1 = M2 (There is no statistically significant difference in purchase averages between the control and test groups.)
# H1: M1 != M2 (There is a statistically significant difference in purchase averages between the control and test groups.)
# p < 0.05 Reject H0, p > 0.05 Fail to reject H0


test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                              df.loc[df["group"] == "test", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Considering the obtained p-value from the test, interpret whether there is a statistically significant difference in purchase averages between the control and test groups.
# p-value = 0.3493
# Fail to reject H0. There is no statistically significant difference in purchase averages between the control and test groups.

