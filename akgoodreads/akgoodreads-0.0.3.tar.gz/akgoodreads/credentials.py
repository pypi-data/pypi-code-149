import sys
if sys.platform=="win32":
    #pip install keyring
    import keyring


def getpwd(item, username):
    if sys.platform=="win32":
        pwd = keyring.get_password(item, username)
        if not pwd:
            from rich.prompt import Prompt
            print("Password is not saved in keyring.")
            pwd = Prompt.ask(f"Enter the password for {item} corresponding to Username:{username}",password=True)
            choice = input("Would you like to save this pwd to keyring?(Y|n): ")
            if choice.strip().lower() in ['', 'y','n']:
                if choice.strip().lower() != 'n':
                    keyring.set_password(item, username, pwd)
    else:
        from rich.prompt import Prompt
        pwd = Prompt.ask(f"Enter the password for {item} corresponding to Username:{username}",password=True)
    
    return pwd