
# Data Types in Python

'''
1. Number Data Type : int(), float(), complex()  (Immutable Data Types)

student_id = 100
marks = 75.35
print(student_id,type(student_id),id(student_id))
print(marks,type(marks),id(marks))

datainfo = 3+5J
print(datainfo)

int()
float()
complex()

2. String Data Type : str()   (Immutable Data Types)

list_of_cloud_providers = 'ABCDEF abcdef 0123404 % # @'
print(list_of_cloud_providers,type(list_of_cloud_providers))

3. List Data Type : list()  (Mutable Data Types)

#cloudVendors = []
cloudVendors = ['AWS',"azure",1985,10.75,3+5j,' ',"#",'@']
print(cloudVendors,type(cloudVendors),id(cloudVendors),len(cloudVendors))

#print(list(enumerate(cloudVendors)))

cloudVendors[1]='IBM'
print(cloudVendors,type(cloudVendors),id(cloudVendors),len(cloudVendors))

#print(list(enumerate(cloudVendors)))

4. Tuple Data Type : tuple() : (Immutable Data Types)

#listOfBanks = 'SBI',"ABN",'HDFC',"HSBC"
#listOfBanks = ('AWS',"azure",1985,10.75,3+5j,' ',"#",'@')
#listOfBanks = 'AWS',"azure",1985,10.75,3+5j,' ',"#",'@'
listOfBanks = tuple('AWS')
print(listOfBanks,type(listOfBanks),id(listOfBanks),len(listOfBanks))

5. Dict Data Types 

6. Sets Data Types 

'''




