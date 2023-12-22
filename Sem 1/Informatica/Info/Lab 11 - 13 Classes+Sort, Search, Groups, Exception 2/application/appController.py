'''
Created on Jan, 2023

@author: Mathew
'''
from domain.patient import Patient
from domain.department import Department

class AppController:
    '''
    Controlls the patient and department repository.
    Composed of 2 classes.
    '''
    def __init__(self, patientRepository, departmentRepository, patientValidaor, departmentValidator):
        '''
        Initializes the controller.
        '''
        self.__patientRepo = patientRepository
        self.__departmentRepo = departmentRepository
        self.__patientValidator = patientValidaor
        self.__departmentValidator = departmentValidator
        #First Name, Last Name, cnp, Disease
        #ID, Name, Number of beds, List of patients
        
        #Stomach ailments
        p1 = Patient("Pop", "Ioana", "216456", "obesity")
        p2 = Patient("Gradinita", "Emilutzbac", "164456", "obesity")
        
        #Serious diseases
        p3 = Patient("Baciu", "Tudose", "124658", "Ecoli")
        p4 = Patient("Enigma", "Otiliei", "264769", "Ecoli")
        p5 = Patient("Baciu", "Gheorghe", "264768", "Ecoli")
        
        #Special diseases
        p6 = Patient("Baciu", "Aihai", "298784", "fever")
        p7 = Patient("Ion", "Creanga", "212348", "fever")
        p8 = Patient("Mester", "Pelea", "212346", "fever")
        p9 = Patient("Garbau", "Opris", "212348", "pain")
        
        #Pshihical diseases
        p10 = Patient("Eminescu", "Mihai", "298784", "Schizofrenic")
        p11 = Patient("Pintea", "Vasile", "2123484", "Schizofrenic")
        p12 = Patient("Term", "Enescu", "212346", "fever")
        p13 = Patient("Ulise", "Zeu", "212341", "pain")
        
        d1 = Department(702, "Stomach ailments", 5, [p1, p2])
        d2 = Department(100, "Serious diseases", 3, [p3, p4, p5])
        d3 = Department(500, "Special diseases", 10, [ p6, p7, p8, p9])
        d4 = Department(10, "Boli psihice", 5, [ p10, p11, p12, p13])
        
        self.__patientRepo.addNew(p1)
        self.__patientRepo.addNew(p2)
        self.__patientRepo.addNew(p3)
        self.__patientRepo.addNew(p4)
        self.__patientRepo.addNew(p5)
        self.__patientRepo.addNew(p6)
        self.__patientRepo.addNew(p7)
        self.__patientRepo.addNew(p8)
        self.__patientRepo.addNew(p9)
        self.__patientRepo.addNew(p10)
        self.__patientRepo.addNew(p11)
        self.__patientRepo.addNew(p12)
        self.__patientRepo.addNew(p13)
        
        self.__departmentRepo.addNew(d1)
        self.__departmentRepo.addNew(d2)
        self.__departmentRepo.addNew(d3)
        self.__departmentRepo.addNew(d4)
    
    def getPatientRepository(self):
        '''
        Returns the repository of patients.
        '''
        return self.__patientRepo
    
    def getDepartmentRepository(self):
        '''
        Returns the repository of departments.
        '''
        return self.__departmentRepo
    
    #CREATE
    def createPatient(self,firstName, lastName, cnp, disease):
        '''
        Creates a new instance of Patient.
        IN: 4 strings
        OUT: a Patient
        CONDIS: -
        '''
        p = Patient(firstName, lastName, cnp, disease)
        self.__patientValidator.validate(p)
        return p
    
    #CREATE
    def createDepartment(self, id, n, beds, listOfPatients):
        '''
        Creates a new instance of Department.
        IN: string, int, int, list of tuples
        OUT: a Department
        CONDIS: number and beds are positive numbers
        '''
