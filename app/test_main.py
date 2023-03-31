from app.main import root
def test_root(): 
    print(root())
    assert root() == {"message": "Hello, smith!!!"}

def test_alex():
    print(alex())
    assert alex() == {"message": "Hello, Alex"}
