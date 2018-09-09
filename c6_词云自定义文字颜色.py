# -*- coding: utf-8 -*-
# @Author: kjjdas
# @Date:   2018-09-09 18:17:46
# @Last Modified time: 2018-09-09 22:53:55


from wordcloud import WordCloud
import matplotlib.pyplot as plt 
from PIL import Image
import numpy as  np 
import  jieba
import random  


text = open('xyj.txt',encoding = 'utf-8').read()

text = ' '.join(jieba.cut(text))


#颜色函数
### HSL 参考文档 https://www.w3.org/wiki/CSS3/Color/HSL
def random_color(word,font_size,position,orientation,font_path,random_state):
    s = 'hsl(120 ,%d%%,%d%%)' % (random.randint(0, 100),random.randint(0, 100))
    return s 

mask = np.array(Image.open('black_mask.png'))
wc = WordCloud(mask = mask ,color_func = random_color,
                font_path = 'Hiragino.ttf',mode = 'RGBA',
                background_color = None).generate(text)


plt.imshow(wc,interpolation = 'bilinear')
plt.axis('off')
plt.show()

