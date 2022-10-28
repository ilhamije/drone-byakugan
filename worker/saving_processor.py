import json
from sqlalchemy import create_engine
from sqlalchemy.sql import text


dbname = 'instance/test.db'
engine = create_engine('sqlite:///' + dbname)
# hey = engine.execute(text("SELECT * from point"))
# print(hey)


conn = engine.connect()
trans = conn.begin()

point_data = open('parsedjsontest/2022-10-27.json', mode='r', encoding='utf-8')
data = json.load(point_data)

for data_dict in data:
    for key, val in data_dict.items():
        print(key, val, type(val))
        IMG_NAME = key
        LAT_VAL = val.get('latitude')
        LON_VAL = val.get('longitude')
        sql_script = f"INSERT INTO point (image_name, latitude_off, longitude_off) VALUES ('{IMG_NAME}', '{LAT_VAL}', '{LON_VAL}')"

        print(sql_script)
        conn.execute(sql_script)


trans.commit()

# trans.rollback()

conn.close()

results = engine.execute("SELECT * FROM point")
print(results.fetchall())
