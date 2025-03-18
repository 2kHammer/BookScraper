import logging
import os
from logging.handlers import TimedRotatingFileHandler

class Logger:
    _logger = None
    _log_dir = None

    @staticmethod
    def init_logger(path, log_level=logging.DEBUG):
        if Logger._logger is not None:
            raise RuntimeError(f"Logger already initialized")

        Logger._log_dir = path + "bookscraper/"

        os.makedirs(Logger._log_dir, exist_ok=True)

        # create logger
        Logger._logger = logging.getLogger("bookscraper_logger")
        Logger._logger.setLevel(log_level)

        # Log-Format
        formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")

        file_handler = TimedRotatingFileHandler("app.log", when="midnight", interval=1, encoding="utf-8")
        file_handler.setFormatter(formatter)
        file_handler.suffix = "%Y-%m-%d.log"

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        if not Logger._logger.hasHandlers():
            Logger._logger.addHandler(file_handler)
            Logger._logger.addHandler(console_handler)

        return Logger._logger

    @staticmethod
    def get_logger():
        return Logger._logger

