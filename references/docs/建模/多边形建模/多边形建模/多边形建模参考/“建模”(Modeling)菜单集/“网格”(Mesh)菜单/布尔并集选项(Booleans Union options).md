# 布尔并集选项(Booleans Union options)

使用这些选项可设置在选择“网格 > 布尔 > 并集”(Mesh > Booleans > Union)时发生的情况。

#### 使用旧版布尔算法(Use legacy Boolean algorithm)

启用后，将使用旧版布尔算法执行选定的布尔操作。

**注**

包含以 Maya 2014 或更早版本创建的布尔节点的场景会自动使用 Maya 的旧版布尔算法。

#### 保留颜色(Preserve Color)

启用后，将在网格上保留逐顶点颜色数据。请参见[为多边形顶点指定颜色](../../../多边形上色/为多边形顶点指定颜色.md)。

#### 交集类别(Intersection Classification)

系统会对交集执行布尔操作。使用开放网格（平面或有洞的网格）时，Maya 可以使用两种方式计算选定网格的交集：

#### 边(Edge)

“边”(Edge)类别会将开放网格视为闭合体积。

![图：“边”(Edge)类别会将开放网格视为闭合体积。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-D91FEC52-715E-4984-8D7C-94A9BBF5372E.png) <!-- baize:img-hook downloaded=false reason="正文 380 字 ≥300，非承重" -->

#### 法线(Normal)

“法线”(Normal)类别将开放网格视为开放体积。

![图：“法线”(Normal)类别将开放网格视为开放体积。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-87075F9A-5FBE-40C9-A63D-76D0C70FFBFA.png) <!-- baize:img-hook downloaded=false reason="正文 380 字 ≥300，非承重" -->

## 相关主题

- [布尔](../../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔.md)

- [关于布尔](../../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔/关于布尔.md)

- [使用布尔运算组合多边形网格](../../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔/使用布尔运算组合多边形网格.md)
