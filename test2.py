import sys

if __name__ == '__main__':
    file_name = sys.argv[1]
    fd = open(file_name,'r')
    productDict = {}
    for line in fd.readlines():
        lineList = line.strip().replace('\"',"").replace('{','').replace('}','').split(',')
        productId = lineList[1].split(':')[1]
        quantity = lineList[2].split(':')[1]
        if not productDict.has_key(productId):
            productDict[productId] = [1, int(quantity)]
        else:
            productDict[productId][0] += 1
            productDict[productId][1] += int(quantity)
        
        maxPurchasedIdList = []
        maxPurchasedValue = 0 
        maxSoldQuantityIdList = []
        maxSoldQuantityValue = 0 

        for key, value in productDict.items():
            if value[0] > maxPurchasedValue:
                maxPurchasedIdList = [key.strip()]
                maxPurchasedValue = value[0]
            elif value[0] == maxPurchasedValue:
                maxPurchasedIdList.append(value[0])

            if value[1] > maxSoldQuantityValue:
                maxSoldQuantityIdList = [key.strip()]
                maxSoldQuantityValue = value[1]
            elif value[1] == maxSoldQuantityValue:
                maxSoldQuantityIdList.append(value[1])
    
    PurcharsedPrefix = 'Most popular product(s) based on the number of purchasers: [ '
    PurcharsedContent = []
    for id in maxPurchasedIdList:
        PurcharsedContent.append('\"' + id + '\"')
    print PurcharsedPrefix + ','.join(PurcharsedContent) + ' ]'
            
    SoldQuantityPrefix = 'Most popular product(s) based on the quantity of goods sold: [ '
    SoldQuantityContent =[] 
    for id in maxSoldQuantityIdList:
        SoldQuantityContent.append('\"' + id + '\"')
    print SoldQuantityPrefix + ','.join(SoldQuantityContent) + ' ]'
