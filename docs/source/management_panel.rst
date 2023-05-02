Management Panel
################


Section Box List
****************

Here are all section boxes listed which are inside the current scene.

**List Entry**
 
 Represents one section box inside the current scene, giving you access to the following features.
 
 :Select: By clicking on a listed section box it gets selected and automatically selected in the viewport as well.
          The same goes the other way around, when selecting a section box in the viewport it will be selected automatically in the hierarchy.

 :Rename: 

 :Enable: When ticked, the section box is enabled, else the section box gets disabled which is like it doesn't exist.

 :Hide: Toggle whether the bounding box of the section box should be visible or not. This won't affect the visibility of the sections made from the box.

 :Reload: (:ref:`Collection Section Box <From Collection>` only!) When changing the content of the collection of a Collection Section Box use this feature to include/exclude the added/removed objects from the section box.

|
**List Operators**

 Manage your section box list with the following features.

 :Add: :ref:`Create <Create Section Box>` a section box based just like when creating through the *Object Context Menu*.

 :Remove: :ref:`Delete <Delete Section Box>` the selected section box.

 :Move: Either move entries up or down in the list.


|
Section Box Settings
********************

 Here are all settings located regarding the whole section box.

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