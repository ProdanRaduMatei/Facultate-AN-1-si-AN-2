'''
Created on Jan, 2023

@author: Mathew
'''
import datetime

class Patient:
    '''
    Composed of First name, Last name, Personal numerical code and Disease
    '''
    #First name, Last name, Personal numerical code and Disease
    
    def __init__(self, firstName, lastName, cnp, disease):
        '''
        Constructor
        '''
        self.__firstName = firstName
        self.__lastName = lastName
        self.__cnp = cnp
        self.__disease = disease
    
    def getFirstName(self):
        '''
        Returns the first name variable of the class.
        '''
        return self.__firstName
    
    def getLastName(self):
        '''
        Returns the last name variable of the class.
        '''
        return self.__lastName
    
    def getCnp(self):
        '''
        Returns the cnp variable of the class.
        '''
        return self.__cnp
    
    def getDisease(self):
        '''
        Returns the disease variable of the class.
        '''
        return self.__disease    
    
    def setFirstName(self, value):
        '''
        Sets the first name value to the first name variable of the class.
        '''
        self.__firstName = value
    
    def setLastName(self, value):
        '''
        Sets the first name value to the first name variable of the class.
        '''
        self.__lastName = value
    
    def setCnp(self, value):
        '''
        Sets the cnp value to the cnp variable of the class.
        '''
        self.__cnp = value
    
    def setDisease(self, value):
        '''
        Sets the disease value to the disease variable of the class.
        '''
        self.__disease = value
    
    def equal(self, p2):
        '''
        Checks if 2 patients have the same attributes.
        IN: 2 instances of a class
        OUT: True if equal, else False
        CONDIS: -
        '''
        if self.getFirstName() != p2.getFirstName() or self.getLastName() != p2.getLastName():
            return False
        if self.getCnp() != p2.getCnp() or self.getDisease() != p2.getDisease():
            return False
        return True
    
    def __repr__(self):
        '''
        Returns the attributes of the class as strings in order to be printed.
        '''
        #First name, Last name, cnp, Disease
        return self.__firstName + " " + self.__lastName + " " + self.__cnp + " " + self.__disease +"" 

    def getAge(self):
        '''
        Computes age of person if age is less than 101.
        IN: -
        OUT: integer
        CONDIS:
        '''
        #year = 2023
        year = datetime.date.today().year
        dif = year - 2000
        s = self.getCnp() #string cnp
        birth = int(s[2]) + 10 * int(s[1])
        if birth <= dif:
            #its been born this millenia
            birth = 2000 + birth
        else:
            birth = 1900 + birth
        
        res = year - birth
        if res < 0:
            raise PatientException("Age is negative!") 
        return res

class PatientException(Exception):
    '''
    Handles the errors appearing when working with class Patient.
    '''

    def __init__(self, message):
        self.__message = message
        
        
    def __str__(self):
        return self.__message

