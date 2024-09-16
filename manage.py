"""
© 2024 Jerry Tan. All Rights Reserved.

This software is the confidential and proprietary information of Jerry Tan
("Confidential Information"). You shall not disclose such Confidential Information
and shall use it only in accordance with the terms under which this software
was distributed or otherwise published, and solely for the prior express purposes
explicitly communicated and agreed upon, and only for those specific permissible purposes.

This software is provided "AS IS," without a warranty of any kind. All express or implied
conditions, representations, and warranties, including any implied warranty of merchantability,
fitness for a particular purpose, or non-infringement, are disclaimed, except to the extent
that such disclaimers are held to be legally invalid.
"""
#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
This is the main entry point to manage your Django project.
"""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_mvp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
