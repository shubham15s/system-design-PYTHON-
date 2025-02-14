"""
The Single Responsibility Principle (SRP) is one of the SOLID principles of object-oriented design. 
It states that a class should have only one reason to change, meaning it should have only one responsibility. 
This makes the code easier to maintain, test, and understand.

Explanation:
Marker Class: Represents a marker with attributes like name, color, and price. It has a single responsibility: to hold marker data.

Invoice Class: Responsible for calculating the total price of the markers. It does not handle printing or saving.

InvoicePrinter Class: Responsible for printing the invoice. It does not calculate the total or save the invoice.

InvoiceSaver Class: Responsible for saving the invoice to a file. It does not calculate the total or print the invoice.

Problem Statement:
We have a Marker class that represents a marker with attributes like name, color, and price. 
We also have an Invoice class that calculates the total price of the marker and prints the invoice.

If we violate SRP, the Invoice class might handle multiple responsibilities, such as calculating the total price, printing the invoice, 
and saving the invoice to a file. This makes the class harder to maintain.

"""


# Marker class: Represents a marker
class Marker:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price


# Invoice class: Responsible for calculating the total price
class Invoice:
    def __init__(self, marker, quantity):
        self.marker = marker
        self.quantity = quantity

    def calculate_total(self):
        return self.marker.price * self.quantity


# InvoicePrinter class: Responsible for printing the invoice
class InvoicePrinter:
    def __init__(self, invoice):
        self.invoice = invoice

    def print_invoice(self):
        total = self.invoice.calculate_total()
        print(f"Invoice for {self.invoice.marker.name} ({self.invoice.marker.color}):")
        print(f"Quantity: {self.invoice.quantity}")
        print(f"Total: ${total}")


# InvoiceSaver class: Responsible for saving the invoice to a file
class InvoiceSaver:
    def __init__(self, invoice):
        self.invoice = invoice

    def save_to_file(self, filename):
        total = self.invoice.calculate_total()
        with open(filename, "w") as file:
            file.write(
                f"Invoice for {self.invoice.marker.name} ({self.invoice.marker.color}):\n"
            )
            file.write(f"Quantity: {self.invoice.quantity}\n")
            file.write(f"Total: ${total}\n")


# Example usage
if __name__ == "__main__":
    # Create a marker
    marker = Marker(name="Sharpie", color="Red", price=5.0)

    # Create an invoice
    invoice = Invoice(marker, quantity=10)

    # Print the invoice
    printer = InvoicePrinter(invoice)
    printer.print_invoice()

    # Save the invoice to a file
    saver = InvoiceSaver(invoice)
    saver.save_to_file("invoice.txt")



"""
Without SRP (Violation):

class Invoice:
    def __init__(self, marker, quantity):
        self.marker = marker
        self.quantity = quantity

    def calculate_total(self):
        return self.marker.price * self.quantity

    def print_invoice(self):
        total = self.calculate_total()
        print(f"Invoice for {self.marker.name} ({self.marker.color}):")
        print(f"Quantity: {self.quantity}")
        print(f"Total: ${total}")

    def save_to_file(self, filename):
        total = self.calculate_total()
        with open(filename, "w") as file:
            file.write(f"Invoice for {self.marker.name} ({self.marker.color}):\n")
            file.write(f"Quantity: {self.quantity}\n")
            file.write(f"Total: ${total}\n")

"""