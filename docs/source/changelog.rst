=========
Changelog
=========

#####
2.0.9
#####

*January 06th, 2024*

************
New Features
************

**Update System**
    Added an 'ignore this update' option.

*********
Bug Fixes
*********

**Elevation Performance**
    Elevations generate much faster now in heavy scenes.

**Elevation Display**
    Fixed an issue where the elevation got displayed with an offest when the resolution scale setting wasn't at 100% in the render settings.

**Non-Mesh Objects**
    Fixed an issue were non-mesh objects inside collection instances or in the form of linked objects resulted in an error when creating a section box.

**Update System**
    Fixed a rare issue where Blender crashed when checking for updates on startup.

#####
2.0.6
#####

*November 14th, 2023*

*********
Bug Fixes
*********

**Update System**
    Fixed an issue where Blender crashed when checking for updates on startup.

**Plane Selection**
    Fixed an issue where selecting a plane from the viewport resulted in an error message when the view overlapped with the box.

#####
2.0.5
#####

*November 12th, 2023*

************
New Features
************

**Compatible with Blender 4.0**
    Section Box is now compatible with Blender 4.0!

#####
2.0.4
#####

*November 10th, 2023*

*********
Bug Fixes
*********

**Empty Section Box**
    Fixed an issue where the empty section box auto detecting did not work when there were unapplied transforms.


**Enabling Addon afterwards**
    When opening a file with section boxes in it but without the addon enabled, everything will work immediately after enabling the addon afterwards.

#####
2.0.3
#####

*November 9th, 2023*

*********
Bug Fixes
*********

**Select Plane**
    Fixed an issue where selecting a plane from the viewport resulted in an error message when the view overlapped with the box.

**Views**
    Loading saved views now considers the transform of all planes.

**Delete Section Box**
    Fixed an issue where deleting a section box did result in an error when a material of an included object was edited manually.

**Change Workspace**
    Fixed an issue where changing the workspace gave an error and stopped the handle hovering animation from working.


#####
2.0.2
#####

*November 1st, 2023*

*********
Bug Fixes
*********

**Export DXF**
    Fixed an issue where the export did not work when using custom colors for displaying cross sections or elevations.

**Export Mesh: Naming**
    The generated mesh objects from drawings are now properly named.

#####
2.0.1
#####

*October 31th, 2023*

*********
Bug Fixes
*********

**Create Section Box**
    Fixed an issue where the section box cutted with an offset on create.

#####
2.0.0
#####

*October 30th, 2023*

************
New Features
************

**Object Support**
    Section Box now supports all object types. This works for all non-mesh objects by working on temporary realized geometry in the background.
    Linked objects are also supported, they get automatically copied and localized when creating a section box.
    Don't worry, you will not end up with a bunch of copies of your objects, section boxes clean up after themselves.

    * Geometry Nodes
    * Curves
    * Text
    * Metaballs
    * Instanced Objects
    * Linked Objects

**Elevations**
    You can now create elevation plans from any side of the section box and export them as DXF.
    Learn more about them :ref:`here <settings:elevation>`.

**Customization**
    You can now customize the appearance of cross section and elevation plans.
    See what is now possible :ref:`here <settings:section>`.

**Apply**
    You can now apply section boxes.
    This lets you realize sections, learn more about it :ref:`here <menu:operations>`.

**UI Improvements**
    You can now customize the handles of section boxes in the :ref:`preferences <preferences:ui>`.
    And they are now responsive when hovering over them to indicate when they can be dragged.

**Update System**
    Never miss an update again, Section Box now automatically checks for updates every time you start Blender.
    You can also disable this and check for updates manually in the :ref:`preferences <preferences:addon>`.

#####
1.1.0
#####

************
New Features
************

**Expanded Preferences**
    Added material and empty size default settings.

**Export Object**
    Added the option to export cross sections as object for use inside blender.

**Export DXF Settings**
    Added more export settings.

**Hide Render**
    Added the option to hide the sections in renders only.

**Loading Indicator**
    Loading is now indicated by the mouse cursor when using performance heavy features on more complex objects, to make clear when a operation is finished.

**Merge Panels**
    Added the option to merge all panels of my addons into a single panel called *Ruben's Addons*. You'll find the option under the addon preferences (*Edit>Preferences>Add-Ons>Section Box*).

*********
Bug Fixes
*********

**Geometry Nodes**
    Fixed not working sections when using instances that are not realized.
    Fixed an issue when having a 'Set Material' node with a empty material property in the node tree.

**Non-Geometry Objects**
    Fixed an issue when creating a section box while having non-geometry objects selected.


 