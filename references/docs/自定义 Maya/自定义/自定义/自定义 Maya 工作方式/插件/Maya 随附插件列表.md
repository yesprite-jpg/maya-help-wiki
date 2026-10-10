# Maya 随附插件列表

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 4204 字 ≥300，非承重" -->

#### AbcBullet.mll

用于缓存 Bullet 模拟的结果，包括导出刚体集和常规刚体模拟。结果保存在仅有动画的 Alembic 文件中。请参见[使用 Alembic 渲染 Bullet 模拟](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C0C66CE1-A2BB-402E-AA16-49F58E8BFB8E)。

#### AbcExport.mll

用于将所有或选定的对象和动画导出到 Alembic 缓存文件中，并将这些文件保存在当前 Maya 项目的 cache\alembic 文件夹中。请参见 [Alembic 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9D272E39-9279-4146-8449-928DDA865C9D)。

#### AbcImport.mll

用于将 Alembic 缓存文件中的数据加载到 Maya 场景中。请参见 [Alembic 缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9D272E39-9279-4146-8449-928DDA865C9D)。

#### animImportExport.mll

可以将动画曲线导入或导出到 API 剪贴板。有关详细信息，请参见“Maya 文档归档”中的“动画曲线”。有关详细信息，请参见 [Maya 文档归档](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D2DE8439-F0D9-41B1-B9BB-F38977E52501)。

#### ArubaTessellator.mll

用于在 Viewport 2.0 中细分 NURBS 并提供良好的性能，特别是对已修剪的曲面尤其如此。请参见[使用 Viewport 2.0](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-677E53F2-E63B-4078-8896-959B3B9BC3AB)。

#### atomImportExport.mll

用于在 Maya 中使用 ATOM（动画传递对象模型）文件格式导入和导出动画。请参见 [ATOM 动画文件格式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A3FB51ED-3023-4E1E-AF20-4D38E2E2FEBD)。

#### AutodeskPacketFile.mll

允许 Maya 识别 Autodesk 数据包文件 (.apf) 文件扩展名。

#### bifmeshio.mll

允许以逐帧 .bif 文件格式缓存多边形网格。请参见[使用 BIF 格式缓存网格](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F4F0A21E-815B-45A1-8030-5318E284202E)。

#### bifrostGraph.mll

激活[适用于 Maya 的 Bifrost Extension](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/files/GUID-DF9366D9-E24B-4A08-88F1-8EE1B78A52F9.htm?guid=Bifrost_MayaPlugin_bifrost_for_maya_html)，这是一个用于实现程序效果的基于节点的框架。

#### bifrostshellnode.mll、bifrostvisplugin.mll

激活 Bifröst 流体模拟框架。请参见 [Bifröst](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F37B36D7-5ABB-4509-B2E6-9F27A3794DA3)。

#### Boss.mll

激活 Bifröst 海洋模拟系统。请参见 [BOSS](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1D4CE594-25ED-4442-9C22-759E3111EFD7)。

#### bullet.mll

用于使用 MayaBullet 的物理学引擎来实现动力学模拟，包括交互的柔体和刚体对象以及受约束的碰撞对象。请参见 [MayaBullet 物理学模拟插件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-88C5DD26-97D2-4972-A3DC-212FEE514175)。

#### cgfxShader.mll

可以创建硬件着色器。请参见 [CgFX 着色器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-93DF9662-E1EA-49E5-8A97-64C491030CD7)。

#### cleanPerFaceAssignment.mll

执行以下操作：

- 跟踪材质连接。

- 如果发现一个材质有多个连接，则合并这些连接。

- 更改指定顺序。

- 返回可以作为 MEL 命令执行的字符串阵列。

#### clearcoat.mll

可以将菲涅尔反射应用到着色器。请参见[透明涂层](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D896F7DC-7E60-402A-ABD9-B00F5BE27065)。

#### deformerEvaluator.mll

用于加速 GPU 上的变形。如果启用“GPU 覆盖”(GPU Override)首选项（在[“动画”(Animation)首选项（在“设置”(Settings)下）](../../../../首选项/首选项/“首选项”%28Preferences%29窗口/“动画”%28Animation%29首选项（在“设置”%28Settings%29下）.md)中），则自动加载此插件。另请参见[使用解算管理器提高性能](../../../../性能提高技巧/性能提高技巧/使用解算管理器提高性能.md)。

#### ddsFloatReader.mll

读取一半（16 位）或 IEEE 32 位浮点 .dds 图像。请参见[显示高动态范围图像](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4B91A24F-1921-4DB2-89EE-E2B90232E465)。

#### dgProfiler.mll

用于打开 DG 分析器。该工具可生成依存关系图所包含的所有节点的分析数据。使用“分析”(Profiling)菜单可将该数据导出到电子表格中，以供进一步分析。请参见 [DG 分析器](../../../../性能提高技巧/性能提高技巧/分析场景以提高性能/DG%20分析器.md)。

#### dx11Shader.mll

