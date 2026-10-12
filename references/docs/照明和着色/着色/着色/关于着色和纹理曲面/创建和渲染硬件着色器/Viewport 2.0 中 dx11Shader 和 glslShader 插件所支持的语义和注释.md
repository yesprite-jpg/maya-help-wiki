# Viewport 2.0 中 dx11Shader 和 glslShader 插件所支持的语义和注释

如果您编写自己的自定义着色器在 Viewport 2.0 中使用 dx11Shader 或 glslShader 插件，以下是支持的语义和注释。

## 支持的参数和一致注释

dx11ShaderNode 和 GLSLShaderNode 类在参数和一致 (GLSL) 上查找以下注释并在创建时将相关信息发送给 MUniformParameter 类：

**注**

尽管 OpenGL 着色语言 (GLSL) 不支持注释，但是 OGSFX 支持并且可以用于一致、技术和过程定义。

| **名称** | **类型** | **描述** |
|---|---|---|
| UIOrder | int | 允许在“属性编辑器”(Attribute Editor)中重新排序参数，由于编译器返回的参数顺序并不是始终遵循 FX 文件中的声明顺序，因此尤其有用。UIOrder 最小的参数放在 AE 的顶部，其他参数按 UIOrder 递增顺序添加。 如果未设置，则该参数将按在着色器文件中出现的顺序放置，但位于具有指定 UIOrder 的参数后面。 |
| UVEditorOrder | int | 允许在“UV 纹理编辑器”(UV Texture Editor)中重新排序纹理。“纹理”(Textures)菜单中首先显示 UVEditorOrder 最低的纹理参数。 |
| UIGroup | string | 具有相同 UIGroup 属性的所有参数放在单独的可收拢面板上，其标签为 UIGroup 值。这些面板将插入 UIOrder 最低的组参数所在的位置。 如果未设置（或为空），则该参数不放置在任何命名组中。 |
| Object | string | 将不同的着色器参数分组为相同 Maya 对象的一部分。 这通常用于定义灯光的所有参数。在“属性编辑器”(Attribute Editor)参数布局级别，除了面板默认情况下处于收拢状态以外，其行为与 UIGroup 注释完全相同。当灯光对象名称包含“Light”（或“Lamp”）和“Point”、“Spot”、“Ambient”或“Directional”时，这也用于确定灯光对象的类型。 为每个不同对象创建一个下拉菜单，以轻松连接到现有 Maya 场景灯光。 示例： uniform lightColor : DIFFUSE < Object = "Light0_Spot"; >; uniform lightPosition : POSITION < Object = "Light0_Spot; >; LightColor 和 lightPosition 将绑定到相同灯光节点（可能会是聚光灯）的属性。 |
| UIName | string | 允许在 UI 中重命名参数（“属性编辑器”(Attribute Editor)）。默认情况下，显示变量名称。 |
| SasUiVisible UIType UIWidget | bool 字符串 字符串 | 控制 UI 中变量的可见性。 对于这两个字符串注释，“无”(None)值将隐藏变量。 将 UIType 或 UIWidget 设置为 ColorPicker 以使用“颜色选择器”(Color Chooser)构件。 |
| SasUiMin UIMin uimin | float/int （与参数相同） | 最小范围值。 对应于 MUniformParameter::setRangeMin()。 |
| SasUiMax UIMax uimax | float/int （与参数相同） | 最大范围值。 对应于 MUniformParameter::setRangeMax()。 |
| UISoftMin uisoftmin | float/int （与参数相同） | 范围的最小滑块值。可以在参数的数值输入中输入小于 UISoftMin 但大于 UIMin（如果已指定）的值。 对应于 MUniformParameter::setSoftRangeMin()。 |
| UISoftMax uisoftmax | float/int （与参数相同） | 范围的最大滑块值。可以在参数的数值输入中输入大于 UISoftMax 但小于 UIMax（如果已指定）的值。 对应于 MUniformParameter::setSoftRangeMax()。 |
| UIFieldNames | string | 使用属性值中的字符串为整型参数创建下拉菜单。 格式与 MEL 命令 `attributeQuery -listEnum` 相同，该字符串中用冒号“:”分隔场名称，用等号“=”分隔索引值。索引从零开始，如果未明确指定，项目的索引值等于前一项（如果有）的索引加一。 例如：“着色:线框=8:边界框”定义 3 项，值分别为 0、8 和 9。 |
| ResourceName SasResourceAddress | string | 默认纹理文件名。在设置效果时插件自动加载并连接纹理。 路径可以是绝对路径或相对路径。如果定义的是相对路径，则插件将先尝试搜索与当前 ogsfx 文件位于相同文件夹层次中的文件。 如果未找到该文件，则插件会在 MHWRender::MTextureManager::imagePaths() 中定义的路径下搜索该文件。 |
| TextureType ResourceType | string | 如果变量被描述为不明确纹理，而不是纹理[1D\|2D\|3D\|立方体]，则此注释将允许您指定纹理类型。有效值为“1D”、“2D”、“3D”和“立方体(Cube)”。 |
| Space | string | 允许为位置和方向语义指定默认空间。有效值为“对象(Object)”、“世界(World)”、“视图(View)”和“摄影机(Camera)”。任何其他值均会忽略，且语义仍未定义。 “对象(Object)”对应于：语义 MUniformParameter::kSemanticObjectPos 或 MUniformParameter::kSemanticObjectDir “世界(World)”对应于：MUniformParameter::kSemanticWorldPos 或 MUniformParameter::kSemanticWorldDir “视图(View)”或“摄影机(Camera)”对应于：MUniformParameter::kSemanticViewPos 或 MUniformParameter::kSemanticViewDir |

