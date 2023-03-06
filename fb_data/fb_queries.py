from typing import List

import strawberry

from auth_middleware import IsAuthenticated
from fb_data.fb_schema import accountType, EngagementType
from fb_data.services.fb_data_service import FbDataService


@strawberry.type
class FB_Queries:
    active_accounts: List[accountType] = strawberry.field(FbDataService.get_all_users,
                                                          permission_classes=[IsAuthenticated])
    engagements: List[EngagementType] = strawberry.field(resolver=FbDataService.engagement_data,
                                                         permission_classes=[IsAuthenticated])
