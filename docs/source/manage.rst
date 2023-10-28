======
Manage
======

######
Create
######

.. warning::
	When working with section boxes there will be 3 collections created.

	The first named ``section_boxes.SceneXXX`` storing all section boxes.
	The second named ``section_box_tmps`` storing mesh versions of all non-mesh objects included in the box.
	The third, if any cross sections active, named ``cross_sections`` storing all cross section objects.

	Do NOT delete or rename any of them! They will be automatically managed by the addon.

**From Selection**
	Select all objects you want to include into the section box then choose *Create Section Box* under the *Object Context Menu* (``RIGHTCLICK``) to instantiate it.
	The new created section box will be exactly bounding all selected objects.
	
	The section method will be automatically set to *Boolean* or *Shader* if the active viewport shading mode is either *Solid*, *Wireframe* or *Material Preview*, *Rendered* respectively.    

**From Collection**
	Select the collection which containing objects you want to include into the section box in the *Outliner* and then choose *Section Box* under the *Object Context Menu* opened with ``RIGHTCLICK`` to instantiate it.
	This section box will be a *Collection Section Box* and will be displayed with a *Collection* icon in the :ref:`menu:outliner`.

	The instantiation works just like for a normal section box but with the method always set to *Boolean*.

	With *Collection Section Boxes* you get the option to :ref:`Reload <menu:outliner>`. 

**Empty**
	When no objects selected you can create an emtpy section box located at the 3D Cursor by choosing *Section Box* just like when instantiating from a selection.
	This box will detect which objects it's hitting and includes them automatically. This is especially useful in huge scenes with huge amounts of objects.

##########
Add/Remove
##########

Add objects to a section box by selecting them first, then select the section box and choose *Add Objects* under the *Object Context Menu* (``RIGHTCLICK``).
The same works for removing objects from a section box by choosing *Remove Objects*.

#####
Reset
#####

Reset the section box to it's initial shape by pressing ``BACKSPACE``. You can change this hotkey in the :ref:`preferences:keymap`.

######
Delete
######

Press ``X`` to delete the selected section box. Alternatively you can choose *Remove* under the :ref:`menu:outliner`.