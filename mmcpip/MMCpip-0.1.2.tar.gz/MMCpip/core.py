# Insert your code here. 
from os import *


print('''如果您是第一次使用这个库，想获取具体用法，请调用\'帮助()\'获取帮助
注意！！！这个库可能会很慢，速度根据大家电脑性能和网速决定''')

def 帮助():
    帮助信息 = '''升级()      升级pip                        例：升级()
    安装列表()               查看所有已安装的库              例：安装列表()
    修改默认源(链接)          修改pip时的默认源（pip默认PYPI），此函数默认为清华源               例：修改默认源('http://mirrors.aliyun.com/pypi/simple/')
    安装(库,源,版本)          此函数为下载库后自动配置到Python解释器(下载后直接用)，如果你不知道具体要使用哪个版本的库，请勿填写               例：安装(MMCpip,清华源,0.1.0)
    卸载(库)                 卸载指定的库                    例：卸载('MMCpip')
    查看更新()               查看所有需要更新的库             例：查看更新()
    查看冲突(库)              查看所有不兼容的库              例：查看冲突()
    下载(库)                 下载库但不安装(下载后不能直接用),默认下载到运行这个文件的同一文件夹下                                  例：下载('MMCpip')
    尝试(库)                  在import之前使用，测试指定的库是否能正常工作，如果不能，那么安装 例:尝试('MMCpip')
    搜索(库)                  搜索库，因为中国大部分地区的\'pip search\'不能使用，所以这里用了第三方库pip_search                例：搜索(MMCpip)
    pyhon转exe(文件路径,图片路径)     利用ptinstaller将python文件转成windows可执行程序   例：pyhon转exe('E:\\MMCpip.py','有图标','E:\\MMC.png'):
    '''
    print(帮助信息)

def 升级pip():
    '''升级() 升级pip 例：升级()'''
    print(system('python -m pip install --upgrade pip'))

def 安装列表():
    print(system('pip list'))

def 修改默认源(链接='https://pypi.tuna.tsinghua.edu.cn/simple/'):
    print(system(f'pip config set global.index - url - i {链接}'))


def 安装(库,源= '',版本= ''):
    if 版本 == '':
        pass
    else:
        版本 = ' matplotlib=='+版本

    if 源 == '':
        print(system(f'pip install {库}'))
    elif 源 == '阿里云':
        print(system(f'pip install -i http://mirrors.aliyun.com/pypi/simple/ {库}{版本}'))
    elif 源 == '中国科技大学':
        print(system(f'pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ {库}{版本}'))
    elif 源 == '豆瓣':
        print(system(f'pip install -i  http://pypi.douban.com/simple/ {库}{版本}'))
    elif 源 == '清华大学':
        print(system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ {库}{版本}'))


def 卸载(库):
    print(system(f'pip uninstall {库}'))

def 查看更新():
    print(system('pip list -o'))

def 查看冲突(库 = ''):
    print(system(f'pip check {库}'))

def 信息(库):
    print(system(f'pip show -f{库}'))

def 下载(库):
    路径 = (path.dirname(path.abspath(__file__))).replace('\\', '/')
    system(f'{路径[:1]}:')
    system(f'cd {路径}')
    print(system(f'pip download  {库}'))


def 搜索(库):
    try:
        import pip_search
    except ImportError:
        print ('检测到您的search功能被禁用，正在自动为您下载pip_search')
        安装('pip_search','清华大学')
    print(system(f'pip_search{库}'))

def 尝试(库):
    try:
        import 库
    except ImportError:
        安装(f'{库}','清华大学')

def pyhon转exe(文件路径,模式 = '无图标',图片路径 = ''):
    尝试('pyinstaller')
    if 模式 == '无图标':
        print(system(f'pyinstaller -F {路径}'))
    else:
        print(system(f'pyinstaller -F -i {图片路径} {文件路径}'))
