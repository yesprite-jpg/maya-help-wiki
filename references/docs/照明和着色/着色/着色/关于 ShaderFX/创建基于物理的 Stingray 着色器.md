# 创建基于物理的 Stingray 着色器

可以创建和指定遵循物理定律和能量守恒的、基于物理的着色器。通过 Stingray PBS（基于物理的着色器）节点，可以使用粗糙度贴图、法线贴图和金属贴图对扩散/反射和微曲面细节/反射率进行平衡。

创建基于物理的 Stingray 着色器

1. 请执行下列任一操作：

  - 右键单击对象并选择“指定新材质”(Assign New Material)，然后从“指定新材质”(Assign New Material)窗口中选择 Stingray PBS。

  - 打开 Hypershade 窗口，然后从 Maya 类别下的“表面”(Surface)子类别中选择 Stingray PBS。

    （若要为某对象指定 Stingray PBS，可以使用鼠标中键将材质从 Hypershade 拖至场景中的该对象上，操作过程如同其他 Maya 着色器一样。）

然后可以执行以下操作：

- 将输入纹理贴图连接到着色器。

  默认情况下，Stingray PBS 节点接受“颜色”(Color)、“放射光”(Emissive)和“金属”(Metallic)等贴图输入。如果您仅需要将纹理贴图连接到着色器节点，请参见[将贴图连接到基于物理的 Stingray 着色器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-04F2FFA5-1797-4FEF-8A52-AEE00C47224E.htm)。

- 使用 ShaderFX 节点，在 ShaderFX 编辑器窗口中构建着色器网络。

  如果要自定义 StingrayPBS 节点的着色器图表，可以使用 ShaderFX 编辑器窗口和可用的 ShaderFX 节点构建此图表。请参见[使用 ShaderFX 编辑器构建基于物理的 Stingray 着色器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-DC9B7CAC-B949-4C37-99D0-A1B3D8FD1EC9.htm)。

  有关 Stingray ShaderFX 节点属性的参考信息，请参见 [Stingray 着色器节点参考](http://www.autodesk.com/stingray-help?contextId=shaders_ref_list_globals_cat)。

- 通过将 Stingray PBS 节点与其他 Maya 渲染节点连接在一起，在 Hypershade 中创建着色网络。

## 相关主题

- [关于 ShaderFX 节点](使用%20ShaderFX%20编辑器构建%20ShaderFX%20或%20Stingray%20基于物理的着色器网络/关于%20ShaderFX%20节点.md)

- [使用 ShaderFX 节点](使用%20ShaderFX%20编辑器构建%20ShaderFX%20或%20Stingray%20基于物理的着色器网络.md)

- [ShaderFX 介绍性的采样工作流](创建%20ShaderFX%20着色器/ShaderFX%20介绍性的采样工作流.md)

- [导出基于物理的 Stingray 着色器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-CD59A6C7-CC54-4037-8800-6569711FBD78.htm)
