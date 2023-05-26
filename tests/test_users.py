from fastapi.testclient import TestClient
from app.main import app
from app import schema
# from .testdatabase import client,session
import pytest
from jose import jwt
from app.config import settings



# client=TestClient(app)

# def test_root(client):
#     res = client.get("/")
#     print(res.status_code)
#     print(res.json())
#     print(res.json().get('message'))
#     assert res.json().get('message') == 'Hello Ganesh'
#     assert res.status_code == 200


# def test_create_user(client):
#     res = client.post("/users/",json={"email":"jammu123@gmail.com","password":"password123"})
#     new_user = schema.UserOut(**res.json())
#     assert new_user.email == "jammu123@gmail.com"
#     assert res.status_code == 201

def test_login(test_user,client):
    res = client.post("/login",data={"username":test_user['email'],"password":test_user['password']})
    login_res = schema.Token(**res.json())
    payload = jwt.decode(login_res.access_token,settings.secret_key,algorithms=[settings.algorithm])    
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "Bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email,password,status_code",[
    ('wrongpassword@gmail.com','password123',403),
    ('ganesh@gmail.com','wrongpassword123',403),
    (None,'password123',422),
    ('wrongpassword@gmail.com',None,422),
])

def test_incorrect_login(test_user,client,email,password,status_code):
    res = client.post("/login",data= {"username":email,"password":password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'INVALID Credentials'