# “平滑蒙皮权重”(Smooth Skin Weights)选项

#### 所需权重差异(Required Weight Difference)

指定由“平滑蒙皮权重”(Smooth Skin Weights)操作进行平滑前，顶点蒙皮权重需要与其相邻顶点蒙皮权重相区分的权重量阈值 (%)。“平滑蒙皮权重”(Smooth Skin Weights)操作将忽略权重在该阈值之外的所有顶点。

#### 平滑迭代次数(Smoothing Iterations)

用于设定平滑算法的运行次数。如果为“平滑迭代次数”(Smoothing Iterations)设定较大的数字，顶点接收到的平滑数量也会增加，从而提供更好的结果。但是，平滑算法运行的次数越多，处理效果所需的时间就越长。默认迭代次数值为 5。

#### 预览(Preview)

启用该选项后，将由“平滑蒙皮权重”(Smooth Skin Weights)操作进行平滑的顶点会在单击“应用”(Apply)后以黄色亮显于场景视图中。当前“权重更改百分比”(Weight Change Percentage)值和目标蒙皮权重的粗糙度确定亮显哪些顶点。

#### 遵守最大影响(Obey Max Influences)

如果 Maya 遇到接近零的权重，则会删减权重以实现高效处理。激活此选项可确保存在小平滑权重时，Maya 始终引用您在[“编辑影响”(Edit Influences)菜单](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-9B2EF2CB-25AF-431D-8A53-62311A08B9ED.htm)中的“设置最大影响”(Set Max Influences)对话框中指定的影响权重。这在您需要固定数量的权重时很重要。默认情况下启用该设置。

请参见[平滑蒙皮权重](../../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/平滑蒙皮权重.md)。
