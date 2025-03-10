import numpy as np
import matplotlib.pyplot as plt

# 参数设置
p = 0.5
n_max = 100
n_values = np.arange(1, n_max + 1)

# 计算求和、积分和误差
sum_terms = np.cumsum(1 / (n_values ** p))          # 求和 S(n) = Σ1/k^p
integral = (n_values ** (1 - p)) / (1 - p) - 1/(1 - p)  # 积分 ∫1/x^p dx 从1到n的解析解
error = sum_terms - integral                         # 误差 R(n) = S(n) - I(n)

# 画图
plt.figure(figsize=(15, 5))

# 子图1：函数 f(x) = 1/x^p 的图像
plt.subplot(1, 3, 1)
x = np.linspace(1, n_max, 1000)
y = 1 / (x ** p)
plt.plot(x, y, 'b-', label='$f(x) = 1/x^{0.5}$')
plt.fill_between(x, y, alpha=0.2, color='blue')
plt.xlabel('$x$'), plt.ylabel('$f(x)$'), plt.title('递减函数 $f(x)$')

# 子图2：求和与积分的增长对比
plt.subplot(1, 3, 2)
plt.plot(n_values, sum_terms, 'r-', label='求和 $S(n) = \sum_{k=1}^n 1/k^{0.5}$')
plt.plot(n_values, integral, 'g--', label='积分 $I(n) = \\frac{n^{0.5}}{0.5} - 2$')
plt.xlabel('$n$'), plt.title('求和与积分的增长'), plt.legend()

# 子图3：误差项 R(n) 趋近常数
plt.subplot(1, 3, 3)
plt.plot(n_values, error, 'k-', label='误差 $R(n) = S(n) - I(n)$')
plt.xlabel('$n$'), plt.title('误差项趋近常数'), plt.legend()

plt.tight_layout()
plt.show()