## tk_hotBox
###### *PySide marking menu style layered ui and toolkit for maya and max.


*work in progress..*

## Design:
*To build an app agnostic modular ui to house tools where each piece is constructed dynamically to allow 
for as little overhead as possible in construction and maintainence. Literally all you have to do to have 
a new ui up and running, is to drop a qt ui file into the ui folder, and create a module and class of the 
same name. Naming convention allows for a stacked ui to be built, signals added/removed, and a master dictionary 
(stored in the switchboard module) to be created, that handles the getting/setting of all data from one 
simple location, in one simple way.*

 Structure:

## tk_main: 
*handles main gui construction.*

* get dynamic ui files relative to folder location.

* handle coordinates to populate ui at cursor position.

* add each ui to a layout stack.

* set window flags and attributes.

* set event filters and overrides.

* construct paint event overlay.


## tk_signals: 
*constructs signal connections.*

* build connection dict in switchboard for each class with corresponding signals and slots.

* add/remove signals using the switchboard dict each time the stacked layout index is changed.



## tk_slots: 
*master class holding methods that are inherited across all app specific slot class modules.*



## tk_switchboard: 
*holds the following information for each tool class instance. From this information, you can call switchboard methods to 
get most relevent information easily wherever you need it.*

* class name as string

* class object

* widget size

* widget name/method name as string

* widget Object

* widget Object with Signal

* method Object

* method docString

* uiList : *string list of all ui filenames in the ui folder*

* prevName : *list of last called relevant ui*

* prevCommand : *history of commands. uses the method docstring to generate a user friendly name from the dynamic element and stores it along side the command method.*



 Naming convention:

* ui files:     <name>.ui
 
* tools module: tk_slots_<app>_<name>.py
 
* class name:   <Name>

*widget/corresponding class methods share the same naming convention across all modules: ie. widget b021 connects to method b021.
the docstring of each method houses a user friendly name that is stored with all other widget info in the switchboard dict when an
instance is populated. Any of the buttons will also connect to a corresponding class method should it exist.*

* QPushButton   b000    (b000-b999) can contain 1000 buttons of one type max per class using this convention.

* QPushButton   v000    these buttons are attached an event filter to change the ui index.

* QPushButton   i000    buttons that are initially invisible.

* QComboBox     cmb000  ""

* QCheckBox     chk000  ""

* QSpinBox      s000    ""

* QtextField    t000    ""



##
-----------------------------------------------
 Basic use:
-----------------------------------------------

######
* pressed hotkey shows instance. release hides;

* mouse not pressed: heads up info

* right mouse down: shows main navigation window.

* left mouse down: shows viewport navigation.

* middle mouse down: shows mesh display options.

* releasing the mouse over any of the buttons in those windows takes you to the corresponding submenu.

* double left mouseclick: produces last used window.

* double right mouseclick: repeats last command.

* dragging on an empty are of the widget moves the window and pins it open in a separate instance.

* holding ctrl while using Spinboxes increments/decrements by an extra decimal place.

* mouse over buttons while window pinned to get an explanation of its function.


#times
tk_signals
time: 0.11471084274
tk_slots_max_viewport
time: 0.0632666986347
tk_slots_max_polygons
time: 0.0816165578988

# to install:

#set path to the directory containing the ui files.
# ie. path = os.path.expandvars(r'%CLOUD%/____Graphics/Maya/Scripts/_Python/_path/tk_maya_ui')
#have tk_maya(or max)_functions and tk_maya(or max)_buttons in your python path





# Notes

#comment ascii font=Nancyj
#shelf item scripts can be found: C:\Users\m3\Documents\maya\2016\prefs\shelves


# Re-load Ui:
# import sys
# import os.path as os

# path = os.expandvars("%CLOUD%/__portable/_scripts/")
# sys.path.append(path)

# reload(tk_main)




# THINGS TO DO NOW:
# -----------------------------------------------








#scene> rename;  with selection, and find field empty, nothing is renamed. (an * in the find field returns correct result) 




