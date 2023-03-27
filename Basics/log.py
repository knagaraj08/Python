import logging
import sys

logger = logging.getLogger(__name__)

# logging.basicConfig acts on the root logger.
logging.basicConfig(

    format="{asctime}{levelname:<8} {message}",
    style="{",
    level=logging.DEBUG,
    stream=sys.stdout,
)

# logging.info("Hello!!!")
# logging.info("This is log info")
# logging.warning("This operation cannot be performed")

sh = logging.StreamHandler()
fh = logging.FileHandler("spam.log")
logger.addHandler(sh)
sh.setLevel(logging.INFO)
