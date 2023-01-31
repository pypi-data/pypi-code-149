class Chelsea:

    def __init__(self):
        self.name = 'Frank Lampard'
        self.page = 'https://www.chelseafc.com/en/frank-lampard'
        
    def showLegend(self):
        print('{} is Chelsea legendary'.format(self.name))
        
    def showLegendMove(self):
        print('https://www.youtube.com/watch?v=C99gxtQNz2U')
        
    def showInfo(self):
        text = """ my name is potter I'm your new head coach """
        print(text)
        
    def showFootball(self):
        text = """
                _...----.._
             ,:':::::.     `>.
           ,' |:::::;'     |:::.
          /    `'::'       :::::\\
         /         _____     `::;\\
        :         /:::::\\      `  :
        | ,.     /::SSt::\\        |
        |;:::.   `::::::;'        |
        ::::::     `::;'      ,.  ;
        \\:::'              ,::::/
          \\                 \\:::/
           `.     ,:.        :;'
             `-.::::::..  _.''
                ```----''
        """
        print(text)
        
        
if __name__ == '__main__':
    chelsea = Chelsea()
    
    chelsea.showLegend()
    chelsea.showLegendMove()
    chelsea.showInfo()
    chelsea.showFootball()