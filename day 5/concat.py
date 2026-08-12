import numpy as np
x=np.array([[2,1,1],[2,1,3]])
y=np.array([[2,3,4],[3,2,1]])
concat=np.concat((x,y),axis=0)
concat1=np.concat((x,y),axis=1)
print(concat)
print(concat1)