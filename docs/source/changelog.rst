=========
Changelog
=========

#####
2.0.0
#####

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


 