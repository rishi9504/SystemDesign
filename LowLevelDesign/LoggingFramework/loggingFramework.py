import redis
from datetime import datetime
from enum import Enum
from queue import Queue
from threading import Thread

# Initialize Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Enum for Log Levels
class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    FATAL = 5

# Base class for Log Handlers
class LogHandler:
    def write(self, message: str):
        raise NotImplementedError

# Console Log Handler
class ConsoleHandler(LogHandler):
    def write(self, message: str):
        print(message)

# File Log Handler
class FileHandler(LogHandler):
    def __init__(self, file_name: str):
        self.file_name = file_name
    
    def write(self, message: str):
        with open(self.file_name, "a") as f:
            f.write(message + "\n")

# Asynchronous Log Handler using Queue
class AsyncLogHandler(LogHandler):
    def __init__(self):
        self.queue = Queue()
        self.worker = Thread(target=self._process_logs, daemon=True)
        self.worker.start()

    def write(self, message: str):
        self.queue.put(message)

    def _process_logs(self):
        while True:
            message = self.queue.get()
            print(message)  # Replace with actual log processing

# Redis Lock Implementation
class RedisLock:
    def __init__(self, name, timeout=5):
        self.name = f"lock:{name}"
        self.timeout = timeout

    def acquire(self):
        # Attempt to set a value in Redis with the key `self.name`
        # The value is set to "1"
        # `ex=self.timeout` sets an expiration time for the key in seconds
        # `nx=True` ensures that the key is only set if it does not already exist
        # The method returns True if the key was set, and None if it was not
        return r.set(self.name, "1", ex=self.timeout, nx=True)

    def release(self):
        r.delete(self.name)

# Logger Class
class Logger:
    _instance = None
    _redis_lock = RedisLock("logger_lock")
    
    def __new__(cls, *args, **kwargs):
        """
        This is a special method that is called when an object is created from a class.
        We use this method to implement the Singleton pattern, which ensures that there is
        only one instance of the Logger class.

        The Singleton pattern is implemented using a Redis lock. Before creating a new
        Logger instance, we acquire a Redis lock. If the lock is acquired successfully,
        we check if the Logger instance is None. If it is, we create a new Logger instance.
        Finally, we release the Redis lock.

        If the Redis lock is not acquired, it means that another process is currently
        creating a Logger instance. In this case, we simply return the existing instance.
        """
        if cls._redis_lock.acquire():
            if cls._instance is None:
                # Create a new Logger instance
                cls._instance = super(Logger, cls).__new__(cls)
            # Release the Redis lock
            cls._redis_lock.release()
        # Return the Logger instance
        return cls._instance
    
    def __init__(self, level: LogLevel = LogLevel.INFO, handlers=None):
        """
        Initialize the Logger instance.

        The __init__ method is called when an object is created from a class.
        However, since we're implementing the Singleton pattern, we need to
        make sure that the Logger instance is only initialized once.

        We use the "initialized" attribute to keep track of whether the Logger
        instance has been initialized or not. If it has not been initialized,
        we set the level and handlers attributes.

        The level attribute determines the minimum log level that will be
        processed by the Logger. The handlers attribute is a list of LogHandler
        instances that will process the logs.

        If handlers is not provided, we default to a list containing a single
        ConsoleHandler instance.
        """
        if not hasattr(self, "initialized"):
            self.level = level
            self.handlers = handlers or [ConsoleHandler()]
            self.initialized = True
    
    def log(self, level: LogLevel, message: str):
        """
        Log a message with the given level.

        This method checks if the given log level is greater than or equal to
        the current log level. If it is, it formats the message with a timestamp
        and the log level name, and writes it to each of the log handlers.

        The method acquires the Redis lock before writing to the log handlers,
        to ensure that only one process can write to the log handlers at a time.
        """
        if level.value >= self.level.value:
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Format the message with the timestamp and log level name
            formatted_message = f"[{timestamp}] [{level.name}] {message}"
            
            # Acquire the Redis lock
            if self._redis_lock.acquire():
                # Write the formatted message to each of the log handlers
                for handler in self.handlers:
                    handler.write(formatted_message)
                # Release the Redis lock
                self._redis_lock.release()
    
    def set_level(self, level: LogLevel):
        self.level = level
    
    def add_handler(self, handler: LogHandler):
        """
        Add a log handler to the logger.

        This method adds the given log handler to the list of log handlers
        that the logger will write to. We acquire the Redis lock before
        modifying the list of log handlers, to ensure that only one process
        can modify the list of log handlers at a time.
        """
        # Acquire the Redis lock
        if self._redis_lock.acquire():
            # Add the log handler to the list of log handlers
            self.handlers.append(handler)
            # Release the Redis lock
            self._redis_lock.release()

# Example Usage
if __name__ == "__main__":
    logger = Logger(level=LogLevel.DEBUG, handlers=[
        ConsoleHandler(),
        FileHandler("app.log"),
        AsyncLogHandler()
    ])
    
    logger.log(LogLevel.INFO, "This is an info message.")
    logger.log(LogLevel.ERROR, "An error has occurred.")
