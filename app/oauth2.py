from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

# login endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# SECRET_KEY
# Algorithm
# Expiration Time (w/o expiration, user can login forever)

# $ openssl rand -hex 32  (generates Hash pw)
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

# create Access Token - copying data inside of `Payload`
def create_access_token(data: dict):
  to_encode = data.copy()
   
  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})

  #send copy expiry data (payload) + other 2 parts into JWT for security
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

  return encoded_jwt


def verify_access_token(token: str, credentials_exception):
  
  try:
    # verify token 3 part data
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #  get the data array name that was used to create the token
    id: str = payload.get("user_id")
    if id is None:  
      raise credentials_exception
    token_data = schemas.TokenData(id=id)
  except JWTError:
    raise credentials_exception
  return token_data

# fetches user from the database (login endpoint)
def get_current_user(
  token: str = Depends(oauth2_scheme),
  db: Session = Depends(database.get_db)
  ):
  credentials_exception = HTTPException(
    status_code=401,
    detail=f"Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"}
    )

  token = verify_access_token(token, credentials_exception)

  user = db.query(models.User).filter(models.User.id == token.id).first()

  return user