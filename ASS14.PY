
# Experiment 14: Logging Module

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,

    # Display logs on console and save in file
    format="%(asctime)s - %(levelname)s - %(message)s",

    handlers=[
        logging.FileHandler("app.log", mode="w"),
        logging.StreamHandler()
    ]
)

# Display different logging levels
logging.debug("This is a debug message")

logging.info("Program started successfully")

logging.warning("This is a warning message")

logging.error("An error occurred")

logging.critical("Critical error occurred")


# Demonstrate exception logging
try:

    # Division by zero
    result = 10 / 0

except ZeroDivisionError:

    logging.exception("Division by zero error")

print("\nLogging completed successfully!")
