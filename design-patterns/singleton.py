"""
Singleton Pattern with Thread Safety
Demonstrates thread-safe Singleton pattern implementation.
Ensures only one instance of a class exists across the application.
"""

import threading

class SingletonMeta(type):
    """
    Thread-safe Singleton metaclass implementation.
    """
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        """
        Controls the instantiation process.
        Uses double-checked locking for thread safety.
        """
        # First check without lock for performance
        if cls not in cls._instances:
            with cls._lock:
                # Double-check after acquiring lock
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    """
    Example singleton class representing a database connection.
    """
    
    def __init__(self):
        self.connection_id = id(self)
        print(f"Database connection created with ID: {self.connection_id}")
    
    def query(self, sql):
        return f"Executing: {sql}"

# Example usage
if __name__ == "__main__":
    # Create first instance
    db1 = DatabaseConnection()
    
    # Try to create second instance
    db2 = DatabaseConnection()
    
    # Verify they're the same instance
    print(f"\ndb1 is db2: {db1 is db2}")
    print(f"db1 ID: {id(db1)}")
    print(f"db2 ID: {id(db2)}")
    
    # Test thread safety
    def create_connection():
        db = DatabaseConnection()
        print(f"Thread {threading.current_thread().name}: {id(db)}")
    
    threads = [threading.Thread(target=create_connection, name=f"Thread-{i}")
               for i in range(5)]
    
    print("\nTesting thread safety:")
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
