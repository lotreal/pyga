import sys
from coloredlogger import ColoredLogger

# use my ColoredLogger
# PYTHONPATH=../pylib python src/app.py
print(sys.path)

if __name__ == '__main__':
    logger = ColoredLogger()
    logger.info('just a blue info')