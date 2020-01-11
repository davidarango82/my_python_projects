from array import *

vals = array('i',[1,3,5,7,8])
#print(vals)
NewArr = array(vals.typecode, (a for a in vals))

print()