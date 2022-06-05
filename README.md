# Capstone

## Database

This project will use a PostgreSQL database to store the data from the datasets chosen for the project. The database has been designed and loaded with the cleaned datasets. Python code is also included to collect the latitude and longitude coordinates for each country in the datasets and store this information in a regions table. A join has been written to combine the region details with each row of the coffee data to allow for providing maps of coffee-growing regions in the dashboard.

![Database ERD](https://github.com/jkannis/Capstone/blob/database/CoffeeDB_ERD.png)

[Database Schema](https://github.com/jkannis/Capstone/blob/database/CoffeeDB_Schema.sql)