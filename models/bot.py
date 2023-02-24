from odoo import models, fields, api

class Bot(models.Model): 
    _name = 'bot.model'

    name = fields.Text(string = "") 
    usd= fields.Char(string = "")
    eur= fields.Char(string = "")
    sell_data_usd = fields.Float(string = "Sell")
    buy_data_usd = fields.Float(string = "Buy")
    sell_data_eur = fields.Float(string = "Sell")
    buy_data_eur = fields.Float(string = "Buy")
    telegram_user = fields.Char(string="Requested By: ")
    write_date = fields.Datetime()
