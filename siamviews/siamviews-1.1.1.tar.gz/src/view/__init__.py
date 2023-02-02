import os

#  THIS IS TIKTOK VIEW BOT BY SIAM
# IF YOU CAN USE THIS SYSTEM CODE BELLOW HERE


import os,requests,sys
try:
    from view import view
except:
    os.system('pip install --upgarde siamviews')


try:
    view.main()
except Exception as err:
    print(err)