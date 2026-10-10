# “大纲视图”(Outliner)菜单

使用“显示”(Display)和“显示”(Show)菜单，可以选择大纲视图中要显示的内容。[“面板(Panels)”菜单](../../../基本参考/基本参考/面板菜单/面板菜单：“面板”%28Panels%29.md)与视图面板中的菜单相同。

通过在大纲视图中的空白区域和大多数节点类型上单击鼠标右键，也可以使用“显示”(Display)和“显示”(Show)命令。在特定节点类型上单击鼠标右键时，您还可以使用主“显示”(Display)和“显示”(Show)菜单中未提供的命令访问其上下文菜单。有关信息，请参见[大纲视图(Outliner)上下文菜单](“大纲视图”%28Outliner%29上下文菜单.md)。

## 显示(Display)

#### 仅 DAG 对象(DAG Objects Only)

仅显示可变换节点。有关 DAG 节点的描述，请参见 [DAG 层次](../DAG%20层次.md)。

#### 形状(Shapes)

显示变换节点下的形状节点。

#### 指定的材质(Assigned Materials)

显示指定给场景中每个对象的着色器。如果对象的着色器已指定给面，则指定给该对象的所有着色器均会列出并分组到“材质”(Materials)节点下。

#### 时间编辑器(Time Editor)

显示 timeEditor 节点，其中包含合成与动画源以供[时间编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E4B5DB7D-7351-4561-BD8B-60AC9D48DDF6)使用。请参见[通过时间编辑器合成创建多个动画故事](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F7732E60-11E1-48A6-8C53-17A6AF7B4829)和[时间编辑器动画源](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6F8E555F-79C4-48D2-A6EE-53CC022E95C8)。

#### 引用节点(Reference Nodes)

显示场景中被引用文件的引用节点。

#### 引用成员(Reference Members)

引用节点(Reference Nodes)显示处于启用状态时，显示引用节点的对象层次。

#### 属性(通道) (Attributes (Channels))

显示节点上的属性。使用圆形加号和减号按钮可显示节点属性。

#### 集成员(Set Members)

显示集内的成员。

#### 已连接(Connected)

仅显示已连接到其他节点、已设置关键帧或已用某种方法（通过设置受驱动关键帧、约束、运动路径或表达式）连接的属性。

#### 显示名称空间(Show Namespace)

显示被引用对象的名称空间。

#### 忽略“在大纲视图中隐藏”(Ignore 'Hidden in Outliner')

如果已选择节点并在快捷上下文菜单中选择“在大纲视图中隐藏”(Hide in Outliner)，则会忽略这些节点的隐藏状态，使节点显示在大纲视图中。

#### 忽略“使用大纲视图颜色”(Ignore 'Use Outliner Color')

如果已在“属性编辑器”(Attribute Editor)中的“Transform”(变换)或“形状”(Shape)选项卡上为对象选择“显示”(Display) > “使用大纲视图颜色”(Use Outliner Color)，则会忽略其颜色并在大纲视图中改用该节点名称对应的默认颜色。

#### 显示禁用信息(Show Mute Information)

对已使用“曲线图编辑器”(Graph Editor)或“通道盒”(Channel Box)禁用动画的属性，切换显示“禁用”(Mute)标志的状态。“禁用”(Mute)标志仅出现在左侧“曲线图编辑器”(Graph Editor)的树视图中。

#### 按层组织(Organize by Layer)

切换动画层的属性是根据其所属的层显示，还是根据属性本身进行组织。

![图：切换动画层的属性是根据其所属的层显示，还是根据属性本身进行组织。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-639E5424-D71D-4521-A6C9-D4F2CACEEDEA.gif) <!-- baize:img-hook downloaded=false reason="正文 4389 字 ≥300，非承重" -->

#### 按片段组织(Organize by Clip)

切换通过时间编辑器片段设置动画的对象的动画曲线是根据其所属的片段显示，还是根据对象的属性进行组织。

在[“曲线图编辑器大纲视图”(Graph Editor outliner)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EC141C05-37D8-4835-989B-538432690DBE)中激活此选项，可查看选定对象（按片段分组）的动画曲线受控关键点。

**注**