#while in heads up display; holding any additional key shows keyboard shortcuts mapped to that key. similar to substance




select by edge angle function


component path tool
	supporting
	nth component
	loop
	ring
	contigious
	shortest path


mesh clean-up



	

edit> delete menu
with delete, delete loop, delete history
for edge in rt.selection:
	edge.SelectEdgeLoop()
	edge.EditablePoly.Remove()


set normal by angle not working with no error.


set crease amount 	obj.EditablePoly.setEdgeData(1, 0.5)


assign scene material cmb does nothing. ui list doesnt expand to fit contents.


display> toggle material override


editors:
scene> editors cmb> Asset Tracking System		ATSOps.visible = true
selection> editors> Named Selection Sets 	 macros.run "Edit" "namedSelSets"
editors> Crease Explorer	CreaseExplorerManager.OpenCreaseExplorer ()

selection>  select similar



override materials with fast shader
	actionMan.executeAction 0 "63574"  -- Views: Override Off





search field returns related commands.



framework for interactive tools
# method for storing values


radial array: add interactive update on pivot change
set pivot;  move -r -0.829437 0 0 pCylinder27.scalePivot pCylinder27.rotatePivot


create> cmb001> keep window open on indexChanged.  closing and re-opening hides spinboxes.


fix repeat last command


move polygon collapse to merge area

 
create camera from view
look through [camera from drop down list]
 

create; creating a primitive doesnt align to set axis
spinboxes visible on set point
wrap setattributes call in an undoinfo chunk

duplicate w/transform spinboxes; convert to being interactive.
add center pivot option

bug: transform negative '-' sets spinbox value to 0.  

line 1640, in b010
    parent = pm.listRelatives(instances[0], parent=True)[0]
UnboundLocalError: local variable 'instances' referenced before assignment

build convert menu with a pair of comboboxes to select to/from

create; angled pipe.  creates a basic pipe section and allows to interactively add angles/fittings/ etc.
create; stairs.  step, rise, amount
create; railing
create; saved asset. store points to building block items etc ascii


move ui path variable to a config file

scene: set unreal/unity project. GamePipeline -sp "Unreal";
scene: re-export last

display; build a layer editor

fix recent autosave;  %userprofile%/AppData/Local/Temp  get dir file list,  sort by date modified

add try/except to delete history function

fix in-view message alpha transparency

use grow/shrink selection buttons to scroll through 'select by name' results.
commands change the textfielchrome-extension://mpognobbkildjkofajifpdfhcoklimli/components/startpage/startpage.htmld text and call t001 function to select that node.
possibly use the toggle function to keep tabs on list place
prevent focus initially.  when focused chkpin down



edit; delete (component) not working
  File "O:\Cloud/____Graphics/Maya/scripts/_Python/_Python_startup\tk_maya_buttons.py", line 1420, in b032
    faces = func.getAllFacesOnAxis (axis)
  File "O:\Cloud/____Graphics/Maya/scripts/_Python/_Python_startup\tk_maya_functions.py", line 45, in getAllFacesOnAxis
    if pm.exactWorldBoundingBox (attr)[index] < -0.00001:
  File "C:\Program Files\Autodesk\Maya2018\Python\lib\site-packages\pymel\internal\pmcmds.py", line 140, in exactWorldBoundingBox_wrapped
pymel.core.general.MayaAttributeError: Maya Attribute does not exist (or is not unique):: u'|brake_disc|brake_disc|brake_discShape.e[261:262].f[0]'


better clean up menu. with checkboxes for options

better center pivot; check component or object mode and apply interactive transforms accordingly.
possibly merge with main transform menu. and add separate spinboxes for x, y, and z. with the option to chain values to each other. 


save; could not delete: elise_mid.009 find a way to delete file regardless of extension. possibly for filename in filenames: if filename.startswith('elise_mid.009'): remove file. maybe best to just get project root and search recursively.
change default iterations to 5; save iteration amount to settings text file.


undo queue combobox (command start with capital letters and functions start with lower case).
scripting; recent commands combobox
 
