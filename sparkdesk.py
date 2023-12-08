# 导入matplotlib库中的pyplot模块
import matplotlib.pyplot as plt

# 准备数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 使用plot()函数绘制折线图
plt.plot(x, y)

# 设置x轴和y轴的标签
plt.xlabel('X轴')
plt.ylabel('Y轴')

# 设置图像的标题
plt.title('折线图示例')

# 使用show()函数显示图像
plt.show()
