seq = "0 1 2 4 9 44 22 00 9 8 3 2 -1 -99 -0"

seqToList = list(map(int, seq.split(' ')))
seqToList_g = [int(i) for i in seq.split(' ')]

print(seqToList)
print(seqToList_g)

seqIter = iter(seqToList_g)
while True:
    item = next(seqIter, None)
    print(item)
    if item is None:
        print("break")
        break

print("end")
