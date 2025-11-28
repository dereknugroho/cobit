import logging
import os

from logging.handlers import RotatingFileHandler

from cobit.utils.paths import LOG_DIR, PROJECT_ROOT

# Define severity levels
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

class RelativePathFilter(logging.Filter):
    """A class for filtering full pathnames to pathnames relative to project root."""
    def filter(self, record):
        try:
            record.relpath = os.path.relpath(record.pathname, PROJECT_ROOT)
        except ValueError:
            record.relpath = record.pathname
        return True

def logger_setup(name, logfile, level, max_bytes=5*1024*1024, backup_count=5):
    """Create a logger with a RotatingFileHandler."""

    # Create log directory if it does not exist
    os.makedirs(LOG_DIR, exist_ok=True)

    # Initialize new logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Attach handler and formatter
    if not logger.handlers:
        handler = RotatingFileHandler(
            os.path.join(LOG_DIR, logfile),
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(message)s (%(relpath)s)'
        )
        handler.addFilter(RelativePathFilter())
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
