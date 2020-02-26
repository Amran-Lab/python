#!/usr/bin/env python3.8
from family import family_class
import csv
tree = {}


grandfather = family_class('Old Man','Grandad')
print(grandfather.name,grandfather.relation)
tree[grandfather.name]=[grandfather.relation]
tree[grandfather.name].append('Senior')
chicken = family_class('Chick','Pet')
print(chicken.name,chicken.relation)
tree[chicken.name]=[chicken.relation]
tree[chicken.name].append('Hen')



def writ(fdict):
    with open('records.csv','w') as f:
        for key, value in fdict.items():
            f.write("%s, %s\n" % (key, str(value)))

check = {}
def remove(st):
    st = st.replace('[','')
    st = st.replace(']','')   
    st = st.replace(" '",'')
    st = st.replace("'",'')
    return st
def read(fdict):
    with open('records.csv','r') as f:
        reader = csv.reader(f)
        for rows in reader:
        
            key = rows[0]
            fdict[key] =[]
            for el in rows:
                if el != key:
                    fdict[key].append(remove(el))
                else:
                    pass
    return fdict
print(tree, "main tree being saved")
writ(tree)
check={}
check = read(check)
print(check, "tree being read")

"""string = check['Old Man'][0]
st = remove(string)
print(string.replace('[',''))
print(st)"""
