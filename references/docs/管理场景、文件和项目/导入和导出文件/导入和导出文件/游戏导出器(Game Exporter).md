# 游戏导出器(Game Exporter)

- 从主菜单中，选择“文件 > 游戏导出器”(File > Game Exporter)

**注**

在

Maya

中，

“游戏导出器”(Game Exporter)

可作为自动加载插件。如果需要手动加载此工具，例如如果看到

“文件”(File)

菜单中未列出

“游戏导出器”(Game Exporter)

，请使用

“插件管理器”(Plug-in Manager)

（

“Windows > 设置/首选项 > 插件管理器”(Windows > Settings/Preferences > Plug-in Manager)

）加载

gameFbxExporter

插件。

该“游戏导出器”(Game Exporter)提供简化的 FBX 导出工作流，用于将模型和动画片段发送到游戏引擎。每个选项卡显示 FBX 选项的最小集，支持您导出资源而无需了解或更改过多设置。每个选项卡上显示的选项将保存为预设，当从其他场景中导出时可以重用。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-B06EE398-D759-4B61-88E7-FA2F1F0C0D07.png) <!-- baize:img-hook downloaded=false reason="正文 3569 字 ≥300，非承重" -->

## “游戏导出器”(Game Exporter)中的任务

此表简要概述了您在“游戏导出器”(Game Exporter)中执行的简单任务。请参见：

- [使用“游戏导出器”导出动画片段](游戏导出器%28Game%20Exporter%29/使用“游戏导出器”%28Game%20Exporter%29导出动画片段.md)

- [使用“游戏导出器”导出模型](游戏导出器%28Game%20Exporter%29/使用“游戏导出器”%28Game%20Exporter%29导出模型.md)

- [将时间编辑器片段导出到游戏导出器](游戏导出器%28Game%20Exporter%29/将时间编辑器片段导出到游戏导出器.md)

| 目标 | 操作 |
|---|---|
| 在导出选项之间切换。 | 打开第一个下拉菜单，然后选择“动画默认值”(Anim Default)预设、“模型默认值”(Model Default)预设或任何已添加的自定义预设。 ![图：打开第一个下拉菜单，然后选择“动画默认值”(Anim Default)预设、“模型默认值”(Model Default)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-C5CD1D31-55E2-45AD-87F5-1D98C8F34725.png) <!-- baize:img-hook downloaded=false reason="正文 3569 字 ≥300，非承重" --> 窗口中的其余选项将动态更新。 |
| 创建新建预设。 | 单击 ![图：单击 。 另请参见创建“游戏导出器”预设。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-A4D4B95A-0FFD-4B5E-ACFC-075E23801F9B.png) <!-- baize:img-hook downloaded=false reason="正文 3569 字 ≥300，非承重" -->。 另请参见[创建“游戏导出器”预设](游戏导出器%28Game%20Exporter%29/创建“游戏导出器”%28Game%20Exporter%29预设.md)。 |
| 将当前的预设设置保存到磁盘。 | 单击 ![图：单击 。 注： 当您更改当前 FBX 导出的设置时，更改后的设置将自动在场景中保存。当您重新打开场景时这些设置会再次可用…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-AAAB92F2-1363-49A1-BB3A-401BBDDC9151.png) <!-- baize:img-hook downloaded=false reason="正文 3569 字 ≥300，非承重" -->。 注： 当您更改当前 FBX 导出的设置时，更改后的设置将自动在场景中保存。当您重新打开场景时这些设置会再次可用。可以使用此图标将设置保存为单独的文件，这样您可以在其他场景中加载相同的预设。 |
| 从磁盘加载保存的预设。 | 单击 ![图：单击 ，然后导航以选择保存的预设文件。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-E140FE1A-A32C-4068-83DF-A83FDDAAA983.png) <!-- baize:img-hook downloaded=false reason="正文 3569 字 ≥300，非承重" -->，然后导航以选择保存的预设文件。 |
| 编辑默认预设的设置。 | 单击 ![图：单击 以打开“高级设置”(Advanced Settings)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-8E579EDF-E709-4299-8BB2-7437F9FB2263.png) <!-- baize:img-hook downloaded=false reason="正文 3569 字 ≥300，非承重" --> 以打开“高级设置”(Advanced Settings)。 |

