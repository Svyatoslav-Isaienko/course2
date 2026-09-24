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
    # already expired 1 minute ago
    'exp': datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=1),
}

token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print('Token created (already expired):')
print(token)
print()

try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    print('Decoded payload:')
    print(decoded)
except jwt.ExpiredSignatureError as error:
    print(f'Decoding FAILED as expected: {type(error).__name__}: {error}')
