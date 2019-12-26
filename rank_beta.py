from collections import Counter
import random

myList = {}
count = 0
pastDecisions = {} #pastDecisions = {winningPick: [losingPick1, losingPick2, etc]}
timeSaver = True
#Taking in a list from text document and turning it into a workable dictionary
unRanked = open("unRanked.txt", "r").readlines()
newLine = '\n'
for unRank in unRanked:
    count += 1
    if newLine in unRank:
        unRank = unRank.replace(newLine, '')
        myList[unRank] = 0 #mList is a dictionary with listItem: score

#Searches to see if any item has the same score
def search(numeral):
    freq = Counter(myList.values())
    if freq[numeral] > 1:
        return True
    else:
        return False

for number in range(count):
    while search(number) == True: 
        #Taking just the list items from the dictionary, and comparing two lines at a time ( no score)
        allKeys = list(filter(lambda allKeys: myList[allKeys] == number, myList)) #allKeys = [listItem1, listItem2, etc]
        matchup = []
        for repeat in range(2):
            matchup1 = random.choice(allKeys)
            allKeys.remove(matchup1)
            matchup.append(matchup1)
        switch = False #for each matchup, this switch ensures that a workable decision is made
        while switch == False:
            #check to see if decision was already made before
            for each in pastDecisions:
                for all1 in pastDecisions[each]:
                    doubleCheck = []
                    doubleCheck.append(each)
                    doubleCheck.append(all1)
                    if sorted(matchup) == sorted(doubleCheck):
                        myList[doubleCheck[0]] += 1
                        switch = True
                    elif random.randint(2,4) == 4 and timeSaver == False:
                        '''
                        #essentially the transative property. if one listItem (listItem1) was ranked above another (let's call it listItem2)
                        for each2 in pastDecisions: #all listItems (eg [listItem3, listItem4]) that listItem2 was ranked above
                            for all2 in pastDecisions[each2]: #listItem1 is ranked above listItems 3 and 4
                                if all1 == each2: #if a>b and b>c then a>c
                                    pastDecisions[each] += [all2] #so essentially just the transative property, unfortunately currently makes it very slow
                                    switch = True
                                    timeSaver == True
                                    #right now, it's still too slow, so this is optional
                        '''                  
            #Comparing and picking one of two lines from text document
            if switch == False:
                myPick = input(str(matchup) + " 1 or 2?")
                if myPick == '1':
                    myList[matchup[0]] += 1
                    if matchup[0] not in pastDecisions:
                        pastDecisions[matchup[0]] = [matchup[1]]
                    else:
                        pastDecisions[matchup[0]] += [matchup[1]]
                    switch = True
                    if random.randint(1,2):
                        timeSaver = False
                elif myPick == '2':
                    myList[matchup[1]] += 1
                    if matchup[1] not in pastDecisions:
                        pastDecisions[matchup[1]] = [matchup[0]]
                    else:
                        pastDecisions[matchup[1]] += [matchup[0]]
                    switch = True
                    if random.randint(1,2):
                        timeSaver = False
                #Undecisive, gives different match up
                elif myPick == '3':
                    switch = True
                #so any other input doesn't do anything
                    timeSaver = True
                else:
                    switch = False
                    timeSaver = True

myRanking = sorted(myList.items(), key = lambda t: t[1])
print(myRanking)
