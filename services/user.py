import logging

import psycopg2

from endpoints.create_object import CreateObject
from test_data.data import Data

logger = logging.getLogger(__name__)

def delete_user(email):
    try:
        with psycopg2.connect(**Data.db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT id FROM users WHERE email='{email}';")
                id_user = cursor.fetchone()[0]
                cursor.execute(f"DELETE FROM user_roles WHERE user_id='{id_user}';")
                cursor.execute(f"DELETE FROM users WHERE id='{id_user}';")
                conn.commit()
    except Exception as e:
        logger.info('Can`t establish connection to database')



