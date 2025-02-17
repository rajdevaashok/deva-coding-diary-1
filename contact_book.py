# Simple Contact Book
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact added: {name} - {phone}")

add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
print("Contacts:", contacts)
git add .
git commit -m "Added a simple contact book script"
git push origin main
