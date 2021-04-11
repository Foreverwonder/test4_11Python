# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # 打开文件
# fo = open("testNew.txt", "r+")
# print ("文件名为: ", fo.name)
#
#
#
# line = fo.readline()
# print ("读取数据: %s" % (line))
#
# # 关闭文件
# fo.close()



# # 大文件尝试
# # open(r'C:\Users\Meet')
# f = open('testNew.txt',mode='r',encoding='utf-8')
# f1= open('testNew123.txt',mode='w',encoding='utf-8')
# for line in f:
#     # print(line)      #这种方式就是在一行一行的进行读取,它就执行了下边的功能
#     head, sep, tail=line.partition(":")
#     # print(head)
#     f1.write(head+'\n')
# f.close()
# f1.close()





# # 大文件尝试(第一次)(成功去除冒号后面内容)
# # open(r'C:\Users\Meet')
# f = open(r'D:\PIyiyi.txt',mode='r',encoding='utf-8')
# f1= open(r'D:\pi7.txt',mode='w',encoding='utf-8')
# for line in f:
#     # print(line)      #这种方式就是在一行一行的进行读取,它就执行了下边的功能
#     head, sep, tail=line.partition(":")
#     # print(head)
#     f1.write(head+'\n')
# f.close()
# f1.close()





# # 大文件尝试(第二次)(成功去除空格)
# # open(r'C:\Users\Meet')
# f = open(r'D:\test1.txt',mode='r',encoding='utf-8')
# f1= open(r'D:\test2.txt',mode='w',encoding='utf-8')
# for line in f:
#     # print(line)      #这种方式就是在一行一行的进行读取,它就执行了下边的功能
#     # head, sep, tail=line.partition(":")
#     # print(head)
#     # f1.write(head+'\n')
#     f1.write(line.replace(' ',''))
# f.close()
# f1.close()




# # 大文件尝试(第三次)(成功去除空行)
# # open(r'C:\Users\Meet')
# f = open(r'D:\test1.txt',mode='r',encoding='utf-8')
# f1= open(r'D:\test2.txt',mode='w',encoding='utf-8')
# for line in f:
#     if line.split():
#         f1.write(line)
# f.close()
# f1.close()

