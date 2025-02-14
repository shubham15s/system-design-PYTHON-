"""
The Dependency Inversion Principle (DIP) is the last of the SOLID principles of object-oriented design. It states that:

High-level modules should not depend on low-level modules. Both should depend on abstractions.

Abstractions should not depend on details. Details should depend on abstractions.

In simpler terms, DIP encourages designing systems where high-level modules (e.g., business logic) depend on abstractions 
(e.g., interfaces or abstract classes) rather than concrete implementations of low-level modules 
(e.g., database access, external services). This makes the system more flexible, maintainable, and testable.

Key Idea:
Decouple high-level and low-level modules by introducing an abstraction (interface or abstract class) between them.

High-level modules define the business logic and depend on abstractions.

Low-level modules implement the abstractions and provide concrete functionality.

Example of DIP Violation:
Let’s consider an example where a NotificationService (high-level module) directly depends on a EmailService 
(low-level module) to send notifications. This creates a tight coupling between the two, making it difficult to change or 
extend the system.

Problem:
If we want to switch from EmailService to SmsService, we need to modify the NotificationService class.

This violates DIP because the high-level module depends on a low-level module.

"""

# Violation of DIP


# Low-level module
class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")


# High-level module
class NotificationService:
    def __init__(self):
        self.email_service = EmailService()  # Direct dependency on EmailService

    def send_notification(self, message):
        self.email_service.send_email(message)


# Example usage
if __name__ == "__main__":
    notification_service = NotificationService()
    notification_service.send_notification("Hello, World!")

"""
Adhering to DIP
To adhere to DIP, we introduce an abstraction (interface) between the high-level and low-level modules. 
The high-level module depends on the abstraction, and the low-level module implements the abstraction.
"""
from abc import ABC, abstractmethod


# Abstraction (interface)
class MessageService(ABC):
    @abstractmethod
    def send_message(self, message):
        pass


# Low-level module: EmailService
class EmailService(MessageService):
    def send_message(self, message):
        print(f"Sending email: {message}")


# Low-level module: SmsService
class SmsService(MessageService):
    def send_message(self, message):
        print(f"Sending SMS: {message}")


# High-level module
class NotificationService:
    def __init__(self, message_service: MessageService):  # Depends on abstraction
        self.message_service = message_service

    def send_notification(self, message):
        self.message_service.send_message(message)


# Example usage
if __name__ == "__main__":
    # Use EmailService
    email_service = EmailService()
    notification_service = NotificationService(email_service)
    notification_service.send_notification("Hello via Email!")

    # Use SmsService
    sms_service = SmsService()
    notification_service = NotificationService(sms_service)
    notification_service.send_notification("Hello via SMS!")


"""
Real-World Analogy:
Think of a computer's USB port as an abstraction. You can plug in any USB device (e.g., keyboard, mouse, flash drive) 
without needing to modify the computer. The computer (high-level module) depends on the USB interface (abstraction), 
and the devices (low-level modules) implement the USB interface. This is the essence of DIP!

"""
