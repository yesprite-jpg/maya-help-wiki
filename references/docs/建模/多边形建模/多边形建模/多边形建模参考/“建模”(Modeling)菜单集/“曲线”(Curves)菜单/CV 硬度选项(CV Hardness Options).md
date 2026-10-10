# CV 硬度选项(CV Hardness Options)

使用以下选项可设置在选择“曲线 > CV 硬度”(Curves > CV Hardness)时发生的情况。

#### 多重性(Multiplicity)

默认情况下，创建立方体曲线时，末端结具有多重性因子 3 并且之间的弧具有多重性因子 1。

“完全”(Full)将内部 CV 的多重性从 1 更改到 3。若要将多重性因子从 1 更改到 3，被修改的具有多重性因子 1 的 CV 每一侧上必须至少包含两个 CV。

“禁用”(Off)将内部 CV 的多重性从 3 更改到 1。

![图：默认情况下，创建立方体曲线时，末端结具有多重性因子 3 并且之间的弧具有多重性因子 1。 “完全”(Full)将内部 C…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-180F7FEB-B9F5-4BDC-93A5-4D7FD5E2866D.png) <!-- baize:img-hook downloaded=false reason="正文 500 字 ≥300，非承重" -->

#### 保持原始(Keep Original)

更改多重性设置之后保持原始曲线。

## hardenPoint 节点

调整 CV 硬度时，如果启用“保持原始”(Keep Original)，则可以使用“属性编辑器”(Attribute Editor)在这之后随时编辑 CV 硬度。另请参见 [hardenPoint](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/hardenPointCurve.html)。

#### 输入曲线(Input Curve)

“输入曲线”(Input Curve)信息是只读信息。可以访问已更改曲线的历史。单击箭头按钮以选择曲线，并在编辑器中打开该曲线区域。

#### 多重性(Multiplicity)

在“多重性”(Multiplicity)框中输入一个值，或使用滑块指定在调整 CV 时需要插入的结数。

## 相关主题

- [控制多点结和 CV 硬度](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-3CDB7E68-05B8-4546-965A-93D6F16B723D.htm)
