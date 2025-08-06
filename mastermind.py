import getpass

def main():
    player1 = input("Enter name Player 1 : ")
    player2 = input("Enter name Player 2 : ")
    while True:
        num1 = f(player1)
        plyr1Count = int(g(player2,num1))
        print()
        num2 = f(player2)
        plyr2Count = int(g(player1,num2))
        if plyr1Count > plyr2Count:
            print(f"{player1} is the Mastermind!!")
        elif plyr1Count < plyr2Count:
            print(f"{player2} is the Mastermind!!")
        elif plyr1Count == plyr2Count:
            print("It was a draw")
        redo = input("Do you want to try once more?[y/n] ").lower
        if redo == "y":
            continue
        else:
            break
            



def f(player):
    while True:
        print(player, "Enter the number in the range of 1000 to 9999:")    
        num = int(getpass.getpass(""))
        if num >= 1000 and num <= 9999:
            break
    return num

def numToList(num):
    div = []
    div.append(int(num%10))
    div.append(int((num%100 - div[0])/10))
    div.append(int((num%1000 - div[0] - div[1]*10)/100))
    div.append(int((num%10000 - div[0] - div[1]*10 - div[2]*100)/1000))
    div.reverse()
    return div

def g(player,num):
    count = 1
    divNum = numToList(num)
    while True:
        xnum = int(input("Guess the Number : "))
        if num == xnum:
            print(f"Great {player}! You guessed the number in just {count} try! You're a Mastermind!")
            break
        count += 1

        toShow=""
        divXnum = numToList(xnum)
        countX = 0
        for i in range(len(divNum)):
            if divNum[i] == divXnum[i]:
                toShow = toShow + str(divXnum[i])
                countX += 1
            else:
                toShow = toShow + "X"
        if countX >= 1:
            print(f"Not quite the number. You did get {countX} digits correct.")
            print(toShow)
       
        
        print()
    return count




if __name__ == '__main__':
    main()