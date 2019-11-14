#!/usr/bin/env python3
# -*- coding:utf8 -*-
# @TIME  :2018/9/17 9:02
# @Author:ibanezz
# @File  :api.py
'''
读取所有Controller.java文件内的注释内容，备份
'''
import os, shutil, re

filter=["Controller.java"] #设置过滤后的文件类型 当然可以设置多个类型

doc_history = './_apidoc.js'
fp=open(doc_history,"a",encoding="utf-8")

if __name__=='__main__':
    work_dir = 'source/path/src'
    for parent, dirnames, filenames in os.walk(work_dir,  followlinks=True):
        for filename in filenames:
            # file_path = os.path.join(parent, filename)
            # print('文件名：%s' % filename)
            # print('文件完整路径：%s\n' % file_path)
            
            if filename.endswith("Controller.java"):
                target_file = os.path.join(parent, filename)
                f = open(target_file); #打开文件
                lines = f.readlines()
                lindeNumber = 0
                dic = {}
                for line in lines:
                    # 记录注释开始和结束行
                    if (line.lstrip().startswith("/*")):
                        dic['s'] = lindeNumber
                    
                    if (line.rstrip().endswith("*/")):
                        dic['e'] = lindeNumber+1
                        for doc in lines[dic['s']:dic['e']]:
                            # print(doc)
                            fp.write(doc)
                        dic = {}

                    lindeNumber = lindeNumber + 1

                    # 获取版本号
                    # if line.find("@apiVersion") > 0:
                    #     print(line.strip().split(" ")[2])

    fp.close()
