import random
print ("Hi! I'm thinking of a random number between 1 and 100.")
print()
guessing_num = random.randint(1,100)
i=1
while i<8:
    print ("--- Attempt "+str(i)+"")
    guessed_num =int(input("Guess what number I am thinking of :"))
    if (guessed_num == guessing_num):
        print("WINNER!!!!!!")
        print(" The number was "+str(guessing_num)+"")
        break
    elif(guessed_num<guessing_num):
        print("Too low")
        print()
    elif(guessed_num>guessing_num): 
        print("Too high")
        print()
    else:
        print()
    if(i==7):
        print("Aw, you ran out of tries. The number was "+str(guessing_num)+".")

        rerun = input("Do you want to play again, yes or no?")

        if (rerun=="yes"):
            print ("Hi! I'm thinking of a random number between 1 and 100.")
            print()
            guessing_num = random.randint(1,100)
            b=1
            while b<8:
                print ("--- Attempt "+str(b)+"")
                guessed_num =int(input("Guess what number I am thinking of :"))
                if (guessed_num == guessing_num):
                    print("WINNER!!!!!!")
                    print(" The number was "+str(guessing_num)+"")
                    break
                elif(guessed_num<guessing_num):
                    print("Too low")
                    print()
                elif(guessed_num>guessing_num):
                    print("Too high")
                    print()
                else:
                    print()
                if(b==7):
                    print("Aw, you ran out of tries. The number was "+str(guessing_num)+".")
                b+=1
    i+=1
