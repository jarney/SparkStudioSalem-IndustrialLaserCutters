#! /usr/bin/python3
import xml.etree.ElementTree as ET
import os
import copy
import sys

# This is a small utility script that allows design of engravings
# on a series of layers.  Each layer is exported to
# a separate file with "Background-" layers in all files and
# exports only layers named "Export-".  This helps because
# Lightburn doesn't recognize layers, so it's nice to be able
# to design lots of engravings in a single file and then
# export them as separate designs in Lightburn.


export_folder = os.path.splitext(sys.argv[1])[0]
tree = ET.parse(sys.argv[1])
root = tree.getroot()
listoflayers=[]
for g in root.findall('{http://www.w3.org/2000/svg}g'):
	name = g.get('{http://www.inkscape.org/namespaces/inkscape}label')
	listoflayers.append(name)
print(listoflayers)

background_layers = []
export_layers = []
for layer in listoflayers:
    if layer.startswith("Background-"):
        background_layers.append(layer)
    elif layer.startswith("Hidden-"):
        pass
    elif layer.startswith("Export-"):
        export_layers.append(layer)

for layer in background_layers:
    print("Keeping background layer in all exports " + str(layer))
for layer in export_layers:
    print("Keeping export layer in exports " + str(layer))

if not os.path.exists(export_folder):
	os.makedirs(export_folder)

def remove_prefixes(lname):
        lname_unprefixed = lname.removeprefix("Background-")
        lname_unprefixed = lname_unprefixed.removeprefix("Export-")
        lname_unprefixed = lname_unprefixed.removeprefix("Hidden-")
        return lname_unprefixed

#try:
#	listoflayers.remove('background')
#except ValueError:
#	print("No background")
for export_layer_name in export_layers:
        temp_tree = copy.deepcopy(tree)
        export_layer_name_unprefixed = remove_prefixes(export_layer_name)
        print("Exporting layer to file " + export_layer_name + " -> " + export_layer_name_unprefixed)

        temp_root = temp_tree.getroot()
        for g in temp_root.findall('{http://www.w3.org/2000/svg}g'):
                name = g.get('{http://www.inkscape.org/namespaces/inkscape}label')
                if name != export_layer_name and name not in background_layers:
                        temp_root.remove(g)
                else:
                        print("    Exporting layer " + name)
                style = g.get('style')
                if type(style) is str:
                        style = style.replace( 'display:none', 'display:inline' )
                        g.set('style', style)
        temp_tree.write( os.path.join( export_folder, export_layer_name_unprefixed +'.svg' ) )
        
