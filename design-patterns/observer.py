"""
Observer Pattern Implementation
Demonstrates the Observer design pattern for event-driven programming.
Useful for implementing distributed event handling systems.
"""

from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    """Abstract base class for observers."""
    
    @abstractmethod
    def update(self, subject):
        """Called when the subject's state changes."""
        pass

class Subject:
    """Subject class that maintains a list of observers."""
    
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = None
    
    def attach(self, observer: Observer):
        """Attach an observer to the subject."""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer):
        """Detach an observer from the subject."""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self):
        """Notify all observers about state change."""
        for observer in self._observers:
            observer.update(self)
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class ConcreteObserver(Observer):
    """Concrete implementation of an observer."""
    
    def __init__(self, name):
        self.name = name
    
    def update(self, subject):
        print(f"{self.name} notified: Subject state is now {subject.state}")

# Example usage
if __name__ == "__main__":
    subject = Subject()
    
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")
    
    subject.attach(observer1)
    subject.attach(observer2)
    
    print("Setting state to 'active':")
    subject.state = "active"
    
    print("\nSetting state to 'idle':")
    subject.state = "idle"
