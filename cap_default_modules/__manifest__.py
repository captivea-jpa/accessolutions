# coding: utf-8
# Part of CAPTIVEA. Odoo 11.

{
    'name': 'cap_default_modules',
    'author': 'captivea-jpa',
    'description': """
    This module install default odoo's applications and modules for AccesSolutions.
    This module should be the first module to be installed.
    """,
    'depends': ['account_accountant',
                'account_invoicing',
                'auth_signup_verify_email',
                'base_automation',
                'board',
                'calendar',
                'contacts',
                'crm',
                'delivery_ups',
                'mail',
                'mass_mailing',
                'mrp_repair',
                'purchase',
                'sale_management',
                'stock',
                'stock_barcode',
                'website',
                'website_sale'],
    'installable': True
}
