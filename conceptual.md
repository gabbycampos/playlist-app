### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  - is an open source Retaltional Database Management System (RDBMS) that follows the SQL standard. It allows us to interact with our database, it starts a server that connects to the database.

- What is the difference between SQL and PostgreSQL?
  - Postgres in an advanced version of SQL. It provides support to functions like foreign keys and subqueries.

- In `psql`, how do you connect to a database?
  - \c 'database name'

- What is the difference between `HAVING` and `WHERE`?
  - 'HAVING' is used to filter the returned results from a 'GROUP BY' clause. GROUP BY/HAVING are used with an aggregate function(functions used to combine multiple rows like COUNT, AVG)
  - 'WHERE' filters which rows get included. It is similar to a conditional statement.

- What is the difference between an `INNER` and `OUTER` join?
  - 'INNER' joins only the rows that match the condition in both tables.
  - 'OUTER' can join rows in one table with no match in another table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  - If you specify 'left or right' it will join all the rows from the selected direction combined with matching rows from the second table. A full join will select all rows.

- What is an ORM? What do they do?
  - Object Relational Mapper. SQLAlchemy is an ORM and it's used to write python code that executes in a Postgres database. Object-relational-mappers are tools used to create and manipulate models of database tables through a programming language like Python.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  - With client-side requests you don't have to involve Flask in the API, can be faster. A server-side requests can be easier for server to store/process the data. Some websites will not allow browser requests so a server requests can handle it. 

- What is CSRF? What is the purpose of the CSRF token?
  - Cross Site Request Forgery is a security vulnerablity. A form on any site can submit to any other site. The purpose of the CSRF token is to prevent that from happening. It gurantees that the form came from our server.

- What is the purpose of `form.hidden_tag()`?
  - it adds the CSRF hidden field to the form.