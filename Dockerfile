# Use the official MySQL image as a base
FROM mysql:8.4.2

# Set environment variable for MySQL root password
ENV MYSQL_ROOT_PASSWORD=123456

# Copy the SQL script to the Docker container
COPY superstore_test.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port
EXPOSE 3306