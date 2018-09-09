# -*- coding: utf-8 -*-
# @Author: kjjdas
# @Date:   201file8-09-09 17:15:21
# @Last Modified time: 2018-09-09 22:53:02


from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open('constitution.txt').read()

wc = WordCloud().generate(text)

plt.imshow(wc,interpolation = 'bilinear')
plt.axis('off')
plt.show()

