import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="WebSecurity"
)

# Function to search the database
def search_threats(search_term):
    cursor = db.cursor(dictionary=True)
    query = """
    SELECT * FROM Threats
    WHERE title LIKE %s OR description LIKE %s OR category LIKE %s
    """
    cursor.execute(query, ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
    results = cursor.fetchall()
    cursor.close()
    return results

search_threats("example")

# Close the database connection
db.close()
