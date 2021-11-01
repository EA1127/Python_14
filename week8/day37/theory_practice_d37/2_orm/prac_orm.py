# import psycopg2

# connection = psycopg2.connect(
#     database='db_practice',
#     user='hello',
#     password='1',
#     host='localhost',
#     port='5432'
# )                         # \c db_practice

# print('Database successfully opened')


# cursor = connection.cursor()
# cursor.execute(
#     '''CREATE TABLE company(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100) NOT NULL,
#         city  VARCHAR(50) NOT NULL
#     )
#     '''
# )
# print('Table successfully created')
# connection.commit()
# connection.close()


# cursor = connection.cursor()
# cursor.execute(
#     '''INSERT INTO company(name, city) VALUES ('IBM', 'Los Angeles'),
#     ('Apple', 'Cupertino'), ('HP', 'New York'), ('Dell', 'New Jersey')
#     '''
# )
# connection.commit()
# print('Inserted successfully')
# connection.close()


# cursor = connection.cursor()
# cursor.execute(
#     '''INSERT INTO company(name, city) VALUES ('Samsung', 'Seoul')
#     '''
# )
# cursor.execute(
#     '''INSERT INTO company(name, city) VALUES ('Toyota', 'Tokyo')
#     '''
# )
# connection.commit()
# print('Inserted successfully')
# connection.close()


# cursor = connection.cursor()
# cursor.execute(
#     '''SELECT * FROM company'''
# )
# # print(cursor.fetchall())
# data = cursor.fetchall()
# for item in data:
#     # print(f"id: {item[0]}, name: {item[1]}, city: {item[2]}")
#     print(*item)
# connection.close()


# cursor = connection.cursor()
# cursor.execute(
#     '''SELECT name, city FROM company WHERE id=2'''
# )
# data = cursor.fetchone()
# print(data)


# cursor = connection.cursor()
# # cursor.execute(
# #     '''UPDATE company SET city='New Mexico' WHERE id=2'''
# # )
# # connection.commit()
# cursor.execute(
#     '''SELECT * FROM company ORDER BY id'''
# )
# data = cursor.fetchall()
# for item in data:
#     print(*item)
# connection.close()


# cursor = connection.cursor()
# cursor.execute(
#     '''DELETE FROM company WHERE id=3'''
# )
# connection.commit()
# print(f"Total count of deleted: {cursor.rowcount}")
# cursor.execute(
#     '''SELECT * FROM company ORDER BY id'''
# )
# data = cursor.fetchall()
# for item in data:
#     print(*item)
# connection.close()

# ===============================================================================================================
# ORM SQLAlchemy

# from sqlalchemy import create_engine, engine

# engine = create_engine('postgresql+psycopg2://hello:1@localhost:5432/db_practice')   # \c db_practice

# print('Database connected')

# from sqlalchemy import Column, Table, Integer, String, MetaData

# metadata = MetaData()
# students_table = Table(
#     'students', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('last_name', String)
# )
# students_table.create(bind=engine)
# print('Successfully created table')

# inserted_data = students_table.insert().values(name='John', last_name='Snow')
# engine.execute(inserted_data)
# print('Successfully inserted')

# inserted_data = students_table.insert().values(name='Alice', last_name='White')
# engine.execute(inserted_data)
# print('Successfully inserted')


# from sqlalchemy import select
# query = select([students_table.c.name, students_table.c.last_name])
# name, last_name = engine.execute(query).fetchone()
# print(name, last_name)

# query = select([students_table.c.name, students_table.c.last_name])
# data = engine.execute(query).fetchall()
# # print(data)
# for item in data:
#     print(*item)


# from sqlalchemy import create_engine, engine

# engine = create_engine('postgresql+psycopg2://hello:1@localhost:5432/db_practice')

# from sqlalchemy import Column, Table, Integer, String, MetaData

# metadata = MetaData()
# company_table = Table(
#     'company', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('city', String)
# )
# metadata.create_all(engine)
# class Company:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

#     def __str__(self):
#         return f'Company {self.name} in {self.city} city'

# from sqlalchemy.orm import mapper
# mapper(Company, company_table)
# print('Successfully created table')


#------------------------------------------------------------------------------------------------------------------

# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import session, sessionmaker

# engine = create_engine('postgresql+psycopg2://hello:1@localhost:5432/db_practice')

# Base = declarative_base()

# class Company2(Base):
#     __tablename__ = 'company2'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     city = Column(String)

#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

#     def __str__(self):
#         return f'Company {self.name} in {self.city} city'

# # Base.metadata.create_all(engine)
# # print('Table created')

# Session = sessionmaker(bind=engine)
# session = Session()

# apple = Company2(name="Apple", city="Cupertino")
# # session.add(apple)
# # session.commit()
# # query = session.query(Company2.name, Company2.city).all()  # -> fetchall()
# # print(query)

# samsung = Company2('Samsung', 'Seoul')
# # session.add(samsung)
# # session.commit()
# # query = session.query(Company2.name, Company2.city).all()
# # print(query)
# # query = session.query(Company2.name, Company2.city).first()
# # print(query)

# # our_company = session.query(Company2).filter_by(city='Seoul').first()
# #           SELECT * FROM company WHERE city='Seoul'
# # print(our_company)

# # session.add_all([Company2('IBM', 'Washington'),Company2('Dell', 'New York')])
# # session.commit()

# # query = session.query(Company2.name, Company2.city).all()
# # for item in query:
# #     print(*item)
# # # print(query)

# # query = session.query(Company2.name, Company2.city).first()
# # print(*query)

# query = session.query(Company2.name, Company2.city).order_by('id').all()
# #       SELECT name, city FROM company ORDER BY id;
# for item in query:
#     print(*item)