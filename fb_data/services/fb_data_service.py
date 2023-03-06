from datetime import timezone, datetime
from typing import List


from fb_data.fb_schema import accountType, EngagementType
from sql_app.mongo_db_conf import MongoDbConf
from dateutil import parser as parser

class FbDataService:

    def get_all_users(self):
        db=MongoDbConf().connect()
        accounts = list(db.fb_accounts.find({"active": True}))
        return [accountType(**account) for account in accounts]

    def engagement_data(self, start_date:str, end_date:str):
        db = MongoDbConf().connect()
        result=list(db.fb_engagements.find({"date_time": {"$gte": start_date, "$lte": end_date}},{'_id':0}
        ).sort([("date_time", -1)]))

        daily_engagements = []
        for engagement in result:
            print(engagement)
            engagement_date = parser.parse(engagement["date_time"])
            date_key = engagement_date.strftime("%Y-%m-%d")
            if date_key not in daily_engagements:
                daily_engagements.append({

                    "account_id":engagement['account_id'],
                    "likes": engagement["likes"],
                    "shares": engagement["shares"],
                    "comments": engagement["comments"],
                    "date_time":engagement['date_time']
                })
        return [EngagementType(**r) for r in daily_engagements]
