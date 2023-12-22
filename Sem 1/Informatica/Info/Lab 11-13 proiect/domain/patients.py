import utils.helpers as h

class PatientException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class Patient:

    def __init__(self, cnp_, first_name, last_name, disease):
        """
        :param id_: the unique patient id
        :param first name: the first name of the patient
        :param last name: the last name of the patient
        :param diease: the disease of the patient
        """
        if h.checkCNP(cnp_):
            self._patient_cnp = cnp_
        else:
            raise ValueError("CNP isn't correct!")
        self._patient_first_name = first_name
        self._patient_last_name = last_name
        if h.checkDisease(disease):
            self._disease = disease
        else:
            raise ValueError("Disease isn't correct!")

    @property
    def patient_cnp(self):
        """
        Get the CNP of the patient
        :return:
        :rtype: int
        """
        return self._patient_cnp

    @patient_cnp.setter
    def patient_cnp(self, new_cnp):
        self._patient_cnp = new_cnp

    @property
    def patient_first_name(self):
        """
        Get the name of the patient
        :return:
        :rtype: str
        """
        return self._patient_first_name

    @patient_first_name.setter
    def patient_first_name(self, new_name):
        self._patient_first_name = new_name
    
    @property
    def patient_last_name(self):
        """
        Get the name of the patient
        :return:
        :rtype: str
        """
        return self._patient_last_name

    @patient_last_name.setter
    def patient_last_name(self, new_name):
        self._patient_last_name = new_name
    
    @property
    def patient_disease(self):
        """
        Get the disease of the patient
        :return:
        :rtype: str
        """
        return self._disease

    @patient_disease.setter
    def patient_disease(self, new_disease):
        self._disease = new_disease


    def __str__(self):
        """
        :return: returns the string form of a patient
        """
        return str(self.patient_cnp).rjust(6) + ' | ' + str(self.patient_name).rjust(15)

class PatientRepository:
    def __init__(self, initialPatients=None):
        """
        Creating a repository containing patients
        """
        self.__listOfPatients = []
        if initialPatients is not None:
            # check if the cnp's are unique
            for patient in initialPatients:
                if isinstance(patient, Patient) and self.__isCNPUnique(patient.cnp):
                    self.__listOfPatients.append(patient)
                else:
                    raise ValueError("Patient is not correct")
    
    def __isCNPUnique(self, cnp):
        """
        Check if the given id is already in the list
        :param id_:
        :type id_: int
        :return:
        :rtype: bool
        """
        for patient in self.__listOfPatients:
            if patient.cnp_ == cnp:
                return False
        return True