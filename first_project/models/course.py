from odoo import api,models,fields
from odoo.exceptions import ValidationError

class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'Course Information'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    image = fields.Binary(string='Course Image', help='Give here book image')

    @api.constrains('name','description')
    def _check_description(self):
        for rec in self:
            if rec.name == rec.description:
                raise ValidationError("Fields name and description must be different")