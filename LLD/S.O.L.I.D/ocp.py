"""
The Open/Closed Principle (OCP) is another SOLID principle of object-oriented design. 
It states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. 
This means you should be able to add new functionality without changing existing code.

Problem Statement:
We have a UserDAO class that handles saving user data to a database. 
Initially, it only supports saving to a MySQL database. Later, we want to add support for saving to a PostgreSQL database 
without modifying the existing UserDAO class.

Solution:
We will design the UserDAO class to adhere to the Open/Closed Principle by using abstraction (e.g., an interface or base class) 
so that new database implementations can be added without modifying the existing code.
"""

from abc import ABC, abstractmethod

# Abstract base class for database operations
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


# MySQL implementation of the Database interface
class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL database...")


# PostgreSQL implementation of the Database interface
class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to PostgreSQL database...")


# UserDAO class: Depends on the Database abstraction
class UserDAO:
    def __init__(self, database: Database):
        self.database = database

    def save_user(self, user_data):
        self.database.save(user_data)


# Example usage
if __name__ == "__main__":
    # Create a MySQL database instance
    mysql_db = MySQLDatabase()

    # Create a UserDAO with MySQL database
    user_dao_mysql = UserDAO(mysql_db)
    user_dao_mysql.save_user({"name": "Alice", "email": "alice@example.com"})

    # Create a PostgreSQL database instance
    postgresql_db = PostgreSQLDatabase()

    # Create a UserDAO with PostgreSQL database
    user_dao_postgresql = UserDAO(postgresql_db)
    user_dao_postgresql.save_user({"name": "Bob", "email": "bob@example.com"})