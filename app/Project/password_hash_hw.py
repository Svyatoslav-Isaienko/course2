from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'], deprecated='auto')

password = 'vyihreu18byh1gu_e1hu'
hash = context.hash(password)
print(hash)

print(context.verify(password, hash))