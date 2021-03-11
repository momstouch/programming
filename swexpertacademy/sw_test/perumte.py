
length = 6
for i in range(2 ** length):
    print(list(('{0:0%db}' % (length)).format(i)))