用于在 Maya 中显示您自己的 HLSL 着色器。在 DirectX 11 模式下运行 Viewport 2.0 时，该插件可用于创建 DirectX 11 Shader，然后加载自定义的 HLSL 着色器文件。请参见[将 DirectX 11 与 Viewport 2.0 结合使用](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EE108A86-9830-455E-BF2F-64A4075E8303)。

#### fbxmaya.mll

允许 Maya 识别 FBX (.fbx) 文件扩展名。详细信息请参见 [FBX 文件转换器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-18A2CDD7-3334-4FC1-A1B3-A308AD331BB2)。

#### fltTranslator.mll

启用文件与 OpenFlight 的兼容性。详细信息请参见“Maya 文档归档”中的“Maya Open Flight 导入器/导出器”有关详细信息，请参见 [Maya 文档归档](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D2DE8439-F0D9-41B1-B9BB-F38977E52501)。

#### Fur.mll

启用“渲染”(Rendering)菜单集中的“毛发”(Fur)菜单。

#### gameFbxExporter.mll

启用[游戏导出器(Game Exporter)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2DB6E7B0-04B8-4585-91E9-7D64B02D0338)工具（在“文件”(File)菜单中提供），并提供了简化的界面，用于以 FBX 格式导出动画片段或静态网格。

#### GamePipeline.mll

可以启用和禁用“文件”(File)菜单选项，用于将工作导入或导出到 Unity 项目或 Unreal 项目。请参见[将场景导出到 Unity](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-01D019BF-4686-469C-98A1-FDA30C75FFAE) 和[将场景导出到 Unreal Engine 4](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-51B5F746-12B0-4AB5-9701-A0A740D0ADA5)。

#### GameVertexCount.mll

