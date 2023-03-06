import strawberry

@strawberry.type
class UserType:
    email:str
    lastLogin:str
    accessToken:str
    refreshToken:str


@strawberry.input
class UserInput:
    email:str
    password:str

