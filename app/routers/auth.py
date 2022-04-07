from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2

router = APIRouter(
  tags=['Authentication']
  )

@router.post("/login", response_model=schemas.Token) # log into user (POST)
def login(
  user_credentials: OAuth2PasswordRequestForm = Depends(),
  db: Session = Depends(database.get_db)
  ):
  # create user, send response
  user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
  # if email [x]
  if not user:
    raise HTTPException(status_code=403, detail=f"Invalid Credentials")
  #if hash passwords !==
  if not utils.verify(user_credentials.password, user.password):
    raise HTTPException(status_code=403, detail=f"Invalid Credentials")

  access_token = oauth2.create_access_token(data = {"user_id": user.id})
  # if login √ :> create token :> return token
  return {"access_token": access_token, "token_type": "bearer"}