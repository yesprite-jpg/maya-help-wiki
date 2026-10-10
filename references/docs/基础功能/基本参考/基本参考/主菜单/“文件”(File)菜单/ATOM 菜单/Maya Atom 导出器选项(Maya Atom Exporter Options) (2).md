# Maya Atom 导出器选项(Maya Atom Exporter Options)

- 文件 > ATOM > 导出动画(File > ATOM > Export Animation)

通过这些选项可以指定为选定对象导出哪些动画，以及如何将其导出。另请参见[导出 .atom 动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-20FBCA56-2CD7-46F2-B851-682817961430)。

有关输出 .anim 文件格式的技术信息，请参见 [ATOM 格式描述](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9FA7198C-6BC9-4CB7-AA86-74C3C0A47576)和[示例 .atom 文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-074E8890-08F5-4872-9AA6-45932DC5A1B2)。

## Maya Atom 导出器选项(Maya Atom Exporter Options)

#### Atom 文件(Atom file)

为要导出的 .atom 文件输入一个名称。单击浏览图标 ![图：为要导出的 .atom 文件输入一个名称。单击浏览图标 来选择其他目录。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-DF281E46-00A8-46E8-A709-3672AEBA0224.png) <!-- baize:img-hook downloaded=false reason="正文 1947 字 ≥300，非承重" --> 来选择其他目录。

#### 包含

#### 设置受驱动关键帧(Set Driven Keys)

启用时，Maya 在保存的动画文件中包含受驱动关键帧。禁用时，除非启用“已烘焙动画”(Baked Animation)，否则受驱动关键帧将被忽略。启用“已烘焙动画”(Baked Animation)可以导出受驱动关键帧动画的烘焙结果。另请参见[受驱动关键帧](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2C048635-CDD2-4CF7-820D-A032204C8CE8)。

**注**

重要：

如果选择在 .atom 文件中包含

“约束”(Constraints)

或

“设置受驱动关键帧”(Set Driven Key)

动画，则无法基于角色层次执行简单的导入。在

“Maya Atom 导入器选项”(Maya Atom Importer Options)

中，需要将

“匹配方法”(Match Method)

设置为

“字符串”(String)

或

“贴图文件”(Map File)

以导入动画。（请参见

导入 .atom 动画

。）

#### 约束

启用时，Maya 会将约束保存在已保存的动画文件中。在稍后导入 .atom 文件时，如果要继续修改约束，需使用此选项。

禁用时，除非启用“已烘焙动画”(Baked Animation)，用于导出约束动画的烘焙结果，否则约束将被忽略。

#### 动画层

启用时，Maya 会保存当前动画层的数据。

#### 静态值(Static Values)

启用时，Maya 会保存非动画值（未设置关键帧且没有曲线的属性，如摄影机的[视角(Angle of View)](../../../面板菜单/面板菜单：“视图”%28View%29/摄影机属性编辑器%28Camera%20Attribute%20Editor%29.md#GUID-C3EBB008-7DBE-4B9D-B9AC-1DA974CEFE15__GUID-4B1E7E73-D1C2-42A0-B7AB-2CDF4A234247)）。禁用时，仅保存动画值。

**注**

提示：

运行

listAnimatable

命令可查看选定对象的可设置关键帧的属性列表。

#### 已烘焙动画(Baked Animation)

启用时，Maya 会为被约束、受驱动关键帧或动画层驱动的通道，以及被除动画曲线外的其他对象驱动或被单个动画曲线（由其他对象驱动）驱动的任何属性逐帧保存烘焙结果。不受这些连接驱动的对象和属性将保持其原始动画，不应用烘焙。

禁用时，Maya 会保存任何约束、受驱动关键帧和动画层连接网络等，不会将效果烘焙到对象上。

**注**

如果为

“约束”(Constraints)

和

“受驱动关键帧”(Driven Keys)

启用“包括”(Include)

选项，同时使用

“已烘焙动画”(Baked Animation)

，Maya 将为受驱动关键帧、约束和动画层保存连接网络，且不使用

“已烘焙动画”(Baked Animation)

方法。

#### 控制点(Control Points)

启用时，Maya 将保存与选定的几何体形状（或几何体形状的父变换节点）相关的**所有** CV、多边形顶点和晶格点。

#### 层次(Hierarchy)

可以指定 Maya 是仅基于您的选择、选定的对象层次还是模板文件导出动画。从下列选项中进行选择：

**注**

如果选择多个层次，则选择顺序很重要。稍后导入此 .atom 文件时，还必须以希望接收导入动画的顺序来选择目标对象。

#### 选定(Selected)

仅为当前层次中选定的对象导出动画。

#### 下方(Below)

为层次中的选定对象及所有子对象导出动画。

#### 模板(Template)

可以基于使用“模板”(Template)字段指定的模板文件导出动画。（模板文件包含保存哪些对象、通道和属性的信息。）

#### 通道

用于指定为选定对象保存哪些通道。从下列选项中进行选择：

#### 所有可设定关键帧(All Keyable)

保存选定对象动画的所有可设置关键帧的通道。

#### 来自通道盒(From Channel Box)

仅保存在“通道盒”(Channel Box)中选定的通道。

#### 时间范围(Time Range)

可以指定要导出的动画片段。从下列选项中进行选择：

#### 时间滑块(Time Slider)

导出当前显示在“时间滑块”(Time Slider)中的所有关键帧动画。

#### 全部

从选定对象导出所有动画。

#### 单帧(Single Frame)

基于您在“开始时间”(Start Time)字段中输入的帧，导出动画的单个帧（一个姿势）。

#### 开始/结束(Start/End)

导出您在“开始时间”(Start Time)和“结束时间”(End Time)字段中指定的范围内的所有动画。

#### 开始时间(Start Time)

仅在“时间范围”(Time Range)设置为“开始/结束”(Start/End)时可用。可以指定要导出的第一帧（或唯一帧）。

#### 结束时间(End Time)

仅在“时间范围”(Time Range)设置为“开始/结束”(Start/End)时可用。可以指定要导出的最后一帧。
