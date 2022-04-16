class Asking():
    base2Numbers=[]
    base =2                                         #declaring a base variable
    def __init__(self):
        self.X = int(input("Enter a number :"))     # Asking a number and storing it in X variable
        for i in range(self.X):                     #loop through a range of X
            if self.base <= self.X :                # checking if base (line 3) is less then or equle to X (line 5)
                self.base2Numbers.append(self.base) # if so add the base number to base2Numbers array (line 2)
                self.base = (self.base *2)          # and give base (line 3) a new value( multiply the last base number by 2)
            else:                                   # if not break the loop 
                break
            #and outside of the loop print the Number by calling Calculate() function and pass X (line 5) and the last number in the array
        print("the save seat is Seat no: "+ str( self.calculate(self.X,self.base2Numbers[self.base2Numbers.__len__()-1])))
        
        # this methon takes two prameters x and n and returns (2*(x - n)+1) 
    def calculate(self , x ,n ):
        return (2*(x - n)+1)       #--> the formula
        
Asking()   #calling the class  
    
