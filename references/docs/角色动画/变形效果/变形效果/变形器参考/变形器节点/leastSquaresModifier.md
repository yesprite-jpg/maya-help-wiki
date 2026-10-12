# leastSquaresModifier

## 最小平方修改器属性(Least Squares Modifier Attributes)

#### 输入 NURBS 对象(Input NURBS Object)

显示受最小平方修改器节点影响的“NURBS 曲线”(NURBS curve)（例如，curveShape*N*Original）。

## 点约束(Point Constraints)

#### pointConstraint[n]

标识曲线上的点定位器约束。值 n 与默认定位器名称减 1 相对应。例如，pointConstraint[0] 与 locator1 相对应。

#### U

在“NURBS 曲线”(NURBS curve)上，根据“U”参数指定曲线上的点定位器约束的位置。

#### 权重(Weight)

指定曲线上的点定位器约束对与其他曲线上的点定位器约束相关的曲线形状所产生影响的大小。使用滑块从 0.100 到 1.000 之间选择值。默认值为 1.000。“权重”(Weight)属性最初由“点权重”(Point Weight)曲线上的点选项指定。
