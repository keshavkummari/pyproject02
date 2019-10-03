
"""
#                 01234567891011121314
cloud_services = 'aws azure gcp'

print(cloud_services,type(cloud_services),id(cloud_services),len(cloud_services))

print(cloud_services[0])        # Left to Right Indexing
print(cloud_services[-1])       # Right to Left Indexing
print(cloud_services[0:4])      # Range Slice End-1 3 0123 IaaS 0-4-1 = 3 0123  

#         01234567891011121314
values = '10203040506070890'
print(values[0::4])   # Zero Based Indexing

print(cloud_services[:3] + 'Amazon')

print(cloud_services * 3)

print(cloud_services[:3],cloud_services[10:14])

"""
# % Reminder Sign 
# .format()

fname, lname, accnumber = 'Keshav','Kummari',10203040
#print("Firstname: %s LastName: %s AccountNumber: %d " %(fname,lname,accnumber))
#print("Firstname: %s LastName: %s AccountNumber: %d " %('Keshav','Kummari',10203040))

print("Firstname: {} LastName: {} AccountNumber: {}" .format('Keshav','Kummari',10203040))
print("Firstname: {} LastName: {} AccountNumber: {}" .format(fname,lname,accnumber))
print("Firstname: {2} LastName: {0} AccountNumber: {1}" .format(lname,accnumber,fname))
