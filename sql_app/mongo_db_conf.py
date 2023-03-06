import os

import pymongo
from dateutil import parser as parser
from dotenv import load_dotenv

load_dotenv()
class MongoDbConf:

    def connect(self):
        mongo_url=os.environ.get('MONGO_DB')
        client = pymongo.MongoClient(mongo_url)
        db = client["sponsorlytix_db"]
        self.__seed_data_once(db)
        return db

    def __seed_data_once(self,db):
        update_once=db['seed_data']
        is_updated=update_once.find_one({"updated":True})
        if is_updated:
            print('data seed done already')
        else:
            update_once.insert_one({'updated':True})
            self.seed_accounts(db)
            self.__seed_engagement_data(db)

    def seed_accounts(self,db):
        fb_accounts = db["fb_accounts"]

        # seed data
        accounts_data = [
            {"account_name": "Sam", "account_id": "00001", "active":True},
            {"account_name": "Tom", "account_id": "0002", "active":False},
            {"account_name": "Rock", "account_id": "0003", "active":True},
        ]

        # insert data into collection
        for i in accounts_data:
            account = fb_accounts.find_one({"account_id": i['account_id']})

            if account:
                print("Account already exists")
            else:
                # add account
                fb_accounts.update_one(
                    {"account_id":  i['account_id']},
                    {"$set": {"account_name": i['account_name'],'active':i['active']}},
                    upsert=True
                )


    def __seed_engagement_data(self,db):
        fb_engagement=db['fb_engagements']
        engagements_data = [
            {"account_id": "00001", "date_time": parser.parse("2023-02-28T12:00:00Z").isoformat(), "likes": 10, "shares": 5, "comments": 2},
            {"account_id": "00001", "date_time": parser.parse("2023-02-28T00:00:00Z").isoformat(), "likes": 5, "shares": 2, "comments": 1},
            {"account_id": "00001", "date_time": parser.parse("2023-02-27T12:00:00Z").isoformat(), "likes": 15, "shares": 10, "comments": 3},
            {"account_id": "0002", "date_time": parser.parse("2023-02-27T00:00:00Z").isoformat(), "likes": 8, "shares": 3, "comments": 2},
            {"account_id": "0002", "date_time": parser.parse("2023-02-28T12:00:00Z").isoformat(), "likes": 20, "shares": 15, "comments": 7},
            {"account_id": "0002", "date_time": parser.parse("2023-02-28T00:00:00Z").isoformat(), "likes": 12, "shares": 8, "comments": 4},
            {"account_id": "0003", "date_time": parser.parse("2023-02-27T12:00:00Z").isoformat(), "likes": 18, "shares": 12, "comments": 6},
            {"account_id": "0003", "date_time": parser.parse("2023-02-27T00:00:00Z").isoformat(), "likes": 10, "shares": 5, "comments": 2},
        ]
        fb_engagement.insert_many(engagements_data)
