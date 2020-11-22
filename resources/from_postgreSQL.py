import itertools
import os
import sqlalchemy
import psycopg2


def execute(cmd):
    with psycopg2.connect(user='postgres', database='kw_db', host=os.environ['KW_DB_HOST']) as conn:
        with conn.cursor() as cur:
            cur.execute(cmd)


def fetch(cmd):
    with psycopg2.connect(user='postgres', database='kw_db', host=os.environ['KW_DB_HOST']) as conn:
        with conn.cursor() as cur:
            cur.execute(cmd)
            result = cur.fetchall()
            if len(result) > 0 and len(result[0]) == 1:
                return list(itertools.chain.from_iterable(result))
            else:
                return result


def insert(df, table_name):
    engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres@/kw_db', host=os.environ['KW_DB_HOST'])
    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists='append', method='multi', chunksize=5000, index=False)


def join_params_for_where(predicates, delim='OR'):
    res = ''
    for pred in predicates:
        res += f'{pred} {delim} '

    res = res.rsplit(delim, 1)[0]
    return res


if __name__ == '__main__':
    print(fetch('SELECT 1'))