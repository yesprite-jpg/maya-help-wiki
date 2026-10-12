# “融合衰减”(Blend falloff)属性

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" -->

“融合衰减”(Blend Falloff)属性编辑器构件包含一个表，您可以在其中添加各种衰减效果，然后将它们组合在一起以生成复杂的结果。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-B77727C1-351D-47FD-A114-C2EF0AFF6076.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" -->

两个基本体衰减在波浪变形器上融合

访问“融合衰减”(Blend Falloff)属性编辑器构件

- [将变形器衰减应用于几何体](../创建变形器衰减.md)后，在“属性编辑器”(Attribute Editor)的[“变形器属性”(Deformer Attributes)构件](../变形器属性构件.md)中选择“创建融合衰减”(Create Blend Falloff)。此时将显示“融合衰减属性”(Blend Falloff Attributes)选项卡。

有关如何将组件标记附加到组件的信息，请参见[使用组件标记创建变形器衰减](../创建变形器衰减.md)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-29BE0C77-F014-4CFD-89CF-DFBA7E0431F5.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" -->

使用**“添加新指定”(Add New assignment)** ![图：使用“添加新指定”(Add New assignment) 、“移除指定”(Remove assignment) 、“上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-B5E33AF1-E48D-488D-91A2-741BE6430588.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" -->、**“移除指定”(Remove assignment)** ![图：使用“添加新指定”(Add New assignment) 、“移除指定”(Remove assignment) 、“上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-13A1DBD2-73D8-4551-9BC7-16F7B375101A.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" -->、**“上移”(Move Up)** ![图：使用“添加新指定”(Add New assignment) 、“移除指定”(Remove assignment) 、“上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-60321F79-3B0F-4BDE-BDAB-4052742B9647.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" --> 和**“下移”(Move Down)** ![图：使用“添加新指定”(Add New assignment) 、“移除指定”(Remove assignment) 、“上…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-48E848B6-936E-4E42-866A-7241AC284246.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" --> 图标来组织表中的衰减效果。

在行上单击鼠标右键以添加新衰减或指定现有衰减。

#### 基础权重(Base Weight)

为总体融合效果设置“基础权重”(Base Weight)。默认值为 **1.00**。每个顶点的值都由该设置定义。

#### “融合权重”(Blend Weight)表

使用“融合权重”(Blend Weight)表来组织和融合衰减效果。

#### 索引(Idx)

融合数组中的衰减索引（放置）。使用**“上移”(Move Up)** ![图：融合数组中的衰减索引（放置）。使用“上移”(Move Up) 和“下移”(Move Down) 图标重新排列衰减顺序。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-60321F79-3B0F-4BDE-BDAB-4052742B9647.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" --> 和**“下移”(Move Down)** ![图：融合数组中的衰减索引（放置）。使用“上移”(Move Up) 和“下移”(Move Down) 图标重新排列衰减顺序。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-48E848B6-936E-4E42-866A-7241AC284246.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" --> 图标重新排列衰减顺序。

#### 名称

要融合的变形器衰减效果的名称。

#### 重量

变形器衰减效果的权重值。

在“权重”(Weight)字段上单击鼠标右键，可以设置关键帧或锁定权重，以及创建新的表达式或纹理。

#### 创建新表达式...(Create New Expression...)

打开[表达式编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-251640EA-AACC-4F1B-A341-297F0F4CEFE4)。

#### 设置关键帧(Set Key)

为衰减的“权重”(Weight)值设置关键帧。

当“权重”(Weight)属性已设置关键帧时，“权重”(Weight)字段在设置了关键帧的帧上变成亮红色，而暗红色表示该值上有关键帧。

设置关键帧后，在“权重”(Weight)字段上单击鼠标右键，然后选择“断开连接”(Break Connection)以移除关键帧以及到该属性的所有连接。

#### 创建新纹理...(Create New Texture...)

打开[创建渲染节点(Create Render Node)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4918C294-FAAD-45B5-A896-92161177EEED)窗口。

#### 锁定属性(Lock Attribute)

锁定“权重”(Weight)值。Maya 会用灰色背景显示已锁定的属性。

若要解除锁定，请单击鼠标右键，然后选择“解除锁定属性”(Unlock Attribute)。

#### 模式(Mode)

描述如何应用融合的模式。有关详细信息，请参见下面的**“融合模式”**。

## 融合模式

每个顶点的值由“基础权重”(Base Weight)定义，默认值为 1.0。

每个顶点的衰减值修改以前计算的所有值。例如，如果到目前为止计算的值为 A，为衰减计算的值为 B，则新结果为以下模式之一：A、(A*B)、(A/B)、(A+B)、(A-B)、B 或 max(A,B)。

**注**

衰减值在“融合模式”(Blend Mode)表中从上到下解算。

选择希望融合变形器衰减效果的方式。

| 名称 | 行为 |
|---|---|
| 无运算(No Operation) | 在不进行任何更改的情况下应用基础权重值 (B)，忽略衰减，就像未连接衰减一样。 这是默认设置。 示例公式：**A**（无效果） |
| 相乘(Multiply) | 通过将衰减权重 (A) 乘以基础权重值 (B) 来创建放大效果，如以下公式中所示： 衰减融合结果 = 基础权重 x 变形器衰减权重。 例如，将值设置为 0 与禁用效果是一样的。值为 1 时的效果对变形不进行任何更改，而值为 2 会使效果加倍，依此类推。 示例公式：**A*B** |
| 相除(Divide) | 将衰减权重 (A) 除以基础权重值 (B)。 示例公式：**A/B** |
| 添加(Add) | 将衰减权重 (A) 与基础权重值 (B) 合并。 示例等式：**A+B** ![图：将衰减权重 (A) 与基础权重值 (B) 合并。 示例等式：A+B “相加”(Add)模式应用于基本体衰减 A. 设置为…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-ACA370EA-8C37-4F2F-8CA2-97EEFFE6587C.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" -->“相加”(Add)模式应用于基本体衰减 **A**. 设置为 0，**B**. 设置为 10，**C**. 设置为 25 |
| 相减(Subtract) | 衰减权重 (A) 的效果减去基础权重值 (B)。 示例公式：**A-B** |
| 覆盖(Override) | 在不进行任何更改的情况下应用衰减权重值 (A)，忽略基础权重值 (B)，就像没有基础权重一样。 示例公式：**B** |
| 最大值(Max) | 使每个基本体衰减权重值 (A) 独立影响网格。页面顶部的动画显示了使用“最大值”(Max)模式的两个基本体衰减。 示例公式：**max(A,B)** |
| Alpha 融合(AlphaBlend) | 用于创建衰减权重的 Alpha 融合。 示例公式：**out = out*(1-in) + in*inValue** |
