from odoo import models, fields, api

class Bot(models.Model): 
    _name = 'bot.model'

    name = fields.Text(string = "Bank") 
    usd= fields.Text(string = "1")
    eur= fields.Text(string = "1")
    sell_data_usd = fields.Float(string = "Sell")
    buy_data_usd = fields.Float(string = "Buy")
    sell_data_eur = fields.Float(string = "Sell")
    buy_data_eur = fields.Float(string = "Buy")
