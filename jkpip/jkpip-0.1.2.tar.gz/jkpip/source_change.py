import subprocess
pip_source = {
	"官方源":"https://pypi.python.org/simple/",
	"清华源":"https://pypi.tuna.tsinghua.edu.cn/simple/",
	"阿里云":"http://mirrors.aliyun.com/pypi/simple/",
	"中科大":"https://pypi.mirrors.ustc.edu.cn/simple/",
	"豆瓣源":"http://pypi.douban.com/simple/",
	"中科院":"http://pypi.mirrors.opencas.cn/simple/",
}
while 1:
	choice = int(input(
	'''
	1、使用pip官方源
	2、使用pip清华源
	3、使用pip阿里云
	4、使用pip中科大
	5、使用pip豆瓣源
	6、更新pip版本
	7、退出
	'''
	))
	cmd_list = ["pip","config","set","global.index-url",]
	if choice == 1:
		cmd_list.append(pip_source["官方源"])
		subprocess.Popen(cmd_list)
		quit()
	if choice == 2:
		cmd_list.append(pip_source["清华源"])
		subprocess.Popen(cmd_list)
		quit()
	if choice == 3:
		cmd_list.append(pip_source["阿里云"])
		subprocess.Popen(cmd_list)
		quit()
	if choice == 4:
		cmd_list.append(pip_source["中科大"])
		subprocess.Popen(cmd_list)
		quit()
	if choice == 5:
		cmd_list.append(pip_source["豆瓣源"])
		subprocess.Popen(cmd_list)
		quit()
	if choice == 6:
		print("默认更新python3的pip")
		subprocess.Popen("python3 -m pip install --upgrade pip")
		quit()
	if choice == 7:
		quit()		

# TODO ubuntu换源 
# TODO deepin换源 
