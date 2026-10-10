# 方形选项(Square Options)

使用以下选项可设置在选择“曲面 > 方形”(Surfaces > Square)时发生的情况。

**注**

为了创建方形曲面，必须满足下列条件：

- 四条边界曲线必须相交。通过将曲线端点捕捉到一条公共栅格线，或者通过将一条曲线的端点磁体捕捉到另一条曲线的端点，可以确保曲线相交。

- 必须按顺时针方向或逆时针方向选择曲线。

#### 连续性类型(Continuity Type)

设置所创建的曲面相切的类型。

“固定的边界”(Fixed Boundary)不保证曲面曲线处的连续性。

“切线”(Tangent)从选定曲面曲线构建平滑的连续曲面。启用“切线”(Tangent)时，“曲线适配检查点”(Curve Fit Checkpoints)选项将变得可用。它指定构建“方形”(Square)曲面的精确程度。

“暗含的切线”(Implied Tangent)基于选定曲线所在的平面的法线创建曲面相切。

#### 曲线适配检查点(Curve Fit Checkpoints)

设置为了实现整个曲面曲线的连续性需要使用的等参线的数量。较大的值可能会创建精度更高的连续性，但曲面可能会变得不太有用。当曲面曲线相交成锐角时，这特别有可能。

#### 结束点容差(End Point Tolerance)

“全局”(Global)容差意味着会使用“首选项”(Preferences)窗口中设置的“位置”(Positional)值。位置容差设置端点为了被视为重合而需要靠近的程度。

使用“局部”(Local)容差可以输入新值以覆盖在“首选项”中设置的“位置”(Positional)容差值。

#### 重建(Rebuild)

“重建”(Rebuild)提供了一个用于重建曲面曲线的选项，这些曲面曲线用于生成“方形”(Square)曲面。在某些情况下，这可以改进曲线参数化。

#### 输出几何体(Output Geometry)

指定创建的几何体类型。（“Subdiv”表示“细分曲面”(Subdiv)。）

## 相关主题

- [创建具有连续性的四边曲面（方形）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-C004657D-B2DD-40A8-B376-1288D18F3747.htm)