## 工具设置

“游戏导出器”(Game Exporter)中显示的大多数选项可以更改，具体取决于所选择的预设。默认情况下，“动画默认值”(Anim Default)预设设置用于动画片段的标准导出，“模型默认值”(Model Default)预设设置用于静态网格的标准导出。

有关使用其他或不同的 FBX 选项创建自己的预设的信息，请参见[创建“游戏导出器”(Game Exporter)预设](游戏导出器%28Game%20Exporter%29/创建“游戏导出器”%28Game%20Exporter%29预设.md)。

#### “导出全部”(Export All)、“导出当前选择”(Export Selection)、“导出对象集”(Export Object Set)

使用此下拉列表来指定要从场景中导出的内容。

如果您的场景中包含具有想导出的对象的集，您可以选择“导出对象集”(Export Object Set)，然后从第二个下拉列表中选择您的场景中的特定集。

**注**

如果有多个角色在同一场景并要仅导出其中之一，在这里可以指定要导出哪个角色。若要从选定对象中创建集，只需选择

“创建 > 集 > 集”(Create > Sets > Set)

。另请参见

创建和编辑设置

。

### “动画片段”(Animation Clips)设置（“动画片段”(Animation Clips)选项卡）

在此部分中，您可以在场景中定义多个动画片段，以便将它们导出为单独的文件，或导出为单个 FBX 文件中的单独镜头。您可以创建、命名、设置开始和结束帧，然后在此区域播放片段。请参见[使用“游戏导出器”(Game Exporter)导出动画片段](游戏导出器%28Game%20Exporter%29/使用“游戏导出器”%28Game%20Exporter%29导出动画片段.md)。

创建了片段列表后，可以使用右侧的复选框，选择要通过当前操作导出的片段。

### 几何体设置（“模型”(Model)选项卡）

#### 平滑组(Smoothing Groups)

将边的硬度/柔和度转化为导出几何体的平滑组。禁用时，只有明确的法线可以通过该文件导出。

#### 平滑网格(Smooth Mesh)

启用此选项，可将多边形网格视口内的细分烘焙到已导出的几何体。

#### 分割顶点法线(Split-Vertex Normals)

基于边的连续性分割几何体的顶点法线。顶点法线决定了多边形面之间的视觉平滑效果。

#### 三角化(Triangulate)

对于导出的几何体，自动将多边形转化为三角形。

#### 切线和次法线(Tangents & Binormals)

根据导出几何体上的 UV 和法线信息创建切线和次法线数据。这样，您可以获得几何体的精确切线空间表示形式，可将其用于某些游戏引擎。

#### 蒙皮

设置是否导出蒙皮网格的所有蒙皮变形信息。

#### 混合变形(Blendshapes)

设置是否要导出导出对象上的任何混合变形。

### 设置(Settings)

#### 将片段保存到单个文件(Save Clips to Single File)/保存多个片段文件(Save Multiple Clip Files)

（“动画片段”(Animation Clips)选项卡。）设置是否要将在“动画片段”(Animation Clips)部分定义的全部片段导出为单个 FBX 文件，或将其导出为多个或单个片段文件。

“将多个片段保存为单个文件”操作将片段以 FBX 镜头数保存在单个 FBX 文件内。

#### 导出到单个文件(Export to Single File)/导出到多个文件(Export to Multiple Files)

（“模型”(Model)选项卡。）设定是将多个网格导出到一个 FBX 文件，还是将每个网格或层次分别导出为多个 FBX 文件。

#### 移动到原点(Move to Origin)

启用时，变换坐标将清零，即在导出的文件中将对象或层次移动到原点。

#### 烘焙动画(Bake Animation)

（“动画片段”(Animation Clips)选项卡。）将任意约束烘焙到动画曲线，以便动画烘焙到骨骼并可以将其加载到游戏引擎。（在大多数情况下，约束动画不会传递到游戏引擎，因此如果不烘焙骨骼就不会显示动画。）

