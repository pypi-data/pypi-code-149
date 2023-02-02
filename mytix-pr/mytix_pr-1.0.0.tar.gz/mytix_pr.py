from colorama import Fore
import time



class pr():
    def info(content):
        print(Fore.LIGHTBLACK_EX + time.strftime("%H:%M:%S", time.gmtime()) + Fore.WHITE + " - " +  content + Fore.WHITE)
    
    def success(content):
        print(Fore.LIGHTBLACK_EX + time.strftime("%H:%M:%S", time.gmtime()) + Fore.WHITE + " - " + "("+Fore.GREEN+"+"+Fore.WHITE+") "+Fore.GREEN + content + Fore.WHITE)
    
    def fail(content):
        print(Fore.LIGHTBLACK_EX + time.strftime("%H:%M:%S", time.gmtime()) + Fore.WHITE + " - " + "("+Fore.RED+"-"+Fore.WHITE+") "+Fore.RED + content + Fore.WHITE)
    
    def input(content):
        input(Fore.LIGHTBLACK_EX + time.strftime("%H:%M:%S", time.gmtime()) + Fore.WHITE + " - " + "("+Fore.YELLOW+"?"+Fore.WHITE+") "+Fore.WHITE + content + Fore.LIGHTBLACK_EX)   
    
    def warn(content):
        print(Fore.LIGHTBLACK_EX + time.strftime("%H:%M:%S", time.gmtime()) + Fore.WHITE + " - " + "("+Fore.LIGHTRED_EX+"!"+Fore.WHITE+") "+Fore.LIGHTRED_EX + content + Fore.WHITE)

