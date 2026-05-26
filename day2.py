import pandas as pd
# df1= pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# df2=pd.DataFrame({'A':[10,20,30,40,50],'B':[60,70,80,90,100]}, index=[1,2,3,4,5])
# print(df1)
# print(df2)

#Ariithmetic operation on single dataframe
# print("\nAddition:\n",df1+5)
# print("\nAddition on data A:\n",df1['A']+2)
# print("\nMultiplication:\n",df1*2)

#Arrithmetic operation on multiple df
# print("\nAddition on mul. df\n",df1+df2)

#Concat along rows
one= pd.DataFrame({
    'id':[1,2,3,4],
    'Name':['Harsh','Harshita','a3','a4'],
    'Subject':['FSD','DBMS','sub3','sub4'],
    'Marks':[80,90,68,54]
    
})
two= pd.DataFrame({
    'id':[1,2,3,4],
    'Name':['Harshita','Harsh','b1','b2'],
    'Subject':['FSD','DBMS','sub5','sub6'],
    'Marks':[70,20,46,43]
})
# print(one)
# print(two)
# result= pd.concat([one,two], ignore_index=True)
# #result= pd.concat([one,two],keys=['x','y'])
# print(result)
# result_col= pd.concat([one,two],axis=1)
# print(result_col)

#merge
# res1= one.merge(two,on='id')
# print(res1)
# res2= one.merge(two, on='Subject', how='inner')
# print (res2)

#join
res3=one.join(two,on=None,lsuffix="_lsuffix",rsuffix="_rsuffix")
print(res3)