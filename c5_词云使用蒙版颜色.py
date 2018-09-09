# -*- coding: utf-8 -*-
# @Author: kjjdas
# @Date:   2018-09-09 18:09:17
# @Last Modified time: 2018-09-09 22:53:43


from wordcloud import WordCloud,ImageColorGenerator 
import matplotlib.pyplot as plt 
import jieba 
import numpy as np 
from PIL import Image


text = open('xyj.txt',encoding ='utf-8').read()

text  = ' '.join(jieba.cut(text))

mask = np.array(Image.open('color_mask.png'))
wc = WordCloud(mask = mask ,font_path = 'Hiragino.ttf',
                mode = 'RGBA',background_color = None
                ).generate(text)

image_colors = ImageColorGenerator(mask)
wc.recolor(color_func = image_colors)

plt.imshow(wc,interpolation = 'bilinear')
plt.axis('off')
plt.show()
