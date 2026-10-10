# 在“灯光编辑器”(Light Editor)中启用或禁用灯光

您可以禁用灯光，使其不会影响场景。切换 ![图：您可以禁用灯光，使其不会影响场景。切换 可启用或禁用灯光，或者选择灯光并在“特性编辑器”(Property Editor…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-27B575D0-61B0-4C25-9CE9-3CF915264C93.png) <!-- baize:img-hook downloaded=false reason="正文 712 字 ≥300，非承重" --> 可启用或禁用灯光，或者选择灯光并在“特性编辑器”(Property Editor)中**切换其“启用”(Enable)属性**。

在“灯光编辑器”(Light Editor)中，**禁用的灯光会显示带对角线图案**。

禁用灯光组可同时禁用其所有成员灯光。请参见[在灯光编辑器中创建和分组灯光](创建和分组灯光.md)。

**注**

提示：

您也可以

隔离灯光

。

如果已使用渲染设定系统将场景划分为不同的层，则可以通过**在“启用”(Enable)属性上创建覆盖**，来**禁用单个层的灯光**。请参见 [Maya 渲染设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-646154F9-E4D2-4A3E-A0D9-B2F062960A4E)或[在渲染层中创建灯光覆盖](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1E0804B5-F81E-4CF4-81A6-BB821790A63B)。

## “灯光编辑器”(Light Editor)和“属性编辑器”(Attribute Editor)之间的关系

打开“灯光编辑器”(Light Editor)会在该编辑器与场景中灯光形状节点上的“可见性”(Visibility)属性之间创建连接。通过此连接，您可以使用“灯光编辑器”(Light Editor)的“启用”(Enable)和“隔离”(Isolate)属性控制灯光的可见性；但是，“属性编辑器”(Attribute Editor)中的“可见性”(Visibility)开关也变得不可用。若要启用或禁用灯光，请改为使用“灯光编辑器”(Light Editor)。

**注**

如果您右键单击

“可见性”(Visibility)

属性并选择

“断开连接”(Break Connection)

，则在

“灯光编辑器”(Light Editor)

中，相应灯光的

图标显示为带红色边框，以指示您无法再使用此图标来控制灯光。您可以通过

“属性编辑器”(Attribute Editor)

继续控制灯光的可见性；或者，关闭并重新打开

“灯光编辑器”(Light Editor)

以再次使用它。
