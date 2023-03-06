"""
we are using JWT tokens to authorize user and protect our API routes

"""
import os
from jose import jwt # used for encoding and decoding jwt tokens
from fastapi import HTTPException # used to handle error handling
from passlib.context import CryptContext # used for hashing the password
from datetime import datetime, timedelta # used to handle expiry time for tokens
from dotenv import load_dotenv

load_dotenv()

class AuthService:


    def __init__(self):
        self.__JWT_SECRET=os.environ.get('SECRET_KEY')
        self.__JWT_ALGO=os.environ.get('ALGORITHM')

    hasher = CryptContext(schemes=['bcrypt'])
    secret = os.getenv("SECRET_KEY")
    print('secret',secret)
    def encode_password(self, password):
        return self.hasher.hash(password)

    def verify_password(self, password, encoded_password):
        return self.hasher.verify(password, encoded_password)

    def encode_token(self, username):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=30),
            'iat': datetime.utcnow().timestamp(),
            'scope': 'access_token',
            'sub': username
        }
        print(self.secret)
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def decode_token(self, token):
        try:
            print(self.secret,'\n', token)
            payload = jwt.decode(token,self.secret, algorithms=['HS256'])
            print('result', payload)
            if (payload['scope'] == 'access_token'):
                return True,payload['sub']
            raise HTTPException(status_code=401, detail='Scope for the token is invalid')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except Exception:
            raise HTTPException(status_code=401, detail='Invalid token')

    def encode_refresh_token(self, username):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, hours=10),
            'iat': datetime.utcnow(),
            'scope': 'refresh_token',
            'sub': username
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def refresh_token(self, refresh_token):
        try:
            payload = jwt.decode(refresh_token, self.secret, algorithms=['HS256'])
            if (payload['scope'] == 'refresh_token'):
                username = payload['sub']
                new_token = self.encode_token(username)
                return new_token
            raise HTTPException(status_code=401, detail='Invalid scope for token')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Refresh token expired')
        except Exception:
            raise HTTPException(status_code=401, detail='Invalid token')