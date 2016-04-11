# ![icon](https://raw.githubusercontent.com/AfriGIS-South-Africa/disconnected-islands/master/icon.png) disconnected-islands

A QGIS plugin that finds disconnected "islands" in a transport network layer, so that a routing tool will work between all nodes. A tolerance field allows for imperfect topology.

This plugin runs on a polyline layer, building up a road (or rail, etc.) network graph of connected links. It then analyses connected subgraphs, ones that are connected to each other, but not connected to isolated or floating links. It creates an additional attribute containing the group ID of the subgraph. This can then be used to style the layer with Categorised styles, or Zoom to selection. The disconnected links can then be fixed. 

Based on Detlev's answer to my question: http://gis.stackexchange.com/questions/184319/how-to-find-disconnected-islands-in-a-road-network-layer-using-qgis 

Sample data to test this plugin can be found:
- in your plugins directory: ~/.qgis2/python/plugins/disconnected-islands/sample-data/islands.zip (NB: .qgis2 is normally a hidden directory.)
- via GitHub: https://github.com/AfriGIS-South-Africa/disconnected-islands/raw/master/sample-data/islands.zip

This plugin depends on the NetworkX module.  Mac OS X users need to install it manually, simply by executing, in a Terminal: sudo easy_install networkx.  Then restart QGIS.
