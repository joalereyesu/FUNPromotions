class User:
    def __init__(self, f_name, l_name, username, mail, password):
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.mail = mail
        self.password = password

    def getFullName(self):
        return self.f_name + self.l_name

    def getMail(self):
        return self.mail

    def getUsername(self):
        return self.username

    def validateUser(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False
