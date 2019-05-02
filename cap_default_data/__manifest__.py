# coding: utf-8
# Part of CAPTIVEA. Odoo 11.

{
    'name': 'cap_default_data',
    'author': 'captivea-jpa',
    'description': """
    This module add default odoo's application and module data for AccesSolutions.
    This module should be the third module to be installed, after the cap_default_settings one.
    """,
    'depends': ['cap_default_settings'],
    'data': ['data/account_data.xml',
             'data/base_data.xml',
             'data/mail_data.xml',
             'data/purchase_data.xml',
             'data/sale_data.xml',
             'data/stock_data.xml',
             'data/product_data.xml'],
    'installable': True
}