#         if number < 0 or beds < 0:
#             raise AppControllerException("Number or number of beds of department is negative!")
        
        #l contains tuple of 4 strings, we transform them in list with Patients
        l2 = []
        for el in listOfPatients:
            p = self.createPatient(el[0], el[1], el[2], el[3])
            l2.append(p)
        
        d = Department(id, n, beds, l2)
        self.__departmentValidator.validate(d)
        return d
    
    def addPatient(self, firstName, lastName, cnp, disease):
        '''
        Add/Create
        IN: 4 strings
        OUT: -
        CONDIS: - 
        '''
        p = self.createPatient(firstName, lastName, cnp, disease)
        self.__patientRepo.addNew(p)
       
    def addDepartment(self, id, n, beds, listOfPatients):
        '''
        Adds/Creates a new instance of Department in the repository.
        IN: string, int, int, list of tuples
        OUT: -
        CONDIS: -
        '''
        d = self.createDepartment(id, n, beds, listOfPatients)
#         for el in d.getListPatients():
#             self.__PRepo.addNew(el)
        self.addListPRec(d.getListPatients())
            
        self.__departmentRepo.addNew(d)
    
    def addListPRec(self, listOfPatients):
        '''
        Adds recursively a list of patients to the patients repository.
        IN: -
        OUT: -
        CONDIS: -
        '''
        if len(listOfPatients) == 0:
            return
        else:   
            self.__patientRepo.addNew(listOfPatients[0])
            self.addListPRec(listOfPatients[1:])
      
    #READ
    def findPatientCommand(self, index):
        '''
        Finds an instance of a class from a repository.
        IN: a positive number
        OUT: an instance class
        CONDIS: handled in get() function
        '''
        return self.__patientRepo.get(index)
    
    #READ
    def findDepartmentCommand(self, index):
        '''
        Finds an instance of a class from a repository.
        IN: a positive number
        OUT: an instance class
        CONDIS: handled in get() function
        '''
        return self.__departmentRepo.get(index)  
    
    #READ, ut
    def findDepartmentByIDCommand(self, nr):
        '''
        Finds an instance of a class from a repository.
        IN: a positive number
        OUT: an instance class
        CONDIS: nr is positive
        '''
        return self.__departmentRepo.findDepartmentByID(nr)
    
    #UPDATE    
    def updatePatientByIndexCommand(self, firstName, lastName, cnp, disease, index):
        '''
        Replaces an element from both repositories if exists.
        IN: a positive number
        OUT: -
        CONDIS: handled in updateDepartementByIndex function
        '''
        newP = self.createPatient(firstName, lastName, cnp, disease)
        p = self.findPatientCommand(index)
        
        #check if patient exists in department
        if self.getDepartmentRepository().findPatientInDepartment(p) != False:
            indices = self.getDepartmentRepository().findPatientInDepartment(p)
            #update patient in department
            self.getDepartmentRepository().getAll()[indices[0]].getListPatients()[indices[1]] = newP
        
        #update in patients repository            
        self.__patientRepo.updatePatientByIndex(index, newP)
        
        
    #UPDATE    
    def updateDepartmentByIndexCommand(self, id, n, beds, listOfPatients, index):
        '''
        Replaces an element from the repository.
        IN: a positive number
        OUT: -
        CONDIS: handled in updateDepartementByIndex function
        '''
        d = self.createDepartment(id, n, beds, listOfPatients)
        self.__departmentRepo.updateDepartmentByIndex(index, d)

    #DELETE    
    def deletePatientByIndexCommand(self, index):
        '''
        Removes an instance of a class from a specific repository.
        IN: a number
        OUT: -
        CONDIS: handled in deleteByIndex function
        '''
        p = self.findPatientCommand(index)
        
        #check if patient exists in department
        if self.getDepartmentRepository().findPatientInDepartment(p) != False:
            indices = self.getDepartmentRepository().findPatientInDepartment(p)
            #delete patient in department
            del self.getDepartmentRepository().getAll()[indices[0]].getListPatients()[indices[1]]
        self.__patientRepo.deleteByIndex(index)
        
        
    #DELETE    
    def deleteDepartmentByIndexCommand(self, index):
        '''
        Removes an instance of a class from a specific repository.
        IN: a number
        OUT: -
        CONDIS: handled in deleteByIndex function
        '''
        self.__departmentRepo.deleteByIndex(index)
      
    def showPatientRepository(self):
        '''
        Shows the patient repository.
        '''
        return str(self.__patientRepo)    
        
    def showDepartmentRepository(self):
        '''
        Shows the department repository.
        '''
        return str(self.__departmentRepo) 
    
    def clearRepos(self):
        '''
        Clears the repositories.
        '''
        self.__departmentRepo.clearAll()
        self.__patientRepo.clearAll()
    
    def sortPatientsByCnpCommand(self, number):
        '''
        Calls a function that sorts patients in a department with given number.
        IN: -
        OUT: a list with one object department and its patients sorted
        CONDIS: -
        '''
        d = self.findDepartmentByIDCommand(number)
        return self.__departmentRepo.sortPatientsByCnp(d)    

    def sortDepartmentsByNrPatientsAgeCommand(self, value):
        '''
        Sorts departments by which one has more patients with higher age than given value.
        IN: a natural number
        OUT: a list with departments
        CONDIS: -
        '''
        return self.__departmentRepo.sortDepartmentsByNrPatientsAge(value)
    
    def sortDepartmentsByNrPatientsAndPatientsAlphbeticallyCommand(self):
        '''
        Sorts departments by which one has more patients and the patients in these departments are alphabetically ordered
        IN: - 
        OUT: a list with departments
        CONDIS: -
        '''
        return self.__departmentRepo.sortDepartmentsByNrPatientsAndPatientsAlphabetically()
    
    def findDepartmentsWithPatientsUnderAgeCommand(self, age):
        '''
        Returns departments which have patients under age
        IN: -
        OUT: a list with departments
        CONDIS: 
        '''
        return self.__departmentRepo.findDepartmentsWithPatientsUnderAge(age)
    
    def findPatientsWithStrInNameCommand(self, nr, st):
        '''
        Returns a list with patients containing the string st in first or last name from a given department
        IN: a string
        OUT: a list with Patients
        CONDIS: - 
        '''
        d = self.findDepartmentByIDCommand(nr)
        #la creare se considera ca nu pot avea acelasi nr, deci exista un singur d
        return self.__departmentRepo.findPatientsWithStrInName(d, st)
    
    def findDepartmentsByPatientsFirstNameCommand(self, fN):
        '''
        Identifies the departments where there are patients with a given first name.
        IN: a string
        OUT: a list with departments
        CONDIS: -
        '''
        return self.__departmentRepo.findDepartmentsByPatientsFirstName(fN)
        
    def groupPatientsByDiseaseCommand(self, gs):
        '''
        For each department it groups the patients having the same disease.
        IN: an int
        OUT: a list with lists of patients
        CONDIS: gs is > 0
        '''
        if gs <= 0:
            raise AppControllerException("Group size is not valid! <= 0")
        
        aux = []
        for dep in self.__departmentRepo.getAll():
            aux.append( self.__departmentRepo.groupPatientsByDisease(gs, dep) )
        return aux
    
    
    def groupDepartmentsCommand(self, gs, p):
        '''
        Groups departments with at most p pats with same disease.
        IN: 2 natural numbers
        OUT: a list with lists consisted of departments
        CONDIS: gs and p are positive and p > 0
        '''
        if gs <= 0 or p < 1:
            raise AppControllerException("Group size or most patients number is not valid! <= 0")
          
        return self.__departmentRepo.groupDepartments(gs, p)
        
        
class AppControllerException(Exception):
    '''
    Handles the errors appearing when working with class Patient.
    '''
    def __init__(self, message):
        self.__message = message
        
    def __str__(self):
        return self.__message 
        
# PRepo = PatientRepository()
# DRepo = DepartmentRepository()
# ctrl = AppController(PRepo, DRepo)
# l = [("a","b","C","d"), ("z","Y","f","v")]
# 
# print( ctrl.createDepartment(100, "Simple diseases", 5, l) )