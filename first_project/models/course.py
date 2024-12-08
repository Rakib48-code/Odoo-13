from odoo import api,models,fields

class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'Course Information'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    image = fields.Binary(string='Course Image', help='Give here book image')