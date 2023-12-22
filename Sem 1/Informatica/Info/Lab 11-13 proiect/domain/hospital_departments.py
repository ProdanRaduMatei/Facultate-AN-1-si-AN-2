import utils.helpers as h

class HospitalDepartmentsException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class HospitalDepartments:

    def __init__(self, id_, name, number_of_beds, list_of_patients):
        """
        :param id_: the unique id for the hospital department
        :param name: the name of the hospital department
        :param number_of_beds: the number of beds in the hospital department
        :param list_of_patients: list with the patients in the hospital department
        """
        self._hospital_department_id = id_
        self._hospital_department_name = name
        self._hospital_department_number_of_beds = number_of_beds
        self._hospital_department_list_of_patients = list_of_patients
    

    @property
    def hospital_department_id(self):
        """
        Get the the ID of the department
        :return:
        :rtype: int
        """
        return self._hospital_department_id

    @hospital_department_id.setter
    def hospital_department_id(self, new_id):
        self._hospital_department_id = new_id

    @property
    def hospital_department_name(self):
        """
        Get the the name of the department
        :return:
        :rtype: str
        """
        return self._hospital_department_name

    @hospital_department_name.setter
    def hospital_department_name(self, new_name):
        self._hospital_department_name = new_name

    @property
    def hospital_department_number_of_beds(self):
        """
        Get the the number of beds of the department
        :return:
        :rtype: int
        """
        return self._hospital_department_number_of_beds
    
    @hospital_department_number_of_beds.setter
    def hospital_department_number_of_beds(self, new_number_of_beds):
        self._hospital_department_number_of_beds = new_number_of_beds
    
    @property
    def hospital_department_list_of_patients(self):
        """
        Get the copy of the list of the patients of the department
        :return:
        :rtype: list
        """
        new_list = self.hospital_department_list_of_patients.copy()
        return new_list
    
    @hospital_department_list_of_patients.setter
    def _hospital_department_list_of_patients(self, new_list_of_patients):
        if h.CheckList(new_list_of_patients):
            self._hospital_department_list_of_patients = new_list_of_patients.copy()
        else:
            raise ValueError("List is incorrect!")

    def __str__(self):
        """
        :return: the string form of a hospital departments
        """
        return str(self.hospital_department_id).rjust(9) + ' | ' + str(self.hospital_department_name).rjust(10)

class HospitalDepartmentsRepository:
    def __init__(self, initialDepartments=None):
        """
        Creating a repository containing hospital departments
        """
        self.__listOfDepartments = []
        if initialDepartments is not None:
            # check if the id's are unique
            for department in initialDepartments:
                if isinstance(department, HospitalDepartments) and self.__isIdUnique(department.id):
                    self.__listOfDepartments.append(department)
                else:
                    raise ValueError("Department is not correct")
    
    def __isIdUnique(self, id):
        """
        Check if the given id is already in the list
        :param id_:
        :type id_: int
        :return:
        :rtype: bool
        """
        for department in self.__listOfPatients:
            if department.id_ == id:
                return False
        return True