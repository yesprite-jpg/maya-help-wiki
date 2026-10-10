# 平面选项(Planar Options)

使用以下选项可设置在选择“曲面 > 平面”(Surfaces > Planar)时发生的情况。

#### 次数(Degree)

如果输出为 NURBS 曲面，请选择“线性”(Linear)（1 次）或“立方”(Cubic)（3 次）作为“次数”(Degree)。“立方”(Cubic)是默认设置。

#### 曲线范围(Curve Range)

“完成”(Complete)可沿整个曲线创建平面曲面。

使用“部分”(Partial)，您可以在平面曲面中使用“显示操纵器工具”(Show Manipulator Tool)显示操纵器，并沿输入曲线部分编辑结果平面曲面。单击输入曲线或“通道盒”(Channel Box)中的等参线的标题，可显示该选项。

![图：“完成”(Complete)可沿整个曲线创建平面曲面。 使用“部分”(Partial)，您可以在平面曲面中使用“显示操纵…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-FD2BD4BF-2FF0-4902-9241-7B3E1E0F6D5A.png) <!-- baize:img-hook downloaded=false reason="正文 541 字 ≥300，非承重" -->

#### 输出几何体(Output Geometry)

指定创建的几何体的类型。

**注**

尽管可以通过操纵平面曲面的边界来更改曲面的形状，但该曲面必须始终保持为平面。

尽管平面曲面可包括裁切区域或洞，但定义洞的曲线必须与主曲面共面。

### 从开放曲线中创建已修剪的曲面。

您不必使用单个边界曲线也可创建已修剪的曲面，但必须使用封闭区域。该区域可通过将多条曲线相交来创建。可以使用带有重叠边界的曲线来创建已修剪的曲面。选择曲线并使用曲面 > 平面(Surfaces > Planar)，即可创建已修剪的曲面。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-0D10CDA2-142A-4191-865A-0CF1F069E996.png) <!-- baize:img-hook downloaded=false reason="正文 541 字 ≥300，非承重" -->

## 相关主题

- [在曲线内创建平面](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-4C960C4A-C636-45ED-9E63-874E5AEDD074.htm)
