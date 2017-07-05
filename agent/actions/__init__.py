import os
import glob

# Dynamically add all action modules in __all__ to trigger the intent decorator
modules = glob.glob(os.path.dirname(__file__) + "/*.py")

__all__ = [
    os.path.basename(f)[:-3]
    for f in modules
    if os.path.isfile(f) and not f.endswith('__init__.py')
]
