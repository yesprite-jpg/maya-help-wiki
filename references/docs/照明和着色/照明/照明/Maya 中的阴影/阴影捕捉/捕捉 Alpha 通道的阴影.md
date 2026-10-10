# 捕捉 Alpha 通道的阴影

有关阴影的详细信息，请参见 [Maya 中的阴影](../../Maya%20中的阴影.md)。

以下是如何使用背景材质捕捉阴影的一个简单示例。

仅捕捉 Alpha 通道的阴影

1. 在“Hypershade”中，创建使用背景材质并将其指定给阴影捕捉对象。

2. 选择场景投射阴影中的对象。在对象的“属性编辑器”(Attribute Editor)的“渲染统计信息”(Render Stats)区域，请关闭“主可见性”(Primary Visibility)。

3. 渲染场景。

  将在 Alpha 通道捕捉阴影信息。

将“使用背景”指定给替代对象几何体

1. 使用该工作流，以使 3D 对象看起来像在真实环境中。 真实环境通常来自快照或指定给图像平面的实时动作快照。 对象可以将阴影投射到表面上不可见的平面上，该平面可作为阴影捕捉器。

2. 使用场景创建图像平面，在该场景中，要通过执行下列操作放置替代对象几何体。

3. 从当前视图中选择“视图 > 图像平面 > 导入图像”(View > Image Plane > Import Image)。

4. 浏览到所需的文件并单击“导入”(Import)。

  放置图标将显示在当前视图或所有视图中，具体取决于设定的显示模式，并且“图像平面属性编辑器”(Image Plane Attribute Editor)打开。

5. 从“类型”(Type)下拉列表中选择“图像文件”(Image File)或“纹理”(Texture)，然后单击“图像名称”(Image Name)旁边的文件夹图标以将图像平面加载到视图中。

  **注**

  请确保选择“附加到摄影机的图像平面”(Image Plane Attached to Camera)选项在创建替代对象之前将平面放置到所需位置。有关图像平面的详细信息，请参见[图像平面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-60471C15-F6AC-4041-A7D7-5F89A2D2A4DB.htm)。

6. 在“图像平面属性”(Image Plane Attributes)区域设定以下属性：

  - 显示(Display) – 沿摄影机观看

  - 图像平面(Image Plane) – 附加到摄影机

7. 调整透视摄影机，以便构建栅格平面对齐大约要放置对象的位置。

  ![图：调整透视摄影机，以便构建栅格平面对齐大约要放置对象的位置。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-6BBA1CA2-3BC0-46A6-AF80-AC15882FA939.png) <!-- baize:img-hook downloaded=false reason="正文 1097 字 ≥300，非承重" -->

8. 创建和放置要将阴影和反射投射到其上的 NURBS 或多边形平面。

9. 放置要将阴影投射到栅格平面上的替代对象几何体上的对象。

  ![图：放置要将阴影投射到栅格平面上的替代对象几何体上的对象。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-FC5BD1CF-C1AB-449E-97E6-87D9A3B9B336.png) <!-- baize:img-hook downloaded=false reason="正文 1097 字 ≥300，非承重" -->

10. 在“Hypershade”中，创建“使用背景”(Use Background)材质并将其指定给平面。

11. 在场景中创建和放置灯光。打开灯光的“属性编辑器”(Attribute Editor)的“阴影”(Shadows)部分中的“使用深度贴图阴影”(Use Depth Map Shadows)属性，以便在渲染结果中查看阴影。

  ![图：在场景中创建和放置灯光。打开灯光的“属性编辑器”(Attribute Editor)的“阴影”(Shadows)部分中的…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-DDA4026E-470F-41E6-B1B9-ABB23C8E2855.png) <!-- baize:img-hook downloaded=false reason="正文 1097 字 ≥300，非承重" -->

12. 在“渲染视图”(Render View)中渲染场景（要获得最佳结果，请不要 IPR 渲染）。

  ![图：在“渲染视图”(Render View)中渲染场景（要获得最佳结果，请不要 IPR 渲染）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-89C9CD2A-9283-4341-9611-8A0A638CBFC4.png) <!-- baize:img-hook downloaded=false reason="正文 1097 字 ≥300，非承重" -->

13. 调整几何体、灯光以及“使用背景”(Use Background)属性的位置（如果需要），然后随时重新渲染场景。

  ![图：调整几何体、灯光以及“使用背景”(Use Background)属性的位置（如果需要），然后随时重新渲染场景。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-8172D673-30CF-4CF9-B597-843A17A45FAB.png) <!-- baize:img-hook downloaded=false reason="正文 1097 字 ≥300，非承重" -->
