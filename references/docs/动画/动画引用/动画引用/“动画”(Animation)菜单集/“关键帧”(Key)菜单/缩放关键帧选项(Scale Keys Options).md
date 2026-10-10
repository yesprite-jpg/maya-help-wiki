# 缩放关键帧选项(Scale Keys Options)

- 在“动画”(Animation) [菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129) (**F4**) 中：“关键帧 > 缩放关键帧”(Key > Scale Keys) > ![图：在“动画”(Animation) 菜单集 (F4) 中：“关键帧 缩放关键帧”(Key Scale Keys)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1895 字 ≥300，非承重" -->

#### 对象(Objects)

选择下列选项之一：

#### 选定(Selected)

设置仅缩放选定对象的关键帧。

#### 全部(All)

设置缩放所有对象的关键帧，包括无法从场景视图中选择的对象（例如，构造历史节点）。

#### 层级(Hierarchy)

指定如何缩放由已分组对象或结成父子关系的对象构成的层级中的关键帧集。

#### 选定(Selected)

设置要缩放的关键帧集仅包括选定对象的动画曲线。默认情况下，“选定”(Selected)处于启用状态。

#### 下方(Below)

设置要缩放的关键帧集包括选定对象和层级中该选定对象下方所有对象的动画曲线。默认情况下，“下方”(Below)处于禁用状态。

#### 通道(Channels)

指定哪个通道的（可设置关键帧属性）动画曲线包括在要缩放的关键帧集中。

#### 所有可设置关键帧(All Keyable)

设置要缩放的关键帧集包括选定对象的所有可设置关键帧属性的动画曲线。默认情况下，“所有可设置关键帧”(All Keyable)处于启用状态。

#### 来自通道盒(From Channel Box)

设置要缩放的关键帧集仅包括当前在“通道盒”(Channel Box)中选定的那些通道的动画曲线。默认情况下，“通道盒”(Channel Box)处于禁用状态。

#### 受驱动通道(Driven Channels)

设置要缩放的关键帧集包括选定对象的所有受驱动关键帧。请参见[受驱动关键帧](../../../../关键帧动画/关键帧动画/受驱动关键帧.md)。默认情况下，“受驱动通道”(Driven Channels)处于禁用状态。

#### 控制点(Control Points)

设置要缩放的关键帧集包括选定可变形对象的控制点的所有动画曲线。控制点包括 NURBS 控制顶点 (CV)、多边形顶点和晶格点。默认情况下，“控制点”(Control Points)处于禁用状态。

#### 形状(Shapes)

设置要缩放的关键帧集包括选定对象的形状节点及其变换节点的动画曲线。通常，如果直接在场景视图中选择一个对象，则会仅选中该对象的变换节点。

若要缩放对象的形状节点及其变换节点的动画曲线，请启用“形状”(Shapes)。若要仅缩放对象的变换节点的动画曲线，请禁用“形状”(Shapes)。默认情况下，“形状”(Shapes)处于启用状态。

#### 时间范围(Time Range)

指定关键帧集的动画曲线的时间范围。从下列选项中进行选择：

#### 全部(All)

将时间范围设置为无限制。

#### 开始/结束(Start/End)

将时间范围设置为从“开始时间”(Start Time)到“结束时间”(End Time)。

#### 时间滑块(Time Slider)

将时间范围设置为由“时间滑块”(Time Slider)的“播放开始时间”(Playback Start)和“结束时间”(End times)定义。

#### 开始时间(Start Time)

设置时间范围的开始时间。“开始时间”(Start Time)仅在启用“开始/结束”(Start/End)时可用。

#### 结束时间(End Time)

设置时间范围的结束时间。“结束时间”(End Time)仅在启用“开始/结束”(Start/End)时可用。

#### 方法(Method)

选择下列选项之一：

#### 缩放/枢轴(Scale/Pivot)

对选定范围内的时间和值应用倍增。这还将设置枢轴点，各轴上从这里开始进行缩放。

启用该选项后，将缩放动画，而不影响位于指定范围前后的动画的曲线。与缩放区域相邻的关键帧和动画曲线分段会同时偏移已压缩或展开的缩放范围量，并保留其形状。

#### 开始/结束(Start/End)

压缩或展开选定范围以适配“新开始/结束时间”(New Start/End Times)字段指定的范围。

#### 仅缩放指定关键帧(Only Scale Specified Keys)

启用该选项后，“缩放关键帧”(Scale Keys)仅影响选定的关键帧。禁用该选项后，“缩放关键帧”(Scale Keys)影响所有关键帧。

#### 时间缩放/枢轴(Time Scale/Pivot)

设置时间倍增。第一个字段设置关键帧集的所有时间的倍增值。第二个字段设置从其开始执行缩放的枢轴点。

**注**

提示：

您可以使用

“时间缩放/枢轴”(Time Scale/Pivot)

选项将一定范围的动画的持续时间减半。

#### 值缩放/枢轴(Value Scale/Pivot)

设置倍增值。第一个字段设置关键帧集的所有值的倍增值。第二个字段设置从其开始执行缩放的枢轴点。

#### 新开始/结束时间(New Start/End Times)

设置压缩或展开关键帧集的时间范围。“新开始/结束时间”(New Start/End Times)仅在启用“开始/结束”(Start/End)时可用。

## 相关主题

- [缩放片段](../../../../Maya%20中的非线性动画/Maya%20中的非线性动画/Trax%20编辑器/操纵片段/缩放片段.md)
