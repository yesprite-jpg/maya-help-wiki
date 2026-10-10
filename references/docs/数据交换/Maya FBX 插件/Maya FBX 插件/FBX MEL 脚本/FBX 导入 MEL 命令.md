# FBX 导入 MEL 命令

以下 MEL 命令用于模拟 FBX 导入器用户界面中的导入选项。

**注**

提示：

如果您正编写脚本且想要防止 FBX UI 在每次导入文件时都出现，请使用以下命令来在导入时隐藏 FBX UI：

```text
FBXImport -file "c:/myfile.fbx";
```

#### FBXImport

FBXImport -f [filename] -t [take index];

导入 [filename] 中指定的文件和 [take index] 中指定的镜头。

导入的文件是在执行命令后镜头查询可访问的文件。

指定适当的镜头编号以加载相应的镜头。如果指定 0，则插件将不导入动画。（这相当于从 Maya FBX 插件用户界面的菜单中选择“无动画”(No Animation)。）

如果指定 -1，插件将检索镜头阵列中的最后一个镜头。插件将大于文件中所含镜头数的镜头数或小于 -1 的任何负值视为无效。如果发生这种情况，将显示“无此镜头”(No such take)错误。

**注**

FBXImport 命令可用于指定镜头。如果 FBX 文件中不包含镜头，则可以使用

Python File(...)

命令。

#### FBXImportAxisConversionEnable

FBXImportAxisConversionEnable -v [true|false];

FBXImportAxisConversionEnable -q;

该命令是“FBX 导入器”(FBX Importer)中“轴转化”(Axis conversion)选项的脚本版本。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“轴转化”(Axis conversion)。

#### FBXImportCacheFile

FBXImportCacheFile -v [true|false];

FBXImportCacheFile -q;

该命令是“FBX 导入器”(FBX Importer)中“导入几何体缓存文件”(Import geometry Cache file(s))选项的脚本版本。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“几何体缓存文件”(Geometry cache file(s))。

#### FBXImportCameras

FBXImportCameras -v [true|false];

FBXImportCameras -q;

使用此脚本可导入或排除 FBX 文件中的摄影机。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“摄影机”(Cameras)。

**注**

默认情况下，此函数处于启用状态。

#### FBXImportConstraints

FBXImportConstraints -v [true|false];

FBXImportConstraints -q;

使导入进程忽略 FBX 文件中定义的所有约束，并从 Maya 场景中排除此类约束。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“约束”(Constraints)。

#### FBXImportConvertDeformingNullsToJoint

FBXImportConvertDeformingNullsToJoint -v [true|false];

FBXImportConvertDeformingNullsToJoint -q;

将变形元素转化为 Maya 关节。

##### True

将所有变形元素变换为关节节点。

**注**

最初提供该选项的原因是 Maya 不在骨骼层次内支持定位器元素（即，变换不是关节的节点）。虽然 Maya 现在支持此功能，但在某些情况下该选项会改进蒙皮行为。

有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“将元素变形为关节”(Deforming elements to joints)。

#### FBXImportConvertUnitString

FBXImportConvertUnitString [mm|dm|cm|m|km|In|ft|yd|mi];

该命令返回用于将一厘米转化为指定单位所需的比例因子，并且是 FBX 导出器和导入器窗口中“文件单位转化为”菜单的脚本版本。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“文件单位转化为”(File units converted to)。

#### FBXImportDxfWeldVertice

FBXImportDxfWeldVertice [true|false];

FBXImportDxfWeldVertice -q;

**注**

此命令仅适用于 Macintosh 和 Linux 平台。

#### FBXImportDxfReferenceNode

FBXImportDxfReferenceNode [true|false];

FBXImportDxfReferenceNode -q;

**注**

此命令仅适用于 Macintosh 和 Linux 平台。

#### FBXImportDxfObjectDerivation

FBXImportDxfObjectDerivation [layer|entity|block];

FBXImportDxfObjectDerivation -q;

**注**

此命令仅适用于 Macintosh 和 Linux 平台。

#### FBXImportFillTimeline

FBXImportFillTimeline -v [true|false];

FBXImportFillTimeline -q;

在导入时填充场景时间轴（而不使用 Maya 默认设置）。

#### FBXImportForcedFileAxis

FBXImportForcedFileAxis [y|z];

FBXImportForcedFileAxis -q;

使用该命令可“强制”FBX 插件认为文件中的数据是通过用户指定的轴在本地生成的。FBXImportForcedFileAxis 命令没有等效 UI，且可以生成异常结果，因为该命令只更改全局设置中的传入文件轴。

