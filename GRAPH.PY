#matplotllb
import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns
sns.displot([1.1,1.2,1.3,1.4,1.5])
plt.show()

#normal distribution
sns.displot(random.normal(size=5000))
plt.show()

#binomial distribution
sns.displot(random.binomial(n=5,p=0.55,size=(5000)))
plt.show()

#poisson distribution
sns.displot(random.poisson(lam=15,size=1000),kde=False)
plt.show()
            
#uniform distribution
sns.displot(random.uniform(size=(7,11)))
plt.show()