add maya uv workflow to uv notes https://www.youtube.com/watch?v=cy1vqLw-agk


consolidate all in edit> transfer.  batch transfer is missing. batch translate is being called instead.

start a store settings text file

in the functions module build a list and function that can track selection order
later use it to create a tool instance

align pivot; face normal

create menu creates object on combobox index changed. adjusting settings edits the created objects inputs
pm.plane = polyPlane[]   plane[0] points to pPlane1 (transform node), and plane[1] points to polyPlane1 (history node).

tooltip for polygons>split vertex

display> wireframe inactive; set to query current mode and if wireframe: set to shaded then apply.  otherwise doesn't work

create function for populating new window/message window

add custom keyboard shortcuts via python script instead of manually

pinned windows re-open as separate instance

radial array 
['VRayLightRect1', 'VRayLightRect1_ins1', 'VRayLightRect1_ins2', 'VRayLightRect1_ins3', 'VRayLightRect1_ins4', 'VRayLightRect1_ins5', 'VRayLightRect1_ins6', 'VRayLightRect1_ins7', 'VRayLightRect1_ins8', 'VRayLightRect1_ins9', 'VRayLightRect1_ins10', 'VRayLightRect1_ins11', 'VRayLightRect1_ins12', 'VRayLightRect1_ins13', 'VRayLightRect1_ins14', 'VRayLightRect1_ins15', 'VRayLightRect1_ins16', 'VRayLightRect1_ins17', 'VRayLightRect1_ins18', 'VRayLightRect1_ins19', 'VRayLightRect1_ins19', 'VRayLightRect1_ins19_ins1', 'VRayLightRect1_ins19_ins2', 'VRayLightRect1_ins19_ins3', 'VRayLightRect1_ins19_ins4', 'VRayLightRect1_ins19_ins5', 'VRayLightRect1_ins19_ins6', 'VRayLightRect1_ins19_ins7', 'VRayLightRect1_ins19_ins8', 'VRayLightRect1_ins19_ins9', 'VRayLightRect1_ins19_ins10', 'VRayLightRect1_ins19_ins11', 'VRayLightRect1_ins19_ins12', 'VRayLightRect1_ins19_ins13', 'VRayLightRect1_ins19_ins14', 'VRayLightRect1_ins19_ins15', 'VRayLightRect1_ins19_ins16', 'VRayLightRect1_ins19_ins17', 'VRayLightRect1_ins19_ins18', 'VRayLightRect1_ins19_ins19', 'VRayLightRect1', 'VRayLightRect1_dup1', 'VRayLightRect1_dup2', 'VRayLightRect1_dup3', 'VRayLightRect1_dup4', 'VRayLightRect1_dup5', 'VRayLightRect1_dup6', 'VRayLightRect1_dup7', 'VRayLightRect1_dup8', 'VRayLightRect1_dup9', 'VRayLightRect1_dup10', 'VRayLightRect1_dup11', 'VRayLightRect1_dup12', 'VRayLightRect1_dup13', 'VRayLightRect1_dup14', 'VRayLightRect1_dup15', 'VRayLightRect1_dup16', 'VRayLightRect1_dup17', 'VRayLightRect1_dup18', 'VRayLightRect1_dup19', 'VRayLightRect1_dup19', 'VRayLightRect1_dup19_dup1', 'VRayLightRect1_dup19_dup2', 'VRayLightRect1_dup19_dup3', 'VRayLightRect1_dup19_dup4', 'VRayLightRect1_dup19_dup5', 'VRayLightRect1_dup19_dup6', 'VRayLightRect1_dup19_dup7', 'VRayLightRect1_dup19_dup8', 'VRayLightRect1_dup19_dup9', 'VRayLightRect1_dup19_dup10', 'VRayLightRect1_dup19_dup11', 'VRayLightRect1_dup19_dup12', 'VRayLightRect1_dup19_dup13', 'VRayLightRect1_dup19_dup14', 'VRayLightRect1_dup19_dup15', 'VRayLightRect1_dup19_dup16', 'VRayLightRect1_dup19_dup17', 'VRayLightRect1_dup19_dup18', 'VRayLightRect1_dup19_dup19', 'VRayLightRect1', 'VRayLightRect1_ins1', 'VRayLightRect1_ins2', 'VRayLightRect1_ins3', 'VRayLightRect1_ins4', 'VRayLightRect1_ins5', 'VRayLightRect1_ins6', 'VRayLightRect1_ins7', 'VRayLightRect1_ins8', 'VRayLightRect1_ins9', 'VRayLightRect1_ins10', 'VRayLightRect1_ins11', 'VRayLightRect1_ins12', 'VRayLightRect1_ins13', 'VRayLightRect1_ins14', 'VRayLightRect1_ins15', 'VRayLightRect1_ins16', 'VRayLightRect1_ins17', 'VRayLightRect1_ins18', 'VRayLightRect1_ins19'] #
Traceback (most recent call last):
  File "O:\Cloud/____Graphics/Maya/scripts/_Python/_Python_startup\tk_maya_func.py", line 1836, in b038
    self.b001(create=True)
  File "O:\Cloud/____Graphics/Maya/scripts/_Python/_Python_startup\tk_maya_func.py", line 1554, in b001
    pm.polyUnite (radialArrayObjList, name=objectName)
  File "C:\Program Files\Autodesk\Maya2018\Python\lib\site-packages\pymel\internal\factories.py", line 957, in newFuncWithReturnFunc
    res = beforeReturnFunc(*args, **kwargs)
  File "C:\Program Files\Autodesk\Maya2018\Python\lib\site-packages\pymel\internal\pmcmds.py", line 140, in polyUnite_wrapped
    raise pymel.core.general._objectError(obj)