#### 动画(Animation)

（仅“模型”(Model)选项卡。）设定在导出的文件中是否在目标模型中包含动画。关闭以仅导出目标网格。

#### 输入连接(Input Connections)

设定是否导出与您的选择关联的所有节点。

如果您正在使用“烘焙动画”(Bake Animation)，并且不希望整个装备包含在导出的 FBX 文件中，您可以关闭此选项。

#### 上方向轴(Up Axis)

默认情况下，“上方向轴”(Up Axis)设置为 Y，这与 Maya 中的设置一致。如果目标应用程序不支持 Y 向上世界轴且无法转换场景的 Y 轴向上世界轴，则可以使用 Z 轴向上轴将场景导出。

**注**

“游戏导出器”(Game Exporter)

仅会对导出场景的根元素应用轴转化。如果在导出时必须转换的根对象中存在动画，则需要对这些动画曲线重新采样以应用轴转化。为避免对曲线重新采样，可以在场景中添加一个根节点（虚拟对象）作为已设置动画对象的父对象，然后再导出。

#### 嵌入的媒体(Embed Media)

（默认情况下启用。）

启用“嵌入的媒体”(Embed Media)包括（在FBX 文件内嵌入）FBX 文件内 的相关媒体（如纹理）。这有助于防止出现以下类似问题，例如，如果从关联媒体文件位置的相对和绝对路径上移动或删除任何纹理，纹理可能会消失。如果您将 FBX 文件给使用另一台计算机的某个用户，但在相同计算机驱动器上该目录下却不存在那种纹理，则可能会出现以上情况。

#### 文件类型(File Type)

选择“二进制”(Binary)或“ASCII”。

#### FBX 版本(FBX Version)

选择用于导出的文件的 FBX 版本。若要确认您具有准确的插件版本，请单击“高级设置”(Advanced Settings)图标 ![图：选择用于导出的文件的 FBX 版本。若要确认您具有准确的插件版本，请单击“高级设置”(Advanced Settings…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-8E579EDF-E709-4299-8BB2-7437F9FB2263.png) <!-- baize:img-hook downloaded=false reason="正文 3569 字 ≥300，非承重" -->，验证“FBX 选项”(FBX Options)底部列出的内容。

#### 高级设置(Advanced Settings) ![图：高级设置(Advanced Settings)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-8E579EDF-E709-4299-8BB2-7437F9FB2263.png) <!-- baize:img-hook downloaded=false reason="正文 3569 字 ≥300，非承重" -->

“游戏导出器”(Game Exporter)中未显示的任何 FBX 选项使用默认的 FBX 值。要更改这些设置，请单击 ![图：“游戏导出器”(Game Exporter)中未显示的任何 FBX 选项使用默认的 FBX 值。要更改这些设置，请单击 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-8E579EDF-E709-4299-8BB2-7437F9FB2263.png) <!-- baize:img-hook downloaded=false reason="正文 3569 字 ≥300，非承重" --> 以打开“高级设置”(Advanced Settings)并更改当前预设的设置。

在“高级设置”(Advanced Settings)窗口中，启用“编辑动画片段高级设置”(Edit Animation Clips Advanced Settings)或“编辑模型高级设置”(Edit Model Advanced Settings)，可开始进行更改。

### 路径(Path)设置

#### 在 FBX Review 中查看(View in FBX Review)

如果您已经在计算机上安装了 FBX Review，可以使用此选项直接在 FBX Review 中启动导出的文件。另请参见[使用 FBX Review 预览文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6946B053-40F3-4C04-AA5C-81311DFE562D)。

#### 路径(Path)

输入目录，或单击文件夹图标以浏览并选择文件的导出位置。

#### 文件名(Filename)

输入导出文件的文件名。

如果正在导出的动画为多个动画片段文件，则该名称将附加到每个片段文件名称的开头。如果“文件名”(Filename)为空，则不附加前缀。

投影文件名显示在其他“路径”(Path)设置下方，以显示导出文件的完整名称。

## 相关主题

- [FBX 文件转换器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-18A2CDD7-3334-4FC1-A1B3-A308AD331BB2)
