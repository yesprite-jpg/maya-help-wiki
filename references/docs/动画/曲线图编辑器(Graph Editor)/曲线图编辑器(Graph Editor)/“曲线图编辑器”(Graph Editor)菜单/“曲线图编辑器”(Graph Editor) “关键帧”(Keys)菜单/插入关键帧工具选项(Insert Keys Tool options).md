# 插入关键帧工具选项(Insert Keys Tool options)

- 在[“曲线图编辑器”(Graph Editor)“关键帧”(Keys)菜单](../“曲线图编辑器”%28Graph%20Editor%29%20“关键帧”%28Keys%29菜单.md)中，选择“插入关键帧”(Insert Keys) > ![图：在“曲线图编辑器”(Graph Editor)“关键帧”(Keys)菜单中，选择“插入关键帧”(Insert Keys)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 773 字 ≥300，非承重" -->

#### 插入受控关键点(Insert Breakdowns)

受控关键点是一种与相邻关键帧保持成比例时间关系的特殊关键帧。

![图：受控关键点是一种与相邻关键帧保持成比例时间关系的特殊关键帧。 在第一个示例中，插入一个普通关键帧，并移动相邻关键帧。在第…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-8E223BA4-CD16-4BEC-840E-34610AB80C9C.gif) <!-- baize:img-hook downloaded=false reason="正文 773 字 ≥300，非承重" -->

![图：受控关键点是一种与相邻关键帧保持成比例时间关系的特殊关键帧。 在第一个示例中，插入一个普通关键帧，并移动相邻关键帧。在第…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-A035B237-C6BF-4EFB-8B50-5BA825B23707.gif) <!-- baize:img-hook downloaded=false reason="正文 773 字 ≥300，非承重" -->

在第一个示例中，插入一个普通关键帧，并移动相邻关键帧。在第二个示例中，插入一个受控关键点关键帧，并移动相邻关键帧，这次，插入的关键帧会调整以适应曲线形状的变化。请注意，受控关键点关键帧为纯绿色。

#### 保留切线类型(Preserve Tangent type)

**注**

对于

“插入关键帧工具选项”(Insert Keys Tool options)

，此设置默认处于禁用状态，但在

“添加关键帧工具选项”(Add Keys Tool options)

中，此设置默认处于活动状态。

激活此设置，以便插入的关键帧可识别已存在的任何入切线和出切线，插入关键帧会更改曲线的形状以适应新关键帧任意一侧的切线类型。

![图：注： 对于“插入关键帧工具选项”(Insert Keys Tool options)，此设置默认处于禁用状态，但在“添加…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-D4E66982-6696-4C37-986B-711DC33181FC.gif) <!-- baize:img-hook downloaded=false reason="正文 773 字 ≥300，非承重" -->

“保留切线类型”(Preserve Tangent Type)遵循插入的关键帧任意一侧的关键帧切线类型。

默认情况下，使用“插入关键帧工具”(Insert Keys tool)（热键：**Alt** + **i**）时，将使用固定切线创建新关键帧，也会固定相邻关键帧以遵循曲线的形状。“保留切线类型”(Preserve Tangent type)选项会覆盖此内容，且新关键帧的切线类型会遵循当前入切线和出切线并影响曲线的形状。

例如，使用此设置时，如果插入一个关键帧且其切线类型为“自动”(Auto)，则任意一侧的关键帧切线都不会改变。这会使插入关键帧行为与设置关键帧相同（热键：**s**）。

**注**

“添加关键帧工具”(Add Keys Tool)

菜单中有

“保留切线类型”(Preserve Tangent Type)

选项，但此选项默认处于启用状态，其作用与此设置相反，即，添加的关键帧不会更改曲线的形状。