例如，在 3ds Max 的 Z 轴向上世界中创建的平面具有以下顶点坐标：(0,0,0) - (1,0,0) - (1,0,1) - (0,0,1)。（此平面看起来像表上的一张图纸，该表位于 XY 平面上且 Z = 0 标高。）在导入 Maya 时使用 FBXImportUpAxis 选项，该平面将旋转，这样它在 Maya 中的位置与在 3ds Max 中位置看起来将相同。因此，在 Maya 中，平面位于 XZ 平面上且 Y = 0 标高。（假设 Maya 设置为默认的“Y 轴向上”轴）。

如果使用 FBXImportForcedFileAxis 强制轴在导入时为“Y 轴向上”，Maya 插件不会对轴应用任何转换。这是因为，使用此命令时，插件会将文件和系统轴都视为“Y 轴向上”，使平面与 XY 平面上且 Z = 0 深度的表垂直。

**注**

如果已将 Maya 配置为“Z 轴向上”轴，而“强制”轴为“Y 轴向上”，FBX 插件仍会执行从“Y 轴向上”（在传入 FBX 文件中设置）到“Z 轴向上”（导入到 Maya 中）的转换。

#### FBXImportGenerateLog

FBXImportGenerateLog -v [true|false];

FBXImportGenerateLog -q;

使用此命令可在导出时生成日志文件。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“生成日志数据”(Generate Log Data)。

#### FBXImportHardEdges

FBXImportHardEdges -v [true|false];

FBXImportHardEdges -q;

将位于完全相同位置的所有顶点合并回一个唯一顶点。然后，Maya FBX 插件根据连接到每个顶点的边的法线确定相应边是硬边还是平滑边。

在导出时，如果 FBXExportHardEdges 设置为 True，则使用此函数。

该命令是 FBX 导入器(FBX Importer)中“逐顶点合并法线”(Combine per-vertex Normals)选项的脚本版本。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“逐顶点合并法线”(Combine per-vertex Normals)。

#### FBXImportLights

FBXImportLights -v [true|false];

FBXImportLights -q;

使用该函数可以在导入过程中包含或排除灯光。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“灯光”(Lights)。

#### FBXImportMergeBackNullPivots

FBXImportMergeBackNullPivots -v [true|false];

FBXImportMergeBackNullPivots -q;

##### True

将层次中用作前期旋转和后期旋转的 null（或关节）元素的旋转变换指定为原始节点的关节方向和旋转轴。

之后，删除前期旋转和后期旋转节点。

将按名称完成查找，因为前期旋转节点的名称包含 “__Pre_”后缀，而后期旋转节点的名称包含“__Post_”后缀。

**注**

当导入模式设置为

“更新动画”(Update animation)

或

“添加和更新动画”(Add and Update animation)

时，此选项将自动设置为 True

。

#### FBXImportMergeAnimationLayers

FBXImportMergeAnimationLayers -v [true|false];

FBXImportMergeAnimationLayers -q;

激活“烘焙动画层”(Bake animation layers)可以烘焙（或绘制）传入文件中包含的动画层。

#### FBXImportMode

FBXImportMode -v [exmerge|add|merge;]

FBXImportMode -q;

此命令有三种可能的状态：

##### Exmerge

采用以下方式，将导入的 FBX 文件合并到当前场景中：

具有相同名称和性质的节点只能替换自己的动画曲线。不创建新节点。此命令与插件 UI 中“更新动画”(Update animation)选项的功能相同。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“更新动画”(Update Animation)。

##### Add

将内容添加到当前场景内容。此命令与插件 UI 中“添加”(Add)选项的功能相同。

##### Merge

采用以下方式，将导入的 FBX 文件合并到当前场景中：创建场景中无等效节点的任何节点。替换名称相同但性质（如球体和骨骼）不同的节点。名称和特性都相同的节点只能替换自己的动画。此命令与 UI 中“添加并更新动画”(Add and Update animation)的功能相同。

**注**

若要在 UI 中查看这些信息，请参见

FBX 导入选项

主题中的

“文件内容”(File Content)

。

#### FBXImportProtectDrivenKeys

FBXImportProtectDrivenKeys -v [true|false];

FBXImportProtectDrivenKeys -q;

使用该脚本可防止任何传入动画覆盖具有受驱动关键帧的通道。

如果设置为 True，受驱动关键帧将受到保护，且不会将传入动画应用于受驱动通道。

如果设置为 False，则丢弃受驱动关键帧，并将传入动画应用于受驱动通道。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“保护受驱动关键帧”(Protect Driven Keys)。

#### FBXImportQuaternion

FBXImportQuaternion -v [quaternion|euler|resample] ;

FBXImportQuaternion -q;

可用于指定在导入到 Maya 的过程中应该如何处理四元数旋转。该选项可修正 Maya 和 MotionBuilder 四元数之间的差异。该命令相当于四元数插值模式设置。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“四元数插值模式”(Quaternion interpolation mode)。

