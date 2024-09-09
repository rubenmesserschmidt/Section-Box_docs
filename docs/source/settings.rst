========
Settings
========

All section box specific settings and features regarding the active box are located under the :ref:`Outliner <menu:outliner>`.

.. hint:: All settings can be set as default by right clicking on them and choosing *Set as Default*.

.. tip:: You can also animate every setting by right clicking it and choosing *Insert Keyframe*. 

#####
Views
#####

Save and load different states of the section box. This works just like a preset system.

**Views List**
    Load a saved state by selecting it from the list.

**Override**
    Override the selected view with the current state of the section box.

**Add**
    Save the current state of the section box as a new view. Make sure to give it a unique name.

**Remove**
    Remove the selected view from the list.



################
General Settings
################

Here are all settings of the active section box located that are affecting the whole box.


******
Method
******

The technique used for calculating and displaying the sections.

**Boolean**
    The sections are created by making use of a dynamic boolean modifier setup.

    :Exact: When enabled, the 'Exact' boolean solver will be used. This is slower but more accurate. Recommended for more complex meshes.
    :Hole Tolerant: When enabled, the boolean will work with meshes containing holes. This makes the section box slower, so only enable it when needed.
    :Self Intersection: When enabled, the boolean will work with meshes intersecting themselves. This makes the section box slower, so only enable it when needed.
    :Material: The material which will be applied to the faces capping the sections.

        :From Mesh: The material of the nearby faces will be used respectively, giving the most realistic result.
        :Custom Material: Choose any  material you have available inside your project!

**Shader**
    The sections are created by making use of a custom shader applied to the materials of all affected objects. If there is no material applied, it will automatically create one.
    
    :Color: The color of the sections. Lowering the alpha value will reduce the coloring of the backfaces (0.0 is no coloring, showing the original material only).
    
.. list-table:: Method Comparison
   :widths: 50 25 25
   :header-rows: 1
    
   * - 
     - Boolean
     - Shader
   * - **Viewport Shading**
     - 
     - 
   * - Wireframe
     - ✅
     - ❌
   * - Solid
     - ✅
     - ❌
   * - Material Preview
     - ✅
     - ✅
   * - Rendered
     - ✅
     - ✅
   * - 
     - 
     - 
   * - **Results**
     - 
     - 
   * - Capping
     - ✅
     - ❌
   * - Customization
     - *Mesh/Any Material*
     - *Flat Color*  
   * - 
     - 
     - 
   * - **Performance**
     - 
     - 
   * - Speed
     - 🟡
     - 🟢
   * - Depends on
     - *Amount Triangles*
     - *Amount Materials*


******
Invert
******

When enabled, everything what is inside the section box will be cut away and everything what is outside will be shown.

##############
Plane Settings
##############

Here are all settings located of the active section plane.

*********
Transform
*********

**Plane Transform**
    The amount of meters the plane is shifted away from the section box.
    Can also be modified in the viewport by using the handles, see :ref:`here <transform:Plane Transform>`.

**Edge Transform**
    The amount of meters each edge is additionally shifted away. This is useful to create diagonal sections.
    Can also be modified in the viewport by using the handles, see :ref:`here <transform:Edge Transform>`.

*******
Section
*******

**Create**
    Create a cross section from the plane. This works only when the plane is intersecting with any objects.

**Update**
    Regenerate the cross section. This will delete the old and create a new one.

**Settings**
    Customize the cross section.
    
    :Entire: When enabled, the cross section will be generated while ignoring all other section planes. To take effect, you need to update the section.
    :Original: When enabled, the cross section will be generated based on the original mesh, instead of the section from the section box.
    :Distance: Meters the generated cross section is away from the plane.
    :Thickness: Line thickness of the generated cross section.
    :Color: Line color of the generated cross section.

*********
Elevation
*********

**Create**
    Create a elevation from the plane. When the plane is intersecting any objects, you need to create a cross section first.

**Link Creation**
    Link the creation of the elevation to the creation of the cross section. This will automatically create a elevation when you create a cross section.

**Settings**
    Customize the elevation.
    
    :Crease: Amount of degrees to which edges are considered in the elevation. Higher values will result in a more detailed elevation. 
    :Link: Link the setting to the cross section. This will automatically update the elevation when you update the cross section.
    :Distance: Meters the generated elevation is away from the plane. (Linkable)
    :Thickness: Line thickness of the generated elevation. (Linkable)
    :Color: Line color of the generated elevation. (Linkable)


******
Export
******

**Format**
    The format of the export.
    
    :DXF: Export the cross section as DXF.
    :Object: Export the cross section into a Object for further use in Blender.

**Clean up**
    Clean up the cross section mesh before export.
    
    :Doubles: Merge vertices that are not further apart than the specified distance. Keep this value as low as possible to avoid merging vertices you want to keep.
    :Dissolve: Dissolve vertices that don't hold the shape of the cross section, specified by a maximum angle. Keep this value as low as possible to avoid dissolving vertices that are holding the shape.