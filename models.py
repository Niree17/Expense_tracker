from datetime import date

class Expense:
    def __init__(self,title: str, category:str, amount:float, ex_date:str |None=None,)-> None:
        self.title=title
        self.category=category
        self.amount=amount
        self.date=ex_date or str(date.today())


    def to_dict(self)-> dict:
        return{
            "title": self.title,
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
        }
    def __str__(self)-> str:
        return f"{self.date} | {self.title} | {self.category} | Rs {self.amount}"
if __name__=="__main__":
    pizza=Expense("Pizza","Food",300) 
    bus=Expense("Bus","travel", 500)
    print(bus.to_dict())
    print(bus)
    print(pizza)
