from os import getenv

user = getenv("HBNB_MYSQL_USER")
pwd = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
db = getenv("HBNB_MYSQL_DB")

print(f"HBNB_MYSQL_USER: {user}")
print(f"HBNB_MYSQL_PWD: {pwd}")
print(f"HBNB_MYSQL_HOST: {host}")
print(f"HBNB_MYSQL_DB: {db}")
