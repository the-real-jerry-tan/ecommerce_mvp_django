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

from django.apps import AppConfig

class EcommerceMvpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce_mvp'
