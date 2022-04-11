from odoo import api, fields, models


class ProjectTaskType(models.Model):
    _name = 'project.task.type'

    project_task_id = fields.One2many(
        comodel_name="project.task",
        required=True,
        inverse_name="project_task_type_id",
    )
    name = fields.Char(string='Name')


class ProjectTask(models.Model):
    _inherit = "project.task"

    project_task_type_id = fields.Many2one(
        comodel_name="project.task.type",
    )
