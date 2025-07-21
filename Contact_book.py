import sqlite3


conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()


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
            
            
def search_contact(name_query):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name_query + '%',))
    results = cursor.fetchall()
    conn.close()
    
    if results:
        print("--- Search Results ---")
        for contact in results:
            print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]} | Email: {contact[3]}")   
    else:
        print(f"No contacts found with this name {name_query}")   
          
    
def update_contact():
    view_contacts()
    try:
        contact_id = int(input("Enter the ID of the contact you want to update: "))
        new_name = input("Enter new name (leave empty to keep current): ")
        new_phone = input("Enter new phone number (leave empty to keep current): ")
        new_email = input("Enter new email (leave empty to keep current): ")

        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()

        cursor.execute("SELECT name, phone, email FROM contacts WHERE id = ?", (contact_id,))
        result = cursor.fetchone()

        if result:
            current_name, current_phone, current_email = result

            updated_name = new_name if new_name else current_name
            updated_phone = new_phone if new_phone else current_phone
            updated_email = new_email if new_email else current_email

            cursor.execute('''
                UPDATE contacts
                SET name = ?, phone = ?, email = ?
                WHERE id = ?
            ''', (updated_name, updated_phone, updated_email, contact_id))

            conn.commit()
            print("✅ Contact updated successfully.")
        else:
            print("❌ Contact not found.")

        conn.close()

    except ValueError:
        print("Invalid input. Please enter a valid number for ID.")



def delete_contact(contact_id):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id))
    conn.commit()
    conn.close()
    
    print("Contact deleted successfully❕")
  
# name = input("Enter Your Name: ")
# phone = input("Enter Your Phone: ")
# email = input("Enter Your Email: ")

# add_contact(name, phone, email)
# search = input("Search name: ")
# search_contact(search)



