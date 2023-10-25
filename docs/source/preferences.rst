###########
Preferences
###########


****************
General Settings
****************
 
**Lazy Load**
 When enabled the section will be updated only after committing a transform change of a section box using the *Boolean* method.
 Else it will be updated in realtime always. This is especially useful when working with higher amounts of triangles to save performance while transforming a section box.

:Default: ``Enabled``

**Method**
 The method you want to use to create a section box. The *Shader* method is faster but does not support solid viewport shading.

:Default: ``Shader``

**Margin**
  The margin of the section box. This is the distance between the section box and the actual geometry to prevent z-fighting and unintentional cutting. Use 0.0 to disable the margin.
  :Default: ``0.01``

**Empty Size**
 The default size of an :ref:`Empty Section Box <Create>`.
 :Default: ``2.0 (Default Cube Size)``

***********
UI Settings
***********

**Show Menu**
 When enabled the create section box operator will be displayed inside the *Object Context Menu*.
 Else you can only create section boxes through the :ref:`Outliner`.
 :Default: ``Enabled``

**Select Radius**
 The hitbox radius of the section box handles. This is the distance from the mouse cursor to the handle to select it.
 :Default: ``30``

**Handle Color**
  The standard color of the section box handles.
  :Default: ``R:0 G:0 B:0 A:0.5``

**Handle Color (Active)**
  The color of the active section box handle.
  :Default: ``R:0 G:0 B:0 A:1``

**Handle Hover Scale**
  The increase in scale of the section box handles when hovering over their hitbox with the cursor.
  :Default: ``1.2``

******
Keymap
******

**Select**
 The mouse button you use to select objects in Blender.
 :Default: ``LEFT MOUSE BUTTON``

**Reset**
 The key you want to use to reset a section box to its original bounds.
 :Default: ``BACKSPACE``

**Delete**
 The key you want to use to delete a section box.
 :Default: ``X``

**Edge Mode**
  The key you want to use to toggle edge mode.
  :Default: ``E``

*****
Addon
*****

**Merge Panels**
 When enabled the panel of the addon will be under the "Ruben's Addons" category among the panels of my other addons.
 Else it will be under the "Section Box" category.
 :Default: ``Disabled``

**Check for Updates**
 Check if the addon is up to date. This requires an internet connection.

**Auto check on startup**
  Check for updates automatically when Blender starts.
  :Default: ``Enabled``


