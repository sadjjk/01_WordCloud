# -*- coding: utf-8 -*-
# @Author: kjjdas
# @Date:   2018-09-09 17:35:09
# @Last Modified time: 2018-09-09 22:53:28


from wordcloud import WordCloud
import matplotlib.pyplot as plt 
from PIL import Image
import numpy as np 
import jieba 

text = open('xyj.txt',encoding = 'utf-8').read()


text = ' '.join(jieba.cut(text))

wc = WordCloud(font_path = 'Hiragino.ttf',
                mode = 'RGBA',background_color = None).generate(text)

plt.imshow(wc,interpolation= 'bilinear')
plt.axis('off')
plt.show()

