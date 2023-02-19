from odoo import models, fields, api

class Bot(models.Model): 
    _name = 'bot.model'

    name = fields.Char(string = "UAH") 
    usd= fields.Char(string = "USD")
    eur= fields.Char(string = "EUR")
    sell_data = fields.Integer(string = "Sell")
    buy_data = fields.Integer(string = "Buy")
