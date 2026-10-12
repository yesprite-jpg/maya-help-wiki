# 有关使用 ShaderFX 的提示和技巧

## Ubershader 预设

UberShaderGraph.sfx 图形可在安装目录的 presets/ShaderFX/Scenes 文件夹下获得。可以将此图表与所有的 OpenGL、OpenGL 核心配置和 DirectX 11 一起使用。但是有些功能（如细分）仅在 OpenGL 核心配置或 DirectX 11 模式下可用。该图形相当于 AutodeskUberShader.fxo 着色器，后者与您在 Hypershade 中创建的 [DirectX 11 Shader](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-21D2A020-EC76-4679-B38A-D5270CE52566.htm) 一起使用。

若要加载此着色器图表，请执行以下操作：

1. 创建“Shaderfx 着色器”(Shaderfx Shader)材质，然后单击“打开 ShaderFX”(Open ShaderFX)以打开 ShaderFX 编辑器。

2. 从 ShaderFX 编辑器菜单中选择“文件 > 导入图表”(File > Import Graph)，然后导航到 presets/ShaderFX/Scenes 文件夹中的 UberShaderGraph.sfx 文件。

## 使用 UV 集

若要选择 UV 集以与“纹理贴图”(Texture Map)节点或“UV 集”(UV Set)节点一起使用，请在“ShaderFX” “属性编辑器”(Attribute Editor)中使用这两个属性中的任一个。如果使用 Maya 创建的默认 UV 集名称，则使用“UV/UV 集索引”(UVs / UV set index)属性。如果使用自定义的 UV 集名称，则必须使用“UV/UV 集名称”(UVs / UV Set Name)属性。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-0A87A35F-915B-49D6-B4E9-3B9EB3AEC996.png) <!-- baize:img-hook downloaded=false reason="正文 939 字 ≥300，非承重" -->

使用默认的 UV 集名称

  默认情况下，UV 集按照如下顺序命名，如下所示：

  - map1

  - uvSet

  - uvSet1

  - uvSet2

  - 依此类推

  如果使用默认的 UV 集名称，则使用“UV/UV 集索引”(UVs / UV set index)来选择您的 UV 集。例如，索引 0 选择 map1，索引 1 选择 uvSet，依此类推。

使用自定义的 UV 集名称

1. 使用“UV 集编辑器”(UV Set Editor)（“创建 UV > UV 集编辑器”(Create UVs > UV Set Editor)）重命名 UV 集。

2. 在“UV/UV 集名称”(UVs / UV set Name)字段中指定自定义 UV 集名称。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-7B407E8F-5602-4955-AF29-56665C736904.png) <!-- baize:img-hook downloaded=false reason="正文 939 字 ≥300，非承重" -->

## 使用 FBX 导出 ShaderFX 节点

如果将场景导出为 FBX 文件，请注意 FBX 不支持导出 ShaderFX 基本体变量节点属性。
