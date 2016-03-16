# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DisconnectedIslands
                                 A QGIS plugin
 Finds disconnected "islands" in a road network layer, so that a routing tool will work between all nodes. A tolerance field allows for imperfect topology.
                             -------------------
        begin                : 2016-03-15
        copyright            : (C) 2016 by Peter Smythe / AfriGIS
        email                : peters@afrigis.co.za
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DisconnectedIslands class from file DisconnectedIslands.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .disconnected_islands import DisconnectedIslands
    return DisconnectedIslands(iface)
