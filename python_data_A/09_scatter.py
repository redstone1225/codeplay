import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.scatter([1, 2, 3, 4], [10, 30, 20, 40], s = [30, 60, 90, 120], c = range(4), cmap = 'jet')
# plt.colorbar()
# plt.show()

import csv
import random

from matplotlib import font_manager, rc

font_path = "python_data_A/src/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)

x = list(range(0, 101))
y = []

for i in data:
    if "용문면" in i[0]:
        y = i[3:]

for change in range(len(y)):
    y[change] = int(y[change])

size = y

# for i in range(100) :
#     x.append(random.randint(50, 100))
#     y.append(random.randint(50, 100))
#     size.append(random.randint(10, 100))
plt.scatter(x, y, s=size)

# plt. scatter(x, y, s=size, c=size, cmap='jet')
# plt.colorbar()

plt.scatter(x, y, s=size, c=size, cmap = 'jet', alpha=0.7)
plt.colorbar()

plt.show()