import sqlite3

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create the contacts table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT
)
""")

# Save and close
conn.commit()
conn.close()

print("Database setup complete.")


def add_contact(name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()
    print("Contact added successfully❕")
    
    
def view_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    
    if contacts:
        print("---- Contact list ---")
        for contact in contacts:
            print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]} | Email: {contact[3]}")
        else:
            print("No contacts found")
    
    
name = input("Enter Your Name: ")
phone = input("Enter Your Phone: ")
email = input("Enter Your Email: ")

add_contact(name, phone, email)

view_contacts()