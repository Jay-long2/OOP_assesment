class Car():
    def __init__(self,Make,model,year):
        self.Make = Make
        self.model = model
        self.year = year
    def display_info(self):
        return f"{self.Make}{self.model}{self.year}"

Car1 = Car("Toyota","Lexus","2018")
print(Car1.display_info())


                        
        