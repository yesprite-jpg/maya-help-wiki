# “通道盒”(Channel Box)菜单

## 通道(Channels)

#### 为选定项设置关键帧(Key Selected)

在“时间滑块”(Time slider)中的当前帧处为选定对象的亮显属性创建动画关键帧。有关详细信息，请参见[关键帧](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-68F66F69-1F76-4F58-A88A-0A58FBDE5350)。

#### 为所有可设置关键帧的项设置关键帧(Key All Keyable)

在“时间滑块”(Time slider)中的当前帧处为选定对象所有可设置关键帧的属性创建动画关键帧。

#### 为选定项设置受控关键点(Breakdown Selected)

在“时间滑块”(Time slider)中的当前帧处为选定对象的亮显属性创建受控关键点。有关详细信息，请参见[受控关键点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5B605DBF-63DC-44A3-83AE-33EAE2B025F5)。

#### 为所有项设置受控关键点(Breakdown All)

在“时间滑块”(Time slider)中的当前帧处为选定对象的所有属性创建受控关键点。

#### 禁用选定项(Mute Selected)

在播放过程中禁用选定对象的亮显属性动画。“通道盒”(Channel Box)中所有禁用的属性均显示为灰色。有关详细信息，请参见[禁用动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-82DB354C-54BE-4909-B3F8-09926CF90D84)。

#### 禁用全部(Mute All)

在播放过程中禁用选定对象的所有动画。“通道盒”(Channel Box)中所有禁用的属性均显示为灰色。

#### 取消禁用选定项(Unmute Selected)

在播放过程中启用选定对象的亮显属性动画。

#### 全部取消禁用(Unmute All)

在播放过程中启用选定对象的所有动画。

#### 在曲线图编辑器中同步选择(Sync Selection in Graph Editor)

