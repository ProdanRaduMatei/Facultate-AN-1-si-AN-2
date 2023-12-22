'''
Created on Jan, 2023

@author: Mathew
'''
#from domain.patient import Patient

class Department:
    '''
    Composed of ID, Name, Number of beds and List of patients.
    '''
    
    def __init__(self, id, n, beds, listOfPatients):
        '''
        Initialization of the class.
        '''
        #name, number, number of beds,and list of patients
        self.__name = n
        self.__id = id
        self.__nrBeds = beds
        self.__listPatients = listOfPatients
        
    def getName(self):
        '''
        Returns the name variable of the class.
        '''
        return self.__name
    
    def getNumber(self):
        '''
        Returns the id variable of the class.
        '''
        return self.__id
    
    def getNrBeds(self):
        '''
        Returns the number of beds variable of the class.
        '''
        return self.__nrBeds
    
    def getListOfPatients(self):
        '''
        Returns the list of patients variable of the class.
        '''
        return self.__listPatients
    
    def setName(self, value):
        '''
        Sets the name value to the name variable of the class.
        '''
        self.__name = value 
    
    def setNumber(self, value):
        '''
        Sets the id value to the id variable of the class.
        '''
        self.__id = value   
    
    def setNrBeds(self, value):
        '''
        Sets the number of beds value to the number of beds variable of the class.
        '''
        self.__nrBeds = value 
     
    def setListOfPatients(self, value):
        '''
        Sets the list of patients value to the list of paitents variable of the class.
        '''
        self.__listPatients = value    
    
    def equal(self, p2):
        '''
        Checks if 2 Departments have the same attributes.
        IN: 2 instances of a class
        OUT: True if equal, else False
        CONDIS: -
        '''
        if self.getName() != p2.getName() or self.getNumber() != p2.getNumber():
            return False
        if self.getNrBeds() != p2.getNrBeds() or len(self.getListOfPatients()) != len(p2.getListOfPatients()):
            return False 
        for i in range( len(p2.getListOfPatients()) ):
            if self.getListOfPatients()[i].equal( p2.getListOfPatients()[i] ) == False:
                return False
        return True
          
    def __repr__(self):
        '''
        Returns the attributes of the class as strings in order to be printed.
        '''
        #name, number, number of beds,and list of patients
        res = "DEPARTMENT: "
        res += self.__name + "\nNo. " + str(self.__id)
        res += "\nNumber of beds: " + str(self.__nrBeds) 
        res += "\nList of patients: \n"
        for el in self.getListOfPatients():
            res += "\t" + str(el) + "\n"
        return res
    
    def higherAgePatients(self, value):
        '''
        Computes how many patients in a department's list of patients have age higher than a given value.
        IN: a natural number
        OUT: a natural number
        CONDIS: value is positive
        '''
        res = 0
        for el in self.getListPatients():
            if el.getAge() > value:
                res += 1
        return res
    
    def numberOfPatients(self):
        '''
        Returns how many patients are in a department.
        IN: -
        OUT: a positive number
        CONDIS: -
        '''
        return len(self.__listPatients)  
    
    def patientsUnderAge(self, value):
        '''
        Returns how many patients are under given age in department.
        IN: a natural number
        OUT: an int
        CONDIS: value is positive
        '''
        res = 0
        for el in self.getListPatients():
            if el.getAge() < value:
                res += 1
        return res
    
    
class DepartmentException(Exception):
    '''
    Handles the errors appearing when working with list of patients.
    '''

    def __init__(self, message):
        self.__message = message
        
    def __str__(self):
        return self.__message      
        