# 设置关键帧选项(Set Key Options)

- 在“动画”(Animation) [菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129) (**F4**) 中：“关键帧 > 设置关键帧”(Key > Set Key) > ![图：在“动画”(Animation) 菜单集 (F4) 中：“关键帧 设置关键帧”(Key Set Key)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1374 字 ≥300，非承重" -->

#### 在以下对象上设置关键帧(Set Keys on)

指定将在哪些属性上设置关键帧。

#### 所有操纵器控制柄和可设置关键帧的属性(All Manipulator Handles and Keyable Attributes)

为当前操纵器设置关键帧，如果没有任何操纵器，则选择当前对象。这是默认设置。

#### 所有可设置关键帧的属性(All Keyable Attributes)

在选定对象的所有属性上设置关键帧。

#### 所有操纵器控制柄(All Manipulator Handles)

在受选定操纵器影响的属性上设置关键帧。例如，在使用“移动工具”(Move Tool)时，将在“平移 X”(Translate X)、“平移 Y”(Translate Y)和“平移 Z”(Translate Z)属性上设置关键帧。

#### 当前操纵器控制柄(Current Manipulator Handle)

在受选定操纵器控制柄影响的属性上设置关键帧。例如，在使用“移动工具”(Move Tool)的 X 平移控制柄时，将在“平移 X”(Translate X)属性上设置关键帧。

#### 在以下时间设置关键帧(Set Keys at)

指定设置关键帧的时间。

#### 当前时间(Current Time)

仅在当前时间设置关键帧。

#### 提示(Prompt)

Maya 提示设置关键帧的时间。

#### 设置 IK/FK 关键帧(Set IK/FK Keys)

在为 IK 控制柄或关节链设置关键帧时，“设置 IK/FK 关键帧”(Set IK/FK Keys)会为控制柄的所有属性和链的所有关节添加关键帧。这样，您可以创建平滑的 IK/FK 动画。仅在启用“所有可设置关键帧的属性”(All Keyable Attributes)时，该选项才可用。有关详细信息，请参见[设置 IK/FK 关键帧(Set IK/FK Key)](“IKFK%20关键帧”%28IKFK%20Keys%29菜单.md#GUID-C5ACDDBC-9E30-443C-8419-F07FC41E9A86__SECTION_E3C2A7D6F8064F578E2024CA90F447F9)和[启用 IK 解算器(Enable IK Solver)](“IKFK%20关键帧”%28IKFK%20Keys%29菜单.md#GUID-C5ACDDBC-9E30-443C-8419-F07FC41E9A86__SECTION_E8C719563A274D0CB493D538B5A38F89)。

#### 设置关键帧保留(Set Key Preserves)

在设置关键帧时保留曲线形状。启用时，设置关键帧（未更改 TRS 值时，在现有曲线上），并保留曲线的形状和关键帧在任意一侧的切线形状。

#### 层级(Hierarchy)

指定将在父子层级中的哪些对象上设置关键帧。

#### 选定(Selected)

仅在选定对象的属性上设置关键帧。

#### 下方(Below)

在选定对象及其子对象的属性上设置关键帧。

#### 通道(Channels)

指定将在哪些通道上设置关键帧。

#### 所有可设置关键帧(All Keyable)

在选定对象的所有通道上设置关键帧。

#### 来自通道盒(From Channel Box)

在选定对象的选定通道上设置关键帧。

#### 控制点(Control Points)

在选定对象的控制点上设置关键帧。控制点是 NURBS CV、多边形顶点或晶格点。请注意，如果启用“控制点”(Control Points)并对具有许多控制点的对象设置关键帧（例如，复杂的 NURBS 曲面），则将设置大量关键帧。这样会降低 Maya 操作的速度。如果还将“层级”(Hierarchy)设置为“下方”(Below)，则可能会导致 Maya 的操作速度更慢。仅在必要时启用这些选项。

如果删除具有关键帧 CV 的对象的构建历史，动画将不再正常工作。

#### 形状(Shapes)

如果启用该选项，则在对象的形状节点和变换节点的属性上设置关键帧。如果禁用该选项，则将仅在变换节点的属性上设置关键帧。
