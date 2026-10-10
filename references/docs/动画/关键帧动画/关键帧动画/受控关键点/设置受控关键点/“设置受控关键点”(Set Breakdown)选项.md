# “设置受控关键点”(Set Breakdown)选项

打开“设置受控关键点”(Set Breakdown)选项

- 选择“关键帧 > 设置受控关键点关键帧”(Key > Set Breakdown Key) > ![图：选择“关键帧 设置受控关键点关键帧”(Key Set Breakdown Key) 。受控关键点可用的选项与通过选择“关…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1108 字 ≥300，非承重" -->。受控关键点可用的选项与通过选择“关键帧 > 设置关键帧”(Key > Set Key) > ![图：选择“关键帧 设置受控关键点关键帧”(Key Set Breakdown Key) 。受控关键点可用的选项与通过选择“关…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1108 字 ≥300，非承重" --> 获得的选项相同。

请参见[设置受控关键点](../设置受控关键点.md)。

### 在以下对象上设置受控关键点(Set Breakdowns on)

指定将在哪些属性上设置受控关键点。

#### 所有可设定关键帧的属性(All Keyable Attributes)

在选定对象的所有属性上设置受控关键点。

#### 所有操纵器控制柄(All Manipulator Handles)

在受选定操纵器影响的属性上设置受控关键点。例如，使用“移动工具”(Move Tool)时，仅会在“平移”(Translate)“X”、“Y”和“Z”属性上设置受控关键点。

#### 当前操纵器控制柄(Current Manipulator Handle)

在受选定操纵器控制柄影响的属性上设置受控关键点。例如，使用“移动工具”(Move Tool)的“X”平移控制柄时，仅在“平移 X”(Translate X)属性上设置受控关键点。

### 在以下位置设置受控关键点(Set Breakdowns at)

指定在何时设置受控关键点。

#### 当前时间(Current Time)

仅在当前时间处设置受控关键点。

#### 提示(Prompt)

Maya 提示设置受控关键点的时间。

### 层次(Hierarchy)

指定将在父子层次内的哪些对象中设置受控关键点。

#### 选定(Selected)

仅在选定对象的属性上设置受控关键点。

#### 下方(Below)

在选定对象及其子对象的属性上设置受控关键点。

### 通道(Channels)

指定将在哪些通道上设置受控关键点。

#### 所有可设定关键帧(All Keyable)

在选定对象的所有通道上设置受控关键点。

#### 来自通道盒(From Channel Box)

在选定对象的选定通道上设置受控关键点。

#### 控制点(Control Points)

在选定对象的控制点上设置受控关键点。“控制点”(Control points)可为 NURBS CV、多边形顶点或晶格点。请注意，如果启用“控制点”(Control Points)，并将受控关键点添加到含有多个控制点的对象（例如，复杂的 NURBS 曲面），则将设定大量受控关键点。这样会导致 Maya 的操作速度变慢。如果还将“层次”(Hierarchy)设定为“下方”(Below)，则可能会导致 Maya 的操作速度更慢。请仅在必要时才启用这些选项。

如果删除具有 CV、且含有受控关键点或关键帧的对象的构建历史，则动画将不再正常工作。

#### 形状(Shapes)

如果启用，则在对象的形状节点和变换节点的属性上设置受控关键点。如果禁用，则仅在变换节点的属性上设置受控关键点。
