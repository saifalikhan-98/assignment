import typing

import strawberry


@strawberry.type
class EngagementType:
    account_id:str
    likes:int
    comments:int
    shares:int
    date_time:str


@strawberry.type
class accountType:
    _id:str
    account_name:str
    account_id:str
    active:bool
    #engagements:typing.List["EngagementType"]

