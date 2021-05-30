#Open the File
handle = open('mbox-short.txt')

counts = dict()
hours = list()
lst = list()

for line in handle:
    # Skip the line if not starts with 'From:'
    if not line.startswith('From '):
        continue
    else:
        # Split the line, take the entire Hour
        line = line.split()
        num = line[5]
        # Split the Hour separated by ':'
        # and append Honly the Hour into a list
        num = num.split(':')
        hours.append(num[0])

#Count the number of times the Hour and let them in Dictionary
for hour in hours:
    counts[hour] = counts.get(hour,0) + 1

# Make a list from the Dictionary
for k,v in counts.items():
    newtup = (k,v)
    lst.append(newtup)

#Sort the list from the lowest to the highest
lst = sorted(lst)

#Print the outcomes one by one
for k,v in lst:
    print(k,v)

