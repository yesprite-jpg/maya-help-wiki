# 在“属性编辑器”(Attribute Editor)中显示 ShaderFX 节点

## 将 ShaderFX 节点显示为属性

在“ShaderFX”编辑器中创建节点时，可以将该节点作为属性显示在“属性编辑器”(Attribute Editor)中。这样便可以调整其值，而不必打开“ShaderFX”编辑器。

打开“ShaderFX”编辑器后，选择节点，然后单击 ShaderfxShader“属性编辑器”(Attribute Editor)中的“显示为材质输入”(Expose as Material Input)。

**注**

当禁用

“属性编辑器”(Attribute Editor)

中的

“显示为材质输入”(Expose as Material Input)

后，在

“属性编辑器”(Attribute Editor)

中设置的所有值都将还原为其原始值。

现在，关闭“ShaderFX”编辑器后，该属性会在“属性编辑器”(Attribute Editor)的“属性”(Attributes)部分（ShaderfxShader 选项卡）中提供。现在可以调整该属性，并查看其在场景中的实时更新。

**注**

如果您单击节点上的“渲染样例”(Render Swatch)图标

，则其预览样例中的颜色可能未与其在

“属性编辑器”(Attribute Editor)

中的颜色同步。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E113529A-3991-4BDC-8EA6-905637DE6357.png) <!-- baize:img-hook downloaded=false reason="正文 1365 字 ≥300，非承重" -->

### 在“属性编辑器”(Attribute Editor)中为 ShaderFX 属性分组

默认情况下，所有启用了“显示为材质输入”(Expose as Material Input)的节点都将显示在“属性编辑器”(Attribute Editor)中，并将在“属性”(Attributes)下方进行分组。为了更好地组织，可以为每个节点提供组名，并且每个节点都列在“属性编辑器”(Attribute Editor)中自己所属的组下方。

在本示例中，组名称 MyGroupColor 将添加到“颜色”(Color)中，MyGroupVal 将添加到“浮点型”(Float)中。每个节点都已启用“显示为材质输入”(Expose as Material Input)属性。

当您关闭“ShaderFX”编辑器时，“颜色”(Color)将显示在类别 MyGroupColor 下方，“Val”将显示在类别 MyGroupVal 下方。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A2E95803-CA3B-429C-9B5C-201B76A776EB.png) <!-- baize:img-hook downloaded=false reason="正文 1365 字 ≥300，非承重" -->

## 将 ShaderFX 节点添加为设置

在 Advanced Mode 中，一些节点还具有名为 Expose as Setting 的选项。

启用该选项后，该参数将在“属性编辑器”(Attribute Editor)的“设置”(Settings)部分可用。

“设置”(Settings)不同于“属性”(Attributes)，因为它们根据新的设置值触发着色器重新生成操作，而属性仅更新现有着色器内的值。

设置通常与 Path Direction 或 Skip 节点结合使用，以根据特定条件确定要在图表中采用的路径。例如，启用或禁用细分或不透明度的使用。

在此示例中，创建了 Bool Value 节点，并将其命名为 UseTexture 以更好地体现其用途。已启用其 Expose as Setting 属性，因此，在关闭“ShaderFX”编辑器时，您可以在“属性编辑器”(Attribute Editor)的 Settings 部分将其值设置为“True”或“False”。将 UseTexture 设置为 True 时，TextureMap 将提供漫反射颜色。当设置为 False 时，Color 提供漫反射颜色。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-DC933C00-DE14-406D-886E-7553E8AD3649.png) <!-- baize:img-hook downloaded=false reason="正文 1365 字 ≥300，非承重" -->
