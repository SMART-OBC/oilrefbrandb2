# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

{
    'name': 'Aloha Odoo Connector',
    'summary': '''Fetch order line from aloha csv and import in odoo sale order.
    ''',
    'description': ''' Aloha Odoo''',
    'category': 'Sales',
    'version': '15.0.1.0.1',
    'author': 'SMART Outsourcing & Business Consulting',
    'license': 'OPL-1',
    'website': 'http://www.smart-obc.com',
    'depends': ['sale_management'],
    'data': [
        
        'views/sale_aloha_view.xml',
        'data/auto_connector.xml',
    ],
    'qweb': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
