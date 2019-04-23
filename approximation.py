import math
import time
import os
import csv
import sys

def readData(filename):
    with open(filename) as file:
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


def bound():
    return math.ceil(sum(instance)/capacity)


def nextFit():
    containers, actualWeight = 0, 0
    for item in instance:
        if actualWeight + item <= capacity:
            actualWeight += item
        else:
            containers += 1
            actualWeight = item
    containers += 1
    return containers


def firstFitDecreasing():
    containers = []
    sortedList = sorted(instance, reverse=True)
    for item in sortedList:
        packed = False
        for container in containers:
            if sum(container) + item <= capacity:
                container.append(item)
                packed = True
                break
        if not packed:
            containers.append([item])
    return len(containers)


def round_to_n(x, n):
    if not x: return 0
    power = -int(math.floor(math.log10(abs(x)))) + (n - 1)
    factor = (10 ** power)
    return round(x * factor)/factor


def doTests(directory):
    global n
    global capacity
    global instance
    with open('results/'+directory.rpartition('/')[-1]+'_'+'results.csv', mode='w', newline='') as results_file:
        fieldnames = ['File Name', 'No', 'N', 'C', 'Bound', 'NF', 'NFratio', 'tNF', 'FFD', 'FFDratio', 'tFFD']
        writer = csv.DictWriter(results_file, fieldnames=fieldnames)
        writer.writeheader()
        index = 1
        for filename in os.listdir(directory):
            print(filename)
            n, capacity, instance = readData(directory+'/'+filename)
            start = time.perf_counter()
            NF = nextFit()
            t_NF = time.perf_counter() - start

            start = time.perf_counter()
            FFD = firstFitDecreasing()
            t_FFD = time.perf_counter() - start
            writer.writerow({'File Name': filename,
                             'No': index,
                             'N': n, 'C': capacity,
                             'Bound': bound(),
                             'NF': NF,
                             'NFratio': '{0:.2f}'.format((NF-bound())/bound() * 100),
                             'tNF': '{0:.10f}'.format(round_to_n(t_NF, 3)).rstrip("0"),
                             'FFD': FFD,
                             'FFDratio': '{0:.2f}'.format((FFD-bound())/bound() * 100),
                             'tFFD': '{0:.10f}'.format(round_to_n(t_FFD, 3)).rstrip("0")
                             })
            index += 1


generated = ['N100', 'N500', 'N1000', 'N5000', 'N10000', 'N20000']

doTests('./data/bin3data')
for n in generated:
    doTests('./data/generated/' + n)

