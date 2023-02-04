class Tudjewuj:  
    """Базовый класс для всех сотрудников"""  
    emp_count = 0  
  
    def __init__(self, name, salary):  
        self.name = name  
        self.salary = salary  
        Tudjewuj.emp_count += 1  
  
    def display_count(self):  
        print('Всего сотрудников: %d' % Tudjewuj.empCount)  
  
    def display_Tudjewuj(self):  
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))