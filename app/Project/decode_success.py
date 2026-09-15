import datetime
import uuid

import jwt

SECRET_KEY = 'my-super-secret-key-for-jwt-homework-2026'
ALGORITHM = 'HS256'

payload = {
    'last_name': 'Isaienko',
    'first_name': 'Sviatoslav',
    'group': 'group20260825',
    'sub': str(uuid.uuid4()),
    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5),
}

token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print('Token created:')
print(token)
print()

decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print('Successfully decoded payload:')
print(decoded)
