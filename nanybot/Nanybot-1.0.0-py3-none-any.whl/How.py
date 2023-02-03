#Copyright (C) 2022 X CODER
from time import sleep

class color:
      red = '\033[91m'
      green = '\033[92m'
      blue = '\033[94m'
      yellow = '\033[93m'
      magenta = '\033[95m'
      cyan = '\033[96m'
      white = '\033[97m'
      bold = '\033[1m'
      underline = '\033[4m'
      black='\033[30m'

class chup:
      x_coder = f"""{color.bold}
{color.white} [⏦] - {color.cyan} 𝚁𝚞𝚋𝚒 {color.yellow} 𝚅𝙴𝚁𝚂𝙴𝙽𝙸𝙾𝚂  {color.red}1.0.0    

{color.white} [⏦] - {color.cyan} 𝚁𝚞𝚋𝚒 {color.yellow} 𝙲𝙾𝙿𝚈𝚁𝙸𝙶𝙷𝚃 (𝙲) {color.red} 2022 {color.green}𝙽𝚊𝚗𝚢𝚖𝚘𝚞𝚜

{color.white} [⏦] - {color.cyan} 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁  {color.yellow} 𝚁𝚄𝙱𝙸𝙺𝙰 {color.red} 𝙸𝙳 : {color.green} @Nanymous

{color.white}╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾
"""
      print(x_coder)
      
for x in range(3):
    for i in ("⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"):
        sleep(0.1)
        if x == 10:
            print('',end='')
            break
        else:
            print( color.blue+'   𝐋𝐈𝐁𝐑𝐀𝐑𝐘 𝐑𝐮𝐛𝐢 𝐑𝐔𝐍𝐈𝐍𝐆 𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓   ',color.cyan+i,end='\r')
print(color.white+"\n")