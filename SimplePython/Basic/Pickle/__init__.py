
'''
pickle is a sustainable storage container 
cPickle implement in C language
pickle implement in python
'''
import cPickle as pk 
#import pickle as p 

filePath=r'd:\pickle.data'

catalog=['shoes','T-shits','cats']

#write to the file d:\pickle.data
f=file(filePath,'a')
# dump the object to a file
#pk.dump(catalog,f)

# dump the object to a file
pk.dump(list(['w','e']),f)

f.close()

del catalog

#read file from d:\pickle.data
f=file(filePath,'r')
catalog_bak=pk.load(f)
print(catalog_bak)
