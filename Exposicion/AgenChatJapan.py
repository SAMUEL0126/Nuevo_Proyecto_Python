class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Agenda:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if len(self.contacts) < 5:
            self.contacts.append(contact)
            print("Contacto agregado exitosamente.")
        else:
            print("La agenda está llena. No se puede agregar más contactos.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contacto eliminado exitosamente.")
                return
        print("No se encontró ningún contacto con ese nombre.")

    def edit_contact(self, name, new_phone, new_email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                print("Contacto editado exitosamente.")
                return
        print("No se encontró ningún contacto con ese nombre.")

    def display_contacts(self):
        if len(self.contacts) == 0:
            print("La agenda está vacía.")
        else:
            print("Contactos en la agenda:")
            for contact in self.contacts:
                print(f"Nombre: {contact.name}, Teléfono: {contact.phone}, Email: {contact.email}")


agenda = Agenda()

while True:
    print("\n--- Agenda ---")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Editar contacto")
    print("4. Mostrar contactos")
    print("5. Salir")

    choice = input("Ingrese el número de la opción que desea ejecutar: ")

    if choice == "1":
        name = input("Ingrese el nombre del contacto: ")
        phone = input("Ingrese el número de teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        contact = Contact(name, phone, email)
        agenda.add_contact(contact)

    elif choice == "2":
        name = input("Ingrese el nombre del contacto que desea eliminar: ")
        agenda.remove_contact(name)

    elif choice == "3":
        name = input("Ingrese el nombre del contacto que desea editar: ")
        new_phone = input("Ingrese el nuevo número de teléfono del contacto: ")
        new_email = input("Ingrese el nuevo email del contacto: ")
        agenda.edit_contact(name, new_phone, new_email)

    elif choice == "4":
        agenda.display_contacts()

    elif choice == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")