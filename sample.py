from tkinter_colored_logging_handlers import LoggingHandler
import logging
from tkinter import Tk, Text
import threading
import time
from coloredlogs import ColoredFormatter


def main():
    for i in range(3):
        try:
            time.sleep(1)
            logger.debug("message with level debug (10)")
            time.sleep(1)
            logger.info("message with level info (20)")
            time.sleep(1)
            logger.warning("message with level warning (30)")
            time.sleep(1)
            logger.error("message with level error (40)")
            time.sleep(1)
            logger.critical("message with level critical (50)")
            time.sleep(1)
            logger.debug(1 / 0)
        except Exception as e:
            logger.error(e, exc_info=True)


root = Tk()
root.title("DEBUG LOG")
root.geometry("800x300")


entry = Text(root, background="black", foreground="white")
entry.pack(fill="both", expand=True)

logger = logging.getLogger(__name__)
handler = LoggingHandler(entry, light=True)
format = "%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s"
handler.setFormatter(ColoredFormatter(format))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


thread = threading.Thread(target=main)
thread.start()
root.mainloop()
