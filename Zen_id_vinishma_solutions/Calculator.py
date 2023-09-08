#Calculator class
class calculator:
  
  def __init__(self, num1, num2):                 #Constructor
    self.num1 = num1
    self.num2 = num2

  def add(self):                                    #Addition
    return(f"Addition : {self.num1+self.num2}")

  def sub(self):                                      #Subtraction
    return(f"Subtraction : {self.num1-self.num2}")

  def mul(self):                                      #Multiplication
    return(f"Multiplication :  {self.num1*self.num2}")
  
  def mod(self):                                       #Modulo
    return(f"Reminder :  {self.num1%self.num2}")

#Main
if __name__ == '__main__':               #Get two inputs
  Num_1 = int(input("Enter number1: "))
  Num_2 = int(input("Enter number2: "))

  calc = calculator(Num_1, Num_2)     #Create an object for the class
  #Call the methods
  print(calc.add())
  print(calc.sub())
  print(calc.mul())
  print(calc.mod())