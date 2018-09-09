# -*- coding: utf-8 -*-
# @Author: kjjdas
# @Date:   2018-09-09 17:27:17
# @Last Modified time: 2018-09-09 22:53:18


from wordcloud import WordCloud
import matplotlib.pyplot as plt

text  = open('xyj.txt',encoding ='gbk').read()

wc = WordCloud(font_path='Hiragino.ttf',width = 800,height= 600,
    mode = 'RGBA',background_color =None).generate(text)


plt.imshow(wc,interpolation = 'bilinear')
plt.axis('off')
plt.show()

