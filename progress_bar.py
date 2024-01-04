import time
barLength = 100

def progress(itemsLeft, totalItems):
    fraction = itemsLeft / totalItems
    
    arrow = int(fraction * barLength - 1) * '-' + '>' if fraction != 1 else int(fraction * barLength) * '-'
    padding = int(barLength - len(arrow)) * ' '
    
    ending = '\n' if itemsLeft == totalItems else '\r'
    
    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)
    
total = 150
count = 0

for i in range(150):
    count = count + 1
    time.sleep(20/1000)
    progress(count, total)
