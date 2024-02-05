#logging means - Capture details and which are usefull while debugging as well as show the user details
# and show the user details about the executuon of the program.

#warning to the users
#information to the users
# Errors or critical errors

"""
Chrome options - Every browser will provide some functions.
Using Chrome options - Chrome with extentsion, window size, proxy , JS disabled.

"""


import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)

    # Intentional Logging to User
    LOGGER.info("This is information Logs")
    LOGGER.warning("This is warning Logs")
    LOGGER.error("This is error Logs")
    LOGGER.critical("This is critical Logs")
