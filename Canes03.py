# Just press f5 to start!


import random
from os import path


def canes03():
    mainlist = ['What we do', 'How and Why', 'Cleanliness', 'Mystery Shops',
                'Training']
    # First round of lists to get every value
    WWD = []
    HaW = []
    C = []
    MS = []
    T = []
    # Second round of lists to make sure indexing later does not become a problem
    # They are the "priority lists"
    What = []
    How = []
    Clean = []
    Mystery = []
    Train = []
    # Final dictionary
    Final = {}

    trycount = 1

    while True and trycount < 3:
        try:
            fname = '/Users/Aaron/Documents/list.csv'
            efile = open(fname, 'r')  # opens file and reads it
            trycount = 10  # If it works then it won't go through the loop again

        except FileNotFoundError:
            print('File not found. Try count =', trycount, '/3')
            trycount += 1  # If it is not found it will add to the try count
            if trycount == 3:  # Stops program if file is not found after 3 tries
                print('File not found. Out of tries.')
                return False

    ofname = '/Users/Aaron/Documents/PyOutput.csv'
    if path.isfile(ofname):  # Checks to see if the file you want to create exists
        q = str(input('File exists... overwrite? (y for yes, n for no): '))
        q = q.lower()  # Makes sure that the y or n is lowercase no matter what is entered
        if q == 'y':
            ofile = open(ofname, 'w')
        else:
            return False  # Ends the program if you do not want to overwrite the file
    else:
        ofile = open(ofname, 'w')  # If it does not exist, it just opens like normal

    line = efile.readline()  # Skips the first line because it is the title
    line = line.strip()  # Gets rid of blank space at the beginning and end of each line
    line = line.split(',')  # Strips each value at the comma
    line = efile.readline()

    while line != '':
        line = line.strip()
        line = line.split(',')

        WWD += [line[0]]  # Adds the first thing to the first list
        HaW += [line[1]]  # Adds the second thing to the second list
        C += [line[2]]  # 3rd
        MS += [line[3]]  # 4th
        T += [line[4]]  # 5th

        line = efile.readline()
    # The next 5 loops get rid of all the periods
    for i in range(len(WWD) - 1):
        if WWD[i] == '.':
            del WWD[i]
    for i in range(len(HaW) - 1):
        if HaW[i] == '.':
            del HaW[i]
    for i in range(len(C) - 1):
        if C[i] == '.':
            del C[i]
    for i in range(len(MS) - 1):
        if MS[i] == '.':
            del MS[i]
    for i in range(len(T) - 1):
        if T[i] == '.':
            del T[i]
            # The next 5 blocks of code are used to make sure that each list is correct
            # It is not necessary but at least you can see everything going into the file
            # Helps with debugging
    ofile.write(mainlist[0])
    ofile.write(':')
    ofile.write(str(WWD))
    ofile.write('\n')

    ofile.write(mainlist[1])
    ofile.write(':')
    ofile.write(str(HaW))
    ofile.write('\n')

    ofile.write(mainlist[2])
    ofile.write(':')
    ofile.write(str(C))
    ofile.write('\n')

    ofile.write(mainlist[3])
    ofile.write(':')
    ofile.write(str(MS))
    ofile.write('\n')

    ofile.write(mainlist[4])
    ofile.write(':')
    ofile.write(str(T))
    ofile.write('\n')
    # Next block of five
    # This is where it adds each thing into a new list as many times as it is important
    # Ex: The first thing is the most important so it is added in as many times as the list is long (List length = 3, is added in 3 times)

    for i in range(len(WWD) - 1):  # Gets the index number of each thing in the list
        for eachThing in WWD:  # Looks at each individual value in the list
            if eachThing == WWD[i]:  # If that thing is equal to the index we got from the first loop
                for t in range(len(
                        WWD) - i):  # The value is added into the new list as many times as the list is long minus the original index
                    What += [eachThing]
    for i in range(len(HaW) - 1):
        for eachThing in HaW:
            if eachThing == HaW[i]:
                for t in range(len(HaW) - i):
                    How += [eachThing]
    for i in range(len(C) - 1):
        for eachThing in C:
            if eachThing == C[i]:
                for t in range(len(C) - i):
                    Clean += [eachThing]
    for i in range(len(MS) - 1):
        for eachThing in MS:
            if eachThing == MS[i]:
                for t in range(len(MS) - i):
                    Mystery += [eachThing]
    for i in range(len(T) - 1):
        for eachThing in T:
            if eachThing == T[i]:
                for t in range(len(T) - i):
                    Train += [eachThing]
                    # Next block of 5
                    # This code checks to make sure the random selection will work
    if len(What) == 0:  # If there is nothing in this list, then it will just add a null string
        Final[mainlist[0]] = ''
    else:  # Otherwise, it will go ahead and pick a random number and then add the value that is at that number to the dictionary
        a = random.randint(0, len(What) - 1)
        Final[mainlist[0]] = What[a]

    if len(How) == 0:
        Final[mainlist[1]] = ''
    else:
        b = random.randint(0, len(How) - 1)
        Final[mainlist[1]] = How[b]

    if len(Clean) == 0:
        Final[mainlist[2]] = ''
    else:
        c = random.randint(0, len(Clean) - 1)
        Final[mainlist[2]] = Clean[c]

    if len(Mystery) == 0:
        Final[mainlist[3]] = ''
    else:
        d = random.randint(0, len(Mystery) - 1)
        Final[mainlist[3]] = Mystery[d]

    if len(Train) == 0:
        Final[mainlist[4]] = ''
    else:
        e = random.randint(0, len(Train) - 1)
        Final[mainlist[4]] = Train[e]

    ofile.write('Priority Lists')
    ofile.write('\n')

    ofile.write(mainlist[0])
    ofile.write(':')
    ofile.write(str(What))
    ofile.write('\n')

    ofile.write(mainlist[1])
    ofile.write(':')
    ofile.write(str(How))
    ofile.write('\n')

    ofile.write(mainlist[2])
    ofile.write(':')
    ofile.write(str(Clean))
    ofile.write('\n')

    ofile.write(mainlist[3])
    ofile.write(':')
    ofile.write(str(Mystery))
    ofile.write('\n')

    ofile.write(mainlist[4])
    ofile.write(':')
    ofile.write(str(Train))
    ofile.write('\n')

    ofile.write('Final List:')  # Writest the final list on the document
    ofile.write(str(Final))  # Note: dictionaries do not have any specfic order

    print()  # They will not be written to the file in any specific order
    print(Final)  # Prints the dictionary so you can see it immediately
    # To see everything that was written to the file, you will have to open the file on your own
    ofile.close()  # Both files are closed
    efile.close()
