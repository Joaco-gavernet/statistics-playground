import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data = np.random.normal(100, 20, 200)

fig = plt.figure(figsize=(8, 6))

plt.boxplot(data)  # Creating plot
plt.show()
