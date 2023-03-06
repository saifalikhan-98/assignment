import os

from dotenv import load_dotenv

load_dotenv()
APP_PORT = os.getenv('DB_PORT')

class PostgresConfiguration:
    POSTGRES_DB_PORT = os.getenv('DB_PORT')
    POSTGRES_DB_NAME = os.getenv('DB_NAME')
    POSTGRES_DB_USER = os.getenv('DB_USER')
    POSTGRES_DB_PASSWORD = os.getenv('DB_PASS')
    POSTGRES_DB_HOST = os.getenv('DB_HOST')

    @property
    def postgres_db_path(self):
        print(f'postgres://{self.POSTGRES_DB_USER}:{self.POSTGRES_DB_PASSWORD}@' \
               f'{self.POSTGRES_DB_HOST}:' \
               f'{self.POSTGRES_DB_PORT}/{self.POSTGRES_DB_NAME}')
        return f'postgresql://{self.POSTGRES_DB_USER}:{self.POSTGRES_DB_PASSWORD}@' \
               f'{self.POSTGRES_DB_HOST}:' \
               f'{self.POSTGRES_DB_PORT}/{self.POSTGRES_DB_NAME}'
