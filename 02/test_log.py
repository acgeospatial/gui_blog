## in acknowledgment of https://www.youtube.com/watch?v=jxmzY9soFXg
## and https://github.com/CoreyMSchafer/code_snippets/blob/master/Logging-Advanced/log-sample.py

from datetime import datetime
import logging

name_out =  (datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".log")

print ("log file being written: ", name_out)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(name_out)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)


def main():
	x = 0
	print ("another go")
	print ('script running')
	logger.info('script running')
	while x < 10:
		print ('calculating')
		logger.info("Position, %s" % x)
		x += 1
	logger.info("loop closed")

if __name__ == '__main__':
	main()
	
