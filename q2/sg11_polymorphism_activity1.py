class Patient: #creates parent class
    def __init__(self, name, bill_amount): #datatypes
        self._name = name
        self._bill_amount = bill_amount
      
  #gets name of the patient
    @property
    def name(self):
        print("Patient Name:", self._name)
        return self._name
      
    #gets bill amount
    @property
    def bill_amount(self):
        print(f"Original Bill: P{self._bill_amount:.2f}")
        return self._bill_amount

  #changes the name of the patinet
    @name.setter
    def name(self, name):
        self._name = name

  #verifies the bill amount is greater than 0 and changes the bill amount
    @bill_amount.setter
    def bill_amount(self, amount):
        if amount > 0:
            self._bill_amount = amount
            print(f"Original Bill: P{self._bill_amount:.2f}")
        else:
            print("No no no no no no no no, DONT DO DAT")

    def calculate_bill(self):
        print(f"Final Bill: P{self._bill_amount:.2f}")
        return self._bill_amount

  #displays the patient type
    def display_patient_type(self):
        print("Patient Type: Regular Patient")
        
class Senior(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

  #calculates discount of the Senior Citizen patient
    def calculate_bill(self):
        final_bill = self._bill_amount * 0.80
        print(f"Final Bill: P{final_bill:.2f}")
        return final_bill

   #displays the patient type
    def display_patient_type(self):
        print("Patient Type: Senior Citizen")
        
class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

   #calculates discount of the PhilHealth Member patient
    def calculate_bill(self):
        final_bill = self._bill_amount * 0.85
        print(f"Final Bill: P{final_bill:.2f}")
        return final_bill

   #displays the patient type
    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")

regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = Senior("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]

#displays information
print("Hospital Billing System")
print("- - - - - - - - - - - - - - ")
for patient in patients:
    patient.name
    patient.display_patient_type()
    patient.bill_amount
    patient.calculate_bill()
    print("=--------------=")
