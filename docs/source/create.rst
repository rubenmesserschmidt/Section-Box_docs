Create Section Box
##################


From Selection
**************
 Select all objects you want to include into the section box then choose *Section Box* under the *Object Context Menu* opened with ``RIGHT CLICK`` to instantiate it.
 The new created section box will be exactly bounding all selected objects.

 The section method will be automatically set to either *Boolean* or *Shader* if the active viewport shading mode is *Solid*, *Wireframe* or *Material Preview*, *Rendered* respectively.

|
From Collection
***************
 Select the collection which containing objects you want to include into the section box in the *Outliner* and then choose *Section Box* under the *Object Context Menu* opened with ``RIGHT CLICK`` to instantiate it.
 This section box will be a *Collection Section Box* and will be displayed with a *Collection* icon in the :ref:`Section Box Outliner`.
 
 The instantiation works just like for a normal section box but with the method always set to *Boolean*.
 
 With *Collection Section Boxes* you get the option to :ref:`Reload <Section Box Outliner>`.

|
Empty
*****
 When no objects selected you can create an emtpy section box located at the 3D Cursor by choosing *Section Box* just like when instantiating from a selection.

 This box will detect which objects it's hitting and includes them automatically. This is especially useful in huge scenes with massive amounts of objects.

 *Tip*: :ref:`Reset` the section box to automatically bound all hitted objects afterwards.
 
 


