from unittest import mock
from BinaryTree import Tree
import pytest

tree = Tree()

MockObj = [
    {
        "name": "END OF SCHOOL",
        "date": 1687365000,
        "normalDate": "21 June 2023"
    },
    {
        "name": "BACK TO BASICS",
        "date": 1673487000,
        "normalDate": "11 January 2023"
    },
    {
        "name": "TOO TURNT FEST",
        "date": 1677915000,
        "normalDate": "4 March 2023"
    },
    {
        "name": "NEW YEARS FEST",
        "date": 1704088800,
        "normalDate": "1 January 2024"

    },
    {
        "name": "BORN THIS WAY",
        "date": 1661346000,
        "normalDate": "24 August 2022"
    },
    {
        "name": "30 ADELE",
        "date": 1700492400,
        "normalDate": "20 November 2023"
    },
    {
        "name": "ENTROPIA",
        "date": 1670788800,
        "normalDate": "11 December 2022"
    },
    {
        "name": "UN VERANO SIN TI",
        "date": 1677603600,
        "normalDate": "28 February 2023"
    }
]

for object in MockObj:
    tree.insert(object)


def test_insert():
    node = {"name": "CHRTISTMAS FEST",
            "date": 1672074000, "normalDate": "26 December 2022"}
    assert tree.insert(node) == True


def test_find():
    node = tree.find(1672074000)
    assert 1672074000 == node['date']


def test_delete():
    date = 1672074000
    assert tree.delete(date) == True
