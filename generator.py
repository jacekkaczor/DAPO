import secrets
import os

number_of_items = [100, 500, 1000, 5000, 10000, 20000]
#number_of_items = [200]
capacities = [1000]

for instanceSize in number_of_items:
    for capacity in capacities:
        fileName = "N"+str(instanceSize)+"C"+str(capacity)+"_15.BPP"
        lines = []
        directory = "./data/generated/" + "N" + str(instanceSize)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory + '/' + fileName, 'w+') as file:
            lines.append(str(instanceSize)+'\n')
            lines.append(str(capacity)+'\n')
            for item in range(instanceSize):
                lines.append(str(300 + secrets.randbelow(100))+'\n')
            file.writelines(lines)
