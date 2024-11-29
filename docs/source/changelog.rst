=========
Changelog
=========

#####
2.4.0
#####

*November 29th, 2024*

************
New Features
************

**Blender 4.3 Support**
    Section Box now supports Blender 4.3!

#####
2.3.4
#####

*October 31th, 2024*

************
Improvements
************

**Install Python Packages**
    Section Box now installs required Python packages automatically on first use. This replaces the dependency popup that appeared when installing the addon and is more reliable and user-friendly.


#####
2.3.3
#####

*October 4th, 2024*

*********
Bug Fixes
*********

**Animate Section Box**
    Fixed an issue where Blender crashed when rendering an animated section box.

**SVG Importer Addon**
    The built-in SVG importer addon will now be enabled automatically when creating a drawing.

**Numpy Issues**
    Fixed an issue where numpy issues occured with other addons when installing Section Box.


#####
2.3.2
#####

*September 25th, 2024*

*********
Bug Fixes
*********

**Cycles: Shading Artifacts**
    Fixed an issue where shading artifacts appeared on the section when using Cycles.

**Section Material: Not Saved**
    Fixed an issue where the section material turned blank when reopening a file. Now the material is saved and restored properly.

**Numpy Conflicts**
    Section Box won't install numpy anymore to avoid conflicts with other addons.


#####
2.3.1
#####

*September 9th, 2024*

************
New Features
************

**Shader Method: Cycles Compatible**
    The shader method is now fully compatible with Cycles.

**Shader Method: Adjust Alpha**
    You can now change the transparency of the backface coloring when using the shader method. Setting the alpha of the color to 0.0 will add no coloring but shows the original material instead.


#####
2.3.0
#####

*September 5th, 2024*

************
New Features
************

**Boolean Method: Fast**
    Added the option to change between 'Fast' and 'Exact' boolean solvers. The 'Fast' method is faster but can result in artifacts on more complex meshes.

**Cross Section: Original**
    Added the option to create a cross section from the original mesh instead from the section created by the section box. This is particularly useful when the section is not perfect, like when using the 'Fast' boolean method. Most differences will be for loose parts and non-planar faces.

*********
Bug Fixes
*********

**Shader Method: Cross Section**
    Fixed an issue where no cross section was possible when using the shader method.


#####
2.2.4
#####

*September 3rd, 2024*

*********
Bug Fixes
*********

**Drawing Creation**
    When creating cross sections and elevations only visible objects are considered now.
    Also the section box stays active after creating drawings now.


#####
2.2.3
#####

*September 2nd, 2024*

*********
Bug Fixes
*********

**Elevations**
    Fixed an issue where no elevations where possible when having Section Box installed as legacy addon in Blender 4.2 or above.


#####
2.2.2
#####

*August 28th, 2024*

*********
Bug Fixes
*********

**Sidebar Panels**
    Fixed an issue where multiple panels showed up above the main Section Box panel in the sidebar. This also caused a conflict with other addons that use the sidebar.

**Merge Panel**
    There is now the merge into "Ruben's Addons" panel option again in the addon preferences under display.


#####
2.2.1
#####

*August 27th, 2024*

*********
Bug Fixes
*********

**(Linux) Installation Issue**
    Fixed an issue where the installation failed on Linux.


#####
2.2.0
#####

*August 15th, 2024*

************
New Features
************

**Blender 4.2 Extensions**
    Section Box now supports Blender 4.2 extensions.

*********
Bug Fixes
*********

**Cross Sections**
    Fixed an issue where the cross section generation failed if there were zero length edges in the mesh.

************
Known Issues
************

**(macOS) Elevation**
    Elevation generation could crash on macOS using Blender 4.2. Hopefully this will work reliable again with the next Blender update.


######
2.1.6
######

*July 8th, 2024*

*********
Bug Fixes
*********

**Cross Sections**
    Fixed an issue where it was not possible to create cross sections.


**Delete Section Box**
    Fixed an issue where an error occured when deleting a section box including an object that was deleted before.


######
2.1.2
######

*May 6th, 2024*

*********
Bug Fixes
*********

**DXF Export**
    Fixed an issue where the DXF export was not working.


#####
2.1.0
#####

*April 9th, 2024*

************
New Features
************

**Cross Section Modifier Support**
    When creating a cross section, the addon now takes modifiers into account.

*********
Bug Fixes
*********
    
**Section Box Cycles Visibility**
    The Section Box is now invisible when using Cycles.


######
2.0.15
######

*March 11th, 2024*

*********
Bug Fixes
*********

**Minor Fixes**
    Fixed a few minor issues.

**Merge Panels**
    Fixed an issue where the merge panels option did not work properly after restarting Blender.


#####
2.0.9
#####

*January 6th, 2024*

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


 