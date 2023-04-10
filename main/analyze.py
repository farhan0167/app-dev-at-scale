import random
import requests
import collections

names = ["ahmad","farhan","ishraq"]

for i in range(10):
    rand_idx = random.randint(0,len(names)-1)
    test = f"http://localhost/search/{names[rand_idx]}"
    try:
        requests.get(test)
    except:
        print("there was a problem at ", i)
        continue

name_dict = collections.defaultdict(list)

#question: how many times did an individual get assinged a different server?
with open('results/output.txt', 'r') as f:
        for line in f:
            ln = line.rstrip('\n').strip().split(",")
            if ln[1] not in name_dict[ln[0]]:
                name_dict[ln[0]].append(ln[1])
f.close()
print(name_dict)

