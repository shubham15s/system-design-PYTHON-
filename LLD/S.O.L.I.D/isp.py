"""
The Interface Segregation Principle (ISP) is one of the SOLID principles of object-oriented design. 
It states that clients should not be forced to depend on interfaces they do not use. In other words, an interface should be small, 
focused, and specific to the needs of the client, rather than being large and monolithic.

Key Idea:
Break down large interfaces into smaller, more specific ones so that clients only need to know about the methods 
that are relevant to them.

This reduces the burden on classes that implement the interface and avoids forcing them to provide empty or irrelevant implementations.

Example of ISP Violation:
Let’s consider an example of a Printer interface that has methods for printing, scanning, and faxing. 
Not all printers support all these functionalities, so forcing a class to implement all methods can lead to violations of ISP.

Problem:
A SimplePrinter only supports printing, but it is forced to implement scan and fax methods, which it doesn’t need.

This leads to empty or irrelevant implementations, violating ISP.
"""

# (Violation of ISP):

from abc import ABC, abstractmethod


# A monolithic interface that violates ISP
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass


# A simple printer that only supports printing
class SimplePrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        raise NotImplementedError("Scan not supported")

    def fax(self, document):
        raise NotImplementedError("Fax not supported")


# A multifunction printer that supports all features
class MultifunctionPrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

    def fax(self, document):
        print(f"Faxing: {document}")


# Example usage
if __name__ == "__main__":
    simple_printer = SimplePrinter()
    simple_printer.print("My Document")  # Works fine
    simple_printer.scan("My Document")  # Raises NotImplementedError

"""
Explanation of the Problem:
The Printer interface is too large and forces all implementing classes to provide implementations for print, scan, and fax.

The SimplePrinter class doesn’t need scan and fax functionality, but it is forced to implement them, leading to empty or 
error-raising methods.

This violates the Interface Segregation Principle because the SimplePrinter is forced to depend on methods it doesn’t use.

Solution: Adhering to ISP
To adhere to ISP, we should break the monolithic Printer interface into smaller, more specific interfaces. 
Each class can then implement only the interfaces it needs.
"""

# Adhering to ISP

from abc import ABC, abstractmethod

# Smaller, focused interfaces
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


# A simple printer that only supports printing
class SimplePrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")


# A multifunction printer that supports all features
class MultifunctionPrinter(Printer, Scanner, Fax):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

    def fax(self, document):
        print(f"Faxing: {document}")


# Example usage
if __name__ == "__main__":
    simple_printer = SimplePrinter()
    simple_printer.print("My Document")  # Works fine

    multifunction_printer = MultifunctionPrinter()
    multifunction_printer.print("My Document")  # Works fine
    multifunction_printer.scan("My Document")  # Works fine
    multifunction_printer.fax("My Document")  # Works fine
