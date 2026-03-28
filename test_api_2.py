from requests import get, post, delete
print(get('http://localhost:8080/api/v2/user').json())
print(get('http://localhost:8080/api/v2/user/1').json())
print(get('http://localhost:8080/api/v2/user/1000').json())
print(get('http://localhost:8080/api/v2/user/e').json())
# print(delete('http://localhost:8080/api/v2/user/1').json())
print(delete('http://localhost:8080/api/v2/user/1000').json())
print(post('http://localhost:8080/api/v2/user', json={}).json())
print(post('http://localhost:8080/api/v2/user', json={'name': 'вася'}).json())
print(post('http://localhost:8080/api/v2/user', json={'name': 'вася',
                                                      'surname': 'Роналдо',
                                                      'age': '42',
                                                      'speciality': '42',
                                                      'position': 'position',
                                                      'address': '42',
                                                      'email': '42@gmail.ZOV',
                                                      'hashed_password': '1488'
                                                      }).json())
print(get('http://localhost:8080/api/v2/user/6').json())