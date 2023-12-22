'''
Created on Jan, 2023

@author: Mathew
'''
from application.patientValidator import PatientValidator
from application.departmentValidator import DepartmentValidator
from application.appController import AppController
from repository.departmentRepository import DepartmentRepository
from repository.patientRepository import PatientRepository
from UI.AppUI import AppUI

def start():
    #create repository
    PRepo = PatientRepository()
    DRepo = DepartmentRepository()
    
    #create controller, provide repositories and validators
    pv = PatientValidator()
    dv = DepartmentValidator()
    controller = AppController(PRepo, DRepo, pv, dv)
    
    #create UI, provide controller
    ui = AppUI(controller)
    ui.run()
    
start()