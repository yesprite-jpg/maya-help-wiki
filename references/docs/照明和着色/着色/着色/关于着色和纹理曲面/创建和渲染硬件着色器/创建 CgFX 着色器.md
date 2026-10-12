# 创建 CgFX 着色器

Cgfx 着色器基于传统技术，因此不再建议使用。请改用 [GLSL 着色器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-BD177012-56E1-43D0-B7A5-F4B1A70EA846.htm)。

CgFX 着色器仅在“OpenGL - 旧版”(OpenGL - Legacy)和“OpenGL - 核心配置(兼容性)”(OpenGL - Core Profile (Compatibility))显示模式下受支持。请参见 [Viewport 2.0 渲染引擎](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BF017019-B89A-47F0-8AB5-106C058AB854#GUID-BF017019-B89A-47F0-8AB5-106C058AB854__SECTION_B04F0E5A1332417DA2CD3FE483F186D4)。

加载 CgFX 插件

1. 选择窗口 > 设置/首选项 > 插件管理器(Window > Settings/Preferences > Plug-in Manager)。

2. 在[插件管理器(Plug-in Manager)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2CF7D90B-EF10-40D1-9129-9D401CCAB952)中加载该插件，然后单击 “关闭”(Close)。

创建“CgFX 着色器”(CgFX Shader)材质

1. 在“Hypershade”中，从“Maya > 表面”(Maya > Surface)列表中选择“CgFX 着色器”(CgFX Shader)材质。

  “Hypershade”中将出现新的着色材质，并且“属性编辑器”(Attribute Editor)中将出现“CgFXShader”材质节点。

  ![图：在“Hypershade”中，从“Maya 表面”(Maya Surface)列表中选择“CgFX 着色器”(CgFX …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-14BCABC1-983B-4039-AE58-1596845E3FD2.png) <!-- baize:img-hook downloaded=false reason="正文 1203 字 ≥300，非承重" -->

2. 在“CgFX 着色器”(CgFX Shader)部分中，键入需要使用的 .cgfx 文件的路径，或浏览到 .cgfx 文件。

  一旦 .cgfx 文件连接到 CgFXShader 节点，插件会自动将属性（如果存在）加载至“属性编辑器”(Attribute Editor)的“附加属性”(Extra Attributes)部分中。

3. 打开“附加属性”(Extra Attributes)部分，然后根据需要调整任何属性。

4. 将新的“CgFX 着色器”(CgFX Shader)材质指定给场景中的对象。详细信息请参见[将现有材质指定给曲面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-D41AF807-F7CB-447E-BACC-7F0867C14E8D.htm)。

5. 在场景视图中，打开[面板：“着色”(Shading)菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C6188583-EA9E-4880-AAE7-8D895FD94DD6)中的“硬件纹理”(Hardware Texturing)。

## 将放置添加到 CGFX 着色器

由于 Cgfx 是一个使用可编程着色语言的节点，因此，Cgfx 着色器不会自动支持在 Maya（place2DTexture 节点或 place3DTexture 节点）内找到的纹理放置。使用此语言意味着无法从外部设定纹理变换。相反，它必须明确编码至着色器中。如果这类参数仅次于着色器中，则自动 UI 生成功能将创建 UI 元素。然后，您应将适当的属性从纹理放置节点连接到着色器内的属性。

## 重新加载、编辑并查看 CgFX 文件

在“cgfxShader”节点的“属性编辑器”(Attribute Editor)中，可以使用“重新加载”(Reload)、“编辑”(Edit)和“打开”(Open)按钮来使用指定的 FX 文件。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-7CEC47E3-5052-43E4-BEC4-0F2EB0FFD6A1.png) <!-- baize:img-hook downloaded=false reason="正文 1203 字 ≥300，非承重" -->

#### 重新加载(Reload)

从磁盘中重新加载指定的 CgFx 文件。

#### 编辑(Edit)

在 Windows 的 Microsoft® 记事本以及 Linux 的vi 中，打开指定的 CgFx 文件进行编辑。根据需要编辑并保存文件。Maya 将自动重新加载 CgFx 文件。

#### 打开(Open)

在 Windows 的记事本以及 Linux 的 vi 中，以只读格式打开指定的 CgFx 文件。
