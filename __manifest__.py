# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Bot",
    'version': '1.0',
    'depends': ['base'],
    'author': "Oleg Zubak",
    # 'category': 'contacts',
    'description': 'Telegram bot for test',
    'data': ['views/bot.xml',
             'security/ir.model.access.csv',
    ], 
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
