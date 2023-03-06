import strawberry
from user_app.user_schema import UserType
from user_app.services.user_service import UserService

"""
This class has all the mutation services required for users apis
"""

@strawberry.type
class Mutation:
    add_user: UserType = strawberry.mutation(resolver=UserService.register_user)
    signin_user:UserType=strawberry.mutation(resolver=UserService.signin_user)