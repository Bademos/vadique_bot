import logging

class ErrorLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname =='ERROR' and "важно" in record.msg.lower()



logging.basicConfig(
    level=logging.DEBUG,
    #format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
     #      '%(lineno)d - %(name)s - %(message)s'
    format='[{asctime}] #{levelname:8} {filename}:'
           '{lineno} - {name} - {message}',
    style='{'
)

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs.log")
file_handler_err = logging.FileHandler("log_err.log",encoding='utf-8')
file_handler_err.addFilter(ErrorLogFilter())
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(file_handler_err)