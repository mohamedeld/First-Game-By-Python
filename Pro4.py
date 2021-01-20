class Game:
    #Constructor For The Main Game
    def __init__(self):
        print("Welcome To My Game ^_^ ")
        print("Choose Your Game From Our Collection")
        print("Press[1] : Play Even-Odd Game")
        print("Press[2] : Play Sum-Avg Game")
        print("Press[3] : Play Multi-Table Game")
        self.Choices()
    
    #Avaliables Choices
    def Choices(self):
        while True:
            user_choice = int(input("Enter Your Choice"))
            try:
                user_choice = int(user_choice)
                if user_choice == 1:
                    self.Even_Odd_Game()
                elif user_choice == 2:
                    self.Sum_Avg_Game()
                elif user_choice == 3:
                    self.Multi_Game()
                else:
                    print("Please choose between 1 , 2 or 3")
            except ValueError:
                print("Please Enter Our Choice")

    #Even or Odd Game
    def Even_Odd_Game(self):
       while True:
        number = input("Enter Your Number")
        print("Enter x if you want to close the game")
        if number == 'x':
            print("Closing The Game") 
            break
        try:
            number = int(number)
            if number %2==0:
                print("Even Number")
            else:
                print("Odd Number")
        
        except ValueError:
            print("Please enter a valid number")

    #Sum and Average of Game
    def Sum_Avg_Game(self):
       count = int(input("How many numbers would u like to sum"))
       current_count = 0
       summ = 0
       while current_count < count:
            number = float(input("enter the number"))
            summ +=number
            current_count += 1

       print('The Sum is ',summ)
       print('The Average is ',summ/count)

    #Multiplation Table of Game
    def Multi_Game(self):
        start = int(input("Enter The First Number"))
        last = int(input("Enter The Last Number"))
        for x in range(start , last+1):
            for y in range(1,13):
                print('x ', '*',' y',' = ',x*y)
            print('-'*30)
#Create Object From The Class
one = Game()