#### FBXImportResamplingRateSource

FBXImportResamplingRateSource -v [Scene|File|Custom];

FBXImportResamplingRateSource -q;

该命令可用于设置“FBX 导入器”(FBX Importer)在需要重新对数据采样时生成关键帧所用的速率。通过 *Scene* 使用 Maya 的当前工作单位（请参见“首选项”(Preferences)窗口的“设置”(Settings)区域中的[“工作单位”(Working Units)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4D653DC9-57AA-4D8B-987A-5B7A9735CAF0#GUID-4D653DC9-57AA-4D8B-987A-5B7A9735CAF0__WS17956D7ADBC6E736-4CE538CA117AE30C631-7FC5)），通过 *File* 使用 FBX 文件定义的采样率，或者通过 *Custom* 指定自定义值。

当 Maya 中的动画曲线的插值不能由 MotionBuilder 中的曲线精确表示时，将需要进行重采样。

#### FBXImportScaleFactorEnable

FBXImportScaleFactorEnable [true|false];

FBXImportScaleFactorEnable -q;

该命令是“FBX 导入器”(FBX Importer)中“比例因子”(Scale Factor)选项的脚本版本。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“比例因子”(Scale factor)。

#### FBXImportScaleFactor

FBXImportScaleFactor [float];

FBXImportScaleFactor -q;

该命令是“FBX 导入器”(FBX Importer)中“比例因子”(Scale Factor)菜单的脚本版本。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“比例因子”(Scale factor)。

#### FBXImportSetMayaFrameRate

FBXImportSetMayaFrameRate -v [true|false];

FBXImportSetMayaFrameRate -q;

此命令可从 FBX 文件中导入帧速率。将会覆盖 Maya 中使用的速率。

#### FBXImportSetLockedAttribute

FBXImportSetLockedAttribute -v [true|false];

FBXImportSetLockedAttribute -q;

此命令是功能相当于 UI 对话框中“全部保持锁定状态”(Keep all locked)或“全部解除锁定”(unlock all)选项的脚本。在将包含动画的 FBX 文件导入已锁定通道的对象时，请使用此命令。

如果使用 UI，Maya FBX 插件会提示您将所有通道保持锁定状态或对锁定的通道解除锁定，这样才能正确导入动画。对于在不使用 UI 的情况下已尝试执行此操作的用户，会产生问题。

##### False

解除锁定所有通道。

##### True

通道保持锁定状态。

##### 示例代码

FBXImportSetLockedAttribute -v False;

FBXImport -f "C:/myFile.fbx";

#### FBXImportSetTake

FBXImportSetTake -takeIndex [take index]

FBXImportSetTake -ti [take index]

如果 FBX 文件包含多个 Take，使用此命令可指定要导入的 Take。导入 [take index] 中指定的 Take。

指定适当的镜头编号以加载相应的镜头。如果指定 0，则插件将不导入动画。如果指定 -1，插件将检索镜头阵列中的最后一个镜头。插件将大于文件中所含镜头数的镜头数或小于 -1 的任何负值视为无效。如果发生这种情况，将显示“无此镜头”(No such take)错误。

#### FBXImportShapes

FBXImportShapes -v [true|false];

FBXImportShapes -q;

使用此脚本可在 FBX 文件中导入或排除图形。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“变形模型”(Deformed models)。

#### FBXImportSkeletonType

FBXImportSkeletonType -v [none|fbik|humanik];

FBXImportSkeletonType -q;

使用该函数可以导入或排除 FBX 文件中的骨架定义。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“骨架定义”(Skeleton Definitions)。

**注**

此命令与 FBXImportCharacterType 命令相同，后者已不赞成使用。

#### FBXImportSkins

FBXImportSkins -v [true|false];

FBXImportSkins -q;

使用该函数可在 FBX 文件中导入或排除蒙皮变形。有关详细信息，请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“变形模型”(Deformed models)。

#### FBXImportUnlockNormals

FBXImportUnlockNormals -v true|false;

FBXImportUnlockNormals -q;

覆盖法线的默认 Maya 锁定状态。

##### True

使用 Maya 内部算法重新计算对象上的法线。

#### FBXImportUpAxis

FBXImportUpAxis [y|z];

FBXImportUpAxis -q;

此命令是“FBX 导入器(FBX Importer)”中“轴转化”(Axis conversion)选项的脚本版本，但在插件 UI 中不可用。请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“轴转化”(Axis conversion)。

**注**

FBXImportUpAxis 命令向场景对象添加预旋转，使对象从一个产品的世界轴转到另一个产品的世界轴。如果这不是您所希望的，请尝试使用 FBXImportForcedFileAxis 命令，但先阅读 FBXImportForcedFileAxis 命令的描述，因为该命令会更改对传入数据的解释。
