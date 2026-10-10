# FBX 导出 MEL 命令

以下 MEL 命令用于模拟 FBX 导出用户界面中的导出选项。

#### FBXExport

FBXExport -f [filename] [-s];

导出指定的文件。

如果要更改导出过程以便导出选定的对象而非执行“导出全部”操作，请添加 -s 标志。

例如：

```text
FBXExport -f myfile.fbx -s
```

#### FBXExportAnimationOnly

FBXExportAnimationOnly -v [true|false];

FBXExportAnimationOnly -q;

使用此脚本仅导出动画。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“动画”(Animation)。

#### FBXExportApplyConstantKeyReducer

FBXExportApplyConstantKeyReducer -v [true|false];

FBXExportApplyConstantKeyReducer -q;

这是一个功能相当于 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中“固定关键帧减少器”(Constant Key Reducer)的脚本。

##### True

通过“固定关键帧减少器”(Constant Key Reducer)过滤 FBX 动画 FCurve。这样可消除 FCurve 上的固定关键帧，有助于减小重采样的 FCurve 的大小，特别是“比例”(Scale)。

##### False

将此命令设置为 False，可确保动画数据不会被过滤。

#### FBXExportAxisConversionMethod

FBXExportAxisConversionMethod [none|convertAnimation|addFbxRoot];

FBXExportAxisConversionMethod -q;

通过此命令，可以设置导出转化方法。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“轴转化”(Axis conversion)。

##### 无

不会发生转化并且导出的数据不会受到影响。

##### 转化动画

重新计算所有动画 FCurve，以便它们的值反映新的世界系统。

##### 添加 Fbx_Root 节点

在场景顶部添加变换节点，以包含将数据传输到新的世界系统所需的变换。此选项可以帮助实现向后兼容，因为它使用与早期版本插件使用的相同方式生成 FBX 文件。

**注**

如果插件未检测到转化需求，将不会添加 Fbx_Root 节点。

#### FBXExportBakeComplexAnimation

FBXExportBakeComplexAnimation -v [true|false];

FBXExportBakeComplexAnimation -q;

该命令是功能相当于烘焙动画(Bake animation)选项的脚本。请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“烘焙动画”(Bake Animation)。

#### FBXExportBakeComplexEnd

FBXExportBakeComplexEnd -v [int];

FBXExportBakeComplexEnd -q;

此命令是功能相当于烘焙动画(Bake animation)选项中“结束”(End)字段的脚本。传递的值是一个整数。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“烘焙动画”(Bake Animation)。

#### FBXExportBakeComplexStart

FBXExportBakeComplexStart -v [int];

FBXExportBakeComplexStart -q;

此命令是功能相当于烘焙动画(Bake animation)选项中“开始”(Start)字段的脚本。传递的值是一个整数。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“烘焙动画”(Bake Animation)。

#### FBXExportBakeComplexStep

FBXExportBakeComplexStep -v [int];

FBXExportBakeComplexStep -q;

该命令是功能相当于烘焙动画(Bake animation)选项中“步长”(Step)字段的脚本。传递的值是一个整数。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“烘焙动画”(Bake Animation)。

#### FBXExportBakeResampleAnimation

FBXExportBakeResampleAll -v [true|false];

FBXExportBakeResampleAnimation -q;

该命令是“FBX 导出器”(FBX Exporter)中“对动画重采样”(Resample Animation)选项的脚本版本。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“全部重采样”(Resample All)。

#### FBXExportCacheFile

FBXExportCacheFile -v [true|false];

FBXExportCacheFile -q;

此命令是“FBX 导出器”(FBX Exporter)中“几何体缓存文件”(Geometry Cache file)选项的脚本版本。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“几何体缓存文件”(Geometry Cache File(s))。

**注**

必须将选择集应用于

“对象变换节点”(Objects Transform node)

，而不是

“图形节点”(Shape node)

。

#### FBXExportCameras

FBXExportCameras -v [true|false];

FBXExportCameras -q;

使用该函数可以在 FBX 导出中包括或排除摄影机。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中的“摄影机”(Cameras)。

#### FBXExportColladaFrameRate

FBXExportColladaFrameRate [float];

FBXExportColladaFrameRate -q;

此函数是功能相当于“Collada”选项的脚本。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中的“Collada”。

#### FBXExportColladaSingleMatrix

FBXExportColladaSingleMatrix [true|false];

FBXExportColladaSingleMatrix -q;

此命令是功能相当于 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中“Collada 单一矩阵”(Collada > Single matrix)选项的脚本。

#### FBXExportColladaTriangulate

FBXExportColladaTriangulate [true|false];

FBXExportColladaTriangulate -q;

