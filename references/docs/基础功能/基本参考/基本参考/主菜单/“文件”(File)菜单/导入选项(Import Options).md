# 导入选项(Import Options)

使用这些选项可以设置在选择“文件 > 导入”(File > Import)时会发生什么变化。另请参见[导入文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BB7ABDA1-86E6-4A83-B8E6-3F4D7F1B0F1B)。

**注**

若要导入在 Maya 早期版本中创建的文件，请确保

“忽略版本”(Ignore Version)

首选项在

文件/项目(Files/Projects)首选项

中处于启用状态。

**注**

这些选项仅显示在

Maya 文件浏览器

中。如果使用本地文件浏览器，可以转到

“文件 > 导入”(File > Import) > ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 6735 字 ≥300，非承重" -->

对其进行访问。

## 常规选项(General options)

#### 分组(Group)

指定导入文件时是否将导入的对象分组到一个变换下。通过分组可以更轻松地处理导入对象的节点。默认设置为禁用。

#### 移除重复的着色网络(Remove duplicate shading networks)

在将文件多次导入到 Maya 中时，此选项可以避免重复的几何体和着色网络。

#### 合并基础动画层(Merge Base Animation Layers)

如果要将导入文件的基础动画层与场景中已有的当前基础动画层合并，请启用此选项。否则，将使用早期行为，并将导入的层移动到当前基础层下。默认设置为禁用。

#### 文件类型(File type)

从下拉列表中选择要导入的文件类型。如果不能确定要导入的文件类型，可以选择“最佳推测”(Best Guess)。

根据选择的文件类型，可能会显示多种特定于文件类型的选项。

## 引用选项(Referencing options)

#### 保留引用(Preserve references)

如果启用“保留引用”(Preserve References)，则将保持导入文件中的引用。如果禁用此选项，则所有引用都将导入或导出到文件中；也就是说，它们将不再是引用，而是场景中的对象。默认设置为禁用。

#### 加载保存的引用加载状态(Load saved reference load state)

（默认设置）遵循上次保存引用文件时引用文件中的被引用文件的状态。上次处理文件时加载或卸载的任何引用都将在文件重新打开时正确加载或卸载。

#### 加载所有引用(Load all references)

