def readData(filename):
    with open('data/bin1data/'+filename+'.BPP') as file:
        content = file.readlines()
    return int(content.pop(0)), int(content.pop(0)), [int(x) for x in content]


def printInstance():
    print('Instance size: ', n)
    print('Bin capacity: ', capacity)
    print('Data: ', instance)
    print()


def checkResult(result):
    for item in result:
        if sum(item) > capacity:
            print('ERROR: Capacity of some bin is greater then defined constraint')
            return False
    result_flat = [item for sublist in result for item in sublist]
    if len(result_flat) == len(instance):
        if sum(result_flat) == sum(instance):
            print('Result is correct')
            return True
        else:
            print('ERROR: Sum of result is different then sum of input items')
    else:
        print('ERROR: Number of items in result is different then in input')
    return False


def printResult(result):
    if not checkResult(result):
        return
    print('---------------------------------------------------')
    print('                CALCULATED RESULT')
    print('---------------------------------------------------')
    print('M = %d' % len(result))
    for id, container in enumerate(result):
        print('ID: %d, elements: %s' % (id, str(container)))
    print('---------------------------------------------------')



def firstFit():
    containers, container, actualWeight = [], [], 0
    for item in instance:
        if actualWeight + item <= capacity:
            container.append(item)
            actualWeight += item
        else:
            containers.append(container)
            container = [item]
            actualWeight = item
    containers.append(container)
    printResult(containers)


n, capacity, instance = readData('N1C1W1_A')
printInstance()
firstFit()
