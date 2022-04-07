# utility functions

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
  return pwd_context.hash(password)

# creates has of password input & verifies w/ db hash
def verify(plain_password, hash_password):
  return pwd_context.verify(plain_password, hash_password)