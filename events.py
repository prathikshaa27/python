import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="events_database"
        )
        print("Connected to the database")
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)

# Function to add an event to the database
def add_event(connection, event_name, event_date):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO events (name, date) VALUES (%s, %s)"
        cursor.execute(sql, (event_name, event_date))
        connection.commit()
        print("Event added successfully")
    except mysql.connector.Error as err:
        print("Error:", err)

# Function to delete an event from the database
def delete_event(connection, event_id):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM events WHERE id = %s"
        cursor.execute(sql, (event_id,))
        connection.commit()
        print("Event deleted successfully")
    except mysql.connector.Error as err:
        print("Error:", err)

# Main function to run the program
def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\n1. Add Event")
            print("2. Delete Event")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                event_name = input("Enter event name: ")
                event_date = input("Enter event date (YYYY-MM-DD): ")
                add_event(connection, event_name, event_date)
            elif choice == '2':
                event_id = input("Enter event ID to delete: ")
                delete_event(connection, event_id)
            elif choice == '3':
                print("Exiting program...")
                break
            else:
                print("Invalid choice, please try again")

        connection.close()

if __name__ == "__main__":
    main()
