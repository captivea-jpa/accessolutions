# coding: utf-8
# Part of CAPTIVEA. Odoo 11.

{
    'name': 'cap_default_settings',
    'author': 'captivea-jpa',
    'description': """
    This module configure default odoo's application and module settings for AccesSolutions.
    This module should be the second module to be installed, after the cap_default_modules one.
    """,
    'depends': ['cap_default_modules'],
    'data': ['data/account_settings.xml',
             'data/config_settings.xml',
             'data/mail_settings.xml',
             'data/sale_settings.xml',
             'data/stock_settings.xml',
             'data/website_settings.xml'],
    'installable': True,
}
