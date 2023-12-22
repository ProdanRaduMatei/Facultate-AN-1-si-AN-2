'''
Created on Jan, 2023

@author: Mathew
'''
import unittest
from application.appController import AppController
from application.departmentValidator import DepartmentValidator
from application.patientValidator import PatientValidator
from repository.departmentRepository import DepartmentRepository
from repository.patientRepository import PatientRepository 
from domain.patient import Patient
from domain.department import Department

class AppControllerTest(unittest.TestCase):
    '''
    Asserts the methods from a class in order to check if they work properly.
    '''

    '''
    NOTE: PRepo and DRepo are populated before with some values from the init function in controller.
    Not only those that you see here.
    '''

    def test_Create(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        
        p1 = Patient("Pop", "Andrei", "123456", "coughing")
        p2 = Patient("Pop", "Ioana", "255556", "fever")
        l1 = [p1, p2]
        d1 = Department(100, "Simple diseases", 2, l1)
        
        #test create patient
        cp1 = ("Pop", "Andrei", "123456", "coughing")
        cp2 = ("Pop", "Ioana", "255556", "fever")
        cpp = ctrl.createPatient(cp1[0], cp1[1], cp1[2], cp1[3])
        self.assertEqual( p1.equal(cpp), True)
        
        #test create department
        l1 = [cp1, cp2]
        cd1 = (100, "Simple diseases", 2, l1)
        cdd = ctrl.createDepartment(cd1[0], cd1[1], cd1[2], cd1[3])
        self.assertEqual( d1.equal(cdd), True)
        
        #test add patient
        size = len(ctrl.getPatientRepository())
        cp3 = ("Po", "Oana", "255556", "appendicitis")
        ctrl.addPatient(cp3[0], cp3[1], cp3[2], cp3[3])
        self.assertEqual( len(ctrl.getPatientRepository()), size+1)
        
        #test add department
        size = len(ctrl.getDepartmentRepository())
        ctrl.addDepartment( cd1[0], cd1[1], cd1[2], cd1[3] )
        self.assertEqual( len(ctrl.getDepartmentRepository()), size+1)     
        
        #check if know when one patient exists already
        try:
            cp3 = ("Po", "Oana", "255556", "appendicitis")
            ctrl.addPatient(cp3[0], cp3[1], cp3[2], cp3[3]) 
            assert False
        except Exception:
            assert True
        
    def test_Read(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        
        ''' Repositories are populated by default with some elements in init.'''
#         p1 = ("Pop", "Andrei", "123456", "coughing")
#         p2 = ("Pop", "Ioana", "223456", "fever")
#         p3 = ("Blaga", "Vasile", "194657", "pain")
#         p4 = ("Tuduce", "Matei", "194852", "pain")
#         l1 = [p1, p2]
#         d1 = (100, "Simple diseases", 2, l1)
#         l2 = [p3, p4]
#         d2 = (200, "Serious diseases", 20, l2)
#         ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
#         ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        #test find patient by index
        self.assertEqual( ctrl.findPatientCommand(2), ctrl.getPatientRepository().get(2) )
        
        #test find department by index
        self.assertEqual( ctrl.findDepartmentCommand(1), ctrl.getDepartmentRepository().get(1) )

    def test_Update(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        
        p1 = ("Pop", "Andrei", "123456", "coughing")
        p2 = ("Pop", "Ioana", "223456", "fever")
        p3 = ("Blaga", "Vasile", "194657", "pain")
        p4 = ("Tuduce", "Matei", "194852", "pain")
        l1 = [p1, p2]
        d1 = (100, "Simple diseases", 2, l1)
        l2 = [p3, p4]
        d2 = (200, "Serious diseases", 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        #test update patient
        p4 = ("Rick", "Morty", "194812", "flu")
        vp4 = ctrl.createPatient("Rick", "Morty", "194812", "flu")
        ctrl.updatePatientByIndexCommand(p4[0], p4[1], p4[2], p4[3], 3)
        self.assertEqual( ctrl.getPatientRepository().get(3).equal(vp4), True )
        self.assertEqual( ctrl.getDepartmentRepository().get(1).getListPatients()[1].equal(vp4), True )
        
        #test update department
        l3 = [p1, p4]
        d3 = (200, "Serious diseases", 20, l3)
        vd3 = ctrl.createDepartment(200, "Serious diseases", 20, l3)
        ctrl.updateDepartmentByIndexCommand( d3[0], d3[1], d3[2], d3[3], 1 )
        self.assertEqual( ctrl.getDepartmentRepository().get(1).equal(vd3), True )

    def test_Delete(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        
        p1 = ("Pop", "Andrei", "123456", "coughing")
        p2 = ("Pop", "Ioana", "223456", "fever")
        p3 = ("Blaga", "Vasile", "194657", "pain")
        p4 = ("Tuduce", "Matei", "194852", "pain")
        l1 = [p1, p2]
        d1 = (100, "Simple diseases", 2, l1)
        l2 = [p3, p4]
        d2 = (200, "Serious diseases", 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        #test delete patient
        size = len(ctrl.getPatientRepository().getAll())
        sizeDepartmentPatients = len(ctrl.getDepartmentRepository().get(1).getListPatients())
        ctrl.deletePatientByIndexCommand(2)
        self.assertEqual( len(ctrl.getPatientRepository().getAll()), size-1 )
        self.assertEqual( len(ctrl.getDepartmentRepository().get(1).getListPatients()), sizeDepartmentPatients-1)
        ctrl.deletePatientByIndexCommand(4) #delete one inexistent in any department
        self.assertEqual( len(ctrl.getDepartmentRepository().get(1).getListPatients()), sizeDepartmentPatients-1)
        
        #test delete department
        size = len(ctrl.getDepartmentRepository().getAll())
        ctrl.deleteDepartmentByIndexCommand(0)
        self.assertEqual( len(ctrl.getDepartmentRepository().getAll()), size-1 )


    def test_sortPatientsByCnpCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        
        p1 = ("Pop", "Andrei", "223456", "coughing")
        p2 = ("Pop", "Ioana", "123456", "fever")
        p3 = ("Blaga", "Vasile", "194657", "pain")
        p4 = ("Tuduce", "Matei", "194852", "pain")
        l1 = [p1, p2]
        d1 = (100, "Simple diseases", 2, l1)
        l2 = [p3, p4]
        d2 = (200, "Serious diseases", 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        l1 = [p2, p1]
        d3 = Department(100, "Simple diseases", 2, l1)

        self.assertEqual( d3.equal(ctrl.sortPatientsByCnpCommand(100)[0]), False )
     
     
    def test_sortDepartmentByNrPatientsAgeCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''  
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        ctrl.clearRepos()
        
        p1 = ("Pop", "Andrei", "223456", "coughing")
        p2 = ("Pop", "Ioana", "123456", "fever")
        p3 = ("Blaga", "Vasile", "194657", "pain")
        p4 = ("Tuduce", "Matei", "194852", "pain")
        l1 = [p1, p2]
        d1 = (100, "Simple diseases", 2, l1)
        l2 = [p3, p4]
        d2 = (200, "Serious diseases", 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        res = [ctrl.getDepartmentRepository().get(0), ctrl.getDepartmentRepository().get(1) ]
        self.assertEqual( ctrl.sortDepartmentsByNrPatientsAgeCommand(50), res  )            

    def test_sortDepartmentsByNrPatsAndPatsAlphCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''  
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)  
        
        res = [ctrl.getDepartmentRepository().get(2), ctrl.getDepartmentRepository().get(1), ctrl.getDepartmentRepository().get(0)]
        self.assertEqual( ctrl.sortDepartmentsByNrPatsAndPatsAlphCommand(), res  )            

    def test_findDepartmentsWithPatientsUnderAgeCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''  
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        ctrl.clearRepos()
        
        p1 = ("Pop", "Andrei", "223456", "coughing")
        p2 = ("Pop", "Ioana", "123456", "fever")
        p3 = ("Blaga", "Vasile", "194657", "pain")
        p4 = ("Tuduce", "Matei", "194852", "pain")
        l1 = [p1, p2]
        d1 = (100, "Simple diseases", 2, l1)
        l2 = [p3, p4]
        d2 = (200, "Serious diseases", 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        res = [ ctrl.getDepartmentRepository().get(1) ]
        self.assertEqual( ctrl.findDepartmentsWithPatientsUnderAgeCommand(50), res )            

    def test_findPWithStrInNameCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''  
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        ctrl.clearRepos()
        
        p1 = ("Pop", "Andrei", "223456", "coughing")
        p2 = ("Pop", "Ioana", "123456", "fever")
        p3 = ("Blaga", "Vasile", "194657", "pain")
        p4 = ("Tuduce", "Matei", "194852", "pain")
        l1 = [p1, p2]
        d1 = (100, "Simple diseases", 2, l1)
        l2 = [p3, p4]
        d2 = (200, "Serious diseases", 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        res = [ ctrl.getDepartmentRepository().get(0).getListPatients()[0], ctrl.getDepartmentRepository().get(0).getListPatients()[1] ]
        self.assertEqual( ctrl.findPWithStrInNameCommand(100, "Pop"), res )
    
    def test_findDepartmentsByPatientsFirstNameCommand(self):  
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''  
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        ctrl.clearRepos()
        
        p1 = ("Pop", "Andrei", "223456", "coughing")
        p2 = ("Pop", "Ioana", "123456", "fever")
        p3 = ("Blaga", "Vasile", "194657", "pain")
        p4 = ("Tuduce", "Matei", "194852", "pain")
        l1 = [p1, p2]
        d1 = (100, "Simple diseases", 2, l1)
        l2 = [p3, p4]
        d2 = (200, "Serious diseases", 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        res = [ ctrl.getDepartmentRepository().get(0) ]
        self.assertEqual( ctrl.findDepartmentsByPatientsFirstNameCommand("Pop"), res )  
     
    def test_groupPatientsByDiseaseCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        ctrl.clearRepos()
        p1 = ("Pop", "Andrei", "223456", "coughing")
        p2 = ("Pop", "Ioana", "123456", "fever")
        p3 = ("Blaga", "Vasile", "194657", "pain")
        p4 = ("Tuduce", "Matei", "194852", "pain")
        l1 = [p1, p2]
        d1 = (100, "Simple diseases", 2, l1)
        l2 = [p3, p4]
        d2 = (200, "Serious diseases", 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )
        
        res = list(ctrl.groupPatientsByDiseaseCommand(2))
        self.assertEqual( len(res), 2)  
        self.assertEqual( len(res[1]), 2)  
    
    def test_groupDepartmentsCommand(self):
        '''
        Checks if the function works properly and handles the exception cases.
        IN: - 
        OUT: -
        CONDIS: -
        '''
        pv = PatientValidator()
        dv = DepartmentValidator()
        DRepo = DepartmentRepository()
        PRepo = PatientRepository()
        ctrl = AppController(PRepo, DRepo, pv, dv)
        ctrl.clearRepos()
        p1 = ("Pop", "Andrei", "223456", "coughing")
        p2 = ("Pop", "Ioana", "123456", "coughing")
        p3 = ("Blaga", "Vasile", "194657", "pain")
        p4 = ("Tuduce", "Matei", "194852", "pain")
        l1 = [p1, p2]
        d1 = (100, "Simple diseases", 2, l1)
        l2 = [p3, p4]
        d2 = (200, "Serious diseases", 20, l2)
        ctrl.addDepartment( d1[0], d1[1], d1[2], d1[3] )
        ctrl.addDepartment( d2[0], d2[1], d2[2], d2[3] )   
        
        res = list(ctrl.groupDepartmentsCommand(2, 2))
        self.assertEqual( len(res), 2) 
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()