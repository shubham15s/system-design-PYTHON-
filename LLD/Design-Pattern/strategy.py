"""
The Strategy Pattern is a behavioral design pattern that enables you to define a family of algorithms (or behaviors), 
encapsulate each one, and make them interchangeable. It allows the algorithm to vary independently from the clients that use it.

This pattern is particularly useful when you have multiple ways to perform a task 
and want to switch between them dynamically at runtime without changing the client code.

Key Components of the Strategy Pattern
Strategy Interface:

    Defines a common interface for all concrete strategies.

    This ensures that all strategies can be used interchangeably.

Concrete Strategies:

    Implement the strategy interface with specific algorithms or behaviors.

    Each concrete strategy provides a different implementation of the task.

Context:

    Maintains a reference to a strategy object.

    Delegates the task to the current strategy instead of implementing the behavior itself.

Client:

    Configures the context with a specific strategy and uses it to perform the task.


When to Use the Strategy Pattern:
    When you have multiple ways to perform a task and need to switch between them dynamically.

    When you want to isolate the implementation details of an algorithm from the code that uses it.

    When you want to avoid conditional statements for selecting different behaviors.

    When you want to add new behaviors without modifying existing code (Open/Closed Principle).


Advantages of the Strategy Pattern
    Flexibility: You can switch between algorithms at runtime.

    Separation of Concerns: Algorithms are decoupled from the client code.

    Extensibility: New strategies can be added without modifying existing code.

    Eliminates Conditional Logic: Avoids complex conditional statements for selecting behaviors
"""


# Step 1: Define the Strategy Interface
class RouteStrategy:
    def calculate_route(self, start, end):
        pass


# Step 2: Implement Concrete Strategies
class DrivingStrategy(RouteStrategy):
    def calculate_route(self, start, end):
        return f"Calculating the fastest driving route from {start} to {end}"


class WalkingStrategy(RouteStrategy):
    def calculate_route(self, start, end):
        return f"Calculating the safest walking route from {start} to {end}"


class CyclingStrategy(RouteStrategy):
    def calculate_route(self, start, end):
        return f"Calculating the most scenic cycling route from {start} to {end}"


# Step 3: Define the Context
class Navigator:
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy):
        self._strategy = strategy

    def calculate_route(self, start, end):
        return self._strategy.calculate_route(start, end)


# Step 4: Client Code
if __name__ == "__main__":
    # Create strategies
    driving = DrivingStrategy()
    walking = WalkingStrategy()
    cycling = CyclingStrategy()

    # Create context with a default strategy
    navigator = Navigator(driving)

    # Use the current strategy
    print(navigator.calculate_route("Home", "Office"))  # Output: Driving route

    # Switch to a different strategy
    navigator.set_strategy(walking)
    print(navigator.calculate_route("Home", "Park"))  # Output: Walking route

    # Switch to another strategy
    navigator.set_strategy(cycling)
    print(navigator.calculate_route("Home", "Beach"))  # Output: Cycling route
