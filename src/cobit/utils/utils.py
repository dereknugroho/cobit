from datetime import datetime

def generate_filename_timestamp() -> str:
    """Generate a timestamp 'yyyymmdd-hhmmss_' for prepending to filenames."""
    return datetime.now().strftime('%Y%m%d-%H%M%S')
