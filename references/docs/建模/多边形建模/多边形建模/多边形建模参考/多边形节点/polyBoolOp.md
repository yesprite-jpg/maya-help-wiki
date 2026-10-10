# polyBoolOp

当使用传统布尔算法执行布尔运算时，会创建一个“polyBoolOp”节点。

可以使用以下属性编辑布尔运算。

**注**

提示：

若要使用旧版布尔算法，请选择

“网格 > 布尔 > 并集/差集/交集”(Mesh > Booleans > Union/Difference/Intersection)

>

，然后启用

“使用旧版布尔算法”(Use legacy Boolean algorithm)

。

#### 运算(Operation)

可用于在执行布尔运算之后切换到其他类型的运算：

#### 并集(Union)

合并选定网格的体积。

#### 差集(Difference)

从第一个选定网格中减去第二个选定网格的体积。

#### 交集(Intersection)

仅保留选定网格的共享体积。

#### “使用阈值”(Use Thresholds)

启用时，布尔运算会使用指定的“顶点距离阈值”(Vertex Distance Threshold)和“面区域阈值”(Face Area Threshold)值自动检查并消除极小的面和边。

#### 顶点距离阈值(Vertex Distance Threshold)

检查零长度（或非常短）的边。比指定的值更近的任何顶点将自动合并为一个顶点。

**注**

较大的

“顶点距离阈值”(Vertex Distance Threshold)

值可能会导致网格的某些部分消失或是从原始几何体中提取出来。若要解决此问题，请禁用

“使用阈值”(Use Thresholds)

或降低

“顶点距离阈值”(Vertex Distance Threshold)

值。

#### 面区域阈值(Face Area Threshold)

检查面积为零（或非常小）的面。面积小于指定值的任何面将自动收拢为一个顶点。

**注**

较大的

“面区域阈值”(Face Area Distance Threshold)

值可能会导致网格的某些部分消失或是从原始几何体中提取出来。若要解决此问题，请禁用

“使用阈值”(Use Thresholds)

或降低

“面区域阈值”(Face Area Threshold)

值。

#### 保留颜色(Preserve Color)

启用后，将在网格上保留逐顶点颜色数据。请参见[为多边形顶点指定颜色](../../多边形上色/为多边形顶点指定颜色.md)。

**注**

此选项仅当您使用的是旧版布尔算法时才可用。

## 相关主题

- [布尔](../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔.md)

- [使用布尔运算组合多边形网格](../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/布尔/使用布尔运算组合多边形网格.md)
