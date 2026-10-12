# 创建 HLSL 着色器

dx11Shader.mll 是用于创建 Direct X 着色器的首选插件。因此，不再随标准 Maya 安装提供 HLSL 插件。

为了向后兼容，可以从 Maya Bonus Tools 软件包（从 Maya 菜单中选择“帮助 > Maya 资源和工具 > 下载 Bonus Tools”(Help > Maya Resources and Tools > Download Bonus Tools)）下载 hlslShader.mll，或者从 [Autodesk Developer Network](https://www.autodesk.com/developmaya) 上的开发人员工具包中下载 *hlslShader* 插件示例。

加载 HLSL 插件

1. 选择[窗口 > 设置/首选项 > 插件管理器(Window > Settings/Preferences > Plug-in Manager)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2CF7D90B-EF10-40D1-9129-9D401CCAB952)。

  将显示“插件管理器”(Plug-in Manager)。

2. 加载 hlslShader.mll 插件。

  有关“插件管理器”(Plug-in Manager)的详细信息，请参见[插件管理器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2CF7D90B-EF10-40D1-9129-9D401CCAB952)。

3. 单击“关闭”(Close)。

创建“HLSL 着色器”(HLSL Shader)材质

1. 在“Hypershade”中，从“Maya > 表面”(Maya > Surface)列表中选择“HLSL 着色器”(HLSL Shader)材质。

  在“Hypershade”中将显示新着色材质，而在“属性编辑器”(Attribute Editor)中将显示“HLSLShader”材质节点。

  ![图：在“Hypershade”中，从“Maya 表面”(Maya Surface)列表中选择“HLSL 着色器”(HLSL …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-DC4C7007-7E42-4468-8064-B94EAF32BAB5.png) <!-- baize:img-hook downloaded=false reason="正文 1029 字 ≥300，非承重" -->

2. 在“着色器”(Shader)区域中，键入到要使用的 .fx 文件的路径，或浏览到 .fx 文件。

  在 hlslShader 节点上配置了 .fx 文件之后，插件会自动将属性（如果存在）加载到“属性编辑器”(Attribute Editor)中。

3. 打开“属性编辑器”(Attribute Editor)，并在必要时调整任何属性。

4. 将新“HLSL 着色器”(HLSL Shader)材质指定给场景中的对象。详细信息请参见[将现有材质指定给曲面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-D41AF807-F7CB-447E-BACC-7F0867C14E8D.htm)。

5. 在场景视图中，打开[面板菜单：“着色”(Shading)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C6188583-EA9E-4880-AAE7-8D895FD94DD6)设置中的“硬件纹理”(Hardware Texturing)。

## 支持将纹理放置到 HLSL 着色器中

因为纹理查找是由硬件着色代码本身执行的，Maya 无法为其原生纹理放置节点提供自动支持。

如果希望将 Maya 的纹理放置节点与硬件着色器一起使用，则必须在着色器代码内实施纹理放置计算，然后将放置参数显示为着色器上的一致参数。然后可以将代表这些纹理放置一致参数的属性连接到 Maya 的纹理放置节点上的相应属性，从而使美工人员能够随意将该节点用于本地 Maya 着色器。
