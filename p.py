
import pandas as pd

# data =[10,20,30,40,50]
# ps= pd.Series(data, index=['a','b','c','d','e'])
# print(ps)
# print(type(ps))
# print(ps['c'])

# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#         'Age': [25, 30, 35, 40, 45],}
# df= pd.DataFrame(data)
# print (df)
# print(type(df))
# print (pd.__version__)

# qmarks={"day1":90, "day2":80,"day3":70}
# ps = pd.Series(qmarks, index=['day1','day3'])
# ps= ps.tolist()
# print(ps)

# data={
#     "qmarks":[420,300,390],
#     "duration":[2,3,4],
#     "subject":["python","java","c++"]
# }
# df= pd.DataFrame(data)
# df.columns=["subject","qmarks","duration"]

# print(df.loc[[0]])

df = pd.DataFrame([['a','b',2,3],['c','d',3,4],['e','f',5,5],['g','h',7,0]], columns=['col1','col2','col3','col4'])
#print(df)

# res=df.iloc[1:3,0]=['x','y']
# print(res)
# print(df)

# #drop row
# res3= df.drop(1)
# print(res3)
# df.index=['r1','r2','r3','r4']
# res2= df.loc['r1':'r4','col1']
# print (res2)

#non zero

res4= df[df['col4']!=0]
res5= df.drop(df.index[2:4])
print(res5)
print(res4)