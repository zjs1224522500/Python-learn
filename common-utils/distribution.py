from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
y= random.pareto(a=2, size=1000)
sns.distplot(y, kde=False)

print(x)
sns.distplot(x[x<10], kde=False)
# sns.distplot(x, kde=False)


plt.show()