![图：注： 在先前版本的 Maya 中，此选项名为“同步曲线图编辑器显示”(Sync graph editor display…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 4904 字 ≥300，非承重" -->

**注**

在先前版本的

Maya

中，此选项名为

“同步曲线图编辑器显示”(Sync graph editor display)

。

启用时，会在“通道盒”(Channel Box)中同步您的选择，使其同时显示在“曲线图编辑器”(Graph Editor)中。如果未在“通道盒”(Channel Box)中选择通道，则“曲线图编辑器”(Graph Editor)会照常显示选定对象的曲线。

#### 同步时间轴显示(Sync Timeline Display)

启用时，会将“通道盒”(Channel Box)中的选择同步到“时间滑块”(Time Slider)，以便“时间滑块”(Time Slider)只显示这些选定通道的关键帧。设置关键帧（按 S 键或选择“关键帧 > 设置关键帧”(Key > Set Key)）时，将只对通道盒中选择的通道设置关键帧。如果未在“通道盒”(Channel Box)中选择任何对象，则“时间滑块”(Time Slider)会照常显示选定对象的关键帧。

#### 剪切选定项(Cut Selected)

移除选定对象的亮显属性的动画，并将其放置在关键帧剪贴板中。有关详细信息，请参见[在场景之间剪切、复制和粘贴关键帧](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A1146894-E5B1-48CE-BD4D-547FA5648120)。

#### 复制选定项(Copy Selected)

复制选定对象的亮显属性的动画，并将其放置在关键帧剪贴板中。

#### 粘贴选定项(Paste Selected)

将关键帧剪贴板中的动画应用于选定对象的亮显属性。

#### 删除选定项(Delete Selected)

移除选定对象的亮显属性的动画。

#### 复制值(Duplicate Values)

将一个对象的亮显属性复制到任意数量的其他对象。若要使用该功能，请先在按住 Shift 键的同时选择要为其应用重复值的所有对象。然后，在按住 Shift 键的同时选择包含要复制的值的对象。亮显相应的属性。在其中一个属性上单击鼠标右键，然后从显示的标记菜单中选择“复制值”(Duplicate Values)。

#### 冻结(Freeze)

将选定对象上当前的变换、旋转、缩放或全部三项重置为对象的零位置。有关详细信息，请参见[重置变换选项(Reset Transformations Options)和冻结变换选项(Freeze Transformations Options)](../../../../基本参考/基本参考/主菜单/“修改”%28Modify%29菜单/重置变换选项%28Reset%20Transformations%20Options%29和冻结变换选项%28Freeze%20Transformations%20Options%29.md)。

#### 断开连接(Break Connections)

移除属性与其控制连接之间的链接。如果属性具有控制连接，将以紫色亮显该属性。有关详细信息，请参见[断开属性之间的连接](../../查看和更改节点之间的输入和输出关系/断开属性之间的连接.md)。

#### 选择连接(Select Connection)

选择与选定对象的亮显属性对应的连接节点。使用该方法一次只能选择一个连接节点。

#### 锁定选定项(Lock Selected)

将选定对象的亮显属性锁定为其在“时间滑块”(Time slider)的当前帧中的值。解除锁定属性之前，无法在任何帧操纵这些值。

#### 解除锁定选定项(Unlock Selected)

解除锁定选定对象的亮显属性，从而允许修改其值。

#### 隐藏选定项(Hide Selected)

从通道盒中移除选定属性。

#### 锁定并隐藏选定项(Lock and Hide Selected)

锁定选定属性并将其从通道盒中移除。无法操纵锁定的属性。

#### 使选定项不可设置关键帧(Make Selected Nonkeyable)

禁用为选定对象的亮显属性设置关键帧的功能。

#### 使选定项可设置关键帧(Make Selected Keyable)

启用为选定对象的亮显属性设置关键帧的功能。

## 编辑(Edit)

#### 表达式...(Expressions...)

打开表达式编辑器，此时将显示选定对象的亮显属性的表达式。使用表达式可为属性指定特定行为。有关详细信息，请参见[表达式编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-251640EA-AACC-4F1B-A341-297F0F4CEFE4)。

#### 设置受驱动关键帧...(Set Driven Key...)

在“受驱动”部分中打开“设置受驱动关键帧”窗口及选定对象和属性。使用受驱动关键帧可通过单独对象的属性管理某个对象的属性。有关详细信息，请参见[受驱动关键帧](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2C048635-CDD2-4CF7-820D-A032204C8CE8)。

#### 曲线图编辑器(Graph Editor)

打开选定对象和亮显属性的曲线图编辑器。曲线图编辑器可用于通过属性动画的图形表示对属性的动画进行修改。有关详细信息，请参见[曲线图编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6D38EAEA-6032-471E-BD0E-54A74D4443C0)。

#### 通道控制(Channel Control)

打开选定对象的通道控制编辑器。使用通道控制编辑器可查看节点的属性，并修改其可设置关键帧和可编辑的状态。有关详细信息，请参见[通道控制编辑器](“通道控制”%28Channel%20Control%29编辑器.md)。

#### 连接编辑器(Connection Editor)

打开选定对象的“连接编辑器”(Connection Editor)。使用“连接编辑器”(Connection Editor)可在场景中查看和修改节点之间的连接。有关详细信息，请参见[使用“连接编辑器”(Connection Editor)连接节点](../../使用“连接编辑器”%28Connection%20Editor%29连接节点.md)。

#### 属性编辑器(Attribute Editor)

打开选定对象的“属性编辑器”(Attribute Editor)。使用“属性编辑器”(Attribute Editor)可查看对象的节点并修改其关联的属性。有关详细信息，请参见[属性编辑器](../属性编辑器%28Attribute%20Editor%29.md)。

#### 材质属性(Material Attributes)

打开选定对象的“材质属性编辑器”(Material Attributes Editor)。使用“材质属性编辑器”(Material Attributes Editor)可修改选定对象的曲面的显示。有关详细信息，请参见 [Maya 材质](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E985864A-133C-47E6-B989-890EDB920D9F)。

#### 添加属性(Add Attribute)

打开选定对象的“添加属性”(Add Attribute)窗口。使用“添加属性”(Add Attribute)窗口可创建控制现有属性组合或存储属性值的变量的新属性。有关详细信息，请参见[添加属性(Add Attribute)选项](../../../../基本参考/基本参考/主菜单/“修改”%28Modify%29菜单/“添加属性”%28Add%20Attribute%29选项.md)。

#### 编辑属性(Edit Attribute)

打开选定对象的“编辑属性”(Edit Attribute)窗口。使用“编辑属性”(Edit Attribute)窗口可编辑自定义属性。有关详细信息，请参见[“编辑属性”(Edit Attribute)选项](../../../../基本参考/基本参考/主菜单/“修改”%28Modify%29菜单/“编辑属性”%28Edit%20Attribute%29选项.md)。

#### 删除属性(Delete Attributes)

打开选定对象的“删除属性”(Delete Attribute)窗口。使用“删除属性”(Delete Attribute)窗口可删除自定义属性。选择“修改 > 删除属性”(Modify > Delete Attribute)。

#### 发布到资产(Publish to asset)

将选定属性发布到属性的节点上一级别的资产。有关详细信息，请参见[发布或取消发布属性](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7BBE4BC1-4B18-47DA-A972-62121764AFBF)。

#### 取消从资产发布(Unpublish from Asset)

取消从封装选定属性的资产发布选定属性。

#### 锁定未发布的属性(Lock Unpublished Attributes)

对“通道盒”(Channel Box)中的所有节点锁定当前未发布到资产的所有属性。有关详细信息，请参见[锁定资产](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9B18B9F3-2161-4664-9F35-06CBA9797AC2)。

#### 选择节点(Select Node)

选择与从中选择该选项的属性对应的节点。如果已选择节点，则该选项会对其取消选择。

#### 删除节点(Delete Node)

删除与从中选择该选项的属性对应的节点。

#### 删除历史(Delete History)

删除与从中选择该选项的属性对应的节点的所有历史。

#### 设置(Settings)

包含若干属性相关设置，且这些设置可影响与场景中对象的属性交互的方式。

##### 属性调整速度(Attribute adjustment speed)

控制通过拖动鼠标调整属性时鼠标移动距离和数值更改之间的映射。设置的值越大，拖动鼠标时对象移动的距离越远（最多四种不同的速度）。这还会影响[视图中编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C9C88AA3-CE61-4389-9A19-B6456427EBA2)。

##### 双曲线(Hyperbolic)

控制通过拖动鼠标调整属性时鼠标移动距离和数值更改之间的映射类型。

##### 显示名称空间(Show Namespace)

切换场景中对象的名称的显示。有关名称空间的详细信息，请参见[文件引用提示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4C69BD15-DD28-4631-8EC2-2EEC59B7157A)。

##### 无操纵器/不可见操纵器/标准操纵器(No Manips/Invisible Manips/Standard Manips)

切换选定对象的操纵器的状态。使用“无操纵器”(No Manips)可完全移除属性的操纵器并禁用拖动。使用“不可见操纵器”(Invisible Manips)可防止在选择属性名称时显示操纵器。使用“标准操纵器”(Standard Manip)可在选择属性名称时显示操纵器。有关详细信息，请参见[显示或隐藏“通道盒”(Channel Box)中属性的操纵器](显示或隐藏“通道盒”%28Channel%20Box%29中属性的操纵器.md)。

##### 更改精度(Change Precision)

打开“更改精度”(Change Precision)窗口。使用“更改精度”(Change Precision)窗口可修改可指定给对象属性的值的小数精确度。

##### 重置为默认值(Reset to Default)

将所有“设置”(Settings)值返回到其默认配置。

#### 通道名称(Channel Names)

包含若干属性命名选项。“易读”(Nice)显示可读性最强的属性名称，“长”(Long)显示完整的属性名称，“短”(Short)显示缩短的属性名称。

## 对象(Object)

如果已在场景中选择多个对象，则可通过从“对象”(Object)菜单选择每个对象的属性以进行查看。

## 显示(Show)

#### 资产

包含控制资产及其属性在“通道盒”(Channel Box)中的显示方式的选项。

##### 所有属性(All attributes)

显示某个资产的所有已发布属性。

##### 选定对象属性(Selected object attributes)

只显示资产上已从当前选定对象发布的已发布属性。

##### 在顶部显示(Show at top)

启用时，选定对象的资产将显示在“通道盒”(Channel Box)中该对象的上方。

#### 属性(Attributes)

可用于查看按类型过滤的可用属性子集。可以通过单击各种类型进行切换。

#### 清除以下项(Clear Below)

通过选择“清除以下项”(Clear Below)可将“通道盒”(Channel Box)重置为显示所有类型。创建的所有自定义条目都将显示在底部。

#### 反转所显示内容(Invert Shown)

如果正在查看可用属性的某个子集，则该选项将反转过滤器，以显示当前未显示的所有属性。

#### 显示全部(Show All)

在“通道盒”(Channel Box)中显示选定对象的所有属性。自动重置所有过滤器。

#### 显示选定类型(Show Selected Type(s))

仅显示与“通道盒”(Channel Box)中当前选择的属性类型相同的属性。

#### 创建条目(Create Entry)

为“通道盒”(Channel Box)中当前显示的任何属性类型创建自定义过滤器。请注意，无法创建与其中一种已存在的过滤器类型（例如，“平移”(Translate)、“旋转”(Rotate)和“缩放”(Scale)）相匹配的过滤器类型。

#### 删除条目...(Delete Entry...)

可用于删除通过“创建条目”(Create Entry)选项创建的过滤器。
