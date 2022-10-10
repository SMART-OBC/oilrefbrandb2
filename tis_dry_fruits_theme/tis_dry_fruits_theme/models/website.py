# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

from odoo import fields, models, SUPERUSER_ID, api


class Website(models.Model):
    _inherit = 'website'

    def get_full_banner(self):
        full_banner = self.env['home.banner'].sudo().search([])
        return full_banner

    def get_product_category(self):
        product_category = self.env['dry.fruits.category'].sudo().search([])
        return product_category

    def get_offers(self):
        offers = self.env['offer.one'].sudo().search([])
        return offers

    def get_weekly_offers(self):
        weekly_offers = self.env['weekly.offer'].sudo().search([])
        return weekly_offers

    def get_popular_products(self):
        popular_products = self.env['dry.fruits.popular'].sudo().search([])
        return popular_products

    def get_week_best_selling(self):
        week_best_selling = self.env['week.best.selling'].sudo().search([])
        return week_best_selling

    def get_half_banner(self):
        half_banner_one = self.env['half.banner'].sudo().search([])
        return half_banner_one

    def get_brand(self):
        brands = self.env['dry.fruits.brands'].sudo().search([])
        return brands


class HomeBanner(models.Model):
    _name = "home.banner"
    _description = "HomeBanner"

    name = fields.Char(string="Name")
    image1 = fields.Binary(string="Upload Image")
    header = fields.Char(string="Header")
    footer = fields.Char(string="Footer")


class OfferOne(models.Model):
    _name = "offer.one"
    _description = "OfferOne"

    name = fields.Char(string="Name")
    image1 = fields.Binary(string="Upload Image")
    header = fields.Char(string="Header")


class OfferTwo(models.Model):
    _name = "offer.two"
    _description = "OfferTwo"

    name = fields.Char(string="Name")
    image1 = fields.Binary(string="Upload Image")
    header = fields.Char(string="Header")
    footer = fields.Char(string="Footer")


class WeeklyOffer(models.Model):
    _name = "weekly.offer"
    _description = "WeeklyOffer"

    name = fields.Char(string="Name")
    image1 = fields.Binary(string="Upload Image")
    heading = fields.Char(string='Heading')


class HalfBanner(models.Model):
    _name = "half.banner"
    _description = "Dry Fruits Banner 4 "

    name = fields.Char(string="Name")
    image1 = fields.Binary(string="Upload Image")
    header = fields.Char(string="Header")
    footer = fields.Char(string="Footer")


class WeekBestSelling(models.Model):
    _name = "week.best.selling"
    _description = "Week Best Selling"

    product_id = fields.Many2one('product.template', string="Product")
    name = fields.Char(string="Name")


class DryFruitsPopular(models.Model):
    _name = "dry.fruits.popular"
    _description = " Dry Fruits Product"

    product_id = fields.Many2one('product.template', string="Product")


class DryFruitsBrand(models.Model):
    _name = "dry.fruits.brands"
    _description = " Dry Fruits Brand Product"

    product_id = fields.Many2one('product.template', string="Product")
    name = fields.Char(string="Name")


class DryFruitsCategory(models.Model):
    _name = "dry.fruits.category"
    _description = "Category"
    _rec_name = 'category_id'

    category_id = fields.Many2one('product.public.category', string="Category")
