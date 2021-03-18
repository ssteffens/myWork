# Demonstrates logging
# Attributes that can be put into the basicConfig:
#   level
#   filename
#   filemode
#   format
#       %(name)s - %(levelname)s - %(message)s - %(asctime)s - %(lineno)s

import logging
# Determines the level at which logging will be issued: Info will show all levels up from INFO (INFO, 
# WARNING, ERROR, CRITICAL), ERROR will show all levels up from ERROR (ERROR and CRITICAL)
#logging.basicConfig(level = logging.INFO)
# logging.basicConfig(level = logging.ERROR)

# To create new file with log rather than displaying in command line. Filemode w = write/overwrite new
# file, a = write/append file. Order of format items can be changed. 
logging.basicConfig(filename = "debugging.log", filemode = "a", level=logging.DEBUG, format = " %(name)s - %(levelname)s - %(message)s - %(asctime)s - %(lineno)s") 


name = "Joe"

logging.error("this is an error")
logging.critical("Critical level")
logging.warning("Don't know %s", name)
logging.info("Still going")
logging.debug("and so is this")
