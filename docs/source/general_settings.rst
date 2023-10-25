################
General Settings
################

********
Outliner
********

Here are all section boxes listed which are inside the current scene.

**Entry**
 
 Represents one section box inside the current scene, giving you access to the following features.
 
 :Select: By clicking on a listed section box it gets selected and automatically selected in the viewport as well.
          The same goes the other way around, when selecting a section box in the viewport it will be selected automatically in the hierarchy.

 :Rename: By double clicking on a listed section box you can giving it any name you want.

 :Enable: When ticked, the section box is enabled, else the section box gets disabled which is like it doesn't exist.

 :Hide: Toggle whether the bounding box of the section box should be visible or not. This won't affect the visibility of the sections made from the box.

 :Reload: (Collection Section Boxes only!) When changing the content of the collection of a Collection Section Box use this feature to include/exclude the added/removed objects from the section box.

**Operators**

 Manage your section box list with the following features.

 :Add: :ref:`Create` a section box based just like when creating through the *Object Context Menu*.

 :Remove: :ref:`Delete` the selected section box.

 :Move: Either move entries up or down in the list.



General Settings
****************

 Here are all settings located regarding the selected section box.

* **Method**: The technique used for calculating and displaying the sections.
 :Boolean: The sections are created by making use of a dynamic boolean modifier setup.

 :Shader: The sections are created by making use of a custom shader applied to the materials of all affected objects. If there is no material applied, it will automatically create one.

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
     - ✅ *Eevee only*
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


* **(Boolean) Material**: The material which will be applied to the faces capping the sections.
 :From Mesh: The material of the nearby faces will be used respectively, giving the most realistic result.
 :Custom Material: Choose any  material you have available inside your project!


* **(Shader) Color**: The color of the sections.
 :Color: Any RGB color you want! On creation it will be the determined default color in the :ref:`Settings` under the addon preferences.


* **Invert**: When enabled, everything what's inside the section box will be cutted away and everything what's outside will be shown.



Plane Settings
**************

Here are all settings located regarding the 6 individual planes the selected section box consists of.

**Transform**
 * **Plane Transform**: The amount of meters the plane is shifted along the direction of it's normal inside the box.
 * **Edge Transform**: The amount of meters each edge is additionally shifted along the direction of the plane.

**Cross Section**
 * **Enable**: When enabled the cross section will be generated in form of a 2D Mesh floating over the plane.
 * **Distance**: Determine how many meters away the cross section mesh will be from the center of the plane.
 * **Clear Outer**: When enabled the cross section will be also influenced by the sections of the other planes.
 * **Export**:
   **DXF**: Convert the cross section into a DXF file and save it at a location of your choice.
   **Object**: Convert the cross section into a Object which you can work with in Blender.
  :Clean Mesh: Dissolve vertices that don't hold any shape of the cross section.
  :Angle Threshold: Include only vertices that form an lower angle between their adjacent edges than this value.