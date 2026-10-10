# 滑动边工具选项(Slide Edge Tool Options)

在“建模”(Modeling)菜单集中，选择“网格工具 > 滑动边工具”(Mesh Tools > Slide Edge Tool) > ![图：在“建模”(Modeling)菜单集中，选择“网格工具 滑动边工具”(Mesh Tools Slide Edge Too…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 629 字 ≥300，非承重" -->可打开这些选项。有关如何使用该工具的详细信息，请参见[滑动多边形边](../../../编辑多边形/变换多边形组件/沿边滑动多边形组件.md)。

#### 模式(Mode)

确定如何重新定位选定边或循环边。

#### 相对(Relative)

基于绝对距离沿选定边移动选定边/循环边。例如，当滑动循环边到滑动边越一半的位置时，所有选定边将显示在相对于其原始位置一半的位置。

#### 绝对(Absolute)

基于绝对距离沿选定边移动选定边/循环边。当沿滑动边的距离极为可变时，“滑动边工具”(Slide Edge Tool)默认使用最短边以确定边/循环边可以移动的最大距离。当希望定位边/循环边在距其他现有边特定距离的位置时，该选项非常有用。

**注**

默认情况下，

“滑动边工具”(Slide Edge Tool)

会在选定顶点接触滑动边的下一个顶点时停止滑动边。可以按住 Ctrl 键以便顶点移出，来覆盖此行为。

#### 使用捕捉(Use Snapping)

确定是否使用捕捉设置。复选标记指定是否使用“捕捉点”(Snapping Points)和“捕捉容差”(Spanning Tolerance)。

#### 捕捉点(Snapping Points)

控制滑动顶点将捕捉的捕捉点数量。滑块范围在 0 到 10 之间。默认捕捉点值是 1，这将捕捉到中点。

#### 捕捉容差(Spanning Tolerance)

控制在顶点捕捉到它之前必须距离捕捉点的靠近程度。滑块范围在 0 到 1 之间。当希望确保顶点始终捕捉到捕捉点时，设定该值为 1。
