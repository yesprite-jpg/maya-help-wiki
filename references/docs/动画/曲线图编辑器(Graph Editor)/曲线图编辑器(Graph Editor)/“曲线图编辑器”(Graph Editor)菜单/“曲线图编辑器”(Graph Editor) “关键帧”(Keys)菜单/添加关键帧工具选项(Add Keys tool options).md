# 添加关键帧工具选项(Add Keys tool options)

- 在[“曲线图编辑器”(Graph Editor)“关键帧”(Keys)菜单](../“曲线图编辑器”%28Graph%20Editor%29%20“关键帧”%28Keys%29菜单.md)中，选择“添加关键帧”(Add Keys) > ![图：在“曲线图编辑器”(Graph Editor)“关键帧”(Keys)菜单中，选择“添加关键帧”(Add Keys)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 542 字 ≥300，非承重" -->

#### 添加受控关键点(Add Breakdowns)

受控关键点是一种与相邻关键帧保持成比例时间关系的特殊关键帧。

![图：受控关键点是一种与相邻关键帧保持成比例时间关系的特殊关键帧。 在第一个示例中，插入一个普通关键帧，并移动相邻关键帧。在第…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-8E223BA4-CD16-4BEC-840E-34610AB80C9C.gif) <!-- baize:img-hook downloaded=false reason="正文 542 字 ≥300，非承重" -->

![图：受控关键点是一种与相邻关键帧保持成比例时间关系的特殊关键帧。 在第一个示例中，插入一个普通关键帧，并移动相邻关键帧。在第…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-A035B237-C6BF-4EFB-8B50-5BA825B23707.gif) <!-- baize:img-hook downloaded=false reason="正文 542 字 ≥300，非承重" -->

在第一个示例中，插入一个普通关键帧，并移动相邻关键帧。在第二个示例中，插入一个受控关键点关键帧，并移动相邻关键帧，这次，插入的关键帧会调整以适应曲线形状的变化。请注意，受控关键点关键帧为纯绿色。

#### 保留切线类型(Preserve Tangent Type)

![图：处于活动状态（默认）时，此设置可确保添加的关键帧影响曲线的形状，但不会更改相邻切线类型。 如果不希望新关键帧影响曲线的形…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 542 字 ≥300，非承重" -->

处于活动状态（默认）时，此设置可确保添加的关键帧影响曲线的形状，但不会更改相邻切线类型。

如果不希望新关键帧影响曲线的形状，请禁用此选项。

![图：处于活动状态（默认）时，此设置可确保添加的关键帧影响曲线的形状，但不会更改相邻切线类型。 如果不希望新关键帧影响曲线的形…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-C4F1E53E-46BD-46F2-B93B-EAAD63723480.gif) <!-- baize:img-hook downloaded=false reason="正文 542 字 ≥300，非承重" -->

![图：处于活动状态（默认）时，此设置可确保添加的关键帧影响曲线的形状，但不会更改相邻切线类型。 如果不希望新关键帧影响曲线的形…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-8F6B9B16-7074-4605-8DAC-036DD69BCA89.gif) <!-- baize:img-hook downloaded=false reason="正文 542 字 ≥300，非承重" -->

在第一个示例中，“保留切线类型”(Preserve Tangent Type)设置为**“启用”(On)**（默认），关键帧添加到曲线，同时稍微更改其形状，而相邻切线不更改。在第二个示例中，“保留切线类型”(Preserve Tangent Type)设置为**“禁用”(Off)**，关键帧添加到曲线，但曲线形状不更改。

**注**

默认情况下，在

“添加关键帧工具”(Add Keys Tool)

选项中，此设置处于活动状态，但使用

插入关键帧工具选项(Insert Keys Tool options)

时，同一选项处于禁用状态。
