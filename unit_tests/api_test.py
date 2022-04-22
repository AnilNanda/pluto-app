import pytest
from app.main import getPost, add
import pytest


@pytest.mark.parametrize("num1, num2, expectedResult",[
  (1,2,3),
  (12,3,15),
  (34,12,46)
])
def test_add(num1, num2, expectedResult):
  print("testing add function")
  assert add(num1, num2) == expectedResult



def test_getPost():
  print("testing getPost/")
  assert getPost() == "Hello world!"
