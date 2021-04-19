# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 09:44:56 2021

@author: Yue

博客名称为“日期+文章名称”
"""
import os,re,json

FileDictList = []
FilesDir = os.walk('posts') 
for root, dirs, files in FilesDir: 
    pass
files.reverse()
FilePaths = [root+'/'+i for i in files]
#file = FilePaths[0]
for file in FilePaths:
    time = re.findall('posts/(\d+_\d+_\d+)_',file)[0]
    time = time.replace('_','-')
    title = re.findall('\d+_\d+_\d+_(.*?).md',file)[0]
    FileDict = {'title':title,
                'time':time,
                'file':file}
    FileDictList.append(FileDict)


FileDictListJson = json.dumps(FileDictList,ensure_ascii=False)
with open('list.json','w') as f:
    f.write(FileDictListJson)



