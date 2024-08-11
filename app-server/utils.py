import logging

def get_logger(name: str, log_file: str, level=logging.DEBUG):
    """
    Set up a logger that logs to both console and a file.

    :param name: The name of the logger.
    :param log_file: The path to the log file.
    :param level: The logging level.
    :return: A configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create formatters
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = get_logger("appserver", "logs/applog")