pymel.core.general.MayaNodeError: Maya Node does not exist (or is not unique):: u'VRayLightRect1_ins1'

add all relevant options for smooth preview located in poly display properties.

image plane setup; get size of selected image and construct plane at camera
look at maya/workflow notes for proper workflow to automate
lock; aspect ratio on plane.  backface culling.

default xyz values for transform move and rotate. 
	add rotate (scale, move) 'by camera' option to transform
	center pivot (object seems to work best) option (on by default)
transform:
	add tweak mode checkbox. strsTweakMode true; click and drag mode for adjusting components
	add step snap relative. manipMoveSetSnapMode 1; toggle off 0 checkable transform an object or component in incriments
	add step snap absolute. manipMoveSetSnapMode 2; toggle off 0 checkable ""
	for both; textfield defalt float 1.00. manipMoveContext -edit -snapValue value Move;

add button for soften/ harden edge procedure. I think it is in a tab here or in python startup.
in normals: create procedure for: if creased; edge harden else; soften. crease transfer algorithm my have useful parts.
fix crease transfer algorithm 
	note future features such as bevel all creased edge by crease value
	explore idea of working with hard/soft edges and transforming them to creased edges

create> text
import maya.app.type.typeToolSetup
maya.app.type.typeToolSetup.createTypeTool()

create init button.  rehash functions module

Cannot find procedure "bt_snapAlignObjectToComponentOptions".
	Start of trace: (command window: line 1).

add toggle polyVertex Face to display menu. or look into face draw size option. doMenuComponentSelection("elise_bodyShell_mid_001", "pvf");
	$mode = `selectMode -query -component`;
	if ($mode==0)
	changeSelectMode -component;
	$maskVertex = `selectType -query -vertex`;
	
add grease pencil window to grease pencil tool as option
GreasePencilTool;
createGreasePencilWindow();

add clipping planes to display
could query current camera and getAttr and change perspShape to "current camera"+Shape
or just have a camera settings button that shows the settings in the attribute editor. 
pm.setAttr ("perspShape.nearClipPlane", 0.001)
pm.setAttr ("perspShape.farClipPlane", 10000)

dR_selConstraintAngle; #alternate command syntax. use regex
dR_DoCmd("selConstraintAngle"); #takes an angle value
dR_DoCmd("selConstraintBorder");
dR_DoCmd("selConstraintElement");
dR_DoCmd("selConstraintOff");



