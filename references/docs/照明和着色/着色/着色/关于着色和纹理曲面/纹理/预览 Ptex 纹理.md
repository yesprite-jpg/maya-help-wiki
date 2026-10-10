# 预览 Ptex 纹理

可以预览“Viewport 2.0”中输入的指定给任何标准 Maya 着色网络纹理的 Ptex 纹理。

**注**

仅可以在 Viewport 2.0 和支持 Ptex 的第三方渲染器中预览 Ptex。将 Ptex 与 Maya 软件渲染器一起使用时，不支持默认的高质量视口。

若要使用该功能，Ptex 文件的拓扑**必须**与网格的拓扑匹配。

在 Maya 场景文件中使用 Ptex

1. 选择“渲染器 > Viewport 2.0”(Renderer > Viewport 2.0)以切换到 Viewport 2.0。

2. 选择渲染器 > Viewport 2.0 (Renderer > Viewport 2.0) > ![图：选择渲染器 Viewport 2.0 (Renderer Viewport 2.0) 。会将 Ptex 信息烘焙到 2D…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 618 字 ≥300，非承重" -->。会将 Ptex 信息烘焙到 2D 纹理中。将“不支持的纹理的烘焙分辨率”(Bake Resolution for Unsupported Textures)下的“颜色纹理”(Color Textures)属性设定为所需的分辨率。详细信息请参见 [Viewport 2.0 选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9BBB6035-2A02-41BB-AF2D-99D9BEE580F1)。

3. 将“文件”(File)节点指定给对象的曲面着色器。

4. 在“文件”(File)节点中，单击“浏览”按钮，然后选择 Ptex 文件。

**注**

若要显示高质量的 Ptex 纹理，应提高

“颜色纹理”(Color Textures)

分辨率，例如提高至 2048。调整

“颜色纹理”(Color Textures)

分辨率后，必须单击

“重新烘焙所有纹理”(Re-bake All Textures)

以查看更改效果。

**注**

注意：

会忽略

“文件”(File)

节点上的所有属性，

“图像名称”(Image Name)

属性除外。
