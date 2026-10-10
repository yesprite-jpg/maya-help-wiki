# Maya Atom 导出器选项(Maya Atom Exporter Options)

- 动画 > ATOM > 导入动画(Animate > ATOM > Import Animation)

这些选项允许您指定如何为选定对象导入动画。另请参见[导入 .atom 动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-29639431-48A9-407F-B8D6-FEAF275E5BF0)。

#### Atom 文件(Atom file)

输入要导入的 .anim 文件的名称，或单击“浏览”(Browse)图标 ![图：输入要导入的 .anim 文件的名称，或单击“浏览”(Browse)图标 以导航并选择文件。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-DF281E46-00A8-46E8-A709-3672AEBA0224.png) <!-- baize:img-hook downloaded=false reason="正文 2222 字 ≥300，非承重" --> 以导航并选择文件。

#### 导入方法(Import Method)

可以指定 Maya 用于识别哪些对象收到导入的动画的方法。从下列选项中选择：

#### 选定(Selected)

仅为当前层次中的选定对象导入动画。

#### 层次(Hierarchy)

为所有选定对象导入动画。如果任何选定对象是层次的根（如角色的动画装备的根），Maya 也会尝试为选定对象的所有子对象导入动画。

#### 模板(Template)

可以基于使用“模板”(Template)字段指定的模板文件导入动画。另请参见[基于模板导入动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-29639431-48A9-407F-B8D6-FEAF275E5BF0#GUID-29639431-48A9-407F-B8D6-FEAF275E5BF0__GUID-BD7FBCF5-82F1-4190-84C8-EFB7E1CCADEC)。

#### 匹配方法(Match Method)

指定如何将导入的动画文件映射到选定对象。从下列选项中进行选择：

#### 层次(Hierarchy)

基于 .atom 文件中的层次信息将动画导入到选定对象。Maya 会从根（选定）对象开始并从 .atom 文件中的根对象加载动画，然后遍历层次的其余对象，并与每级中可能的动画进行匹配。

**注**

重要：

如果 .atom 文件包含

“约束”(Constraints)

或

“设置受驱动关键帧”(Set Driven Key)

动画，则无法简单地基于角色层次进行导入操作，需要将

“匹配方法”(Match Method)

设置为

“字符串”(String)

或

“贴图文件”(Map File)

。（请参见

导入 .atom 动画

。）

#### 字符串(String)

基于“搜索”(Search)和“替换”(Replace)字段中输入的术语查找与选定对象匹配的动画。

例如，对于左手层次相似但命名约定不同（L_* 和 Left_*）的两个角色，可以通过在“搜索”(Search) 中输入 L_ 并在“替换”(Replace) 中输入 Left_ 将动画从一个角色的左手导入到另一个角色的左手，来将动画序列从一个角色导入到另一个角色。

当“匹配方法”(Match Method)设置为“字符串”(String)时，还可以使用“添加前缀”(Add Prefix)和“添加后缀”(Add Suffix)字段来输入要附加到动画的字符串。

#### 贴图文件(Map File)

基于使用“贴图文件”(Map File)字段指定的文件将导入的动画匹配到选定对象。

在仅凭“搜索”(Search) +“替换”(Replace) +“添加前缀”(Add Prefix) +“添加后缀”(Add Suffix)字符串不足以确保清晰匹配的情况下，使用贴图文件手动匹配源对象和目标对象是理想的选择。可以设置一个文本文件，列出 .atom 文件中的源对象及其在场景中对应的目标对象的名称。

#### 模板(Template)

可以浏览以指定要在将“导入方法”(Import Method)设置为“模板”(Template)时使用的模板文件。

#### 视图

仅当为导入指定模板文件（在“模板”(Template)字段中）时可用。可以在要加载动画的模板上选择一个更精确的部分（视图）。（例如，选择“手”(Hands)视图以基于角色模板文件仅导入手的动画。）请参见[基于模板导入动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-29639431-48A9-407F-B8D6-FEAF275E5BF0#GUID-29639431-48A9-407F-B8D6-FEAF275E5BF0__GUID-BD7FBCF5-82F1-4190-84C8-EFB7E1CCADEC)。

#### 替换(Replace)

启用此选项后，将使用导入的动画替换选定对象上的任何现有动画。禁用此选项（默认设置）后，Maya 将在指定的时间插入动画，并在之后为任何现有动画设置涟漪。

#### 时间范围(Time Range)

可以指定要导入的动画分段。从下列选项中选择：

#### 开始/结束(Start/End)

导入在“开始时间”(Start Time)和“结束时间”(End Time)字段中指定的范围内的所有动画。

#### 时间滑块(Time Slider)

导入“时间滑块”(Time Slider)中当前显示的时间段内的动画。

**注**

当使用“开始/结束”(Start/End)和“时间滑块”(Time Slider)选项时，如果指定的范围与文件中的范围不匹配，则会进行缩放操作。例如：

- Atom 文件在 1、8、16、24 处包含关键帧

- 导入时，开始/结束时间将设置为 6 和 18。

- 关键帧 8 和 16 将被导入，但可以在 6 到 18 的时间范围内缩放。

若要避免缩放，请在导入选项中指定精确的关键帧范围（在本例中为 8 到 16 之间）。

#### 来自文件(From File)

基于选定 .atom 文件中指定的时间范围导入动画。

#### 开始时间(Start Time)

仅当“时间范围”(Time Range)设置为“开始/结束”(Start/End)时可用。可以指定要导入的第一个（即唯一一个）帧。

#### 结束时间(End Time)

仅当“时间范围”(Time Range)设置为“开始/结束”(Start/End)时可用。可以指定要导入的最后一个帧。

#### 搜索和替换(Search and replace)

仅当“匹配方法”(Match Method)设置为“字符串”(String)时可用。可以搜索导入的 .atom 文件中的特定字符串并在导入数据时替换该字符串。

#### “添加前缀”(Add Prefix)和“添加后缀”(Add Suffix)

仅当“匹配方法”(Match Method)设置为“字符串”(String)时可用。可以输入要在导入的名称之前（前缀）或之后（后缀）附加的字符串。

#### 贴图文件(Map File)

仅当“匹配方法”(Match Method)设置为“贴图文件”(Map File)时可用。可以导航以选择定义如何将 .atom 文件中的导出动画映射到选定对象的贴图文件。
