from typing import Any, Union
from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry import BasePermission
from strawberry.types import Info
from user_app.services.auth_service import AuthService


"""
This class represents jwt authorization
"""

class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    async def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        try:
            request: Union[Request, WebSocket] = info.context["request"]
            if "Authorization" in request.headers:
                result,user = AuthService().decode_token(request.headers['Authorization'].replace('Bearer',''))
                return result
            return False
        except Exception:
            return False