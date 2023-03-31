from app.main import root
from app.main import alex
def test_root(): 
    print(root())
    assert root() == {"message": "Hello, smith!!!"}

def test_alex():
    print(alex())
    assert alex() == {"message": "Hello, Alex"}
