# 使用“二元值切换”(Double Switch)工具

有关“二元值切换”(Double Switch)工具的描述，请参见[二元值切换](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-44394C98-7A39-45F1-9053-2277FEBC50AC.htm)。

切换 2D 纹理上的双精度浮点型属性，如 2D 纹理的“UV 向重复”(Repeat UV)或“平移帧”(Translate Frame)。

为了方便起见，在开始学习此教程之前，请从 Hypershade 菜单中选择“窗口 > 视口”(Window > Viewport)和“窗口 > 大纲视图”(Window > Outliner)，并将这些面板停靠到 Hypershade 中。请参见[在 Hypershade 中自定义布局](../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/使用%20Hypershade%20构建和创建材质/在%20Hypershade%20中自定义布局.md)。

使用“二元值切换”(Double Switch)工具

1. 创建材质并将其指定给对象。

2. 将 2D 纹理贴图到该材质的某一种属性，如“颜色”(Color)。调整纹理的属性（如有必要）。

3. 贴图 2D 纹理时会创建一个 place2dTexture 节点。在 Hypershade 中选择纹理的 place2dTexture 样例，以在特性编辑器中查看其属性。

4. 将光标放在“UV 向重复”(Repeat UV)属性上，然后在弹出菜单的“创建新纹理”(Create New Texture)上单击鼠标右键。

5. 从“创建渲染节点”(Create Render Node)窗口的“Maya > 工具”(Maya > Utilities)中选择“二元值切换”(Double Switch)工具。请注意，球体可能会丢失其纹理。

  此时，可以在 doubleShadingSwitch 特性编辑器中应用[默认](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-193F9C60-FFAD-4BE6-A11F-B11FBB47B4EA.htm#WS73099CC142F48755-3D114B7511812357EFE-589E)设置。您可以贴图新的纹理或更改 U 和 V 的值。在以下两种情况下，U 和 V 的“默认”(Default)值均更改为 1.5。

  ![图：从“创建渲染节点”(Create Render Node)窗口的“Maya 工具”(Maya Utilities)中选择…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-39F3417F-50E8-4614-A94B-F0359A94EED1.png) <!-- baize:img-hook downloaded=false reason="正文 1258 字 ≥300，非承重" -->

6. 在[大纲视图](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4B9A9A3A-83C5-445A-95D5-64104BC47406)中，使用鼠标中键来选择要为其调整 UV 纹理放置的球体，然后将其拖动到 doubleShadingSwitch “特性编辑器”(Property Editor)的“切换属性”(Switch Attributes)区域的“输入形状”(In Shape)列。

  ![图：在大纲视图中，使用鼠标中键来选择要为其调整 UV 纹理放置的球体，然后将其拖动到 doubleShadingSwitch…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-BFDA9A67-B020-48D2-9C0B-BBB880AF6BB7.png) <!-- baize:img-hook downloaded=false reason="正文 1258 字 ≥300，非承重" -->

  请注意，只有移动到“输入形状”(In Shape)列中的球体会丢失其纹理。这些球体即为要修改的球体。

  ![图：在大纲视图中，使用鼠标中键来选择要为其调整 UV 纹理放置的球体，然后将其拖动到 doubleShadingSwitch…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B4FCE9DA-C41A-415D-AA87-217BE7CCDA7E.png) <!-- baize:img-hook downloaded=false reason="正文 1258 字 ≥300，非承重" -->

7. 按住 Shift 键并选择 inShape 列中的所有行，然后单击鼠标右键并选择“贴图”(Map)。

  ![图：按住 Shift 键并选择 inShape 列中的所有行，然后单击鼠标右键并选择“贴图”(Map)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-1DDAFC2C-AAB0-46B4-9C6A-4CEE6ECDCCC3.png) <!-- baize:img-hook downloaded=false reason="正文 1258 字 ≥300，非承重" -->

8. 从“创建渲染节点”(Create Render Node)窗口的“Maya > 工具”(Maya > Utilities)中选择“2D 放置”(2d Placement)工具。此时将出现“连接编辑器”(Connection Editor)。单击“UV 向重复”(Repeat UV) “输出”(Output)属性（在左列中），然后在右列中，展开 input[0] 并选择 input[0].in Double。根据要映射的球体数，还要选择 input[1].inDouble、input[2].inDouble 等。

  ![图：从“创建渲染节点”(Create Render Node)窗口的“Maya 工具”(Maya Utilities)中选择…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-D64E3736-664B-4CC9-A6FF-220389FBD1A5.png) <!-- baize:img-hook downloaded=false reason="正文 1258 字 ≥300，非承重" -->

  只有在“二元值着色切换”(Double Shading Switch)的特性编辑器中贴图的球体才会进行更新。单击 Hypershade 中的 place2dTexture 样例以打开其特性编辑器，并调整“UV 向重复”(Repeat UV)值（如有必要）。较高的“UV 向重复”(Repeat UV)值可使栅格图案变得更密集。

  ![图：从“创建渲染节点”(Create Render Node)窗口的“Maya 工具”(Maya Utilities)中选择…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-1891799B-48CC-4A9B-9E97-AAD8EB8BA7A6.png) <!-- baize:img-hook downloaded=false reason="正文 1258 字 ≥300，非承重" -->
