'''
Created on Jan, 2023

@author: Mathew
'''
from domain.patient import Patient
from unittest import main, TestCase

class PatientTest(TestCase):
    '''
    Asserts the methods from a class in order to check if they work properly.
    '''
    
    def test_Create(self):
        '''
        Tests the initialization of the class.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p = Patient("Pop", "Andrei", "123456", "coughing")
        #test getters
        self.assertEqual( p.getFirstName(), "Pop" )
        self.assertEqual( p.getLastName(), "Andrei" )
        self.assertEqual( p.getCnp(), "123456" )
        self.assertEqual( p.getDisease(), "coughing" )        
        #test setters
        p.setFirstName("Matei")
        self.assertEqual( p.getFirstName(), "Matei" )
        p.setLastName("Corvin")
        self.assertEqual( p.getLastName(), "Corvin" )
        p.setCnp("2364758693526")
        self.assertEqual( p.getCnp(), "236475" )
        p.setDisease("fractura")
        self.assertEqual( p.getDisease(), "fractura" )
        
    
    def test_strPatient(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p = Patient("Pop", "Andrei", "123456", "coughing")
        self.assertEqual( str(p), "Pop Andrei 123456 coughing")
    
    def test_getAge(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p = Patient("Pop", "Andrei", "198456", "coughing")
        self.assertEqual( p.getAge(), 19)
        
           
#=============================== MAIN =============================           
if __name__ == "__main__" :
    main() 