# 将动画添加到时间编辑器(Add Animation to the Time Editor)选项

若要打开将动画添加到时间编辑器选项，请执行以下操作：

- 选择“文件 > 从场景选择中添加动画”(File > Add Animation from Scene Selection)

#### 选项

##### 片段名称(Clip Name)

为新创建的片段输入名称。

##### 将动画从场景移动到时间编辑器(Move Animation to Time Editor from Scene)

激活此选项可从场景中移除动画并在“时间编辑器”(Time Editor)中为其创建片段，使其仅显示在“时间编辑器”(Time Editor)中。选择该选项时，不会复制动画曲线，而是改为将其连接到片段。如果要使原始曲线仍然保留在场景中，但要复制这些曲线并将其连接到片段，请禁用此选项。

**注**

即使

动画源

提供的动画在视口中不可见，但它仍然显示在

大纲视图

中的

“timeEditor”

节点下。通过在大纲视图中的动画源上单击鼠标右键并从菜单中选择

“添加到场景”(Add to Scene)

，您可以随时重新应用它。

为了提高性能，默认情况下此选项处于活动状态。

##### 在时间编辑器和场景中复制动画

在“时间编辑器”(Time Editor)中从动画创建片段，同时也将动画保留在场景中。

##### 仅创建动画源(不创建片段)(Create Animation Source only (no clip))

激活此选项可仅将动画源添加到场景并跳过片段创建。通常，“将动画添加到时间编辑器”(Add Animation to the Time Editor)选项默认为同时创建动画源和片段。如果要在[大纲视图(Outliner)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4B9A9A3A-83C5-445A-95D5-64104BC47406)中创建片段库，以便随后将其拖放到“时间编辑器”(Time Editor)中，则此选项非常有用。

**注**

为了提高性能，默认情况下此选项已禁用。

##### 使用公用父对象变换(Use Common Parent Transform)

如果不希望使用选定变换中最常用的父对象变换（默认设置），请禁用此选项。

通过此选项，可以将资产拖动到“时间编辑器”(Time Editor)中而不包括其父层级，但父层级仍包含在生成的片段中。如果要使用重定位器将变换应用于公用父对象（而非片段中的每个变换），这将非常有用。

默认情况下启用该设置。

#### 要添加的属性(Attributes to be Added)

使用这些设置可过滤掉应该使用的可设置关键帧属性。如果“应用并关闭”(Apply and Close)按钮处于禁用状态，请尝试将其他属性设置包含在此列表中。

##### 属性计数(Attribute Count)字段

显示要添加到已创建的片段的可设置动画属性（例如，XYZ 平移和可见性）数量。此信息字段有助于了解“时间编辑器”(Time Editor)处理的属性数。

##### 已设置关键帧(Keyed)

激活此选项可仅将受动画曲线驱动的动画（显示在“曲线图编辑器”(Graph Editor)中）包含在片段中。包括已填充片段中含 Fcurve 的已设置动画对象。默认情况下，此选项已启用。

**注**

此选项仅导入已设置关键帧（已设置动画）的属性。例如，若要包含尚未设置关键帧的可设置动画属性以便稍后设置动画，请同时激活

“静态(即，已编辑但未设置关键帧)”(Static (i.e. edited but not Keyed))

选项。

##### 静态(即，已编辑但未设置关键帧)(Static (i.e. edited but not Keyed))

激活此选项可将当前尚未设置动画的对象（不受动画曲线、非动画曲线等驱动）包含在片段中。

例如，如果只有对象的旋转已设置动画：

![图：激活此选项可将当前尚未设置动画的对象（不受动画曲线、非动画曲线等驱动）包含在片段中。 例如，如果只有对象的旋转已设置动画…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-D26E7649-B629-4629-996A-4BBB43E59674.png) <!-- baize:img-hook downloaded=false reason="正文 2561 字 ≥300，非承重" -->

当此选项处于活动状态且您在“时间编辑器”(Time Editor)中为此对象创建动画片段时，除旋转属性以外的所有属性都将包含在该片段中。

请参见[使用时间编辑器为属性设置动画](../../在时间编辑器中设置动画关键帧/使用时间编辑器为属性设置动画.md)。

##### 受约束(例如，表达式、自定义 DG 网络等)(Constrained (e.g. expressions, custom DG networks, etc.))

仅包含使用约束动画、设置受驱动关键帧或由自定义节点网络连接（驱动）的属性。

##### 包括整个层次(Include Entire Hierarchy)

将对象的完整层次结构添加到新片段。例如，如果只选择了手臂关节，激活此选项可指示“时间编辑器”(Time Editor)导入相关的子对象，如手和手指。

“包括整个层次”(Include Entire Hierarchy)选项在默认情况下处于活动状态，除非您进行更改，否则该选项的状态将一直持续。

**注**

约束不包含在新创建的片段中。

##### 包括根: 平移、旋转、缩放(Include Root: Translate, Rotate, Scale)

确保所有根属性（平移、旋转、缩放）均已添加到动画片段中。

“包括根: 平移、旋转、缩放”(Include Root: Translate, Rotate, Scale)选项在默认情况下处于活动状态，除非您进行更改，否则该选项的状态将一直持续。

##### 集内的属性(Attributes inside Set)

如果仅在集中指定了对象，则将使用所有可设置关键帧的属性。如果定义了特定属性，那么无论是否可设置关键帧，都将接受这些属性，并且它们独立于驱动自身的对象。

##### 完成 HIK 绑定(必须至少选择一个控制器)(Complete HIK Rig (at least one controller must be selected))

只要选择了一个控制器，即可将[“HumanIK”窗口](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9921EDE1-05E2-4062-9F0D-4BADECA29226)中的已有 HIK 角色添加到“时间编辑器”(Time Editor)。

**注**

只需在

“HumanIK”

窗口的

“控件”(Controls)选项卡

中选择一个控制器，即可将 HumanIK 角色导入

“时间编辑器”(Time Editor)

。请参见

在时间编辑器中为 HumanIK 角色设置动画

中的“从 HumanIK 角色绑定创建动画片段”。

#### 动画时间

##### 设置动画原始时间和持续时间(Set animation at original time and duration)

根据在原始动画中指定的帧和长度导入动画片段。

##### 在每次添加时显示选项以便自定义设置(Show Options on every Add to customize settings)

激活此选项可在每次将动画添加到“时间编辑器”(Time Editor)时显示“将动画添加到时间编辑器”(Add Animation to the Time Editor)选项。

**注**

将始终显示包含在

“要添加的属性”(Attributes to be added)

区域中的设置。
