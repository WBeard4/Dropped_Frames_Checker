import logging

# I want to have more control over the logging, so creating a Logger class
class Logger:
    def __init__(self, filename='log.txt'):
        self.logger_with_time = logging.getLogger('logger_with_time') # Create two seperate loggers
        self.logger_with_time.setLevel(logging.INFO) # Set the logging level, INFO will just be whatever information I add

        self.logger_without_time = logging.getLogger('logger_without_time')
        self.logger_without_time.setLevel(logging.INFO)

        # Creating a file handler for each type of log I want. at the moment one with timestamp, one without
        # I'm doing this to neaten log.txt, though its not entirely necessary
        self.file_handler_with_time = logging.FileHandler(filename, encoding='utf-8')
        self.formatter_with_time = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        self.file_handler_with_time.setFormatter(self.formatter_with_time)
        self.file_handler_with_time.setLevel(logging.INFO)
        self.logger_with_time.addHandler(self.file_handler_with_time)

        # Create a file handler for logs without timestamp
        self.file_handler_without_time = logging.FileHandler(filename, encoding='utf-8')
        self.formatter_without_time = logging.Formatter('%(message)s')
        self.file_handler_without_time.setFormatter(self.formatter_without_time)
        self.file_handler_without_time.setLevel(logging.INFO)
        self.logger_without_time.addHandler(self.file_handler_without_time)

    def log_without_time(self, message):
        # This will log a message with a timestamp
        self.logger_without_time.info(message)

    def log_with_time(self, message):
        # Log a message without timestamp
        self.logger_with_time.info(message)