## 纹理特定参数注释

| **名称** | **类型** | **描述** |
|---|---|---|
| mipmaplevels | int | dx11Shader 允许您控制在技术或纹理描述级别上应加载或生成的 Mip-map 级别数。 请将此注释与纹理描述结合使用。以下值有效。 <val> = 0：为受影响的纹理生成所有 Mipmap 级别。如果纹理中存在任何现有 Mipmap，则会对其进行加载。例如，这允许为 DDS 纹理加载预计算的 Mipmap。 <val> = 1-10：仅生成截至指定级别的 Mipmap。 为了减少纹理内存，dx11Shader 插件的默认值设置为 1，以便只加载/计算第一个 Mipmap 级别 (<val>=1)。 注： 对于 glslShader 和 shaderFX 插件，默认值设置为 0。 还可以强制对每个纹理执行此操作，明确减少内存使用量。 示例实现如下所示： Texture2D DiffuseTexture < string UIName = "Diffuse Map"; string ResourceType = "2D"; int mipmaplevels = <val>; >; 此值优先于为技术注释设置的值 (texture_mipmaplevels)。请参见[支持的技术注释](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D.htm#GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D__SECTION_69F3DD31952242A9A1922AF00307938D)。 有关此注释的使用示例，请参见 Maya 安装文件夹 presets\HLSL11\examples 中的 AutodeskUberShader.fx。 |

## 支持的语义

| **语义** | **类型** | **描述** |
|---|---|---|
| 颜色(Color) | float3/4 (dx11Shader) vec3/4 (glslShader) | 颜色参数：使用“属性编辑器”(Attribute Editor)中的“颜色选择器”(Color Chooser)构件。 |
| Ambient | float3/4 (dx11Shader) vec3/4 (glslShader) | 颜色参数：使用“属性编辑器”(Attribute Editor)中的“颜色选择器”(Color Chooser)构件。 |
| Specular | float3/4 (dx11Shader) vec3/4 (glslShader) | 颜色参数：使用“属性编辑器”(Attribute Editor)中的“颜色选择器”(Color Chooser)构件。 |
| Diffuse | float3/4 (dx11Shader) vec3/4 (glslShader) | 颜色参数：使用“属性编辑器”(Attribute Editor)中的“颜色选择器”(Color Chooser)构件。 |
| TranspDepthTexture | texture | “深度剥离”(Depth Peeling)和“加权平均”(Weighted Average)透明度算法使用的纹理。 |
| OpaqueDepthTexture | texture | “深度剥离”(Depth Peeling)和“加权平均”(Weighted Average)透明度算法使用的纹理。 |

## 灯光特定语义

除了 MUniformParameter 类当前支持的所有语义外，dx11ShaderNode 和 GLSLShaderNode 还添加了额外的灯光特定语义，可将场景灯光的特性绑定到着色器参数。在灯光受 Maya 驱动时，所有支持的参数值将使用绘图上下文中的灯光信息写入。不支持的参数保留着色器中发现的值。这意味着连接点光源将驱动位置参数，而不是方向参数。

| **语义** | **类型** | **Maya 灯光参数** | **描述** |
|---|---|---|---|
| LightColor、Color、 LightDiffuseColor、Diffuse、 LightAmbientColor、Ambient、 LightSpecularColor、Specular | float3/4 (dx11Shader) vec3/4 (glslShader) | 颜色(Color) | 颜色参数：使用“属性编辑器”(Attribute Editor)中的“颜色选择器”(Color Chooser)构件。 值没有预乘灯光强度。 |
| LightIntensity | float | 强度(Intensity) |  |
| LightEnable | bool | 照明(Illuminate)（默认） | 遵循灯光可见性，包括全局灯光设置。如果为 true，则 Maya 灯光处于活动状态且可见。 |
| LightType | int | 类型 | 允许写入连接到任何灯光类型时能正确反应的常规照明代码。有效值为： 2- 聚光灯(2- Spot) 3- 点光源(3- Point) 4- 平行光(4- Directional) 5- 环境光(5- Ambient) 6- 体积光(6- Volume) 7- 区域光(7- Area) |
| Position | float3/4 (dx11Shader) vec3/4 (glslShader) |  | 点光源、聚光灯、区域光和体积光的位置。 对于区域光，位置为区域光的中心。 可以使用注释指定引用空间。 |
| Direction | float3/4 (dx11Shader) vec3/4 (glslShader) |  | 平行光和聚光灯的方向。可以使用注释指定引用空间。 |
| AreaPosition0-3 | float3/4 (dx11Shader) vec3/4 (glslShader) |  | 区域光四个角点的位置。 |
| Hotspot | float | 圆锥体角度(Cone Angle)/半影角度(Penumbra Angle) | 对于聚光灯，一半角度（以弧度为单位）。Hotspot 等于 ConeAngle 和 (ConeAngle+PenumbraAngle) 之中的最小值。 |
| LightFalloff Falloff | float | 圆锥体角度(Cone Angle)/半影角度(Penumbra Angle) | 对于聚光灯，一半角度（以弧度为单位）。Falloff 等于 ConeAngle 和 (ConeAngle+PenumbraAngle) 之中的最大值。 |
| DecayRate | float | 衰退速率(Decay Rate) | 对于聚光灯、点光源、区域光和体积光，表示为指数。 Maya 提供了以下值： 0.0 – 无衰退(0.0 – No Decay) 1.0 – 线性(1.0 – Linear) 2.0 – 二次方(2.0 – Quadratic) 3.0 – 立方(3.0 – Cubic) |
| ShadowFlag | bool | 视情况而定 | 如果为 true，灯光将投射曲面可接收的阴影。仅当全局“阴影”(Shadows)处于启用状态，灯光启用“使用深度贴图阴影”(Use Depth Map Shadows)，且曲面启用“接收阴影”(Receive Shadows)时，该值才为 true。 |
| ShadowColor | float3/4 (dx11Shader) vec3/4 (glslShader) | 阴影颜色(Shadow Color) | 颜色参数：使用“属性编辑器”(Attribute Editor)中的“颜色选择器”(Color Chooser)构件。 |
| ShadowMap | Texture2D |  | 包含由 Maya 计算出的深度贴图阴影纹理。 |
| ShadowMapBias | float | 深度贴图偏移(dmapBias) |  |
| ShadowMapMatrix ShadowMapXForm | float4x4 (dx11Shader) mat4 (glslShader) |  | 查看灯光的变换矩阵 |

## 顶点流的多种属性

| 语义 | 类型 | 说明 |
|---|---|---|
| POSITION | float3/4 (dx11Shader) vec3/4 (glslShader) | 指示 Maya 将此属性绑定到包含这些位置的顶点缓冲区。 |
| NORMAL | float3/4 (dx11Shader) vec3/4 (glslShader) | 指示 Maya 将此属性绑定到法线顶点缓冲区。 |
| TANGENT | float3/4 (dx11Shader) vec3/4 (glslShader) | 指示 Maya 将此属性绑定到切线顶点缓冲区。 |
| BINORMAL | float3/4 (dx11Shader) vec3/4 (glslShader) | 指示 Maya 将此属性绑定到次法线（或双切线）顶点缓冲区。 |
| COLOR0 | float3/4 (dx11Shader) vec3/4 (glslShader) | 指示 Maya 将此属性绑定到颜色集顶点缓冲区。 注： 仅限 glslShader： 目前，只有一个流可用。 尽管 OGSFX 仅限于 COLOR0 语义定义的一个颜色流，但是仍然可以通过使用 TEXCOORDx 语义定义多个颜色流。 使用 vec3 或 vec4 型 TEXCOORDx 语义的属性可用来将颜色流传递给着色器，而使用 vec2 型 TEXCOORDx 语义的属性则可用来传递 UV 坐标流。 |
| TEXCOORD0-7 | float3/4 (dx11Shader) vec2 或 vec3/4 (glslShader) | 指示 Maya 将此属性绑定到 UV 集顶点缓冲区。 目前，有 8 个流可用。 注： 仅限 glslShader： 尽管 OGSFX 仅限于 COLOR0 语义定义的一个颜色流，但是仍然可以通过使用 TEXCOORDx 语义定义多个颜色流。 使用 vec3 或 vec4 型 TEXCOORDx 语义的属性可用来将颜色流传递到着色器，而使用 vec2 型 TEXCOORDx 语义的属性则可用来传递 UV 坐标流。 |

## 硬件雾特定的语义

**注**

当前不支持 glslShader 插件。

| **名称** | **类型** | **描述** |
|---|---|---|
| HardwareFogEnabled | bool | 指定是否已启用硬件雾。 |
| HardwareFogMode | int | 指定雾类型是“线性”(Linear)、“指数”(Exponential)还是“指数平方”(Exponential squared)。 |
| HardwareFogStart | float | 指定在线性雾中使用的近距离。 |
| HardwareFogEnd | float | 指定在线性雾中使用的远距离。 |
| HardwareFogDensity | float | 指定指数雾的密度。 |
| HardwareFogColor | float4 (dx11Shader) vec4 (glslShader) | 指定以 RGBA 值表示的雾颜色。 |

## 选择语义

| **名称** | **类型** | **描述** |
|---|---|---|
| HWS_PrimitiveBase | int | 用于生成对象、第一个组件或第一个几何体实例的颜色的整数。（必须在“Viewport 2.0 选项”(Viewport 2.0 Options)窗口中启用“GPU 实例化”(GPU Instancing)。） 对应于：MUniformParameter::kSemanticHWSPrimitiveBase。 |
| HWS_PrimitiveCountPerInstance | int | 指定需要为每个几何体实例递增 HWS_PrimitiveBase 的量。 对应于：MUniformParameter::kSemanticHWSPrimitiveCountPerInstance。 |
| HWS_ObjectLevel | bool | 指定选择是否要在对象级别完成。 对应于：MUniformParameter::kSemanticHWSObjectLevel。 |
| HWS_FaceLevel | bool | 指定选择是否要在面级别完成。 对应于：MUniformParameter::kSemanticHWSFaceLevel。 |
| HWS_EdgeLevel | bool | 指定选择是否要在边级别完成。 对应于：MUniformParameter::kSemanticHWSEdgeLevel。 |
| HWS_VertexLevel | bool | 指定选择是否要在顶点级别完成。 对应于：MUniformParameter::kSemanticHWSVertexLevel。 |
| HWS_FrontCCW | bool | 指定逆时针三角形是否前置。在生成脂肪点或线时非常有用。 对应于：MUniformParameter::kSemanticHWSFrontCCW。 |
| HWS_InstancedDraw | bool | 指定是否正在绘制几何体实例。 对应于：MUniformParameter::kSemanticHWSInstancedDraw。 |

## 支持的技术注释

| **名称** | **类型** | **描述** |
|---|---|---|
| index_buffer_type | string | 允许通过索引缓冲区生成器和转变器插件指定自定义基本体类型。通常用于细分，以便为着色器提供包含多余数据的索引缓冲区。 dx11Shader/glslShader 项目将包含一个转变器，该转变器可以使用相邻边法线 (PN-AEN) 索引缓冲区生成点法线三角形。请参见“Maya 开发人员帮助”中的“自定义着色器的几何数据”。 对于 dx11Shader/glslShader，请使用以下值： 无值：默认索引缓冲区（默认） “PNAEN9”/“GLSL_PNAEN9”：三角形和相邻边 “PNAEN18”/“GLSL_PNAEN18”：三角形、相邻边、主边和主顶点 与索引转变器的注册名称匹配的任何其他值均可接受。 对应于 MHWRender::MPxPrimitiveGenerator。 |
| texture_mipmaplevels | int | dx11Shader 允许您控制在技术或纹理描述级别上应加载或生成的 Mip-map 级别数。 将此注释与技术定义结合使用，以指定在使用此技术加载纹理时应该生成的 Mipmap 级别。以下值有效。 <val> = 0：为受影响的纹理生成所有 Mipmap 级别。如果纹理中存在任何现有 Mipmap，则会对其进行加载。例如，这允许为 DDS 纹理加载预计算的 Mipmap。 <val> = 1-10：仅生成截至指定级别的 Mipmap。 为了减少纹理内存，dx11Shader 插件的默认值设置为 1，以便只加载/计算第一个 Mipmap 级别 (<val>=1)。 注： 对于 glslShader 和 shaderFX 插件，默认值设置为 0。 还可以强制对每个纹理执行此操作，明确减少内存使用量。 示例实现如下所示： technique11 T0 < bool overridesDrawState = false; int isTransparent = 0; int texture_mipmaplevels = <val>; > 可以与参数注释 mipmaplevels 结合使用，在这种情况下，后者优先。请参见[纹理特定参数注释](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D.htm#GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D__SECTION_4F9C3A41DA47434BBFF815611E9CBAD3)。 |
| isTransparent (dx11Shader) | int | 指定效果的不透明度，允许 Maya 使用正确的过程和消隐。支持的值如下： 0：技术始终是不透明的 1：技术始终是透明的 2：技术的不透明度与使用“不透明度”语义的浮点参数相关，且在不透明度值小于 1.0 时为透明状态。 |
| Transparency (glslShader) | string | 指定是否应该在半透明度模式中渲染此技术。 “Opaque”：不透明（默认） “Transparent”：已启用透明度。 对应于 MPxShaderOverride::isTransparent()。 |
| SupportsAdvancedTransparency | string (bool) | 指定此技术是否支持高级透明度算法（例如，深度剥离）。 如果为 true，则此技术必须为绘制上下文“transparentPeel”、“transparentPeelAndAvg”和“transparentWeightedAvg”定义过程。 “false”：不支持高级透明度（默认值） “true”：支持高级透明度 对应于：MPxShaderOverride::supportsAdvancedTransparency()。 |
| OverridesDrawState | string (bool) | 指定此技术是应该遵循 Maya 的透明对象渲染还是自管（多过程）。 “false”：不覆盖状态（默认值） “true”：自管 对应于：MPxShaderOverride::overridesDrawState()。 |
| OverridesNonMaterialItems | string (bool) | 指定是否应该使用此技术渲染非材质项，如线框和选定边/顶点组件。 此选项特别适用于计算与渲染材质不匹配（导致很难选择）的对象几何体置换的着色效果。 “false”：不覆盖非材质项（默认） “true”：用于渲染非材质项，以便着色器可以显示 UI 基本体 请参见[支持的过程注释](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D.htm#GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D__SECTION_A918E2F899F4430F806D16FEEFCE82B2)中的 DrawContext。 对应于：MPxShaderOverride::overridesNonMaterialItems()。 |
| ExtraScale | float | 指定此技术是否需要额外的比例因子才能应用于对象空间边界框。 这允许此技术指示边界框应该大于基础几何体；通常是由于存在置换等效果，同时防止几何体在移动到视口边缘时或在选择期间被丢弃。 默认值为 1.0。 对应于：MPxShaderOverride::boundingBoxExtraScale()。 |
| VariableNameAsAttributeName | string (bool) | 告知 Maya 使用统一变量名称作为 Maya 属性名称，而不是 UIName（如果存在）。 “false”：使用 UIName 作为属性名称（默认） “true”：使用变量名称作为属性名称 当在着色器文件中定义的 UI 名称已修改时，可用于保持与保存的 Maya 场景向后兼容。 |
| handlesConsolidatedGeometry | string (bool) | 如果设置为 False，则指定应在要应用 glslShader 的几何体上禁用“合并世界”(Consolidate World)功能。 通过技术绘制其计算涉及对象的对象空间坐标（例如，使用世界变换矩阵）的置换时，此注释非常有用。“合并世界”(Consolidate World)会将多个对象的顶点移到一个新的共享对象空间中，因此可能会导致插件着色器渲染错误。在这种情况下，您可能需要禁用“合并世界”(Consolidate World)。 |

## 支持的过程注释

效果可以请求在特定上下文中激活技术中的某些过程，例如绘制阴影深度贴图时。通过添加名为“DrawContext”的字符串注释（用于指定激活过程的上下文）完成此操作。

| **名称** | **类型** | **描述** |
|---|---|---|
| DrawContext | string | 指定应该只为该绘制上下文启用此过程。 多个过程可以具有相同的 DrawContext 值。 这可以是与 MHWRender::MPassContext 中的过程语义匹配的任何字符串值。例如，支持以下上下文：“colorPass”、“shadowPass”、“depthPass”和“normalDepthPass”。 空值（或者如果未设置 DrawContext）等同于将此注释设置为“colorPass”。 对于用于渲染非材质项的过程，设置为“nonMaterialItemsPass”。对于用来选择非材质项的过程，设置为“selectionPass”。请参见上文[支持的技术注释](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D.htm#GUID-13229A83-B6A0-4280-840C-F9C6F40BB13D__SECTION_69F3DD31952242A9A1922AF00307938D)中的 OverridesNonMaterialItems。 |
| PrimitiveFilter | string | 指定此过程可以处理以下组件的渲染： 作为脂肪线的线（线宽 > 1） 作为脂肪点的点（点大小 > 1） 可用于在渲染过程或选择过程中处理边或顶点组件。 顶点组件渲染为四边形而非单像素，边组件在预先选择亮显期间通常会渲染得更大，以获得更好的可见性。 使用几何体着色器将线和点转化为四边形通常可以实现这一点。 “fatLine”：此过程可以将线渲染为四边形 “fatPoint”：此过程可以将点渲染为四边形 如果没有定义处理这种特殊情况的过程，则会使用处理绘制上下文“nonMaterialItemsPass”或“selectionPass”的默认过程。 |

## 全局语义

| **名称** | **类型** | **描述** |
|---|---|---|
| MayaSwatchRender | bool | 标识当前渲染过程何时用于绘制样例。 允许用户在绘制样例时处理特定路径。 |
