import datetime
import uuid

import jwt

CORRECT_SECRET_KEY = 'my-super-secret-key-for-jwt-homework-2026'
WRONG_SECRET_KEY = 'a-completely-different-key'
ALGORITHM = 'HS256'

payload = {
    'last_name': 'Isaienko',
    'first_name': 'Sviatoslav',
    'group': 'group20260825',
    'sub': str(uuid.uuid4()),
    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5),
}

# token is signed with the correct key
token = jwt.encode(payload, CORRECT_SECRET_KEY, algorithm=ALGORITHM)
print('Token created (signed with the correct key):')
print(token)
print()

# but we try to decode it using a different (wrong) key
try:
    decoded = jwt.decode(token, WRONG_SECRET_KEY, algorithms=[ALGORITHM])
    print('Decoded payload:')
    print(decoded)
except jwt.InvalidSignatureError as error:
    print(f'Decoding FAILED as expected: {type(error).__name__}: {error}')
