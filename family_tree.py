#!/usr/bin/env python3.8
from family import family_class

tree = {}
def writ():
    with open('records.txt', 'w') as f:
        for key, value in tree.items():
            f.write('%s:%s' % (key, value))


def read():
    with open('records.txt', 'r') as f:
        string=f.read()
        string = string.split(',')
        print(string)


read()
#print(tree)
#stuff = str(tree['Su'][0])


#print(stuff,"second record first value")

#son = family_class('Rai','bro')
#tree[son.name]=son.relation
#print("new tree", tree,"new rec", tree['Rai'])
#writ()
#read()
#print("after write new tree", tree,"new rec", tree['Rai'])