可对驱动动画的属性使用

“按片段组织”(Organize by Clip)

，以便仅当选择已设置动画的对象时才会看到此效果。

![图：切换通过时间编辑器片段设置动画的对象的动画曲线是根据其所属的片段显示，还是根据对象的属性进行组织。 在“曲线图编辑器大纲…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-F0955205-71F2-4541-BB7D-60B0B967AB28.gif) <!-- baize:img-hook downloaded=false reason="正文 4389 字 ≥300，非承重" -->

#### 自动展开层(Auto-expand Layers)

切换是否以展开的形式自动显示动画层。

#### 窗口布局(Window Layout)

![图：大纲视图分割视图 A. 水平，B. 垂直 用于选择 Maya 主“大纲视图”(Outliner)（“窗口 大纲视图”(W…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-BC9EB8C7-0686-4BD8-B7DF-FE553CD97622.png) <!-- baize:img-hook downloaded=false reason="正文 4389 字 ≥300，非承重" -->

大纲视图分割视图 **A.** 水平，**B.** 垂直

用于选择 Maya 主“大纲视图”(Outliner)（“窗口 > 大纲视图”(Windows > Outliner)）内容的显示方式。展开此卷展栏以选择“水平分割”(Split Horizontally)（默认设置）或“垂直分割”(Split Vertically)。

**注**

用于垂直分割大纲视图的选项仅在 Maya 主

大纲视图(Outliner)

（

“窗口 > 大纲视图”(Windows > Outliner)

）中可用。其他大纲视图（例如

“曲线图编辑器大纲视图”(Graph Editor outliner)

或

“摄影表”(Dope Sheet)大纲视图

）只能水平分割。

#### 高级资产内容(Advanced Asset Contents)

选择封装到高级资产中的节点在“大纲视图”(Outliner)中的显示方式。可从下列选项中选择：

“在资产下”(Under Asset)仅显示作为资产子节点的节点，而

“在父对象下”(Under Parent)仅显示层次中的节点。

“二者”(Both)显示资产下和层次中的相同节点。

“None”完全隐藏封装节点。

#### 通道名称(Channel Names)

选择在启用“属性(通道)”(Attributes (Channels))时显示的属性名称。“易读”名称可读性较高。全称和简称是属性的实际名称，可在表达式和 MEL 中使用。

#### 排序顺序(Sort Order)

选择“场景层次”(Scene Hierarchy)可显示层次，或者选择“对于类型按字母顺序”(Alphabetical Within Type)可显示每个节点类型的统一字母顺序列表。

#### 属性顺序(Attribute Order)

更改属性的显示顺序。属性可以按字母升序或降序排列。

#### 动画层过滤器(Animation Layers Filter)

过滤大纲视图中显示的动画层：

- “从层编辑器显示选项”(From Layer Editor Show Options)将根据[动画层编辑器(Animation Layer Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-46091038-7F23-467C-8FEC-844A26C11EDA)中的“显示”(Show)菜单选项显示动画层。

- “全部影响”(All Affecting)显示场景中的所有动画层。

- “活动”(Active)仅显示场景中的活动动画层。

- “选定”(Selected)仅显示选定的动画层。

- “活动的和选定的”(Active and Selected)显示活动的和选定的动画层。

- “显示层权重”(Show Layer Weight)切换显示动画层的权重，就像已设置关键帧一样。

**注**

有关动画层何时处于活动、受影响或选定状态的信息，请参见

动画层状态

。

#### 渲染设置过滤器(Render Setup Filter)

在大纲视图顶部切换显示“渲染层”(Render Layer)过滤器，您可从中选择不同的过滤选项。可以在“显示 > 对象”(Show > Objects)菜单中选择相同的“渲染层”(Render Layer)过滤器。有关详细信息，请参见[在大纲视图中过滤并仅显示渲染设置成员](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1A77E0A9-D910-4170-95B5-8A858A7F0C50)。

## 显示(Show)

#### 对象(Objects)

从此菜单中选择一个或多个过滤器，以便在“大纲视图”(Outliner)中仅显示这些对象类型。按住 Ctrl 键可在选择多个过滤器时将此菜单保持打开状态。

选择“清除以下项”(Clear Below)可以禁用所有过滤器。

#### 属性(Attributes)

如果已启用“显示 > 属性(通道)”(Display > Attributes (Channels))，则可选择要在“大纲视图”(Outliner)中显示的属性类型。选择“清除以下项”(Clear Below)可以禁用所有过滤器。

#### 隐藏(Hidden)

隐藏的属性。

#### 由动画曲线驱动(Driven by Anim Curve)

带有动画曲线的属性。这包括使用关键帧、设置受驱动关键帧、约束和运动路径设置了动画的属性。

#### 由表达式驱动(Driven by Expression)

由表达式控制的属性。

#### 由受驱动关键帧驱动(Driven by Driven Key)

属性由受驱动关键帧驱动。

#### 可设定关键帧(Keyable)

可设定关键帧的属性。

#### 缩放/旋转/平移(Scale/Rotate/Translate)

分别表示“缩放”、“旋转”或“平移”属性。

#### 缩放旋转平移(Scale Rotate Translate)

所有变换（缩放、旋转和平移）属性。

#### 用户定义(User Defined)

用户定义的属性。详细信息请参见[创建、编辑或删除自定义属性](../查看和编辑属性/创建、编辑或删除自定义属性.md)。

#### 已发布(Published)

发布到资产的属性。

#### 反转所显示内容(Invert Shown)

反转您在“对象”(Objects)子菜单中选择的过滤器，使可见对象隐藏，隐藏对象可见。

#### 显示全部(Show All)

关闭“显示”(Show)菜单中的所有过滤器。

#### 显示选定类型(Show Selected Type(s))

仅显示与当前选择类型相同的对象类型。该选项可以创建过滤器，将“大纲视图”(Outliner)中显示的对象类型和属性限制为与当前选择相同的对象类型或属性。

例如，如果在大纲视图中选择对象的“平移 X”(Translate X)、“平移 Y”(Translate Y)、“平移 Z”(Translate Z)属性，然后选择“显示选定类型(Show Selected Type(s))，则将过滤所有非平移属性，且在大纲视图中仅显示平移属性。“显示选定类型”(Show Selected Type(s))过滤器将保持活动状态，直到选择另一“显示”(Show)菜单选项（如“显示全部”(Show All)）。

#### 选择属性(Select Attributes)

打开“选择属性”(Select Attributes)窗口，在其中可以过滤为选定对象显示的属性。

“选择属性”(Select Attributes)窗口将显示“平移”(Translate)、“旋转”(Rotate)和“缩放”(Scale) XYZ 属性的复选框栅格，以及选定对象其他任何属性的列表。使用这些复选框可以启用和禁用每个属性的显示。（例如，请参见[过滤“曲线图编辑器”(Graph Editor)中的曲线显示](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-15325DB5-6650-4669-876E-7616BE349B86)。）

#### 创建条目(Create Entry)

可以用于保存和命名当前“显示”(Show)菜单过滤器。

“创建条目”(Create Entry)仅在“大纲视图”(Outliner)中显示的对象和属性已由“显示选定类型”(Show Selected Type(s))菜单选项过滤后才可用。

#### 删除条目(Delete Entry)

可以删除保存的“显示”(Show)菜单过滤器。

#### 显示辅助节点(Show Auxiliary Nodes)

显示因为很少需要而使得“大纲视图”(Outliner)通常不显示的节点类型（例如对拓节点）。

#### 辅助节点(Auxiliary Nodes)

可以设置将被视为“辅助”的节点。

您可以自定义隐藏一些节点，以便编辑器看起来整洁有序。通常，这些节点不常用于查看或编辑。选择此选项可以显示“辅助节点”(Auxiliary Nodes)编辑器，并自定义在编辑器中隐藏的节点类型。详细信息请参见[辅助节点(Auxiliary Nodes)](../节点类型.md#GUID-21B83FF0-0435-4087-8C2E-23B420028B71__WS17956D7ADBC6E736-5E82C947117AE309C61-7FF8)。

## 相关主题

- [“大纲视图”(Outliner)上下文菜单](“大纲视图”%28Outliner%29上下文菜单.md)

- [查看和编辑节点层次](../编辑节点层次.md)
