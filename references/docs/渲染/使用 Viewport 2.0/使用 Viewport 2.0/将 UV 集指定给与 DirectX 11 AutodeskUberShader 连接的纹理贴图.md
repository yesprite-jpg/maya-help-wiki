# 将 UV 集指定给与 DirectX 11 AutodeskUberShader 连接的纹理贴图

在使用 DirectX 11 AutodeskUberShader 时，可以将 UV 集绑定到与着色器连接的每个纹理，如漫反射贴图、法线贴图等。有关 AutodeskUberShader 的详细信息，请参见 [DirectX 11 Shader](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-21D2A020-EC76-4679-B38A-D5270CE52566)。

将 UV 集绑定到与 AutodeskUberShader 连接的纹理贴图

1. 为对象创建 UV 集或纹理坐标。

  您最多可以绑定 3 个 UV 集。

2. 在 dx11Shader“属性编辑器”(Attribute Editor)的“曲面数据”(Surface Data)部分下，在适当位置为每个 TexCoord 0/1/2 输入 UV 集名称。![图：在 dx11Shader“属性编辑器”(Attribute Editor)的“曲面数据”(Surface Data)部分…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-C0C1B9D8-C98F-4091-9802-1D60B6077FED.png) <!-- baize:img-hook downloaded=false reason="正文 467 字 ≥300，非承重" -->单击鼠标 () 可查看可用选项。必须在 UV 集名称前面添加 uv:，例如 uv:uvSet。默认情况下，TexCoord0 映射到 uv:map1，TexCoord1 映射到 uv:map2，TexCoord2 映射到 uv:map3。

  现在，您已将 UV 集绑定到 DirectX 11 Shader。

3. 在 dx11Shader“属性编辑器”(Attribute Editor)的“UV”部分下，从下拉列表中选择要绑定到每个纹理贴图的 TexCoord 集。
