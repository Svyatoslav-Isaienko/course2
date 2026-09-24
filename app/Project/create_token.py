import uuid

import jwt

SECRET_KEY = 'my-super-secret-key-for-jwt-homework-2026'
ALGORITHM = 'HS256'

payload = {
    'last_name': 'Isaienko',
    'first_name': 'Sviatoslav',
    'group': 'group20260825',
    'sub': str(uuid.uuid4()),
}

token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

print('Payload:')
print(payload)
print()
print('JWT token:')
print(token)