EXTEND FUNCTIONALITY:

modify'frame selected' to query symmetry state (because when more than 1 vertex is selected, they are generally far apart) edit: $state = `symmetricModelling -query -symmetry`;



UI FUNCTIONALITY:

transparent shortcut buttons reveal text name when moused over
transparent shortcut groups can be changed in preferences. ie. modeling shortcuts, rendering shortcuts

tk_maya init; ui in sub-folder with tk_main instead of path (just copy code from test.py)
importing tk_maya_buttons as buttons instead of * would be pointless if splitting up the button module later 

outputwindow text color for help messages

push text from a helpline to a textfield

finish ui stylesheet
simply the way signals and slots are built based on the way the stylesheet builds styles
move all 

spinboxes increment an extra decimal place while holding shift key (pyside key modifiers)






MORE INVOLVED:

add framework for interactive tools (use radial array as a model)

build layer editor.

build a selection function that returns different the current selection
	filter by type:
	as string:
		main object from component
	as object
	converted to:
		vertices
		faces
		edges
	various ls flags:
	all objects

radial symmetry

straighten circle tool.
average curve tool.


script command popup elf window commands like mel2py won't accept multiple lines of code. tried to fix and now completely broken. possibly have a look and see if its not better to just convert it and 'scene options' elf windows into qt ui and add them to layout stack.


play with contrain edge options to build useful selection constraints

better insert edge tool
polySplitRing -constructionHistory off -smoothingAngle 30 -weight 0.9 -fixQuads 1;

collapse edge/
	pm.selectPref (preSelectClosest=True) #definitely want this setting off when not used
	selectPref -preSelectSize 15; #this sets the preselect area tolerance (i think)
	closestVert = pm.ls (selection=True)
	print closestVert
stitch tool
	selectPref(trackSelectionOrder=True)

build heads up display:
	symmetry state
	any active selection constraits
	polycount
	pm.helpLine(width=20, height=8)
	progress bar

select island doesnt work with symmetry also needs the abiltiy for multiple selections







OLD:

functionality to add:

quick rotate menu set. rotate by textedit amount + or - (default 45).

marking menu normals 'set to face' add command average normals before calling
add button edit> Optimize Scene mel; OptimizeScene;
modify Un crease edge so that it works both in object mode for all edges and component mode on just selected edges
add crease 'sets' button; python code: from maya.app.general import creaseSetEditor creaseSetEditor.showCreaseSetEditor()
add toggle crease edge visibility mel; polyOptions -displayCreaseEdge true; polyOptions -displayCreaseEdge false; modify to iterate through and toggle crease display for all objects in the scene. this is a good candidate for a checkbox
modify script; if nothing selected export visible geometry
understand symmetry and getting the align edge loop tool to work with it
functionality for hotkey g repeat last to be used on custom tools
add button toggle script editor output window size
fix sets in toolkit. add buttons from create> sets; set partition, quick select set and options
add buttons; edit mesh> vertex> average vertices, chamfer vertices, reorder vertices
uv tool popup mel window
add button 'Transfer Maps' (no options) mel: performSurfaceSampling 1; 
hotkey hide other objects f2; check for how many objects visible before executing if <2 inView error message
query poly clean up to get current flag state
building on top of existing straighten edgeloop script:use selection order to build an array and iterate through multiple edgeloops
check box support
create instance toggle for all duplicate actions
mod toolkit selection contraints; create drop down menu to select contraint and user input for contraint angle
change minimum size for tool settings, channel/layers
UV display put current display settings in array and toggle off/on 
heads up display for current selection count
toggle (black) silhouette of geometry  (to see low poly curvature ect)





