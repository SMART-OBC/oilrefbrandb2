# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2021. All rights reserved.

{
    'name': 'Dry Fruits Shop Theme',
    'version': '15.0.0.1.0.0',
    'category': 'Theme/Ecommerce',
    'sequence': 1,
    'summary': 'Ecommerce Dry Fruits Shop Theme',
    'description': '''Ecommerce Dry Fruits Shop Theme''',
    'website': 'https://www.technaureus.com/',
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'price': 40,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'live_test_url': 'https://themes.technaureus.com/web/database/selector',
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.jpg'],
    'depends': ['website_sale', 'website_sale_wishlist'],
    'data': [

        'security/ir.model.access.csv',
        'views/banner_views.xml',
        'views/popular_views.xml',
        'views/category_views.xml',
        'views/best_selling_views.xml',
        'views/brand_views.xml',
        'views/h_f_dry_fruits.xml',
        'views/homepage_dry_fruits.xml',

    ],
    "assets": {
        "web.assets_frontend": ["/tis_dry_fruits_theme/static/src/css/owl.carousel.min.css",
                                "/tis_dry_fruits_theme/static/src/css/font-awesome.min.css",
                                "/tis_dry_fruits_theme/static/src/css/style.css",
                                "/tis_dry_fruits_theme/static/src/js/owl.carousel.min.js",
                                "/tis_dry_fruits_theme/static/src/js/main.js",
                                ]
    },

    'installable': True,
    'auto_install': False,
    'application': True,
}
