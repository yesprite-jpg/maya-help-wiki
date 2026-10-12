# 在 ShaderFX 中可视化透明度

在“ShaderFX”编辑器中，将透明度值连接到“TraditionalGameSurfaceShader”着色器的“不透明度”(Opacity)属性。

**注**

提示：

若要防止透明对象阻止渲染其后的对象，请选择

“材质”(Material)

节点，然后在

“属性编辑器”(Attribute Editor)

中，禁用

“深度写入”(Depth Write)

。

若要防止对象进行双面渲染，您可以选择对象的形状节点，然后在“属性编辑器”(Attribute Editor)中的“渲染统计信息”(Render Stats)部分中禁用“双面”(Double Sided)。

为获得最佳透明度质量，请选择“渲染器 > Viewport 2.0”(Renderer > Viewport 2.0) > ![图：为获得最佳透明度质量，请选择“渲染器 Viewport 2.0”(Renderer Viewport 2.0) ，然后选…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 393 字 ≥300，非承重" -->，然后选择“深度剥离”(Depth Peeling) “透明度算法”(Transparency Algorithm)。但是，此选项牺牲性能来提供高质量。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-130910C0-3F35-4C45-B2D3-F7CC7D0BE032.png) <!-- baize:img-hook downloaded=false reason="正文 393 字 ≥300，非承重" -->
