from datetime import datetime
import sys
import operator
import time

dataLines = []

def solution1(dataLines):
    countryDict = {}
    for line in dataLines:
        words = line.split(',')
        userId = words[1]
        countryId = words[2]
        siteId = words[3].strip().replace('\n','')
        if countryId == 'BDV':
            if not countryDict.has_key(userId):
                countryDict[userId] = [True, siteId]
            else:
                countryDict[userId][0] = False
    
    siteDict = {}
    for _, value in countryDict.items():
        if value[0] == True:
            if not siteDict.has_key(value[1]):
                siteDict[value[1]] = 1
            else:
                siteDict[value[1]] += 1
    
    ansSiteId = ""
    ansValue = 0

    maxValue = 0
    for key, value in siteDict.items():
        if value > maxValue:
            ansSiteId = key
            ansValue = value            

    print ', '.join([siteId, str(ansValue)])
            
        
def solution2(dataLines, startTime = '2019-02-03 00:00:00', stopTime = '2019-02-04 23:59:59'):
    startTimestamp = time.mktime(datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S').timetuple())
    stopTimestamp = time.mktime(datetime.strptime(stopTime, '%Y-%m-%d %H:%M:%S').timetuple())
    userDict = {}
    solution = {}

    for line in dataLines:
        words = line.split(',')
        lineTimestamp = time.mktime(datetime.strptime(words[0], '%Y-%m-%d %H:%M:%S').timetuple())
        userId = words[1]
        countryId = words[2]
        siteId = words[3].strip().replace('\n','')

        if lineTimestamp < startTimestamp:
            continue
        if lineTimestamp > stopTimestamp:
            break

        if not userDict.has_key(userId):
            userDict[userId] = {siteId:1}
        else:
            if not userDict[userId].has_key(siteId):
                userDict[userId][siteId] = 1 
            else:
                userDict[userId][siteId] += 1

        if userDict[userId][siteId] >= 10:
            solution[userId] = [siteId, userDict[userId][siteId]]

    for key, value in solution.items():
        print ', '.join([key, value[0], str(value[1])])

def solution3(dataLines):
    lastVisit = {}
    solution = {}
    for line in dataLines:
        words = line.split(',')
        userId = words[1]
        countryId = words[2]
        siteId = words[3].strip().replace('\n','')
        lastVisit[userId] = siteId

    for key, value in lastVisit.items():
        if not solution.has_key(value):
            solution[value] = 1
        else:
            solution[value] += 1
    solutionList = sorted(solution.items(), key=operator.itemgetter(1), reverse=True)
    cnt = 0
    for element in solutionList:
        if cnt > 2:
           return 
        print ', '.join([element[0], str(element[1])])
        cnt += 1
    
def solution4(dataLines):
    userDict = {}
    for line in dataLines:
        words = line.split(',')
        userId = words[1]
        countryId = words[2]
        siteId = words[3].strip().replace('\n','')

        if not userDict.has_key(userId):
            userDict[userId] = []
            userDict[userId].append(siteId)
            userDict[userId].append(siteId)
        else:
            userDict[userId][0] = siteId
    ansCount = 0
    for _, values in userDict.items():
        if values[0] == values[1]:
            ansCount += 1
    print ansCount

if __name__ == "__main__":
    file_name = sys.argv[1]
    fd = open(file_name,'r')
    dataLines = fd.readlines()
    dataLines = dataLines[1:]

    print 'solution1'
    solution1(dataLines)
    print 'solution2'
    solution2(dataLines)
    print 'solution3'
    solution3(dataLines)
    print 'solution4'
    solution4(dataLines)