此命令是功能相当于 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中“Collada 三角化”(Collada > Triangulate)选项的脚本。

#### FBXExportConstraints

FBXExportConstraints -v [true|false];

FBXExportConstraints -q;

使在 Maya 场景中定义的所有约束包含在导出的 FBX 文件中或从该文件中排除。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中的“约束”(Constraints)。

#### FBXExportConvertUnitString

FBXExportConvertUnitString [mm|dm|cm|m|km|In|ft|yd|mi];

该命令返回用于将一厘米转化为指定单位所需的比例因子，并且是 FBX 导出器和导入器窗口中“文件单位转化为”菜单的脚本版本。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“场景单位转化为”(Scene units converted to)。

#### FBXExportDxfTriangulate

FBXExportDxfTriangulate [true|false];

FBXExportDxfTriangulate -q;

**注**

此命令仅适用于 Macintosh 和 Linux 平台。

#### FBXExportDxfDeformation

FBXExportDxfDeformation [true|false];

FBXExportDxfDeformation -q;

**注**

此命令仅适用于 Macintosh 和 Linux 平台。

#### FBXExportEmbeddedTextures

FBXExportEmbeddedTextures -v [true|false];

FBXExportEmbeddedTextures -q;

##### True

将所有纹理保存在 FBX 文件中。此命令与“FBX 导出器”(FBX Exporter)窗口中“嵌入的媒体”(Embed Media)选项执行的操作相同。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“嵌入的媒体”(Embed Media)。

#### FBXExportFileVersion

FBXExportFileVersion -v [version];

其中，[version] 是支持的 FBX 版本之一。

**注**

仅当要使用较早的插件版本导入文件（在这种情况下，源插件版本和目标插件版本不匹配）时，才需更改此选项。

有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“FBX 版本”(FBX Version)。

#### FBXExportGenerateLog

FBXExportGenerateLog -v [true|false];

FBXExportGenerateLog -q;

使用此命令可在导出时生成日志文件。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“生成日志数据”(Generate log data)。

#### FBXExportHardEdges

FBXExportHardEdges -v [true|false];

FBXExportHardEdges -q;

复制场景网格中的所有顶点，使每个多边形与其相连接。顶点的法线将相应地设置，具体取决于所连接的是硬边还是平滑边。

**注**

该函数允许 MotionBuilder 显示硬边。

如果两个顶点完全位于同一位置，将发出警告，因为当 FBXImportHardEdges 设置为 True 时，会导致不可预测的结果。

此命令是 FBX 导出器(FBX Exporter)中“逐顶点分割法线”(Split per Vertex Normals)选项的脚本版本。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“包含”(Include)。

#### FBXExportInAscii

FBXExportInAscii -v [true|false];

FBXExportInAscii -q;

使用该函数可以导出为 ASCII 文件。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“类型”(Type)。

#### FBXExportIncludeChildren

FBXExportIncludeChildren -v [true|false];

FBXExportIncludeChildren -q;

使用此函数可在导出的 FBX 文件中排除或包含父对象下的层级。

#### FBXExportInputConnections

FBXExportInputConnections -v [true|false];

FBXExportInputConnections –q;

使用此函数可查询输入连接选项的当前值。此函数将返回 0 表示 False，1 表示 True。

如果要导出选定对象，则可将此函数与 FBXExport -f [filename][s] 脚本配合使用。设置为 False，以便在导出过程中不考虑选定对象的输入连接。此命令的默认值为 True，这使得插件包括对选定对象产生影响的所有对象。

这是一个功能相当于 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中“连接”(Connections)选项的脚本。

**注**

在“导出全部”过程将忽略此命令。

#### FBXExportInstances

FBXExportInstances -v [true|false];

FBXExportInstances -q;

这是一个功能相当于 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中“保留实例”(Preserve Instances)选项的脚本。

#### FBXExportLights

FBXExportLights -v [true|false];

FBXExportLights -q;

使用该函数可以在导出的 FBX 文件中包含或排除灯光。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中的“灯光”(Lights)。

**注**

默认情况下，此选项处于启用状态。

#### FBXExportQuaternion

FBXExportQuaternion -v [quaternion|euler|resample];

FBXExportQuaternion -q;

使用四元数插值脚本可选择从主机应用程序导出四元数插值的方式。

#### FBXExportQuickSelectSetAsCache

FBXExportQuickSelectSetAsCache –v “setName”;

FBXExportQuickSelectSetAsCache –q;

此命令将 setName 存储为导出缓存文件时要使用的集。

此命令不验证收到的字符串。但是，如果此处使用的字符串与 Maya 场景中的现有（有效）集不对应，则缓存导出将失败。

#### FBXExportReferencedAssetsContent

