contacts = {}

try:
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    if name == "" or phone == "":
        raise ValueError("Fields cannot be empty")

    if name in contacts:
        raise Exception("Duplicate contact entry")

    if not phone.isdigit():
        raise ValueError("Wrong phone number format")

    contacts[name] = phone

    edit = input("Enter name to edit: ")
    if edit not in contacts:
        raise KeyError("Contact not found")

    new_phone = input("Enter new phone: ")
    if not new_phone.isdigit():
        raise ValueError("Wrong phone number format")

    contacts[edit] = new_phone

    search = input("Enter name to search: ")
    print("Phone:", contacts[search])

except ValueError as e:
    print("Input Error:", e)
except KeyError:
    print("Contact does not exist")
except Exception as e:
    print(e)