![图：添加“显示 平视显示仪 游戏顶点计数”(Display Heads-up Display Game Vertex Cou…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 4204 字 ≥300，非承重" -->

添加“显示 > 平视显示仪 > 游戏顶点计数”(Display > Heads-up Display > Game Vertex Count)，其中显示当前场景的实时游戏引擎（Unreal 或 Unity）顶点计数。

#### ge2Export.mll

可以使用 GE2 文件格式导出场景。详细信息请参见“Maya 文档归档”中的“Game Exchange 2 转换器”。有关详细信息，请参见 [Maya 文档归档](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D2DE8439-F0D9-41B1-B9BB-F38977E52501)。

#### gpuCache.mll

用于将 Maya 对象和动画导入和导出到 GPU 优化的 Alembic 缓存文件中。请参见[流水线缓存](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9D272E39-9279-4146-8449-928DDA865C9D)。

#### glslShader.mll

可以让您使用 GLSL 着色器材质。请参见 [GLSL 着色器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BD177012-56E1-43D0-B7A5-F4B1A70EA846)。

#### GPUBuiltInDeformer.mll

#### ik2Bsolver.mll

启用 2 骨骼 IK 解算器。有关详细信息，请参见 [IK 解算器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-952FC4B3-19A6-4055-B034-3A7D15EC66D6)。

#### ikSpringSolver.mll

启用 IK 弹簧解算器。详细信息请参见 [IK 弹簧解算器属性](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E71102E0-0BA4-4F9D-9402-E6830889D569#WS17956D7ADBC6E7363438120E117AE30D38F-7FEF)。

#### invertShape.mll

实现某些形变创作工作流。有关详细信息，请参见[形变创作](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B8853C3F-2997-4DC2-95A0-7C43E45888E4)。

#### lookdevKit.mll

使您能够创建单一噪波节点，以及各种数学和工具节点，可用于：创建实体颜色、合成修正节点并为其着色、重新关联 RGBA 通道、预乘和取消预乘节点，等等。此外还提供颜色工具的浮点版本。请参见 [Lookdevkit 数学和工具节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-ED31708F-8C54-4EB2-981D-4FCAFE8E45C9)。

#### matrixNodes.mll

启用用于转化和操作变换矩阵的矩阵工具节点。例如，使用矩阵工具节点可计算某一矩阵的逆矩阵，或者将矩阵分隔为平移、旋转、缩放和斜切组件。请参见[工具节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DA9707D2-8A0D-4911-A010-8274C57D3FD3)。

#### mayaCharacterization.mll

启用 HumanIK 窗口中的“定义”(Definition)选项卡的功能。请参见[“定义”(Definition)选项卡](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-630B5349-213C-414D-B6C9-D283CE319472)。

#### mayaHIK.mll

在 HumanIK 窗口中启用 HumanIK 的核心功能。请参见 [HumanIK 窗口](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9921EDE1-05E2-4062-9F0D-4BADECA29226)。

#### MayaMuscle.mll

启用 Maya 肌肉插件并在所有菜单集中加载“肌肉”(Muscle)菜单。

#### mayaUSDPlugin.mll

![图：启用 Maya USD 插件。请参见 Maya USD 插件。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 4204 字 ≥300，非承重" -->

启用 Maya USD 插件。请参见 [Maya USD 插件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9E9D45F2-4DA9-497B-8D69-1573ED6B2BA8)。

#### MayaToAlias.mll

使用 OpenMaya API 检索场景数据，然后使用 OpenModel 导出。有关详细信息，请参见“Maya 文档归档”中的“MayaToAlias 导出插件”。有关详细信息，请参见 [Maya 文档归档](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D2DE8439-F0D9-41B1-B9BB-F38977E52501)。

#### mayaVnnPlugin.mll

Bifrost Extension 和其他应用程序使用的图表编辑组件。

#### melProfiler.mll

用于打开 MEL 分析器。此分析系统用于监视工具使用情况，并记录确定瓶颈所需的度量标准。此外，分析数据还可用于快速而轻松地诊断 MEL 工具集。请参见 [MEL 分析器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F2D6E921-DA8C-4FD8-B8E7-EFEB3CBF9D74)。

#### modelingToolkit.mll

用于访问“建模工具包”(Modeling Toolkit)窗口。此工具集提供了用于多边形建模的附加功能。请参见[建模工具包](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D4CD168A-34F2-465B-A39C-DE20B34E5535)。

#### nearestPointOnMesh.mll

可以访问 closestPointOnMesh 节点。

#### objExport.mll

允许 Maya 将场景导出为 Object (.OBJ) 文件扩展名。

#### OneClick.mll

用于在 Maya 和 3ds Max、Softimage、MotionBuilder 以及 Mudbox 之间发送信息。请参见[将对象发送到其他 Autodesk 应用程序](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-255C3C84-DCDD-4E79-999F-F1464E241E72)。

#### OpenEXRLoader.mll

启用文件与 OpenEXR 的兼容性。有关详细信息，请参见[显示高动态范围图像](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4B91A24F-1921-4DB2-89EE-E2B90232E465)。

#### quatNodes.mll

启用四元数工具节点。例如，使用四元数相加、共轭、反转和归一化节点可操纵和操作四元数。同时，还提供了转化节点，用于更改四元数以改变旋转表示，例如，Euler 角。请参见 [Maya 中的动画旋转](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-CBD30A0A-1166-4076-A564-1ADC946A15F3)。

#### retargeterNodes.mll

用于将 HumanIK 动画重定目标至 Maya 自定义绑定（非 HumanIK 绑定）以及从该 Maya 自定义绑定对 HumanIK 动画进行重定目标。请参见[“自定义绑定”(Custom Rig)选项卡概述](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-803B17FD-B73C-485F-8976-D4478F821218)。

#### rotateHelper.mll

可以访问 rotateHelper 节点。

#### rtgExport.mll

可以一般性输出 Maya 场景信息。有关详细信息，请参见“Maya 文档归档”中的“RTG 工具和文件格式”。有关详细信息，请参见 [Maya 文档归档](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D2DE8439-F0D9-41B1-B9BB-F38977E52501)。

#### sceneAssembly.mll

用于在 Maya 工作流中使用场景集合节点和表示。请参见[场景集合](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6222C2F5-320E-484A-88A3-8B56F9B3A9DC)。

#### shaderFXPlugin.mll

ShaderFX 是实时着色器编辑器，可用于通过连接不同的着色节点创建高级视口着色器。请参见[关于 ShaderFX](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EBC6DF48-857D-4230-9D3C-0B04DAF58403)。

#### stereoCamera.mll

可以让您使用立体摄影机类型。有关详细信息，请参见[使用立体摄影机](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0771E796-7B22-4428-8507-BDF67780E635)。

#### stlTranslator.mll

可以导入/导出 STL 文件。

#### studioImport.mll

可以导入 Alias® Studio® 线文件。详细信息请参见“Maya 文档归档”中的“StudioImport 插件和转换器”。有关详细信息，请参见 [Maya 文档归档](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D2DE8439-F0D9-41B1-B9BB-F38977E52501)。

#### tiffFloatReader.mll

读取 IEEE 32 位浮点 .tif 图像。有关详细信息，请参见[显示高动态范围图像](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4B91A24F-1921-4DB2-89EE-E2B90232E465)。

#### Turtle.mll

Turtle 是一个复杂的烘焙插件，用于在游戏开发中创建照明和内容。使用 Turtle，您可以：

- 创建炫目的游戏级别全局照明

- 将照明烘焙到纹理贴图、顶点贴图或点云。

- 将遮挡和法线贴图从详细模型烘焙到低多边形模型。

#### Type.mll

启用类型和 SVG 工具，通过这些工具可以按设置了样式的文本或向量图形的形状创建多边形。有关详细信息，请参见[创建多边形文本](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5715F385-F27A-49E0-A624-CB376B669EDC)。

#### Unfold3D.mll

启用展开 3D，展开 3D 是更快、更可靠的算法，可替代旧版展开算法。请参见[展开 UV 网格](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6C2B784F-DE8A-4702-8FD5-6FBB8340C9C5)。

#### VectorRender.mll

启用 Maya 矢量渲染器。详细信息请参见 [Maya 向量渲染器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-973D2F51-EB45-49FF-8767-6DE669A2CA5D)。
