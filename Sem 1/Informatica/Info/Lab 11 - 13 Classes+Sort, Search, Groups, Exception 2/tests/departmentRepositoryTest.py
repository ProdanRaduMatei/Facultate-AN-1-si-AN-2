'''
Created on Jan, 2023

@author: Mathew
'''
import unittest
from repository.departmentRepository import DepartmentRepository
#from repository.patientRepository import PatientRepository 
from domain.patient import Patient
from domain.department import Department

class DepartmentRepositoryTest(unittest.TestCase):
    '''
    Asserts the methods from a class in order to check if they work properly.
    '''
    
    def test_Create(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p1 = Patient("Pop", "Andrei", "123456", "coughing")
        p2 = Patient("Pop", "Ioana", "223456", "fever")
        p3 = Patient("Blaga", "Vasile", "194657", "pain")
        p4 = Patient("Tuduce", "Matei", "194852", "pain")
        l = [p1, p2]
        d1 = Department(100, "Simple diseases", 2, l)
        l = [p3, p4]
        d2 = Department(200, "Serious diseases", 20, l)
        repo = DepartmentRepository()
        self.assertEqual( repo.getAll(), [] )
        repo.addNew(d1)
        repo.addNew(d2)
        self.assertEqual( repo.get(1), d2 )
        
        #__len__
        self.assertEqual( len(repo), 2 )
        #clear all
        repo.clearAll()
        self.assertEqual( repo.getAll(), [] )

        
    def test_Read(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p1 = Patient("Pop", "Andrei", "123456", "coughing")
        p2 = Patient("Pop", "Ioana", "223456", "fever")
        p3 = Patient("Blaga", "Vasile", "194657", "pain")
        p4 = Patient("Tuduce", "Matei", "194852", "pain")
        l = [p1, p2]
        d1 = Department(100, "Simple diseases", 2, l)
        l = [p3, p4]
        d2 = Department(200, "Serious diseases", 20, l)
        repo = DepartmentRepository()
        repo.addNew(d1)
        repo.addNew(d2)
        
        self.assertEqual( repo.findByIndex(1), d2 )
        try:
            repo.findByIndex(9)
            repo.findByIndex(-2)
            assert False
        except Exception:
            assert True
        #test_findByNumber/Name
    
    def test_Update(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p1 = Patient("Pop", "Andrei", "123456", "coughing")
        p2 = Patient("Pop", "Ioana", "223456", "fever")
        p3 = Patient("Blaga", "Vasile", "194657", "pain")
        p4 = Patient("Tuduce", "Matei", "194852", "pain")
        l = [p1, p2]
        d1 = Department(100, "Simple diseases", 2, l)
        l = [p3, p4]
        d2 = Department(200, "Serious diseases", 20, l)
        repo = DepartmentRepository()
        repo.addNew(d1)
        repo.addNew(d2)
        
        l = [p1, p4]
        d3 = Department("Boli psihice", 99, 0, l)
        repo.addNew(d3)
        repo.updateDepartmentByIndex(0, d3)
        self.assertEqual( repo.get(0), d3 )
        try:
            repo.updateDepartmentByIndex(9, d3)
            repo.updateDepartmentByIndex(-2, d3)
            assert False
        except Exception:
            assert True
    
    def test_Delete(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p1 = Patient("Pop", "Andrei", "123456", "coughing")
        p2 = Patient("Pop", "Ioana", "223456", "fever")
        p3 = Patient("Blaga", "Vasile", "194657", "pain")
        p4 = Patient("Tuduce", "Matei", "194852", "pain")
        l = [p1, p2]
        d1 = Department(100, "Simple diseases", 2, l)
        l = [p3, p4]
        d2 = Department(200, "Serious diseases", 20, l)
        repo = DepartmentRepository()
        repo.addNew(d1)
        repo.addNew(d2)
        
        size = len(repo)
        repo.deleteByIndex(0)
        self.assertEqual( len(repo), size-1 )
        try:
            repo.deleteByIndex(9)
            repo.deleteByIndex(-2)
            assert False
        except Exception:
            assert True        

    def test_findPatientInDepartment(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p1 = Patient("Pop", "Andrei", "123456", "coughing")
        p2 = Patient("Pop", "Ioana", "223456", "fever")
        p3 = Patient("Blaga", "Vasile", "194657", "pain")
        p4 = Patient("Tuduce", "Matei", "194852", "pain")
        p5 = Patient("a", "b", "c", "d")
        l = [p1, p2]
        d1 = Department(100, "Simple diseases", 2, l)
        l = [p3, p4]
        d2 = Department(200, "Serious diseases", 20, l)
        repo = DepartmentRepository()
        repo.addNew(d1)
        repo.addNew(d2)
        
        self.assertEqual( repo.findPatientInDepartment(p3), (1,0) )
        self.assertEqual( repo.findPatientInDepartment(p5), False )
        
    def test_sortPatientsByCnp(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        p1 = Patient("Pop", "Andrei", "223456", "coughing")
        p2 = Patient("Pop", "Ioana", "123456", "fever")
        l = [p1, p2]
        d1 = Department(100, "Simple diseases", 2, l)
        l = [p2, p1]
        d2 = Department(100, "Simple diseases", 2, l)
        repo = DepartmentRepository()
        repo.addNew(d1)
        
        res = repo.sortPatientsByCnp(d1)
        self.assertEqual( res[0].equal(d2), True )

        #self.assertEqual( res[0].getListPatients(), [p2, p1] )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()