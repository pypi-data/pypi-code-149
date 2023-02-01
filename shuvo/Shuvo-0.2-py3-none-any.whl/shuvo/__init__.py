import os,sys
def shuvo():
    os.system("clear")
    os.system("cls")
    os.system("xdg-open https://facebook.com/ma4D1")
    os.system("xdg-open https://facebook.com/groups/610487559129086")
    logo = ("""\033[1;32m  
╔═════════════════════════════════════════════════╗\033[1;31m
║           WELCOME TO MAHDI SHORTCUT             ║\033[1;33m
║═════════════════════════════════════════════════║\033[1;33m                     
║\033[0;37m##     ##    ###    ##     ## ########  ####     ║
║\033[1;92m###   ###   ## ##   ##     ## ##     ##  ##      ║
║\033[1;93m#### ####  ##   ##  ##     ## ##     ##  ##      ║
║\033[1;91m## ### ## ##     ## ######### ##     ##  ##      ║
║\033[1;92m##     ## ######### ##     ## ##     ##  ##      ║
║\033[1;93m##     ## ##     ## ##     ## ##     ##  ##      ║
║\033[1;33m##     ## ##     ## ##     ## ########  ####     ║ 
║                                    \033[1;33mVERSION 4.2  ║
║╭──────────────\033[1;91m[POWERED BY MAHDI HASAN ]\033[1;33m─────────║
│ ╭──────────────────────────────────────────────╮│
│ │ [A] AUTHOR   :\033[0;37mMAHDI HASAN SHUVO              ││
│ │ \033[1;32m[F] FACEBOOK :m.me/bk4human                  ││
│ │ \033[1;32m[G]GITHUB    : SHUVO-BBHH                    ││ 
│ │ \033[1;37m[W] WHATSAPP : 01616406924                   ││
│ ╰─\033[1;33m─────────────────────────────────────────────╯│
╰\033[1;33m─────────────────────────────────────────────────╯\033[1;32m""")
    print('\033[1;97m====================================================') 
    print('        \x1b[97m\033[37;41m[ WELL COME TO MAHDI SHOTCUT  ]\033[0;m')
    print('\033[1;97m====================================================') 
    print("\033[1;97m[01] \033[1;92mRANDOM CLOINIG TOOL     \033[1;96m")
    print("\033[1;93m[02] \033[1;92mTERMUX BASIC COMMAND")
    print("\033[1;92m[03] \033[1;92mCONATACK ME  ")
    print("\033[1;91m[04] \033[1;92mUPDATE")
    print("\033[1;97m====================================================")                    
    m=input('\033[1;97mCOUSE :')
    if m in['1','01']:
        os.system("rm -rf mahdi-mex")
        os.system("git clone https://github.com/Shuvo-BBHH/mahdi-mex")
        os.system("cd mahdi-mex && python mahdi.py")

    if m in['02','2']:
        os.system('pkg update')
        print('\033[1;97mSUCESSFULLY INSTALL  pkg update')
        os.system('pkg install python')
        print('\033[1;92mSUCESSFULLY INSTALL  PYTHON')
        os.system('pip install requests')
        print('\033[1;91mSUCESSFULLY INSTALL  requests')
        os.system('pip install mechanize')
        print('\033[1;97mSUCESSFULLY INSTALL  mechanize')
        os.system('pip install lolcat')
        print('\033[1;93mSUCESSFULLY INSTALL  lolcat')
        os.system('pip install bs4')
        print('\033[1;91mSUCESSFULLY INSTALL  bs4')
        os.system('pkg install git')
        print('\033[1;97mSUCESSFULLY INSTALL  git')
        os.system('pip install rich')
        print('\033[1;97mSUCESSFULLY INSTALL  rich')
        os.system('termux-setup-storage')
        print('\033[1;91mSUCESSFULLY INSTALL  setup-storage')
        os.system('pip install random')
        print('\033[1;97mSUCESSFULLY INSTALL  random')
        shuvo()
    if m in['6','06']:
        os.system('pip uninstall Shuvo')
        os.system('pip install Shuvo')
        shuvo()
    if m in['3','03']:
        os.system('clear')
        os.system('xdg-open https://github.com/Shuvo-BBHH')
        print (logo)
        print('[1] Facebook \n[2] Whatapp')
        mahd = input('Chouse :')
        if mahd =='1':
            os.system("xdg-open https://facebook.com/bk4human")
            shuvo()
        elif mahd =='2':
            os.system('xdg-open https://wa.me/+8801616406924')
            shuvo()   



    elif m :
        shuvo()

    elif m in ['']:
        shuvo()    

shuvo()
