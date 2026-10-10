# 圆角曲线选项(Fillet Curve Options)

使用以下选项可设置在选择“曲线 > 圆角”(Curves > Fillet)时发生的情况。

#### 修剪(Trim)

仅保持流向圆角曲线端点的原始曲线的部分。将删除其他部分。

![图：仅保持流向圆角曲线端点的原始曲线的部分。将删除其他部分。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F4EE643D-7733-4A62-85D9-833739067206.png) <!-- baize:img-hook downloaded=false reason="正文 857 字 ≥300，非承重" -->

#### 接合(Join)

将已修剪的曲线接合到圆角曲线，从而创建单条曲线。仅当“修剪”(Trim)处于启用状态时可用。

![图：将已修剪的曲线接合到圆角曲线，从而创建单条曲线。仅当“修剪”(Trim)处于启用状态时可用。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-10C79454-18F5-42C8-AC64-4DD5B2CA0997.png) <!-- baize:img-hook downloaded=false reason="正文 857 字 ≥300，非承重" -->

#### 保持原始(Keep Original)

保留用于创建圆角的原始曲线。这样即可在使用不同设置的情况下再次为曲线创建曲线圆角。

#### 构建(Construction)

选择曲线圆角的构建方式。

“圆形”(Circular)将创建一个半圆形的圆弧。

“自由形式”(Freeform)创建的曲线由您在“曲线圆角”(Curve Fillet)操作之前选定的曲线点决定。

#### 半径(Radius)

设定圆形圆角圆弧的锐度。

#### 自由形式类型(Freeform Type)

选择自由形式圆角顶点的放置位置。

“切线”(Tangent)将自由形式圆角顶点放置于相交角附近。

“融合”(Blend)将自由形式圆角顶点放置于曲线点之间中点的附近，曲线点是在之前的“曲线圆角”(Curve Fillet)操作中选定的。

#### 融合控制(Blend Control)

通过启用“深度”(Depth)和“偏移”(Bias)，调整圆角形状曲率。请注意，如果为圆形圆角启用“融合控制”(Blend Control)，则圆角将不会是圆形。

#### 深度(Depth)

“深度”(Depth)的值越高，圆角曲线在相交角处放置的位置就越深。

![图：“深度”(Depth)的值越高，圆角曲线在相交角处放置的位置就越深。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-3322E790-E0BA-40C9-87AA-AC8DA5A5370C.png) <!-- baize:img-hook downloaded=false reason="正文 857 字 ≥300，非承重" -->

#### 偏移(Bias)

控制圆角曲线是否在一条曲线或另一条曲线的方向上进行包裹。值 1 会将圆角曲线朝向一条曲线的方向进行包裹；值 -1 会朝向另一条曲线。值 0 会将圆角曲线放置于两条曲线的正中间。（可以在“属性编辑器”(Attribute Editor)而并非选项窗口中使用小于 0 的值。）

![图：控制圆角曲线是否在一条曲线或另一条曲线的方向上进行包裹。值 1 会将圆角曲线朝向一条曲线的方向进行包裹；值 -1 会朝向…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-CB288765-F98E-438A-8D5A-98AB993101D6.png) <!-- baize:img-hook downloaded=false reason="正文 857 字 ≥300，非承重" -->

#### 输入曲线(Input Curve)

可访问用于创建圆角的曲线的历史。如果需要编辑曲线，请单击箭头按钮以选择其中一个曲线。

#### 曲线参数(Curve Parameters)

“Parameter1”和“Parameter2”将定义创建圆角曲线的两条曲线之间的区域。
