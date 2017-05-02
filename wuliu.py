import numpy as np
#import pandas as pd
#导入图表库以进行图表绘制
import matplotlib.pyplot as plt
#图表字体为华文细黑，字号为15
plt.rc('font', family='STXihei', size=15)
#创建一个一维数组赋值给a
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#创建折线图，数据源为按月贷款均值，标记点，标记线样式，线条宽度，标记点颜色和透明度
plt.plot(loan_plot,'g^',loan_plot,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
#添加x轴标签
plt.xlabel('时间')
#添加y周标签
plt.ylabel('库存')
#添加图表标题
plt.title('分月贷款金额分布')
#添加图表网格线，设置网格线颜色，线形，宽度和透明度
plt.grid( color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
#设置数据分类名称
plt.xticks(a, ('18:47','18:48','18:49','18:50','18:51','18:52','18:53','18:54','18:55','18:56','18:57','18:58') )
#输出图表
plt.show()