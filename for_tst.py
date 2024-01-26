from fo_del import  tsr, func_2
from logs import *
import os
import dotenv
dotenv.load_dotenv()

print(os.getenv('BOT_TOKEN'))


tsr()
logger.debug("otlado4ka)")
logger.error("Важно! 404")
func_2()
for i in range(5):
    logger.error("Важно, мы в жопе номер %d",i)
print(dir(func_2))
try:
    x = 7/0
except:
    logger.error("Важно, тут было исключение")