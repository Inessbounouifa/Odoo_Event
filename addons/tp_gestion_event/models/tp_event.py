from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class TpEvent(models.Model):
    _name = "tp.event"
    _description = "Evenement TP"

    name = fields.Char(string="Nom", required=True)

    responsable = fields.Selection([
        ('iness', 'Bounouifa Iness'),
        ('walid', 'Walid BenAzzouz'),
        ('akram', 'Akram Bounouifa'),
        ('nada', 'Nada Bounouifa'),
    ], string="Responsable", required=True)

    date_debut = fields.Date(string="Date début")
    date_fin = fields.Date(string="Date fin")
    lieu = fields.Char(string="Lieu")

    image = fields.Binary(string="Image")

    statut = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('confirme', 'Confirmé'),
        ('encours', 'En cours'),
        ('termine', 'Terminé'),
    ], default='brouillon')

    description = fields.Text(string="Description")

    # =====================
    # Participants
    # =====================

    participants_ids = fields.Many2many(
        'res.partner',
        string="Participants"
    )

    participants_count = fields.Integer(
        string="Nombre de participants",
        compute="_compute_participants_count",
        store=True
    )

    @api.depends('participants_ids')
    def _compute_participants_count(self):
        for rec in self:
            rec.participants_count = len(rec.participants_ids)

    # =====================
    # Google Maps
    # =====================

    maps_url = fields.Char(
        string="Google Maps",
        compute="_compute_maps_url"
    )

    @api.depends('lieu')
    def _compute_maps_url(self):
        for rec in self:
            if rec.lieu:
                rec.maps_url = (
                    "https://www.google.com/maps/search/?api=1&query="
                    + rec.lieu.replace(" ", "+")
                )
            else:
                rec.maps_url = False

    # =====================
    # Contraintes
    # =====================

    @api.constrains('date_debut', 'date_fin')
    def _check_dates(self):
        for rec in self:
            if rec.date_debut and rec.date_fin and rec.date_fin < rec.date_debut:
                raise ValidationError(
                    "La date de fin doit être postérieure à la date de début."
                )

    # =====================
    # Workflow sécurisé
    # =====================

    def action_confirmer(self):
        for rec in self:
            if not rec.lieu:
                raise ValidationError(
                    "Vous devez renseigner le lieu avant de confirmer l'événement."
                )
            rec.statut = 'confirme'

    def action_demarrer(self):
        for rec in self:
            if not rec.participants_ids:
                raise ValidationError(
                    "Impossible de démarrer un événement sans participants."
                )
            rec.statut = 'encours'

    def action_terminer(self):
        today = date.today()
        for rec in self:
            if rec.date_fin and rec.date_fin > today:
                raise ValidationError(
                    "Vous ne pouvez pas terminer l'événement avant la date de fin."
                )
            rec.statut = 'termine'
