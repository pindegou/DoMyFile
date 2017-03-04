import os
fid = open('all.txt', 'a')#以追加方式，把内容都写到文件末尾
#rootdir = "D:\\2017版本规划（正式稿）\\2017年2月\\BI20170228"#BI20170209,BI20170214,BI20170221,BI20170228
rootdir = "D:\\2017版本规划（正式稿）\\2017年1月\\BI20170118（紧急）"#BI20170105,BI20170116（紧急）,BI20170118（紧急）
pathname = []
specildir = ['DS-JOB发布文件','03_PROCEDURES']#列出特殊文件夹
for (dirpath, dirnames, filenames) in os.walk(rootdir):       
    for filename in filenames:
        pathname += [os.path.join(dirpath, filename)]  
for item in pathname:
	fid.write(str(item)+'\n')#每输出一个文件的完整路径就换行
fid.close() 	