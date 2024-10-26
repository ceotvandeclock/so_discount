# Copyright 2017 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

{
    "name": "Sale Discount",
    "summary": "Allows to apply discounts in Sale.",
    "version": "16.0.1.0.2",
    "category": "Sale",
    "installable": True,
    "depends": ["sale"],
    'author': 'Awad Soltan',
        'images': ['static/description/img.png'],
    "data": [
        "security/ir.model.access.csv",
        "views/sale.xml",
        "wizard/sale_order_discount_views.xml",
    ],
}
