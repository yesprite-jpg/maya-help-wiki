# “UV 编辑器”(UV Editor)的“视图”(View)菜单

#### 线框(Wireframe)

在“UV 编辑器”(UV Editor)中将 UV 壳显示为清晰的线。此模式的热键为 4。

#### 对象线框颜色(Object Wireframe Color)

确定在“对象模式”(Object Mode)下显示的 UV 壳的颜色。

#### 对象线框 Alpha(Object Wireframe Alpha)

确定在“对象模式”(Object Mode)下显示的 UV 壳的透明度。

#### 组件线框颜色(Component Wireframe Color)

确定在“组件模式”(Component Mode)下显示的 UV 壳的颜色。

#### 组件线框 Alpha(Component Wireframe Alpha)

确定在“组件模式”(Component Mode)下显示的 UV 壳的透明度。

#### 着色

以半透明方式对活动 UV 壳进行着色。在“UV 编辑器”(UV Editor)的 2D 视图内 UV 和 UV 壳重叠的区域。与默认着色相比，会使用更多不透明度对 UV 和 UV 壳重叠的区域进行着色。请参见[显示重叠 UV](../../../../显示和选择%20UV/显示重叠%20UV.md)。 此模式的热键为 5。

#### 颜色模式(Color Mode)

指定如何将颜色应用到 UV 壳。

- “多色”(Multi-Color)将不同的随机颜色应用到每个 UV 壳。

  ![图：“多色”(Multi-Color)将不同的随机颜色应用到每个 UV 壳。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-3278EE77-25FF-4B8F-B141-8553A0ECEFE0.png) <!-- baize:img-hook downloaded=false reason="正文 2835 字 ≥300，非承重" -->

