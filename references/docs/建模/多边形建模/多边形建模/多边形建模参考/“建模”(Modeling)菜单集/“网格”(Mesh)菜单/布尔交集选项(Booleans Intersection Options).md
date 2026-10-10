# 布尔交集选项(Booleans Intersection Options)

使用这些选项可设置在选择“网格 > 布尔 > 交集”(Mesh > Booleans > Intersection)时发生的情况。

#### 交集类别(Intersection Classification)

系统会对交集执行布尔操作。使用开放网格（平面或有洞的网格）时，Maya 可以使用两种方式计算选定网格的交集：

#### 边(Edge)

“边”(Edge)类别会将开放网格视为闭合体积。

![图：“边”(Edge)类别会将开放网格视为闭合体积。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-5DE254D3-B498-468D-B9DF-7ADF7E31AB6B.png) <!-- baize:img-hook downloaded=false reason="正文 380 字 ≥300，非承重" -->

#### Normal

“法线”(Normal)类别将开放网格视为开放体积。

![图：“法线”(Normal)类别将开放网格视为开放体积。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-3B9CD034-3EEF-4978-82A3-8AF9295D9ECB.png) <!-- baize:img-hook downloaded=false reason="正文 380 字 ≥300，非承重" -->

#### 保留颜色(Preserve Color)

启用时，将在网格上保留逐顶点颜色数据。请参见[为多边形顶点指定颜色](../../../多边形上色/为多边形顶点指定颜色.md)。

#### 使用旧版布尔算法(Use legacy Boolean algorithm)

启用时，将使用旧版布尔算法执行布尔运算。

**注**

包含以 Maya 2014 或更早版本创建的布尔节点的场景会自动使用 Maya 的旧版布尔算法。

## 相关主题

- [布尔](../../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔.md)

- [关于布尔](../../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔/关于布尔.md)

- [使用布尔运算组合多边形网格](../../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔/使用布尔运算组合多边形网格.md)
