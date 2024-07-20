#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Ensure the correct settings module is used.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myjob_api.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an informative error if Django is not available.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute the command line utility.
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
