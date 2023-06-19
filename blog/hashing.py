from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)


    def verify(hashed_passowrd, normal_password ):
        return pwd_cxt.verify(normal_password, hashed_passowrd)