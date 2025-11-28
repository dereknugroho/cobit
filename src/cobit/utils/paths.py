import os

from cobit.utils.config import PATHS

def find_project_root(marker_files):
    current = os.path.abspath(os.path.dirname(__file__))
    while True:
        if all(os.path.exists(os.path.join(current, m)) for m in marker_files):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            raise RuntimeError("Project root not found")
        current = parent

PROJECT_ROOT = find_project_root(PATHS['files']['root_markers'])
LOG_DIR = os.path.join(PROJECT_ROOT, 'logs')
