import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 示例数据
data = [12, 15, 14, 10, 18, 20, 15, 14, 13, 17]

# 统计操作
minimum = np.min(data)
maximum = np.max(data)
mean = np.mean(data)
median = np.median(data)
mode_result = stats.mode(data)
mode = mode_result.mode  # 获取众数
std_dev = np.std(data)

# 打印统计结果
print(f"最小值: {minimum}")
print(f"最大值: {maximum}")
print(f"平均值: {mean}")
print(f"中位数: {median}")
print(f"众数: {mode}")
print(f"标准差: {std_dev}")

# 可视化操作
plt.figure(figsize=(10, 5))

# 直方图
plt.subplot(1, 2, 1)
plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.title('直方图')
plt.xlabel('值')
plt.ylabel('频率')

# 箱线图
plt.subplot(1, 2, 2)
plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title('箱线图')
plt.xlabel('值')

plt.tight_layout()
plt.show()

