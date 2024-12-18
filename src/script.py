import os

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

def connect_to_database(username, password):
    print(f"Connecting to database with username: {username} and password: {password}")

connect_to_database(username, password)