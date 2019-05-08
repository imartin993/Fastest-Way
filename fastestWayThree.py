'''
Created on Mar 25, 2018

@author: Isaac Martin
'''

'''
Problem:
A car factory has three assembly lines, each with n stations.
A station is denoted by Si,j where i is either 1, 2, or 3 and indicates the assembly line the station is on,
and j indicates the number of the station. The time taken per station is denoted by ai,j.
Each station is dedicated to some sort of work like engine fitting, body fitting, painting and so on.
So, a car chassis must pass through each of the n stations in order before exiting the factory.
The parallel stations of the three assembly lines perform the same task.
After it passes through station Si,j, it will continue to station Si,j+1 unless it decides to transfer to
the other line. Continuing on the same line incurs no extra cost, but transferring from line i at station j – 1 to
station j on the other line takes time ti,j. Each assembly line takes an entry time ei and exit time xi which may be
different for the two lines. Give an algorithm for computing the minimum time it will take to build a car chassis.
'''
#Get transition times from file
with open('ThreeLaneTransitions.txt') as f1:
    content1 = f1.readlines() 
content1 = [x.strip() for x in content1] 
temp = []
for x in content1:
    nList = map(int, x.split('\t'))
    temp.append(nList)

#separate into appropriate lanes
trans1 = []
trans2 = []
trans3 = []
count = 0
for x in temp:
    if count == 0:
        trans1.append(x)
        count +=1
    elif count == 1:
        trans2.append(x)
        count += 1
    else:
        trans3.append(x)
        count = 0
#Get e, x, and a values from files
with open('ProcessTimes.txt') as f1:
    content2 = f1.readlines() 
content2 = [x.strip() for x in content2] 
temp = []
for x in content2:
    nList = map(int, x.split('\t'))
    temp.append(nList)
    
#separate into appropriate lanes
lane1 = []
lane2 = []
lane3 = []
for x in temp:
    count = 0
    for y in x:
        if count == 0:
            lane1.append(y)
            count += 1
        elif count == 1:
            lane2.append(y)
            count += 1
        else:
            lane3.append(y)
            count = 0

def fastestWayThree(a1, a2, a3, t1, t2, t3, n):
    f1 = []
    f2 = []
    f3 = []
    ftotal = 0
    ltotal = 0
    #initialize l1 and l2 to start at same spot as f1 and f2
    l1 = []
    l2 = []
    l3 = []
    l1.append(0)
    l2.append(0)
    l3.append(0)
    f1.append(a1[0] + a1[2])
    f2.append(a2[0] + a2[2])
    f3.append(a3[0] + a3[2])
    for j in range(1, n):
        if((f1[j - 1] + a1[j + 2] <= f2[j - 1] + t1[j - 1][1] + a1[j + 2]) and (f1[j - 1] + a1[j + 2] <= f3[j - 1] + t1[j - 1][2] + a1[j + 2])):
            f1.append(f1[j - 1] + a1[j + 2])
            l1.append(1)
        elif(f2[j - 1] + t1[j - 1][1] + a1[j + 2] <= f3[j - 1] + t1[j - 1][2] + a1[j + 2]):
            f1.append(f2[j - 1] + t1[j - 1][1] + a1[j + 2])
            l1.append(2)
        else:
            f1.append(f3[j - 1] + t1[j - 1][2] + a1[j + 2])
            l1.append(3)
     
        if((f2[j - 1] + a2[j + 2] <= f1[j - 1] + t2[j - 1][0] + a2[j + 2]) and (f2[j - 1] + a2[j + 2] <= f3[j - 1] + t2[j - 1][2] + a2[j + 2])):
            f2.append(f2[j - 1] + a2[j + 2])
            l2.append(2)
        elif(f1[j - 1] + t2[j - 1][0] + a2[j + 2] <= f3[j - 1] + t2[j - 1][2] + a2[j + 2]):
            f2.append(f1[j - 1] + t2[j - 1][0] + a2[j + 2])
            l2.append(1)
        else:
            f2.append(f3[j - 1] + t2[j - 1][2] + a2[j + 2])
            l2.append(3)
        
        if((f3[j - 1] + a3[j + 2] <= f1[j - 1] + t3[j - 1][0] + a3[j + 2]) and (f3[j - 1] + a3[j + 2] <= f2[j - 1] + t3[j - 1][1] + a3[j + 2])):
            f3.append(f3[j - 1] + a3[j + 2])
            l3.append(3)
        elif(f1[j - 1] + t3[j - 1][0] + a3[j + 2] <= f2[j - 1] + t3[j - 1][1] + a3[j + 2]):
            f3.append(f1[j - 1] + t3[j - 1][0] + a3[j + 2])
            l3.append(1)
        else:
            f3.append(f2[j - 1] + t3[j - 1][1] + a3[j + 2])
            l3.append(2)
    print f1
    print f2
    print f3
    if((f1[len(f1) - 1] + a1[1] <= f2[len(f2) - 1] + a2[1]) and (f1[len(f1) - 1] + a1[1] <= f3[len(f3) - 1] + a3[1])):
        ftotal = f1[len(f1) - 1] + a1[1]
        ltotal = 1
    elif(f2[len(f2) - 1] + a2[1] <= f3[len(f3) - 1] + a3[1]):
        ftotal = f2[len(f2) - 1] + a2[1]
        ltotal = 2
    else:
        ftotal = f3[len(f3) - 1] + a3[1]
        ltotal = 3
        
    results = []
    stri = "line " + str(ltotal) + ", station " + str(n)
    results.append(stri)
    j = n
    for x in range(1, j):
        j -= 1
        if ltotal == 1:
            stri = "line " + str(l1[j]) + ", station " + str(j)
            results.append(stri)
        elif ltotal == 2: 
            stri = "line " + str(l2[j]) + ", station " + str(j)
            results.append(stri)
        else:
            stri = "line " + str(l3[j]) + ", station " + str(j)
            results.append(stri)
            
    for x in results:
        print x
    
fastestWayThree(lane1, lane2, lane3, trans1, trans2, trans3, len(lane1) - 2)