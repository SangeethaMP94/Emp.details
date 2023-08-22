class emp:
    def __init__(self,Id,Firstname,Lastname,Salary,Gender,DOB,Location):
        self.firstname=Firstname
        self.lastname=Lastname
        self.id=Id
        self.salary=Salary
        self.gender=Gender
        self.dob=DOB
        self.location=Location
class TCS(emp):
    def salary_format(self):
       self.salary=f"{float(self.salary):.2f}"
    def show(self):
        print("ID",self.id,"\nFirstname",self.firstname,"\nLastname",self.lastname,"\nSalary ",self.salary,"\nDOB ",self.dob,"\nLocation ",self.location,"\nGender",self.gender)
class HCL(emp):
    def salary_format(self):
        self.salary=self.salary-(0.1*self.salary)
    def update(self,Bloodgroup):
       self.location=Bloodgroup
    def update(self,DOJ):
       self.dob=DOJ
    def show(self):
       print("Id",self.id,"\nFirstname",self.firstname,"\nLastname",self.lastname,"\nSalary",self.salary,"\nGender ",self.gender,"\nBloodgroup: ",self.location,"\nDOJ: ",self.dob)
class INFY(emp):
    def update(self,Experience):
        self.gender=Experience
    def update(self,Aadhar):
        self.bloodgroup=Aadhar
    def update(self,Mobileno):
        self.dob=Mobileno
    def show(self):
      print("Id",self.id,"\nFirstname",self.firstname,"\nLastname",self.lastname,"\nSalary",self.salary,"\nExperience ",self.gender,"\nAadhar: ",self.location,"\nMobileno: ",self.dob)


e1=TCS("TCS23","Akila","M",30000,"Tirunelveli","27.04.2000","None")
e2=HCL("HCL23","Sangeetha","Perumal",30000,"Female","27.04.2020","B+ive")
e3=INFY("INFY23","Rathna","S",30000,"2years",9876543210,753920053456)

print("TCS Employee")
e1.salary_format()
e1.show()
print("--------------------------------------")
print("HCL Employee")
e2.salary_format()
e2.show()
print("------------------------------------------")
e3.show()