FBXExportReferencedAssetsContent -v [true|false];

FBXExportReferencedAssetsContent -q;

此命令是“FBX 导出器”(FBX Exporter)中“引用的资源内容”(Referenced Assets Content)选项的脚本版本。请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中的“引用的资源内容”(Referenced Assets Content)。

#### FBXExportScaleFactor

FBXExportScaleFactor [float];

FBXExportScaleFactor -q;

此命令是“FBX 导出器”(FBX Exporter)中“比例因子”(Scale Factor)字段的脚本版本。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)主题中的“比例因子”(Scale Factor)。

#### FBXExportShapes

FBXExportShapes -v [true|false];

FBXExportShapes -q;

使用此函数可在 FBX 文件中排除或包含图形变形。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“变形模型”(Deformed Models)。

**注**

默认情况下，此选项处于启用状态。

#### FBXExportSkeletonDefinitions

FBXExportSkeletonDefinitions -v [true|false];

FBXExportSkeletonDefinitions -q;

使用该函数可以在导出时包含或排除“骨架定义(Skeleton definition)”。

**注**

此命令与 FBXImportCharacter 命令相同，后者已不赞成使用。

#### FBXExportSkins

FBXExportSkins -v [true|false];

FBXExportSkins -q;

使用该函数可以在 FBX 文件中排除或包含蒙皮变形。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中的“变形模型”(Deformed Models)。

**注**

默认情况下，此选项处于启用状态。

#### FBXExportSmoothingGroups

FBXExportSmoothingGroups -v true|false;

FBXExportSmoothingGroups -q;

此命令是 FBX 导出器中“平滑组”(Smoothing Groups)选项的脚本版本。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中的“平滑组”(Smoothing Groups)。

#### FBXExportSmoothMesh

FBXExportSmoothMesh -v true|false;

FBXExportSmoothMesh -q;

使用该函数可以导出网格的细分级别。

#### FBXExportSplitAnimationIntoTakes

FBXExportSplitAnimationIntoTakes -q

FBXExportSplitAnimationIntoTakes -c

FBXExportSplitAnimationIntoTakes -v

使用以下命令可以将动画文件导出到多个录制中。

##### FBXExportSplitAnimationIntoTakes -v

FBXExportSplitAnimationIntoTakes -v 选项需要额外的参数。其语法为：*FBXExportSplitAnimationIntoTakes -v "takename" frameStart frameEnd*。这会在内存中设置“takename frameStart frameEnd”形式。对该函数的后续调用会在表中附加新条目。

例如：

- FBXExportSplitAnimationIntoTakes -v \"toto\" 1 5

- FBXExportSplitAnimationIntoTakes -v \"tata\" 10 25

- FBXExportSplitAnimationIntoTakes -v \"titi\" 3 20

在内部，帧以秒表示。使用当前应用程序帧速率将帧转化为秒。定义都可用后，调用 *FBXExportSplitAnimationIntoTakes -q*。这将返回：

```text
// Result: name=toto start=1 end=5 name=toto start=10 end=25
name=toto start=3 end=20 //
```

**注**

- 如果需要为第二个导出设置新定义，积累数不会自动清除；调用方负责使用 *-clear* 选项调用命令来清除积累数。

- 无论定义了多少分割，Take001 始终存在。

- 如果设置的 frameEnd 小于 frameStart，将返回错误。

- frameStart 和 frameEnd 没有必要使用关键帧定义间隔，而且分割函数不会尝试进行验证。如果没有动画关键帧在该范围内，仍将创建录制，但不使用关键帧。

#### FBXExportTangents

FBXExportTangents -v [true|false];

FBXExportTangents -q;

此命令是 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中“切线和次法线”(Tangents and Binormals)选项的脚本版本。

#### FBXExportTriangulate

FBXExportTriangulate -v [true|false];

FBXExportTriangulate -q;

此命令是 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)部分中“三角化”(Triangulate)选项的脚本版本。

#### FBXExportUpAxis

FBXExportUpAxis [y|z];

FBXExportUpAxis -q;

此命令可以定义 FBX 文件中的上方向轴。上方向轴是向上指的全局轴。有关详细信息，请参见 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)主题中的“轴转化”(Axis conversion)。

默认情况下，Maya 中的上方向轴为 Y 轴。

##### Y

将上方向轴设置为 Y 轴向上。该设置为默认设置。

##### Z

将上方向轴设置为 Z 轴向上。

#### FBXExportUseSceneName

FBXExportUseSceneName -v [true|false];

FBXExportUseSceneName -q;

此命令是 [FBX 导出选项](../FBX%20导出/FBX%20导出选项.md)中“使用场景名”(Use scene name)选项的脚本版本。
