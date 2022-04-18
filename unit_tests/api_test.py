from app.main import getPost


def test_getPost():
  print("testing getPost/")
  assert getPost() == "Hello world!"
