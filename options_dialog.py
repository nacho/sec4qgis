# -*- coding: utf-8 -*-
"""
/***************************************************************************
                               SEC4QGIS v1.0.5
                             -------------------
                               (A QGIS plugin)
                             -------------------
 Funciones relativas a la Sede Electrónica del Catastro (SEC) para QGIS.
 Functions related to Spanish Cadastral Electronic Site (SEC) for QGIS.
                             -------------------
        begin                : 2016-06-30
        copyright            : (C) 2016 by Andrés V. O.
        website              : http://sec4qgis.tk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt import QtGui, uic
from qgis.PyQt.QtWidgets import QDialog, QFileDialog
from qgis.PyQt.QtCore import QSettings
import datetime
import sys
import os
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'options_dialog.ui'))
class OptionsDialog(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(OptionsDialog, self).__init__(parent)
        self.setupUi(self)
