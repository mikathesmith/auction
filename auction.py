#-------------------------------------------------------------------------------
# Name:        Auction
# Purpose:
#
# Author:      Mika Smith
#
# Created:     06/05/2014
# Copyright:   (c) Mika Smith 2014
# Licence:     <Creative Commons>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

def getReserve(n):
    while True:
        try:
            n = int(input("Could the Auction Manager please set a reserve price."))
        except ValueError:
            print("Please enter a valid number bewteen 1 to 999 inclusive.")
            pass
        else:
            if n in range(1, 999):
                return n
            else:
                print("Please enter a valid number bewteen 1 to 999 inclusive.")

def getName(a):
    a = input("What is your name?")
    while not a:
        print("Please enter your name.")
        a = input("What is your name?")
    return a

def scoreboard():
    print("Auction Board:")
    for p in range (0, len(storedNames)):
        print(storedNames[p],"bid $"+str(storedBids[p]))

storedNames=[]
storedBids=[]
reserve='none'
name=0
bid=999999
highest=0
acceptedAffirmative=['y','yes','Y','Yes']
cont="yes"

reserve=getReserve(reserve)
print("The reserve price is $" +str(reserve) + ". Let the auction begin!")
highest=reserve
while cont in acceptedAffirmative:
    name=getName(name)
    name=name.lower()
    name=name.title()
    storedNames.insert(0,name)
    bid=int(input("What is your bid?"))
    while bid<highest:
       print("Please enter a higher bid.")
       bid=int(input("What is your bid?"))
    storedBids.insert(0,bid)
    print(name + ", you have a bid of $" +str(bid))
    highest=max(storedBids)

    print("Highest bid so far is $" +str(highest))
    cont= input("Would someone else like to bid?")

scoreboard()
print(name +" won the auction with the highest bid of $"+str(highest) +".")
