# Just press f5 to start!


import random
from os import path


def canes04():
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
    while line != '':  # All lists are assumed to be the same size

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
        if WWD[i] == '"."':
            del WWD[i]
            print(WWD)
    for i in range(len(HaW) - 1):
        if HaW[i] == '"."':
            del HaW[i]
            print(HaW)
    for i in range(len(C) - 1):
        if C[i] == '"."':
            del C[i]
            print(C)
    for i in range(len(MS) - 1):
        if MS[i] == '"."':
            del MS[i]
            print(MS)
    for i in range(len(T) - 1):
        if T[i] == '"."':
            del T[i]
            print(T)

    lenlist = []
    lenlist += [len(WWD)]
    lenlist += [len(HaW)]
    lenlist += [len(C)]
    lenlist += [len(MS)]
    lenlist += [len(T)]
    lenlist.sort()

    if len(WWD) == lenlist[4]:
        a = []
        for eachThing in WWD:
            a += [eachThing]
    elif len(HaW) == lenlist[4]:
        a = []
        for eachThing in HaW:
            a += [eachThing]
    elif len(C) == lenlist[4]:
        a = []
        for eachThing in C:
            a += [eachThing]
    elif len(MS) == lenlist[4]:
        a = []
        for eachThing in MS:
            a += [eachThing]
    elif len(T) == lenlist[4]:
        a = []
        for eachThing in T:
            a += [eachThing]
    if len(WWD) == lenlist[3]:
        b = []
        for eachThing in WWD:
            b += [eachThing]
    elif len(HaW) == lenlist[3]:
        b = []
        for eachThing in HaW:
            b += [eachThing]
    elif len(C) == lenlist[3]:
        b = []
        for eachThing in C:
            b += [eachThing]
    elif len(MS) == lenlist[3]:
        b = []
        for eachThing in MS:
            b += [eachThing]
    elif len(T) == lenlist[3]:
        b = []
        for eachThing in T:
            b += [eachThing]
    if len(WWD) == lenlist[2]:
        c = []
        for eachThing in WWD:
            c += [eachThing]
    elif len(HaW) == lenlist[2]:
        c = []
        for eachThing in HaW:
            c += [eachThing]
    elif len(C) == lenlist[2]:
        c = []
        for eachThing in C:
            c += [eachThing]
    elif len(MS) == lenlist[2]:
        c = []
        for eachThing in MS:
            c += [eachThing]
    elif len(T) == lenlist[2]:
        c = []
        for eachThing in T:
            c += [eachThing]
    if len(WWD) == lenlist[1]:
        d = []
        for eachThing in WWD:
            d += [eachThing]
    elif len(HaW) == lenlist[1]:
        d = []
        for eachThing in HaW:
            d += [eachThing]
    elif len(C) == lenlist[1]:
        d = []
        for eachThing in C:
            d += [eachThing]
    elif len(MS) == lenlist[1]:
        d = []
        for eachThing in MS:
            d += [eachThing]
    elif len(T) == lenlist[1]:
        d = []
        for eachThing in T:
            d += [eachThing]
    if len(WWD) == lenlist[0]:
        e = []
        for eachThing in WWD:
            e += [eachThing]
    elif len(HaW) == lenlist[0]:
        e = []
        for eachThing in HaW:
            e += [eachThing]
    elif len(C) == lenlist[0]:
        e = []
        for eachThing in C:
            e += [eachThing]
    elif len(MS) == lenlist[0]:
        e = []
        for eachThing in MS:
            e += [eachThing]
    elif len(T) == lenlist[0]:
        e = []
        for eachThing in T:
            e += [eachThing]
    while len(b) != len(a):
        b += ['']
    while len(c) != len(a):
        c += ['']
    while len(d) != len(a):
        d += ['']
    while len(e) != len(a):
        e += ['']
    # The next 5 blocks of code are used to make sure that each list is correct
    # It is not necessary but at least you can see everything going into the file
    # Helps with debugging
    ofile.write(mainlist[0])
    ofile.write(',')
    ofile.write(mainlist[1])
    ofile.write(',')
    ofile.write(mainlist[2])
    ofile.write(',')
    ofile.write(mainlist[3])
    ofile.write(',')
    ofile.write(mainlist[4])
    ofile.write('\n')
    for i in range(len(a)):
        ofile.write(a[i])
        ofile.write(',')
        ofile.write(b[i])
        ofile.write(',')
        ofile.write(c[i])
        ofile.write(',')
        ofile.write(d[i])
        ofile.write(',')
        ofile.write(e[i])
        ofile.write(',')
        ofile.write('\n')
    # Next block of five
    # This is where it adds each thing into a new list as many times as it is important
    # Ex: The first thing is the most important so it is added in as many times
    #  as the list is long (List length = 3, is added in 3 times)

    for i in range(len(WWD) - 1):  # Gets the index number of each thing in the list
        for eachThing in WWD:  # Looks at each individual value in the list
            if eachThing == WWD[i]:  # If that thing is equal to the index we
                # got from the first loop
                for t in range(len(
                        WWD) - i):  # The value is added into the new list as
                    # many times as the list is long minus the original index
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
    fw = []
    fh = []
    fc = []
    fm = []
    ft = []
    # Making lists so that we can randomly select 10 separate things from the
    # old priority lists and put them in the new lists
    if len(What) == 0:  # If there is nothing in this list, then it will just add a null string
        Final[mainlist[0]] = ''
    else:  # Otherwise, it will go ahead and pick a random number and then add
        #  the value that is at that number to the dictionary
        a = random.randint(0, len(What) - 1)
        while len(fw) != 4:
            if What[a] not in fw:
                fw += [What[a]]
            else:
                a = random.randint(0, len(What) - 1)

    if len(How) == 0:
        Final[mainlist[1]] = ''
    else:
        while len(fh) != 10:
            b = random.randint(0, len(How) - 1)
            if How[b] not in fh:
                fh += [How[b]]
            else:
                b = random.randint(0, len(How) - 1)

    if len(Clean) == 0:
        Final[mainlist[2]] = ''
    else:
        c = random.randint(0, len(Clean) - 1)
        while len(fc) != 10:
            if Clean[c] not in fc:
                fc += [Clean[c]]
            else:
                c = random.randint(0, len(Clean) - 1)

    if len(Mystery) == 0:
        Final[mainlist[3]] = ''
    else:
        d = random.randint(0, len(Mystery) - 1)
        while len(fm) != 10:
            if Mystery[d] not in fm:
                fm += [Mystery[d]]
            else:
                d = random.randint(0, len(Mystery) - 1)

    if len(Train) == 0:
        Final[mainlist[4]] = ''
    else:
        e = random.randint(0, len(Train) - 1)
        while len(ft) != 10:
            if Train[e] not in ft:
                ft += [Train[e]]
            else:
                e = random.randint(0, len(Train) - 1)

    Final[mainlist[0]] = fw
    Final[mainlist[1]] = fh
    Final[mainlist[2]] = fc
    Final[mainlist[3]] = fm
    Final[mainlist[4]] = ft
    # Instead of writing everything that is related in one line, write it so
    # that the titles are in the first line and the first values are in the
    # second line and so on
    ofile.write('Priority Lists')
    ofile.write('\n')

    ofile.write(mainlist[0])
    ofile.write(mainlist[1])
    ofile.write(mainlist[2])
    ofile.write(mainlist[3])
    ofile.write(mainlist[4])
    for i in range(len(fw)):
        ofile.write(fw[i])
        ofile.write(',')
        ofile.write(fh[i])
        ofile.write(',')
        ofile.write(fc[i])
        ofile.write(',')
        ofile.write(fm[i])
        ofile.write(',')
        ofile.write(ft[i])
        ofile.write(',')
        ofile.write('\n')

        # Note: dictionaries do not have any specfic order
    print()  # They will not be written to the file in any specific order
    print(Final)  # Prints the dictionary so you can see it immediately
    # To see everything that was written to the file, you will have to open the file on your own
    ofile.close()  # Both files are closed
    efile.close()
