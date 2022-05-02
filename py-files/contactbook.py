

#im trying to figure out what im supposed to do with classes. i sort of understand what they are
#and what they do but im  not sure how to use them in practical code and things like that.


#! still dont understand classes
class Test:
    def __init__(self, firstname, lastname, email, cell, home) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.cell = cell
        self.home = home

    def getContact(self):
        pass

    def add(self):
        Test.firstname = 'Brad'
        Test.lastname = 'TFT'
        Test.email = 'BradTFTgitHub@email.com'
        Test.cell = 'cellnumber'
        Test.home = 'phonenumber'



print(Test)


