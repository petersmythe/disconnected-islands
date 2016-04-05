# disconnected-islands
A QGIS plugin that finds disconnected "islands" in a road network layer, so that a routing tool will work between all nodes. A tolerance field allows for imperfect topology.

This plugin runs on a polyline layer, building up a road (or rail, etc.) network graph of connected links. It then analyses connected subgraphs, ones that are connected to each other, but not connected to isolated or floating links. It creates an additional attribute containing the group ID of the subgraph. This can then be used to style the layer with Categorised styles, or Zoom to selection. The disconnected links can then be fixed. 

Based on Detlev's answer to my question: http://gis.stackexchange.com/questions/184319/how-to-find-disconnected-islands-in-a-road-network-layer-using-qgis 
