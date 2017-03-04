import os
fid = open('BI20170209.txt', 'a')
rootdir = "D:\\2017版本规划（正式稿）\\2017年2月\\BI20170209"
pathname = []
specildir = ['DS-JOB发布文件','03_PROCEDURES']#列出特殊文件夹
for (dirpath, dirnames, filenames) in os.walk(rootdir):       
    for filename in filenames:
        pathname += [os.path.join(dirpath, filename)]  
for item in pathname:
	fid.write(str(item)+'\n')#每输出一个文件的完整路径就换行
fid.close() 	