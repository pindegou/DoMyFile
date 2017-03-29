import os
import re
import time
import shutil
'''
根据实际情况，修改相关信息，即可为每个DS工程生成导出DS JOB到XML的bat文件
1、mydir，SVN版本库的地址，以后若直接与SVN对接，可能会做调整。
2、targetpath，设置为在跳板机上的路径
3、DSProjects，只有新建工程，修改工程名时才需要，根据Datastage的要求，工程名必须小写
4、serverInfo，只有涉及工程服务器信息时才需要调整
5、新建多层级目录(ds和Procedures)，并文件拷贝到下面
'''
def search(sourceDir , targetDir):
    #mydir = sourceDir
    #mydir = "D:\\2017版本规划（正式稿）\\2017年3月"#指定版本库地址
    DSProjects = ['dpods','dpsor','dpsrc','dpstc','dpdsa']#定义DS工程列表
    #定义Datastage服务器信息，有变化才修改
    serverInfo = [[],
                  [],
                  [],
                  [],
                  []]
    #获取脚本执行时的时间数据，并以YYYY-MM-DD生成目标文件夹
    gettime  =  time.localtime()#获取脚本执行时的时间数据，并以YYYY-MM-DD生成目标文件夹
    strTime = time.strftime("%Y-%m-%d", gettime)
    #合成路径
    targetPath = targetDir + "\\" + strTime + "\\ds"#定义DS JOB导出路径
    targetPathProcedures = targetDir + "\\" + strTime + "\\Procedures"#定义存储过程保存路径
    
    #rootdir = mydir
    pathname = []
    specildir = ['DS-JOB发布文件','03_PROCEDURES']#列出特殊文件夹
    for (dirpath, dirnames, filenames) in os.walk(sourceDir):#列出所有路径
        for filename in filenames:
            pathname += [os.path.join(dirpath, filename)]
    for item in pathname:#不写在上一个for中，速度更快
        match_0 = re.search(r'DS-JOB发布文件\\.*?isx',item,re.IGNORECASE)#检查文件是否是在"DS-JOB发布文件"文件夹下面，即判断是否是DS
        match_1 = re.search(r'PROCEDURES\\.*?sql',item,re.IGNORECASE)#检查文件是否是在"PROCEDURES"文件夹下面，即判断是否是存储过程
        pathLists = item.split("\\")
        if match_0:#一个DS工程输出一个批量导出DS JOB到XML的bat文件
            newPathDS = targetPath + "\\" + str(item.split("\\")[-2]).lower()
            if os.path.exists(newPathDS) ==False:
                os.makedirs(newPathDS)
            for DSProject in DSProjects:
                if str(item.split("\\")[-2]).lower() == str(DSProject):#一个DS工程一个TXT文件
                    if str(DSProject) == "dpsrc":#若工程数量发生变化，或工程名发生变化时，需要调整这部分代码
                        ip_port = serverInfo[0][1]
                        host_name = serverInfo[0][2]
                        user_name = serverInfo[0][3]
                        pass_word = serverInfo[0][4]
                    elif str(DSProject) == "dpsor":
                        ip_port = serverInfo[1][1]
                        host_name = serverInfo[1][2]
                        user_name = serverInfo[1][3]
                        pass_word = serverInfo[1][4]
                    elif str(DSProject) == "dpods":
                        ip_port = serverInfo[2][1]
                        host_name = serverInfo[2][2]
                        user_name = serverInfo[2][3]
                        pass_word = serverInfo[2][4]
                    elif str(DSProject) == "dpstc":
                        ip_port = serverInfo[3][1]
                        host_name = serverInfo[3][2]
                        user_name = serverInfo[3][3]
                        pass_word = serverInfo[3][4]
                    elif str(DSProject) == "dpdsa":
                        ip_port = serverInfo[4][1]
                        host_name = serverInfo[4][2]
                        user_name = serverInfo[4][3]
                        pass_word = serverInfo[4][4]
                    with open((targetPath + "\\" + DSProject + ".bat"),'a') as f:
                        dsjob = item.split("\\")[-1].split('.')[0]
                        temp = r'C:\IBM\InformationServer\Clients\Classic\dsexport.exe /D=' + ip_port + r' /H=' + host_name + r' /U=' + user_name + r' /P=' + pass_word +r' /NODEPENDENTS /Job=' + dsjob + r' /XML ' + DSProject + r' '+ targetPath + "\\" +DSProject + "\\" + dsjob + r'.xml'
                        f.write(str(temp + '\n'))#每输出一个文件的完整路径就换行
        if match_1:
            newPathProcedures = targetPathProcedures + "\\" + pathLists[-4] + "\\" + pathLists[-3]+ "\\" + pathLists[-2]
            if os.path.exists(newPathProcedures) ==False:#判断多级目录是否存在,存在则直接拷贝文件；不存在则创建目录后拷贝文件。
                os.makedirs(newPathProcedures)
            shutil.copy(item,newPathProcedures + "\\" + pathLists[-1])
def main():
    sourceDir = "D:\\2017版本规划（正式稿）\\2017年3月"#指定输入目录
    targetDir = "D:\\050058"#指定输出目录
    search(sourceDir , targetDir)
main()
