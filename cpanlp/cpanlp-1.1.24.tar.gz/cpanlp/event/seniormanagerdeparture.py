#高管离职适合单独写一个类。离职是一个独立的事件，不属于高管的常规行为，因此它应该是一个单独的类。这样可以更好地隔离它，更方便维护代码和扩展功能。
class SeniorManagerDeparture:
    def __init__(self, name, reason_for_departure, notice_period, final_day):
        self.name = name
        self.reason_for_departure = reason_for_departure
        self.notice_period = notice_period
        self.final_day = final_day
        
    def announcement(self):
        announcement = f"We would like to inform you that {self.name}, a senior manager, has decided to resign for {self.reason_for_departure}. "
        announcement += f"Their notice period is {self.notice_period}"