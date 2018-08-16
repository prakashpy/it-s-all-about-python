import logging

# One Way

# set logging
logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

logger.info("Something something")
logger.error("my random error")



# another way
log_file = 'my_log_reporting.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logging.error("my error here")




### FIXME ->> diff logger vs logging