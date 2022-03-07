from User import User


def getNameTest(user):
    e_result = 'Jose'
    if e_result == user.getName():
        return True
    else:
        return False


def getFullNameTest(user):
    e_result = 'Jose Reyes'
    print(user.getFullName())
    if e_result == user.getFullName():
        return True
    else:
        return False


def changeNameTest(newName, user):
    e_result = 'Alejandro'
    if e_result == user.changeName(newName):
        return True
    else:
        return False


def getEmailTest(user):
    e_result = 'alejandroreyes@ufm.edu'
    if e_result == user.getMail():
        return True
    else:
        return False


def changeEmailTest(newMail, user):
    e_result = 'joalereyesu@gmail.com'
    if e_result == user.changeMail(newMail):
        return True
    else:
        return False


def getUsernameTest(user):
    e_result = 'joalereyesu'
    if e_result == user.getUsername():
        return True
    else:
        return False


def changeUsernameTest(newUsername, user):
    e_result = 'josereyes21'
    if e_result == user.changeUsername(newUsername):
        return True
    else:
        return False


def validateUserTest(loginUsername, loginPassword, user):
    if (user.validateUser(loginUsername, loginPassword)):
        return True
    else:
        return False


user_object = User('Jose', 'Reyes', 'joalereyesu',
                   'alejandroreyes@ufm.edu', 'fafato123')

print("TESTS CLASE USUARIOS\n___________________________\nSi el resultado fue 'True' el test fue exitoso.\n")
print(f"1. Test getName: {getNameTest(user_object)}")
print(f"2. Test getFullName: {getFullNameTest(user_object)}")
print(f"3. Test changeName: {changeNameTest('Alejandro', user_object)}")
print(f"4. Test getEmail: {getEmailTest(user_object)}")
print(
    f"5. Test changeEmail: {changeEmailTest('joalereyesu@gmail.com', user_object)}")
print(f"6. Test getUsername: {getUsernameTest(user_object)}")
print(
    f"7. Test changeUsername: {changeUsernameTest('josereyes21', user_object)}")
print(
    f"8. Test login: {validateUserTest('josereyes21', 'fafato123', user_object)}")
