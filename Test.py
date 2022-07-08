import pytest
from Cell import Cell
from User import User

@pytest.fixture
def cell():
    cell = Cell("purpose","leader","21/06/2022")
    return cell

@pytest.fixture
def user(cell):
    user = User("CC","12345","Santiago", "Martinez", cell)
    return user

def test_get_purpose_of_cell(cell):
    purpose = cell.get_purpose()
    assert "purpose" == purpose

def test_set_purpose_of_cell(cell):
    cell.set_purpose("desarrollo")
    assert "desarrollo" == cell.get_purpose()

def test_get_leader_of_cell(cell):
    leader = cell.get_leader()
    assert "leader" == leader

def test_set_leader_of_cell(cell):
    cell.set_leader("Andres")
    assert "Andres" == cell.get_leader()

def test_get_document_type_of_user(user):
    document_type = user.get_document_type()
    assert "CC" == document_type

def test_set_document_type_of_user(user):
    user.set_document_type("TI")
    assert "TI" == user.get_document_type()
    
def test_get_document_number_of_user(user):
    document_number = user.get_document_number()
    assert "12345" == document_number

def test_set_document_number_of_user(user):
    user.set_document_number("123456")
    assert "123456" == user.get_document_number()

