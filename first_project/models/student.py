from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Information'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
    ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age')
    guardian = fields.Char(string='Guardian')
    note = fields.Text(string='Description')