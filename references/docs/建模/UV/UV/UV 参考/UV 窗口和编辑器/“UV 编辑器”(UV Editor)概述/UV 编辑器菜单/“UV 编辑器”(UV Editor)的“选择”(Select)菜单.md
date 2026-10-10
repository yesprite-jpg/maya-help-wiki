# “UV 编辑器”(UV Editor)的“选择”(Select)菜单

在 UV 编辑器中工作时，在标记菜单上也会提供此菜单中的项目。按住 Ctrl 键并单击鼠标右键可访问它们。

#### 全部(All)

选择当前组件模式的所有组件。

#### 清除(Clear)

取消选择所有对象。

#### 反转(Inverse)

选择当前组件模式的所有未选定组件，反之亦然。

#### 组件(Components)

在各种组件选择模式之间进行切换。选项包括“顶点”(Vertex)、“边”(Edge)、“面”(Face)、“UV”、“UV 壳”(UV Shell)。

**注**

选择模式将沿用于

“视口”(Viewport)

。

#### 背面(Back-facing)

[显示 UV 缠绕顺序](../../../../显示和选择%20UV/显示%20UV%20缠绕顺序.md)

#### 前面(Front-facing)

[显示 UV 缠绕顺序](../../../../显示和选择%20UV/显示%20UV%20缠绕顺序.md)

#### 重叠(Overlapping)

- UV/顶点：直接彼此重叠的组件。

- UV 壳/边/面：与同类型的其他组件至少部分重叠的组件。

#### 非重叠(Non-Overlapping)

- UV/顶点：不直接彼此重叠的组件。

- UV 壳/边/面：与同类型的其他组件甚至不存在部分重叠的组件。

#### 纹理边界(Texture Borders)

UV 壳开口端上的 UV。

#### 未映射面(Unmapped faces)

没有关联 UV 映射的面。

#### 最短边路径工具(Shortest Edge Path Tool)

在两个或多个选择点（顶点或 UV）之间选择边的最短路径。“选择最短边路径工具”(Select Shortest Edge Path Tool)可确定任意两个选择的点之间的最直接的路径，并可选择两者之间的边。

需要后续执行“切割 UV 边”(Cut UV Edges)操作时，“选择最短边路径工具”(Select Shortest Edge Path Tool)特别适合在网格上选择边的较长且可能缠绕的路径。

#### 增长(Grow)

将当前类型的所有相邻组件添加到当前选择。

#### 沿循环方向扩大(Grow Along Loop)

仅沿同一循环边将当前类型的所有相邻组件添加到当前选择。

**注**

对于顶点和 UV，必须沿同一循环边选择两个组件，此选项才能正常运行。

#### 收缩(Shrink)

从当前选择中移除一层当前类型的相邻组件。

#### 沿循环方向收缩(Shrink Along Loop)

仅沿同一循环边从当前选择中移除一层当前类型的相邻组件。

#### 选择过滤器(Filter Selection)

基于所选的选项改变当前选择。

#### 选定图像的面(Faces of Selected Images)

仅显示与当前选定纹理图像关联的面。

#### 包含的面(Contained Faces)

显示 UV、边或顶点的当前选择包含的所有面。

#### 连接面(Connected Faces)

亮显共享当前选定 UV、边或顶点的所有面。

#### 转化当前选择(Convert Selection)

将当前选定的组件转换为指定类型的连接组件或所选周长周围的组件。详细信息请参见[转化当前选择选项(Convert Selection Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DCE04BA9-A2CF-44AA-8045-FFF2392B6796)。

## 相关主题

- [UV 编辑器菜单栏](../UV%20编辑器菜单.md)

- [UV 编辑器概述](../../../../“UV%20编辑器”%28UV%20Editor%29概述.md)
