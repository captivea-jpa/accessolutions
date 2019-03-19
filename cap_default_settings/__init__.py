# coding: utf-8
# Part of CAPTIVEA. Odoo 11.

__all__ = []


def post_init_hook(cr, registry):
    """Called after module installation."""
    # SET 'DOCUMENT' MODULE STATE TO 'TO UPGRADE'
    cr.execute("UPDATE ir_module_module SET state = 'to upgrade' WHERE name = 'document';")
    # CONFIRM PRE INITIATION
    return True
