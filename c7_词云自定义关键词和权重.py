# -*- coding: utf-8 -*-
# @Author: kjjdas
# @Date:   2018-09-09 18:35:20
# @Last Modified time: 2018-09-09 22:55:04

from wordcloud import WordCloud,ImageColorGenerator 
from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt 
import jieba.analyse


text = open('xyj.txt',encoding = 'utf-8').read()

freq = jieba.analyse.extract_tags(text,topK =20,withWeight = True)
freq = {i[0]:i[1] for i in freq}

#可自定义freq字典

mask = np.array(Image.open('timg.jpg'))
wc = WordCloud(font_path = 'Hiragino.ttf',mask = mask,
                mode = 'RGBA',background_color= None).generate_from_frequencies(freq)
# generate() = process_text() + generate_from_frequencies()

plt.imshow(wc,interpolation = 'bilinear')
plt.axis('off')
plt.show()