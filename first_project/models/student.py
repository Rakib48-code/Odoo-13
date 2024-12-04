from odoo import api, fields, models
from datetime import date

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
    guardian = fields.Char(string='Guardian', default='Odoo Mates')
    note = fields.Text(string='Description')


    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
