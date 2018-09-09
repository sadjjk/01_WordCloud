# -*- coding: utf-8 -*-
# @Author: kjjdas
# @Date:   2018-09-09 22:12:23
# @Last Modified time: 2018-09-09 22:56:24


from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import jieba.posseg as psg
import jieba

# 只获取前一百万字 太多容易卡死
text = open('斗破苍穹.txt', encoding='gbk').read()[:1000000]


# 获取名词
# jieba.enable_parallel(100) #开启并行模式 win下不支持 很气
text = ' '.join(x.word for x in psg.cut(text) if x.flag.startswith('n'))
# jieba.disable_parallel() #关闭并行模式

# 导入停用词
stopwords = open('stopwords.txt').read().split('\n')

# 导入蒙版
mask = np.array(Image.open('1.jpg'))
wc = WordCloud(mask=mask, font_path='Hiragino.ttf',
               mode='RGBA', background_color=None,
               stopwords=stopwords).generate(text)

# 使用蒙版颜色
image_color = ImageColorGenerator(mask)
wc.recolor(color_func=image_color)


# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()


# 保存词云
wc.to_file('doupo.png')
