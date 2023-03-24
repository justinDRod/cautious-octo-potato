from app.main import root
def test_root(): 
    print(root())
    assert root() == {"message": "Hello, Alex!!!"}
