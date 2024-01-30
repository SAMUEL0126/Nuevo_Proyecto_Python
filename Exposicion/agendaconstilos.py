import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class AgendaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agenda")
        self.setGeometry(100, 100, 300, 200)

        self.name_label = QLabel("Nombre:")
        self.name_input = QLineEdit()
        self.phone_label = QLabel("Teléfono:")
        self.phone_input = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.add_button = QPushButton("Agregar")
        self.remove_button = QPushButton("Eliminar")
        self.edit_button = QPushButton("Editar")
        self.display_button = QPushButton("Mostrar")

        self.add_button.clicked.connect(self.add_contact)
        self.remove_button.clicked.connect(self.remove_contact)
        self.edit_button.clicked.connect(self.edit_contact)
        self.display_button.clicked.connect(self.display_contacts)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.display_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.agenda = []

    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        contact = Contact(name, phone, email)
        if len(self.agenda) < 5:
            self.agenda.append(contact)
            QMessageBox.information(self, "Éxito", "Contacto agregado exitosamente.")
            self.name_input.clear()
            self.phone_input.clear()
            self.email_input.clear()
        else:
            QMessageBox.warning(self, "Error", "La agenda está llena. No se puede agregar más contactos.")

    def remove_contact(self):
        name = self.name_input.text()
        for contact in self.agenda:
            if contact.name == name:
                self.agenda.remove(contact)
                QMessageBox.information(self, "Éxito", "Contacto eliminado exitosamente.")
                return
        QMessageBox.warning(self, "Error", "No se encontró ningún contacto con ese nombre.")

    def edit_contact(self):
        name = self.name_input.text()
        new_phone = self.phone_input.text()
        new_email = self.email_input.text()
        for contact in self.agenda:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                QMessageBox.information(self, "Éxito", "Contacto editado exitosamente.")
                return
        QMessageBox.warning(self, "Error", "No se encontró ningún contacto con ese nombre.")

    def display_contacts(self):
        if len(self.agenda) == 0:
            QMessageBox.information(self, "Agenda", "La agenda está vacía.")
        else:
            message = "Contactos en la agenda:\n"
            for contact in self.agenda:
                message += f"Nombre: {contact.name}, Teléfono: {contact.phone}, Email: {contact.email}\n"
            QMessageBox.information(self, "Agenda", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgendaWindow()
    window.setStyleSheet("QMainWindow { background-color: #F5F5F5; }"
                         "QLabel { font-size: 18px; margin-bottom: 10px; }"
                         "QLineEdit { font-size: 16px; padding: 5px; margin-bottom: 10px; }"
                         "QPushButton { font-size: 16px; padding: 10px; background-color: #4CAF50; color: white; border: none; }"
                         "QPushButton:hover { background-color: #45a049; }"
                         "QPushButton:pressed { background-color: #367c39; }")
    window.show()
    sys.exit(app.exec_())
