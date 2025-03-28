"""
Abstract Factory Design Pattern

The Abstract Factory Design Pattern is a creational design pattern that allows you to
create families of related objects without specifying their concrete classes.

The Abstract Factory pattern is commonly used in scenarios where you need to create
multiple related objects. For example, if you are building a user interface, you may
need to create a button, a checkbox, and a text field. The Abstract Factory pattern
allows you to encapsulate the creation of these related objects in a single class.

In this example, we are creating a GUI application with buttons and checkboxes. We
have a Windows version and a MacOS version of the application. We use the Abstract
Factory pattern to create the button and checkbox objects based on the platform.

The Abstract Factory pattern consists of the following components:

1. Abstract Product Interfaces: These are the interfaces for the objects that need
   to be created. In this example, we have a Button interface and a Checkbox
   interface.

2. Concrete Product Classes: These are the concrete classes that implement the
   abstract product interfaces. In this example, we have a WindowsButton class and
   a MacOSButton class, both of which implement the Button interface. We also have
   a WindowsCheckbox class and a MacOSCheckbox class, both of which implement the
   Checkbox interface.

3. Abstract Factory Interface: This is the interface for the factory class that
   creates the objects. In this example, we have a GUIFactory interface that has two
   methods: create_button() and create_checkbox().

4. Concrete Factory Classes: These are the concrete classes that implement the
   abstract factory interface. In this example, we have a WindowsFactory class and
   a MacOSFactory class, both of which implement the GUIFactory interface.

The client code uses the abstract factory interface to create the objects. The
client code does not need to know about the concrete classes.

The benefits of using the Abstract Factory pattern include:

* Decoupling the client code from the concrete classes.
* Allowing for easy extension to support new platforms.
* Providing a single point of change for the creation of all related objects.
"""

# Abstract Product Interfaces
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        """
        Renders the button object.

        Returns:
            str: The rendered string representation of the button.
        """
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        """
        Renders the checkbox object.

        Returns:
            str: The rendered string representation of the checkbox.
        """
        pass

# Concrete Product Classes for Windows
class WindowsButton(Button):
    def render(self):
        """
        Renders a Windows-style button object.

        Returns:
            str: The rendered string representation of the button.
        """
        return "Rendering a Windows-style button"

class WindowsCheckbox(Checkbox):
    def render(self):
        """
        Renders a Windows-style checkbox object.

        Returns:
            str: The rendered string representation of the checkbox.
        """
        return "Rendering a Windows-style checkbox"

# Concrete Product Classes for MacOS
class MacOSButton(Button):
    def render(self):
        """
        Renders a MacOS-style button object.

        Returns:
            str: The rendered string representation of the button.
        """
        return "Rendering a MacOS-style button"

class MacOSCheckbox(Checkbox):
    def render(self):
        """
        Renders a MacOS-style checkbox object.

        Returns:
            str: The rendered string representation of the checkbox.
        """
        return "Rendering a MacOS-style checkbox"

# Abstract Factory Interface
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        """
        Creates a button object based on the platform.

        Returns:
            Button: The created button object.
        """
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        """
        Creates a checkbox object based on the platform.

        Returns:
            Checkbox: The created checkbox object.
        """
        pass

# Concrete Factory for Windows
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        """
        Creates a Windows-style button object.

        Returns:
            Button: The created button object.
        """
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        """
        Creates a Windows-style checkbox object.

        Returns:
            Checkbox: The created checkbox object.
        """
        return WindowsCheckbox()

# Concrete Factory for MacOS
class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        """
        Creates a MacOS-style button object.

        Returns:
            Button: The created button object.
        """
        return MacOSButton()
    
    def create_checkbox(self) -> Checkbox:
        """
        Creates a MacOS-style checkbox object.

        Returns:
            Checkbox: The created checkbox object.
        """
        return MacOSCheckbox()

# Client code that uses the Abstract Factory
class Application:
    def __init__(self, factory: GUIFactory):
        """
        Initializes the application with the given factory.

        Args:
            factory (GUIFactory): The factory to use to create the objects.
        """
        self.factory = factory
        self.button = None
        self.checkbox = None
    
    def create_ui(self):
        """
        Creates the button and checkbox objects using the factory.
        """
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
    
    def render(self):
        """
        Renders the button and checkbox objects.
        """
        print(self.button.render())
        print(self.checkbox.render())

# Client code to demonstrate usage
def create_application(platform: str) -> Application:
    """
    Creates an application based on the given platform.

    Args:
        platform (str): The platform to use to create the application.

    Returns:
        Application: The created application.
    """
    if platform == "Windows":
        return Application(WindowsFactory())
    elif platform == "MacOS":
        return Application(MacOSFactory())
    else:
        raise ValueError("Unsupported platform")

# Demonstration
def main():
    # Create Windows application
    windows_app = create_application("Windows")
    windows_app.create_ui()
    print("Windows Application UI:")
    windows_app.render()

    print("\n")

    # Create MacOS application
    macos_app = create_application("MacOS")
    macos_app.create_ui()
    print("MacOS Application UI:")
    macos_app.render()

if __name__ == "__main__":
    main()
