# blendShape

为基础对象创建融合形变变形器（请参见[创建融合形变变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-7413C450-603C-4EAD-AF70-465D4EAE5973.htm)）时，系统将创建融合变形节点，该节点以每个目标形状的指定量融合到该对象的基础形状中。

对象上的每个融合变形节点都有一组自己的目标形状，且仅融合属于自己的目标形状。每个目标形状都有自己的权重值，您可以在形变编辑器或通道盒中进行设置。

**注**

提示：

如果要为此变形器创建衰减（或渐变效果），以使变形效果在指定的距离后减少或衰减，请使用

组件标记

。请参见

创建变形器衰减

。

## 融合变形属性(Blend Shape Attributes)

#### 原点(Origin)

指定融合变形是相对于基础对象形状的位置、旋转和缩放还是由您直接指定。从下列选项中选择。

#### 世界(World)

将基础对象形状融合到目标对象形状中，并顾及目标对象形状之间的任何位置、旋转和缩放差异。

**注**

局部和世界选择与“原点”(Origin)创建选项的选择相同。有关详细信息，请参见[融合变形选项(Blend Shape Options)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-C954C197-6D56-4EB8-BEA0-70DD1BBBAD6B.htm)。但是，“用户”(User)属性不是“原点”(Origin)创建选项的选择之一。

#### 局部(Local)

将基础对象形状融合到目标对象形状中，同时忽略目标形状之间的位置、旋转和缩放差异。

#### 用户(User)

指定两种特殊属性（baseOrigin 和 targetOrigin）提供原点信息。有关这些属性的详细信息，请参见联机“节点和属性参考”(Node and Attribute Reference)和“MEL 命令参考”(MEL Command reference)。可以使用 setAttr MEL 命令设置 baseOrigin 和 targetOrigin 属性的值。

## 权重(Weight)

#### 目标

指定已命名目标的影响值或权重。值 0.000 指定目标没有影响；值 1.000 指定目标具有最大影响。对于每个已命名目标，可以使用滑块选择从 0.000 到 1.000 的值。

**注**

这些目标“权重”(Weight)滑块对应于[形变编辑器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-3C92402C-B24E-4874-AC8D-EADF976A19DC.htm)中的滑块和通道盒中的目标形状通道值。

#### 支持负权重(Support Negative Weights)

启用后，您可以为融合形变变形器输入负权重值。禁用该选项后，最小权重值将为 0，且负值将不受支持。默认情况下，此选项处于禁用状态。

## 变形器属性(Deformer Attributes)

#### 封套(Envelope)

指定变形比例因子。使用滑块选择从 0.000 到 1.000 的值。您也可以输入从 -2.000 到 2.000 的值。输入值 2.000 将获得双倍的总变形效果。负值将反转效果。默认值为 1.000。

**注**

“封套”(Envelope)属性对应于[形变编辑器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-3C92402C-B24E-4874-AC8D-EADF976A19DC.htm)中的融合形变变形器“权重”(Weight)值和通道盒中的“封套”(Envelope)通道。

## 节点行为(Node Behavior)

请参见[常规变形器节点属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-778B7255-F6F9-4056-8952-B28F8E222E72.htm)。

## 附加属性(Extra Attributes)

默认情况下没有任何附加属性。
