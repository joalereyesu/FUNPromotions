class User:
    def __init__(self, f_name, l_name, username, mail, password):
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.mail = mail
        self.password = password

    def getName(self):
        return self.f_name

    def getFullName(self):
        return self.f_name + ' ' + self.l_name

    def changeName(self, newName):
        self.f_name = newName
        return self.f_name

    def getMail(self):
        return self.mail

    def changeMail(self, newMail):
        self.mail = newMail
        return self.mail

    def getUsername(self):
        return self.username

    def changeUsername(self, newUsername):
        self.username = newUsername
        return self.username

    def validateUser(self, tryUsername, tryPassword):
        if self.username == tryUsername and self.password == tryPassword:
            return True
        else:
            return False