- 当 UV 壳显示在“UV 编辑器”(UV Editor)的 2D 视图中时，“前面和背面”(Front & Back Facing)显示 UV 壳的 UV 缠绕顺序。默认情况下，会将前面 UV 壳（即，具有顺时针缠绕顺序）着色为蓝色。默认情况下，会将背面 UV 壳（即，具有逆时针缠绕顺序）着色为红色。请参见[显示 UV 缠绕顺序](../../../../显示和选择%20UV/显示%20UV%20缠绕顺序.md)。

  ![图：当 UV 壳显示在“UV 编辑器”(UV Editor)的 2D 视图中时，“前面和背面”(Front & Back F…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-62CD2B80-A1CA-44CE-AF53-3B74B5DA20BB.png) <!-- baize:img-hook downloaded=false reason="正文 2835 字 ≥300，非承重" -->

默认值为“前面和背面”(Front & Back Facing)。

#### 多色种子(Multi-Color Seed)

“颜色模式”(Color Mode)设置为“多色”(Multi-Color)时，影响颜色的随机化。

#### 多色 Alpha(Multi-Color Alpha)

“颜色模式”(Color Mode)设置为“多色”(Multi-Color)。

#### 前面颜色(Front facing color)

“颜色模式”(Color Mode)设置为“前面和背面”(Front & Back Facing)时，为缠绕顺序为顺时针的 UV 壳指定着色颜色。默认颜色为蓝。

#### 前面 Alpha (Front facing alpha)

“颜色模式”(Color Mode)设置为“前面和背面”(Front & Back Facing)时，为前面着色 UV 壳指定透明度值。值为 0 是完全透明的，而值为 1 是完全不透明的。默认值为 0.25。

#### 背面颜色(Back facing color)

“颜色模式”(Color Mode)设置为“前面和背面”(Front & Back Facing)时，为缠绕顺序为逆时针的 UV 壳指定着色颜色。默认颜色为红。

#### 背面 Alpha (Back facing alpha)

“颜色模式”(Color Mode)设置为“前面和背面”(Front & Back Facing)时，为背面着色 UV 壳指定透明度值。值为 0 是完全透明的，而值为 1 是完全不透明的。默认值为 0.25。

#### 在 3D 视口中显示(Display in 3D viewport)

确定在选定对象时是否将“UV 编辑器”(UV Editor)着色应用于视口。

#### 在顶部绘制活动选择(Draw active selection on top)

视口。启用后，与包含当前选定组件的对象相关的 UV 壳将显示在所有其他组件之上。

#### UV 扭曲(UV Distortion)

显示 UV 壳的拉伸（红色）或压缩（蓝色）区域。此模式的热键为 7。

#### 解算(Evaluation)

- 每个 UV 壳(Per UV shell)：（默认）比较每个壳各面的平均纹理面积（独立于对象中的其他壳），从而为每个壳生成扭曲反馈。下图显示了 UV 扭曲“每个 UV 壳”(Per UV Shell)。

  ![图：每个 UV 壳(Per UV shell)：（默认）比较每个壳各面的平均纹理面积（独立于对象中的其他壳），从而为每个壳生…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-FC06CFB0-AA7D-4C2A-A4B1-6959EBB7DFC2.png) <!-- baize:img-hook downloaded=false reason="正文 2835 字 ≥300，非承重" -->

- 每对象(Per Object)：将网格的平均面大小与 UV 纹理空间覆盖范围进行比较，从而为整个对象生成扭曲反馈。下图显示了 UV 扭曲“每对象”(Per Object)。

  ![图：每对象(Per Object)：将网格的平均面大小与 UV 纹理空间覆盖范围进行比较，从而为整个对象生成扭曲反馈。下图显…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-B90B8D1B-6792-4762-A6ED-F530B6C7F527.png) <!-- baize:img-hook downloaded=false reason="正文 2835 字 ≥300，非承重" -->

#### Alpha

确定扭曲的透明度。

#### 切换壳边界(Toggle Shell Borders)

以粗体显示当前组件选择中连接的 UV 壳边。有助于查看包含多个 UV 壳的模型以了解壳的排列位置。适用于所有组件模式。此模式的热键为 8。有关详细信息，请参见[显示 UV 壳上连接的边](../../../../显示和选择%20UV/显示%20UV%20壳上连接的边.md)。

#### 纹理边界(Texture Borders)

以粗体显示所有 UV 壳边界。也显示在“视口”(Viewport)中。此模式的热键为 9。

#### 颜色(Color)

确定粗体边界的颜色。

#### 边宽度(Edge Width)

确定粗体边界的厚度。

#### 在 3D 视口中显示(Display in 3D viewport)

在 3D 视口和“UV 编辑器”(UV Editor)中加粗纹理边界。

#### 栅格(Grid)

显示或隐藏纹理坐标栅格。请参见[使用 UV 编辑器栅格](../../../../编辑%20UV/使用%20UV%20编辑器栅格.md)

#### 长度和宽度(Length and width)

按单位确定栅格空间的大小。

#### 栅格线间距(Grid lines every)

按单位确定栅格线之间的间距（从而确定线数）。

#### 细分(Subdivisions)数

将栅格细分为多个更小的区域，使其更易于查看。仅在启用“细分线”(Subdivision Lines)时才可见。

#### 颜色(Color)

#### 显示(Display)

用于显示或隐藏栅格 UI 的各个部分。

#### 栅格数(Grid numbers)

确定是否以及在何处显示栅格间隔。

#### 工具栏(Toolbar)

显示或隐藏编辑器工具栏。

#### 自定义工具架(Custom Shelf)

显示自定义工具架。您可以通过按住 Ctrl + Shift 键并单击将 UV 编辑器项目添加到工具架，或者通过单击鼠标右键添加分割条。

#### 平视显示仪(Heads-Up Display)

允许启用和禁用 HUD 的各个部分。

#### 隔离选择(Isolate Select)

启用和禁用“隔离选择”(Isolate Select)（请参见下文）。

#### UV 统计信息(UV Statistics)

UV 编辑器(UV Editor)。选项包括：

- UV 壳计数(UV Shell count)：选定 UV 壳的数量与当前网格上的 UV 壳总数。

- 重叠 UV 计数(Overlapping UV count)：选定重叠 UV 的数量与重叠 UV 的总数。

- 已反转 UV 计数(Reversed UV count)：按逆时针缠绕方向运行的选定 UV 数与按逆时针方向运行的 UV 总数。请参见[显示 UV 缠绕顺序](../../../../显示和选择%20UV/显示%20UV%20缠绕顺序.md)。

- 已用 UV 空间的百分比(Percentage of used UV space)：壳当前占据的 UV 空间量除以开放空间。可以使用 U 和 V 选项指定特定范围。

**注**

启用

“UV 统计信息”(UV Statistics)

（特别是

“已用 UV 空间的百分比”(Percentage of used UV space)

选项）可能会降低性能。

#### 隔离选择(Isolate Select)

使用该子菜单可以仅显示所有 UV 的一个子集，同时可以将 UV 添加到隔离的子集或从隔离的子集中减去 UV。请参见[显示 UV 的子集](../../../../显示和选择%20UV/显示%20UV%20的子集.md)。

#### 框显全部(Frame All)

平移和缩放编辑器视图以显示整个 UV 集。

#### 框显当前选择(Frame Selection)

平移和缩放编辑器以显示选定 UV。

## 相关主题

- [UV 编辑器菜单栏](../UV%20编辑器菜单.md)

- [UV 编辑器概述](../../../../“UV%20编辑器”%28UV%20Editor%29概述.md)
