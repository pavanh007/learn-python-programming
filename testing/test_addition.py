import addition
import pytest

#NOTE : 
# test command : python3 -m pytest test_addition.py
# test command : py.test test_file.py
# spcific funcion : @pytest.fixture
# test for specific function : python3 -m pytest test_addition.py::test_sub

def test_sub():
  assert addition.sub(4, 5) == -1
  # pass

def test_add():
  assert addition.add(4, 5) == 9
  assert addition.add(5, 5) == 10
  # assert False
  




