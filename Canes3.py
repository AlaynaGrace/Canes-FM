from os import path
import random

class PriorityList():
    def __init__(self):
        self._olist = []
        self._priority = {}
        self._plist = []
        self._rlist = []
        self._length = []

    def getOriginal(self):
        return self._olist
    def getPriority(self):
        return self._priority
    def getPriorityList(self):
        return self._plist
    def add2Original(self,line,index):
         self._olist += [line[index]]
    def keepLength(self,line,index):
        self._length += [line[index]]
    def getLengthList(self,index):
        return self._length[i]
    def getLength(self):
        return len(self._length)
    def createPriority(self):
        for i in range(len(self._olist)-1):
            self._priority[self._olist[i]] = len(self._olist) - i
    def createPriorityList(self):
        for eachThing in self._priority:
            for i in range(self._priority[eachThing]):
                self._plist += [eachThing]
    def randomList(self):
        for i in range(10):
            a = random.randint(0,len(self._olist)-1)
            if self._plist[a] not in self._rlist:
                if self._plist[a] != '.':
                    self._rlist += self._plist[a]
            else:
                a = random.randint(0,len(self._olist)-1)
    def getRandomList(self):
        return self._rlist
    def getRandomIndex(self,index):
        return self._rlist[index]
    def __str__(self):
        return str(self._olist)
    def __repr__(self):
        return self._olist
    
def canes3():
    wwd = PriorityList()
    haw = PriorityList()
    clean = PriorityList()
    mystery = PriorityList()
    train = PriorityList()

    mainlist = ['What we do','How and Why','Cleanliness','Mystery Shops',
                'Training']    
    trycount = 0
    while True and trycount < 3:
        try:
            fname = str(input('Enter source file name: '))
            efile = open(fname,'r') #opens file and reads it
            trycount = 10 #If it works then it won't go through the loop again
            
        except FileNotFoundError:
            print('File not found. Try count =',trycount,'/3') 
            trycount += 1 #If it is not found it will add to the try count
            if trycount == 3:   #Stops program if file is not found after 3 tries
                print('File not found. Out of tries.')
                return False

    ofname = str(input('Enter the name of the file you want to put this data into: '))
    if path.isfile(ofname): #Checks to see if the file you want to create exists
        q = str(input('File exists... overwrite? (y for yes, n for no): ')) 
        q = q.lower()   #Makes sure that the y or n is lowercase no matter what is entered
        if q == 'y':
            ofile = open(ofname, 'w')
        else:
            return False    #Ends the program if you do not want to overwrite the file
    else:
        ofile = open(ofname,'w')    #If it does not exist, it just opens like normal

    line = efile.readline()     #Skips the first line because it is the title
    line = efile.readline()
    while line != '':  #All lists are assumed to be the same size
        
        line = line.strip()
        line = line.split(',')

        wwd.add2Original(line,0) #Adds the first thing to the first list
        haw.add2Original(line,1)    #Adds the second thing to the second list
        clean.add2Original(line,2)   #3rd
        mystery.add2Original(line,3) #4th
        train.add2Original(line,4)     #5th
        
        wwd.keepLength(line,0)
        haw.keepLength(line,1)
        clean.keepLength(line,2)
        mystery.keepLength(line,3)
        train.keepLength(line,4)
        
        line = efile.readline()

    for i in range(4):
        ofile.write(mainlist[i])
        if i != 4:
            ofile.write(',')
        else:
            ofile.write('\n')
    for i in range(wwd.getLength-1):
        ofile.write(wwd.getLengthList(i))
        ofile.write(',')
        ofile.write(haw.getLengthList(i))
        ofile.write(',')
        ofile.write(clean.getLengthList(i))
        ofile.write(',')
        ofile.write(mystery.getLengthList(i))
        ofile.write(',')
        ofile.write(train.getLengthList(i))
        ofile.write('\n')

    wwd.createPriority()
    haw.createPriority()
    clean.createPriority()
    mystery.createPriority()
    train.createPriority()

    wwd.createPriorityList()
    haw.createPriorityList()
    clean.createPriorityList()
    mystery.createPriorityList()
    train.createPriorityList()

    wwd.randomList()
    haw.randomList()
    clean.randomList()
    clean.randomList()
    mystery.randomList()
    train.randomList()

    ofile.write('Priority Lists')
    ofile.write('\n')

    for i in range(4):
        ofile.write(mainlist[i])
        if i != 4:
            ofile.write(',')
        else:
            ofile.write('\n')
    for i in range(9):
        ofile.write(wwd.getRandomIndex(i))
        ofile.write(',')
        ofile.write(haw.getRandomIndex(i))
        ofile.write(',')
        ofile.write(clean.getRandomIndex(i))
        ofile.write(',')
        ofile.write(mystery.getRandomIndex(i))
        ofile.write(',')
        ofile.write(train.getRandomIndex(i))
        ofile.write('\n')

    final = {}
    final[mainlist[0]] += [wwd.getRandomList()]
    final[mainlist[1]] += [haw.getRandomList()]
    final[mainlist[2]] += [clean.getRandomList()]
    final[mainlist[3]] += [mystery.getRandomList()]
    final[mainlist[4]] += [train.getRandomList()]

    print(final)
    
    ofile.close()
    efile.close()
    
    