在加载所有引用的情况下打开文件。在 Maya 中打开文件后可以通过以下方法更改引用加载的状态：打开[引用编辑器(Reference Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8D8E0D4A-DE37-4C63-9F59-8D71F00E3367)，然后选择要卸载的引用。

#### 不加载引用(Load no references)

这将在不加载任何引用的情况下打开文件。在 Maya 中打开文件后可以通过以下方法加载引用：打开[引用编辑器(Reference Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8D8E0D4A-DE37-4C63-9F59-8D71F00E3367)，然后选择要加载的引用。

#### 仅加载顶层级引用(Load top-level references only)

仅加载最顶层的被引用文件（这些文件本身可能包含嵌套的被引用文件）。如果要打开包含许多嵌套引用的复杂嵌套场景引用层次，而您又想要轻松处理层次中的顶层级时，该选项将非常有用。

## 播放选项(Playback Options)

#### 场景为空时始终覆盖(Always Override if Scene is Empty)

如果场景为空，则该设置默认处于活动状态，且场景中的所有计时选项（帧速率、动画范围、动画播放范围）将替换为导入的传入文件中的设置。如果场景已填充，则此选项会自动禁用，使“帧速率导入”(Framerate Import)部分变成活动状态，允许您选择要导入或覆盖的播放元素。

#### 帧速率导入(Framerate Import)

这些选项用于选择 Maya 如何处理导入的帧速率。

##### 保持原始(Maintain Original)

对导入的文件施加 Maya 场景帧速率。

##### 覆盖以匹配源(Override to Match Source)

使用导入文件的帧速率替换 Maya 场景帧速率。

**注**

导入帧速率时，关键帧完全放置在时间轴上。如果要导入到的目标场景与已导入场景的帧速率不同，则可能会出现分数值，这些值由星号表示。

![图：注： 导入帧速率时，关键帧完全放置在时间轴上。如果要导入到的目标场景与已导入场景的帧速率不同，则可能会出现分数值，这些值…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-D541BB3B-1D4A-437C-A953-FF8F993A7A13.png) <!-- baize:img-hook downloaded=false reason="正文 6735 字 ≥300，非承重" -->

禁用[“时间滑块”(Time Slider)首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-51A80586-9EEA-43A4-AA1F-BF1370C24A64) “捕捉到整个帧”(Snap to Whole Frames)选项时，也会发生这种情况。

#### 动画范围(Animation Range)

选择设置，以指定是导入已导入文件的时间和播放范围，还是施加在当前 Maya 场景中使用的范围。

##### 保持原始(Maintain Original)

对导入的文件施加当前 Maya 场景的播放和时间范围。

##### 覆盖以匹配源(Override to Match Source)

使用已导入文件的播放和时间范围替换当前 Maya 场景的播放和时间范围。

##### 合并以包含源(Combine to Include Source)

合并 Maya 场景的范围和已导入文件的范围，以创建可包含所有计时的混合范围。例如，如果将动画范围为 10 到 100 的场景导入到范围为 0 到 120 的 Maya 场景中，则该设置会创建一个介于 0 和 120 之间的动画范围，使其可以同时包含这两个计时。

**注**

在时间滑块中，已舍入到小数点后第二位的任何数字旁边会显示一个星号“

*

”，指示该值是近似值。如果在“时间码”(Time Code)与“帧”(Frames)之间切换，或者如果在

“时间滑块”(Time Slider)首选项

中禁用

“捕捉到整个帧”(Snap to Whole Frames)

选项，有时会出现这种情况。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-D541BB3B-1D4A-437C-A953-FF8F993A7A13.png) <!-- baize:img-hook downloaded=false reason="正文 6735 字 ≥300，非承重" -->

## 名称空间选项(Namespace Options)

#### 使用名称空间(Use namespaces)

如果在启用“使用名称空间”(Use namespaces)的情况下引用或导入场景，则 Maya 将创建包含被引用数据的新名称空间。启用“使用名称空间”(Use namespaces)可确保所有节点都具有唯一的名称。请参见[名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B796BE38-72AC-4B9E-9C03-3C27C3EAA171)和[在引用或导入时创建名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E173CC3D-1638-499C-9F38-73735934D8E5#GUID-E173CC3D-1638-499C-9F38-73735934D8E5__SECTION_EB9F55D366104ECB812FB39664922200)。

**注**

提示：

在引用文件之前，请确保重命名前缀不包含任何无效字符。

当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 ![图：当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 图标指示的。当前设置的名称空间的父…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-085BFA65-7807-43B8-B3C3-3D2393EB8AFB.png) <!-- baize:img-hook downloaded=false reason="正文 6735 字 ≥300，非承重" --> 图标指示的。当前设置的名称空间的父名称空间是由 ![图：当前设置的名称空间是在“名称空间选项”(Namespace Options)区域中由 图标指示的。当前设置的名称空间的父…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-7571C01F-9603-46CB-ACC9-FB41C5768745.png) <!-- baize:img-hook downloaded=false reason="正文 6735 字 ≥300，非承重" --> 图标指示的。当前名称空间可以在“名称空间编辑器”(Namespace Editor)中通过单击“设置当前空间名称”(Set Current)进行设置。请参见[名称空间编辑器概述](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8139C5B1-3C37-43DF-965E-39800AA98EE2)和[编辑名称空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9E2F2AF6-48F3-4628-B23E-0B8A07EAF737)。

名称空间不影响 Maya 的当前选择、DAG、依存关系图或任何其他方面。

#### 使用选定的名称空间作为父对象并添加新的名称空间(文件名) (Use selected namespace as parent and add new namespace (file name))

指定将引用的文件名添加到对象名称空间的开头。

例如，如果引用或导入的名为 foo.ma 的场景中包含名为 ball 的对象，则其名称空间为 foo:ball。

#### 使用选定的名称空间作为父对象并添加新的名称空间字符串(Use selected namespace as parent and add new namespace string)：

指定将文本字符串添加到对象名称的开头。在显示的字段中键入字符串。

#### 合并到选定名称空间并重命名匹配的传入对象(Merge into selected namespace and rename incoming objects that match)

将对象的名称空间与现有的选定名称空间合并。

如果出现重复的名称空间，将合并这些名称空间，并且重复的对象名称将以递增的数字作为后缀。使用此选项可以避免在每次引用或导入具有相同名称空间的对象时累积新的名称空间。

## USD 选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-57E9DA6F-DB97-48FB-859F-5FA7A7471DF8.png) <!-- baize:img-hook downloaded=false reason="正文 6735 字 ≥300，非承重" -->

有关导入 USD 文件的详细信息，请参见[“USD 导入”(USD Import)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-65E19505-E27D-4477-BD7D-7C0F2BC0D328)。

## 音频选项

以下特定于文件类型的选项用于导入音频文件：

#### 音频偏移(Audio offset)

用于指定或使用文件偏移。例如，假定创建了一个小鸟在绷紧的绳上走动的动画，然后想要在小鸟走到绳子尽头的时候播放声音文件。如果已知小鸟走到绳子尽头时处于时间 108 处，就可以在“声音文件偏移”(Sound file offset)字段中将声音文件偏移指定为 108。

##### 继承文件音频偏移(Inherit file audio offset)

如果文件（例如，BWAV 文件）嵌有偏移，Maya 将继承音频文件偏移。如果没有音频偏移且未在“声音文件偏移”(Sound file offset)字段中进行任何设置，则该文件默认放置在场景开始处。

##### 在场景开始处导入(Import at scene start)

将声音文件放置在场景开始处。

##### 按指定的偏移导入(Import at specified Offset)

用于在“声音文件偏移”(Sound file offset)中设置开始播放声音的时间。

##### 声音文件偏移(Sound file offset)

输入一个值作为开始播放声音的时间。添加的值必须与在[“时间滑块”(Time Slider)首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-51A80586-9EEA-43A4-AA1F-BF1370C24A64)的“时间显示”(Time Display)选项中设置的值匹配。

## 移动文件选项

以下特定于文件类型的选项用于导入移动文件：

#### 属性(Attributes)

在“属性”(Attributes)框键入属性名称，然后单击“添加”(Add)，将该属性添加到属性列表中，供导入或导出时使用。如果属性已包含在列表中，系统将不会重复此属性。通过空格分隔属性可以一次添加多个属性。若要移除一个属性，请输入该属性的名称，然后单击“移除”(Remove)。

#### 来自通道盒(From Channel Box)

单击“来自通道盒”(From Channel Box)可以将 Maya 中所有选定的对象按对象的选择顺序与在“通道盒”(Channel Box)中选定的通道合并，然后将其置于列表中。例如，选定了球体 (sphere) 和圆锥体 (cone)，“通道盒”(Channel Box)中选定了 tx 和 sx，则 sphere.tx、sphere.sx、cone.tx 和 cone.sx 将添加到属性列表中，用于导入和导出。

#### 移除选定对象(Remove Selected)

单击“移除选定对象”(Remove Selected)可以移除列表中选定的所有属性。

#### 移除全部(Remove All)

单击“移除全部”(Remove All)可以移除列表中的所有属性。

#### 精度(Precision)

文件导出时将忽略此选项。对于文件导入，这将设置文件的精度。

单击导入或导出时，系统将写入或读取移动文件，只有列表中的属性将受到影响。

## Adobe Illustrator 和 EPS 选项

“Illustrator”导入器无法导入“Illustrator”文本对象。请先将文件中的文本对象转化为路径，然后再将文件导入 Maya。

#### 比例因子(Scale factor)

允许用户控制导入生成的曲线的比例。操作与缩放工具相同。

#### 分组(Group)

启用此选项可以将导入的曲线分成一组。操作与使用“编辑 > 分组”(Edit > Group)相同。

## Autodesk 转换格式 (ATF) 选项

- IGES_ATF

- JT_ATF

- PARASOLID_ATF

- SAT_ATF

- STEP_ATF

- STL_ATF

- WIRE_ATF

- CATIAV4_ATF

- CATIAV5_ATF

- DWG_ATF/DXF_ATF

- NX_ATF

- PROE_ATF

#### 对称层处理(Symmetric Layer Processing)

用于禁用对称层处理。如果对称层导致导入延迟，请禁用此选项。

默认设置为启用。

#### 细分对象

确定如何细分 NURBS 曲面以将其转换为多边形。

- 无(None)：NURBS 曲面保留原样。

- Aruba 细分(Aruba Tessellation)：NURBS 曲面在导入时进行细分。这是最快捷、最可靠的方法。

- ATF 细分(ATF Tessellation)：NURBS 曲面在导入后进行细分。这是过去的方法，因此速度比 Aruba 稍慢。

### Aruba 细分选项

#### 弦偏差(Chordal Deviation)

指定网格三角形与模型几何体之间的最大距离（以厘米为单位）。增加该值会提高整体细分精度，但会降低性能。默认值为 0.0015。

#### 最小弦长(Min Chord Length)

指定边上的任何弦或任意两条相邻栅格线之间允许的最小长度（以厘米为单位）。减小该值可在生成的网格上缩短边，这对于圆边或倒角边尤其重要。 默认值为 0.01。

#### 最大弦长(Max Chord Length)

指定边上的任何弦或任意两条相邻栅格线之间允许的最大长度（以厘米为单位）。增加该值可加长边，这可以减少网格中包含长面的多边形计数。默认值为 100。

#### 采样类型(Sample Type)

确定在细分期间对 NURBS 曲面进行采样所用的方法。选项包括：

- 整个域(Entire Domain)

- G1 分段(G1 Segments)

- 每个跨度(Per Span)（默认值）

- 结值(Knot Values)

- 自适应(Adaptively)

如果遇到与细分精度相关的问题，请尝试不同的“采样类型”(Sample Type)。

#### 自适应(Adaptive)

确定是否在细分期间应用“自适应”(Adaptive)采样。启用此选项可以减少生成的网格中的总体面数。 默认设置为启用。

#### 样例

确定要在细分期间使用的采样数。增加该值可创建更高的多边形网格。默认值为 8。

#### 法线容差(Normal Tolerance)

指定网格中相邻节点之间曲面法线的最大变化（以度为单位）。 使用较小的非零数字会生成更高的多边形网格。默认值：0。

### ATF 细分选项

#### 法线容差(Normal Tolerance)

指定网格中相邻节点之间曲面法线的最大变化（以度为单位）。

#### 表面容差(Surface Tolerance)

指定网格三角形与模型几何体之间的最大距离（以厘米为单位）。

#### 栅格纵横比(Grid Aspect Ratio)

指定整个面中放置的栅格中允许的最大纵横比。

#### 最大边长(Max Edge Length)

指定边上的任何弦或任意两条相邻栅格线之间允许的最大长度（以厘米为单位）。

## 动画曲线选项 (animImport)

必须加载 animImportExport 插件才能看到这些选项。

#### 时间范围(Time Range)

选择一个时间范围选项，然后指定相应设置。

#### 开始(Start)

将动画信息导入选定的对象，使动画在“开始时间”(Start Time)字段中指定的时间开始。

#### 开始/结束(Start/End)

将动画信息导入选定的一个对象或多个对象，缩放动画以适配“开始时间”(Start Time)和“结束时间”(End Time)字段中指定的时间范围。关键帧剪贴板中的动画信息会被缩放或剪裁，具体取决于“剪贴板调整”(Clipboard Adjustment)选项的设置。

#### 当前(Current)

将动画信息导入选定的对象，使动画在“动画控件”(Animation Controls)中显示的当前时间开始。

#### 剪贴板(Clipboard)

将动画信息传递到选定的对象，在关键帧剪贴板上保留动画信息的持续时间和计时。

#### 副本(Copies)

该值将指定导入的动画曲线副本数量。多个副本将按顺序附加。

#### 帮助图像(Help Images)

启用“帮助图像”(Help Images)可以显示多种动画导入选项的效果演示。

#### 剪贴板调整(Clipboard Adjustment)

指定“剪贴板”(Clipboard)内容处理方式选项。

#### 保留(Preserve)

将剪贴板内容复制到曲线上的新位置，不进行任何更改。

#### 缩放(Scale)

选中“开始/结束”(Start/End)后，此选项将变为启用状态。剪贴板曲线的全部内容将拉伸或压缩，以适配指定的导入“时间范围”。

#### 适配(Fit)

选中“开始/结束”(Start/End)后，此选项将变为启用状态。剪贴板内容将被保留（即，不拉伸或压缩），适配指定时间范围的全部内容将被粘贴到新区域中。

#### 粘贴方法(Paste Method)

指定粘贴方法。

#### 插入(Insert)

将剪贴板内容置于指定时间范围中任何现有关键帧之前。指定时间范围之后原始曲线的关键帧将根据粘贴的范围时间进行时间调整。

#### 替换(Replace)

选中“开始/结束”(Start/End)或“剪贴板”(Clipboard)后，此选项将变为启用状态。剪贴板内容将覆盖指定时间范围内的任何现有关键帧。

#### 合并(Merge)

剪贴板内容将添加到曲线上的任何现有关键帧。如果剪贴板关键帧与现有关键帧的时间相同，则剪贴板关键帧将替换现有关键帧。

#### 替换区域(Replace Region)

当“粘贴方法”(Paste Method)设置为“替换”(Replace)后，系统将启用这些按钮。

#### 时间范围(Time Range)

用关键帧剪贴板的内容替换指定时间范围内的关键帧和曲线分段。

#### 整个曲线(Entire Curve)

仅在“时间范围”(Time Range)设置是“剪贴板”(Clipboard)时可用。“整个曲线”(Entire Curve)设置将使用关键帧剪贴板的内容替换导入属性上的动画曲线，实际删除这些属性上的任何现有动画曲线并应用关键帧剪贴板中的新曲线。

#### 连接(Connect)

启用后，可以使用值调整关键帧剪贴板曲线，以便使粘贴分段开始处不出现动画不连续现象。

## 相关主题

- [支持的文件格式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3FDB6F01-1830-4AB3-BB91-287A64A269A6)

- [崩溃后恢复数据](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-89F4AF19-AFDC-40BF-8571-8999C520505C)
