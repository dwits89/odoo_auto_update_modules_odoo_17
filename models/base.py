# -*- coding: utf-8 -*-
from odoo import models
import logging

_logger = logging.getLogger(__name__)

class BaseModuleUpdate(models.AbstractModel):
    _inherit = 'base'

    def _auto_init(self):
        res = super(BaseModuleUpdate, self)._auto_init()
        if self.env.cr.dbname == self.env.registry.db_name:
            _logger.info("🔄 Auto-actualizando lista de módulos OCA en la base de datos %s", self.env.cr.dbname)
            try:
                self.env['ir.module.module'].update_list()
                _logger.info("✅ Lista de módulos actualizada automáticamente.")
            except Exception as e:
                _logger.error("❌ Error actualizando la lista de módulos: %s", str(e))
        return res
