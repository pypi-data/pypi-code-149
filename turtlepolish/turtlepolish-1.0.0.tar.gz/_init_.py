class prześlij:
        def wykorzystaj(moduł):
            if moduł == 'turtle':
                import turtle
            print("Importuję ci moduł żółwia...")

class pomoc:
  def python():
    print("Jestem językiem programowania. Służę twoim poleceniom. ")
    
  def turtle():
        print("Jestem Żółw")
        print("Oto moje polecenia :")
        print("prześlij.wykorzystaj - służy do przesłania mnie \nhelp.python() - służy do wyświetlenie pomocy \nhelp.turtle - służy do wyświetlania informacji o mnie \nżółw.co_to - służy do wyświetlania do czego zostałem stworzony \nżółw.prawo() - służy do obracanie mnie o ileś stopni w prawo \nżółw.lewo - służy do obracanie mnie o wybraną liczbę stopni w lewo \nżółw.przenieś - przenosi mnie o wybraną liczbę pixeli do przodu \nutwórz.pusta_paleta - tworzy pustą kartkę na której będe rysował")

class żółw:
    def co_to():
        print("Jestem modułem rysującym. Zostałem stworzony w języku Python.")
        
    def prawo(stopnie):
        import turtle
        turtle.right(stopnie)

    def lewo(stopnie):
        import turtle
        turtle.left(stopnie)
    
    def przenieś(pixele):
        import turtle
        turtle.forward(pixele)

class utwórz:
    def pusta_paleta():
        import turtle
        t = turtle.Pen()
