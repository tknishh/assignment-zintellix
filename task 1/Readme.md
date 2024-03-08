# Task 1 - SQL Query

Given the following tables:
- `users` (user_id, name, email)
- `orders` (order_id, user_id, order_date, total_amount)
Write an SQL query to retrieve the names of users who have placed orders in the last 30 days,
along with the total number of orders each user has placed.

# Solution 

The query should return the following columns:
- `name` (the name of the user)
- `order_count` (the total number of orders placed by the user in the last 30 days)

# Files

- `query.sql` (contains the SQL query and final submission for the task)
- `query.ipynb` (gives a the result the query will generate)
- `test.db` (created a test database to test the query and populated it using database.py file)
- `database.py` (contains the code to create the test database and populate it with data)
- `Readme.md` (contains the description of the task and the solution)