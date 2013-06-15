'''
Created on 2013-6-11

@author: Administrator
'''

class Person:
    '''represents a person.'''
    population=0
    
    def __init__(self,name):
        '''initalizes the person's data.'''
        self.name=name
        print('initializing %s' % self.name)
        
        #when instancilize the class
        Person.population+=1
    def __del__(self):
        '''destruct the class '''
        Person.population-=1
        if Person.population==0:
            print('this object is deleting')
        else:
            print('this class be instanced %d object' % Person.population)
    def sayHi(self):
        '''say hi'''
        if Person.population==1:
            print('only an object have leave.')
        else:
            print('%d object have leave.' % Person.population)
    def howMany(self):
        '''Prints the current population.'''
        if Person.population==1:
            print('i am the only person here.')
        else:
            print('we have %d persons here.' % Person.population)
        