from User import User
import pytest

user = User('Jose', 'Reyes', 'joalereyesu',
            'alejandroreyes@ufm.edu', 'fafato123')


def test_getName():
    e_result = 'Jose'
    assert e_result == user.getName()


def test_getFullName():
    e_result = 'Jose Reyes'
    assert e_result == user.getFullName()


def test_changeName():
    e_result = 'Alejandro'
    newName = 'Alejandro'
    assert e_result == user.changeName(newName)


def test_getEmail():
    e_result = 'alejandroreyes@ufm.edu'
    assert e_result == user.getMail()


def test_changeEmail():
    e_result = 'joalereyesu@gmail.com'
    assert e_result == user.changeMail("joalereyesu@gmail.com")


def test_getUsername():
    e_result = 'joalereyesu'
    assert e_result == user.getUsername()


def test_changeUsername():
    e_result = 'josereyes21'
    assert e_result == user.changeUsername("josereyes21")
