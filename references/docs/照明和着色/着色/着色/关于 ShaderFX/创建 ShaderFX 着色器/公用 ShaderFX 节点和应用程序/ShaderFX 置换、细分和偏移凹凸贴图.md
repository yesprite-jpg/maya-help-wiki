# ShaderFX 置换、细分和偏移凹凸贴图

## 置换和细分因子

通过将高度（置换）贴图连接到“材质”(Material)节点的“置换”(Displacement)属性，可以向对象添加置换。

若要在 Viewport 2.0 中可视化细分和置换，您必须在 DirectX 11 环境中工作，并且启用 dx11Shader.mll 插件。有关详细信息，请参见[将 DirectX 11 与 Viewport 2.0 结合使用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EE108A86-9830-455E-BF2F-64A4075E8303)。

下图演示了如何连接置换和细分属性：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-27C85066-415D-4CF0-B388-802AA7A05044.png) <!-- baize:img-hook downloaded=false reason="正文 2426 字 ≥300，非承重" -->

  为置换贴图创建一个“纹理贴图”(Texture Map)节点，并将其“颜色”(Color)属性连接到“材质”(Material)节点的“置换”(Displacement)属性。

  创建一个“浮点型”(Float)节点，并将它连接到“材质”(Material)节点的“细分因子”(Tessellation Factor)属性。使用浮点值调整对象的细分量。若要在 Viewport 2.0 中可视化细分量，请选择“材料”(Material)节点并在“属性编辑器”(Attribute Editor)中启用“线框”(Wireframe)选项。设置此浮点值时，应考虑网格的密度是多少；如果网格已经包含大量面，可以使用较小的值，例如 2 或 3。如果网格中没有大量面，可能需要使用较大的值。如果将此值设置得太高，场景可能会变慢；因此，应尝试使用不同的值，以找出最符合您的目的的值。

  ![图：创建一个“浮点型”(Float)节点，并将它连接到“材质”(Material)节点的“细分因子”(Tessellatio…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-700F8464-2BEB-40BA-83B9-B2866037FCDE.png) <!-- baize:img-hook downloaded=false reason="正文 2426 字 ≥300，非承重" -->

  创建一个“法线贴图”(Normal Map)节点，并将它连接到“TraditionalGameSurfaceShader”的“法线”(Normal)属性，如图所示。此步骤是必需的，因为当您置换对象顶点时，法线将因顶点的新位置而变得不正确。您可以通过将具有正确法线值的法线贴图连接到网络来更正此问题。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-CFA51A7B-4BBF-4355-BC93-7C80A999679A.png) <!-- baize:img-hook downloaded=false reason="正文 2426 字 ≥300，非承重" -->

## 向量置换贴图（PNAEN 置换贴图）

通过在“ShaderFX”编辑器中选择“硬件着色器节点 > 纹理 > PNAEN 置换贴图”(Hw Shader Nodes > Textures > PNAEN Displacement Map)来创建此节点。

在“属性编辑器”(Attribute Editor)的“材料”(Material)节点中，您可以通过“置换/选项”(Displacement / Options)属性在提供灰度贴图或向量置换贴图之间选择。

若要在 Viewport 2.0 中可视化细分和置换，您必须在 DirectX 11 环境中工作，并且启用 dx11Shader.mll 插件。有关详细信息，请参见[将 DirectX 11 与 Viewport 2.0 结合使用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EE108A86-9830-455E-BF2F-64A4075E8303)。

下图演示了如何连接法线和高度贴图：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B5A97EC1-EDE6-4EEC-AA0F-6F3937760962.png) <!-- baize:img-hook downloaded=false reason="正文 2426 字 ≥300，非承重" -->

- 创建“PNAEN 置换贴图”(PNAEN Displacement Map)节点（“硬件着色器节点 > 纹理 > PNAEN 置换贴图”(Hw Shader Nodes > Textures > PNAEN Displacement Map)）并将其“颜色”(Color)属性连接到“材质”(Material)节点的“置换”(Displacement)属性。

- 创建一个“浮点型”(Float)节点（“硬件着色器节点 > 值 > 浮点型”(Hw Shader Nodes > Values > Float)），并将它连接到“材质”(Material)节点的“细分因子”(Tessellation Factor)属性。

- 创建一个“法线贴图”(Normal map)节点（“硬件着色器节点 > 纹理 > 法线贴图”(Hw Shader Nodes > Textures > Normal Map)）,并将它连接到“TraditionalGameSurfaceShader”节点的“法线”(Normal)属性。

- 选择“材质”(Material)节点，并在“属性编辑器”(Attribute Editor)中调整下列属性。

  - 将“置换/选项”(Displacement / Options)设置为“VectorDisplacementTangent”或“VectorDisplacementWorld”，具体取决于贴图是在切线还是世界空间中。

  - 从“VDM_CoordSys/选项”(VDM_CoordSys / Options)选择正确的置换轴。轴由生成向量置换贴图的应用程序决定，如 Mudbox。

  - 调整“DisplacementMultiplier”。如果从其创建向量置换贴图的应用程序与 Maya 具有相同的世界缩放，则可以将此值保留为 1。否则，就必须调整此值。

  - 对于向量置换贴图，将“置换偏移”(Displacement Offset)设置为 0（对于灰度置换贴图，将此值设置为 0.5）。

    此属性用于控制置换的基值。

    例如，如果将偏移设置为 0.5，则不会置换灰色部分。黑色会产生缩进。白色将产生挤出。

    同样，如果偏移设置为 0，则不会置换黑色部分。灰色 (0.5) 偏移将挤出 1.0（白色）偏移一半的偏移量。不会产生缩进。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-D49A9ADA-980E-44DB-8F92-6B29F8828581.png) <!-- baize:img-hook downloaded=false reason="正文 2426 字 ≥300，非承重" -->

## 偏移凹凸贴图

通过在“ShaderFX”编辑器中选择“硬件着色器节点 > 纹理 > 偏移凹凸贴图”(Hw Shader Nodes > Textures > Offset Bump Map)创建此节点。

“偏移凹凸贴图”(Offset Bump Map)也称为视差贴图。您可以将法线贴图和其他高度贴图连接到此节点，以便可以更好地表达深度。

下图演示了如何连接法线和高度贴图：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-27229490-DDB3-45D6-BD82-4FBEF78CEAC6.png) <!-- baize:img-hook downloaded=false reason="正文 2426 字 ≥300，非承重" -->

- 在“偏移凹凸贴图”(Offset Bump Map) “属性编辑器”(Attribute Editor)中，连接法线贴图。

- 为高度贴图创建一个“纹理贴图”(Texture Map)节点，并将其“红”(Red)通道连接到“偏移凹凸贴图”(Offset Bump Map)的“高度”(Height)属性。

- 为漫反射贴图创建另一个“纹理贴图”(Texture Map)节点，并将其连接到“TraditionalGameSurfaceShader”的“漫反射颜色”(Diffuse Color)属性。

您可以通过以下方式调整凹凸的高度：选择“偏移凹凸贴图”(Offset Bump Map)并调整“属性编辑器”(Attribute Editor)中的“OffsetAmount”属性。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-13C867AA-6646-49E3-8EB5-CE2BA5EC154F.png) <!-- baize:img-hook downloaded=false reason="正文 2426 字 ≥300，非承重" -->
