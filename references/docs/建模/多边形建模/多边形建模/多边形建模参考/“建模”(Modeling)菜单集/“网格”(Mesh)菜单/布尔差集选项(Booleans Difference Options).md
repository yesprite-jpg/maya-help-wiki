# 布尔差集选项(Booleans Difference Options)

使用这些选项可设置在选择“网格 > 布尔 > 差集”(Mesh > Booleans > Difference)时发生的情况。

**注**

可以通过一次

“差集”(Difference)

运算从第一个选定网格中提取多个网格。

#### 使用旧版布尔算法(Use legacy Boolean algorithm)

启用后，将使用旧版布尔算法执行选定的布尔操作。

**注**

包含以 Maya 2014 或更早版本创建的布尔节点的场景会自动使用 Maya 的旧版布尔算法。

#### 保留颜色(Preserve Color)

启用后，将在网格上保留逐顶点颜色数据。请参见[为多边形顶点指定颜色](../../../多边形上色/为多边形顶点指定颜色.md)。

#### 交集类别(Intersection Classification)

系统会对交集执行布尔操作。使用开放网格（平面或有洞的网格）时，Maya 可以使用两种方式计算选定网格的交集：

#### 边(Edge)

“边”(Edge)类别会将开放网格视为闭合体积。例如，当“边”(Edge)处于选中状态时，您可以使用“差集”(Difference)操作，在平面中创建凹陷或洼地。

![图：“边”(Edge)类别会将开放网格视为闭合体积。例如，当“边”(Edge)处于选中状态时，您可以使用“差集”(Diffe…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E34CBB03-0ED8-4535-9216-0877B483DE14.png) <!-- baize:img-hook downloaded=false reason="正文 484 字 ≥300，非承重" -->

#### 法线(Normal)

“法线”(Normal)类别将开放网格视为开放体积。

![图：“法线”(Normal)类别将开放网格视为开放体积。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D1E7B87C-CEEA-4535-B551-E8294FFD6DEA.png) <!-- baize:img-hook downloaded=false reason="正文 484 字 ≥300，非承重" -->

## 相关主题

- [布尔](../../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔.md)

- [关于布尔](../../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔/关于布尔.md)

- [使用布尔运算组合多边形网格](../../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔/使用布尔运算组合多边形网格.md)
