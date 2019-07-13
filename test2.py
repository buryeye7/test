import sys

def solve(fine_name):
    fd = open(file_name,'r')
    productDict = {}
    for line in fd.readlines():
        lineList = line.strip().replace('\"',"").replace('{','').replace('}','').split(',')
        user = lineList[0].split(':')[1].strip()
        productId = lineList[1].split(':')[1].strip()
        quantity = lineList[2].split(':')[1].strip()
        if not productDict.has_key(productId):
            productDict[productId] = [1, int(quantity), [user]]
        else:
            productDict[productId][1] += int(quantity)
            if not user in productDict[productId][2]:
                productDict[productId][0] += 1
                productDict[productId][2].append(user)
        
    maxPurchaserIdList = []
    maxPurchaserValue = 0 
    maxSoldQuantityIdList = []
    maxSoldQuantityValue = 0 

    for key, value in productDict.items():
        if value[0] > maxPurchaserValue:
            maxPurchaserIdList = [key]
            maxPurchaserValue = value[0]
        elif value[0] == maxPurchaserValue:
            if not key in maxPurchaserIdList:
                maxPurchaserIdList.append(key)

        if value[1] > maxSoldQuantityValue:
            maxSoldQuantityIdList = [key]
            maxSoldQuantityValue = value[1]
        elif value[1] == maxSoldQuantityValue:
            if not key in maxSoldQuntityIdList:
                maxSoldQuantityIdList.append(key)
    
    PurcharserPrefix = 'Most popular product(s) based on the number of purchasers: [ '
    PurcharserContent = []
    for productId in maxPurchaserIdList:
        PurcharserContent.append('\"' + productId + '\"')
    print PurcharserPrefix + ','.join(PurcharserContent) + ' ]'
            
    SoldQuantityPrefix = 'Most popular product(s) based on the quantity of goods sold: [ '
    SoldQuantityContent =[] 
    for productId in maxSoldQuantityIdList:
        SoldQuantityContent.append('\"' + productId + '\"')
    print SoldQuantityPrefix + ','.join(SoldQuantityContent) + ' ]'

if __name__ == '__main__':
    file_name = sys.argv[1]
    solve(file_name)