batch export FBX and OBJ
proc batchExport (string $fileType)
	{
	$selection = createArrayFromSelection();
	$exportPath = sourceDirectory($fileType);

	for ($node in $selection)
		{
		$finalExportPath = ($exportPath+"/"+$node);

		if ($fileType == "obj")
			// select -replace $node;
			file -force
						-exportSelected
						-preserveReferences 
						-type "OBJexport"
						-options "-groups 0 \
											-ptgroups 0 \
											-materials 0 \
											-smoothing 1 \
											-normals 1"
						// ($node+".obj");
						($finalExportPath+".obj");
						print ($finalExportPath+".obj"+"\n");

		if ($fileType == "fbx")
			{
			// // Uncomment for export options
			// // Geometry
			// FBXExportSmoothingGroups -v true;
			// FBXExportHardEdges -v false;
			// FBXExportTangents -v false;
			// FBXExportSmoothMesh -v true;
			// FBXExportInstances -v false;
			// FBXExportReferencedContainersContent -v false;
			// // Animation
			// FBXExportBakeComplexAnimation -v false;
			// // FBXExportBakeComplexStart -v "";
			// // FBXExportBakeComplexEnd -v "";
			// FBXExportBakeComplexStep -v 1;
			// // FBXExportBakeResampleAll -v true;
			// FBXExportUseSceneName -v false;
			// // FBXExportQuaternion -v euler;
			// FBXExportShapes -v true;
			// FBXExportSkins -v true;
			// // Constraints
			// FBXExportConstraints -v false;
			// // Cameras
			// FBXExportCameras -v false;
			// // Lights
			// FBXExportLights -v false;
			// // Embed Media
			// FBXExportEmbeddedTextures -v false;
			// // Connections
			// FBXExportInputConnections -v false;
			// // Axis Conversion
			// FBXExportUpAxis y;

			// print ($finalExportPath+"\n");
			FBXExport -selected -file ($finalExportPath+".fbx");
			print ($finalExportPath+".fbx"+"\n");
			}
		}
	}







- da_intPlay: this script add the interactive play button directly to Time Slider
- da_curveToPoly: this script make possible the conversion of curves in polygons
- da_interactiveBooleans: this script make the Polygonal Boolean process more interactive
- da_BooleanFullIntersect: this script make a full intersect, so this execute a mesh subtraction but maintain subtracted part as separate object
- da_PlaneCutter: this script cut a mesh by using a flat mesh, this can be useful for simulate surface cracks
- da_AutoBevel: this script analyse the angle between faces and try to add a Bevel node only on needed edges
- da_ClothAsDeformer: this script set up the current mesh to be deformed by nCloth solver, this can be useful for simulate character selfcollision skin or muscle dynamics
- da_nParticleConverter: this script add the ability to convert particle to a specific type after their creation
- da_perspToggle: this script convert the current persp view to the closest ortho, and vice versa
- da_shell: this script emulates Shell deformer of Autodesk 3D Studio Max, by adding a thickness to flat polygons
- da_ConvertToMetaballs: this script convert particles to polygonal Metaballs
- da_MashVoxelizer: this script use MASH to voxelize an arbitrary mesh inside of another mesh
- da_RivetMash: this script constraint the pivot of a polygon to a component of another polygon
- da_CurveDistributionMash: this script scatter and constrain a polygonal object along a curve
- da_EdgeToLoopToCurve: this script convert edge selection to loop and then make a batch conversion to curves, this is useful for converting polygonal hair to curve hair 
- da_SurfaceScatterMash: this script scatter and constrain a polygonal object on a mesh
- da_CurveLength: this script returns the length of a curve in Maya unit
- da_MouseTrack: this script tracks the mouse movement and create an animation
- da_FacesFollicles: this script creates a follicle in the centre of selected faces
- da_Compass: this script converts Euler angle into a XYZ vector, for drive wind direction in Nucleus and Air Filed
- da_CombineCurves: this script combines curves in a single transform
- da_SepareCurves: this script separate combined curves
- da_MapFacesUV: this script maps any single faces of a mesh as separate planar UV shell
- da_KeyKeyedOnly: this script creates animation keys only on already animated channels
- Control Constraint: this set of scripts constraint a controller to a single or multiple controlled object(s)





'''
















