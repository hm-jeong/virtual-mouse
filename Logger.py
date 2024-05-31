import logging


loggers = []


def setup_logger(log_file):
    """
    Sets up a logger to write logs to the specified file.
    """
    # Create a custom logger
    logger = logging.getLogger(log_file)
    logger.setLevel(logging.DEBUG)

    # Remove all existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create handlers
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    formatter = logging.Formatter('%(asctime)s %(message)s')
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)

    return logger


def log_message(filename, message):
    logger = setup_logger(filename)
    logger.debug(message)
    print(filename, message)