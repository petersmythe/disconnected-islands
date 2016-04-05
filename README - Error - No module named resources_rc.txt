After editing the UI in Qt Designer, when you save the file disconnected_islands_dialog_base.ui, it adds 3 lines inside the <ui> element:

 <resources>
  <include location="resources.qrc"/>
 </resources>
 
Unfortunately, this results in the following error when the plugin is loaded in QGIS:

 File "C:/PROGRA~1/QGISES~1/apps/qgis/./python\qgis\utils.py", line 572, in _import
			    mod = _builtin_import(name, globals, locals, fromlist, level)
			ImportError: No module named resources_rc
            
The solution, according to http://gis.stackexchange.com/questions/139625/qgis-plugin-problems-importing-resources-resources-rc-file-plugin-doasnt-l, 
is to manually delete the <resources> element (all 3 lines) after saving the UI each and every time.  It works.  Don't forget to do it.











Also, in order to generate resources.py from the icon.png etc, execute:
  pyrcc4 -o resources.py resources.qrc