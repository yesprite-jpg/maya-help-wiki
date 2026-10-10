# “NURBS 到多边形”(NURBS to Polygons)选项

使用以下选项可设置在选择“修改 > 转化 > NURBS 到多边形”(Modify > Convert > NURBS to Polygons)时发生的情况。另请参见[将 NURBS 曲面转化为多边形网格](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-CE7DD4E2-0D14-4980-ADDA-2216735FF63B)。

## 附加多个输出网格(Attaching multiple output meshes)

#### 附加多个输出网格(Attach Multiple Output Meshes)

生成单个网格，即使原始 NURBS 对象由不同的曲面组成。

例如，如果在“附加多个输出网格”(Attach Multiple Output Meshes)启用的情况下将 NURBS 立方体（由六个单独面组成）转化，生成的多边形立方体只有一个网格。如果“附加多个输出网格”(Attach Multiple Output Meshes)处于禁用状态，多边形立方体将由六个单独的网格组成。

#### 合并容差(Merge Tolerance)

决定为了合并成单个网格闭合顶点必须满足什么样的条件（当“附加多个输出网格”(Attach Multiple Output Meshes)处于启用状态）。

#### 匹配渲染细分(Match Render Tessellation)

当“匹配渲染细分”(Match Render Tessellation)处于启用状态，在将其转化为多边形网格时使用为 NURBS 曲面设置的现有渲染细分值。因此，转化的多边形网格将匹配渲染版本的 NURBS 曲面。当“历史”(History)处于启用状态时，只要 NURBS 渲染细分值修改，“NURBS 到多边形”转化就会更新。

## 输出到三角形或四边形

#### 类型(Type)

选择将 NURBS 几何体转化为多边形数据时使用的多边形类型。

如果选择“三角形”(Triangle)（默认），将创建由三条边构成的多边形。如果选择“四边形”(Quads)，将创建由四条边构成的多边形。

![图：选择将 NURBS 几何体转化为多边形数据时使用的多边形类型。 如果选择“三角形”(Triangle)（默认），将创建由…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-41A85C65-0FB8-4E6F-9E3E-AA8AE91BED1D.png) <!-- baize:img-hook downloaded=false reason="正文 2717 字 ≥300，非承重" -->

**注**

当细分修剪的 NURBS 曲面时，即使选项设置为四边形，沿着修剪边可也能会创建某些三边多边形（三角形）。

## 选择细分方法

细分意味着可以从 NURBS 几何体创建一组多边形。每个细分方法提供选项来控制生成的多边形曲面。

有四种细分方法：“标准适配”(Standard fit)、“常规”(General)、“计数”(Count)和“控制点”(Control Points)。

### 标准适配(Standard fit)

“标准适配”(Standard Fit)是默认的细分方法。它是“自适应”的细分，也就是说以下选项用于确定何时停止细分。

例如，细分停止于您设置的“分数容差”(Fractional Tolerance)值。如果有一条边比“最小边长”(Minimal Edge Length)短，细分在该边停止。如果在边内曲面足够平坦（指定弦/高比足够小），细分在此处停止。

#### 弦高比(Chord Height Ratio)

“弦高比”(Chord Height Ratio)是曲线到用于近似它的多边形边的最大距离和弦长之间的比率。弦长是两个多边形的顶点之间的线性距离。

![图：“弦高比”(Chord Height Ratio)是曲线到用于近似它的多边形边的最大距离和弦长之间的比率。弦长是两个多边…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-9C77967B-88A5-4A95-882D-C8C4B1DFBABB.png) <!-- baize:img-hook downloaded=false reason="正文 2717 字 ≥300，非承重" -->

有效值范围介于 0 和 1 之间，其中较大的数值会产生较少的多边形顶点。

例如，默认值为 0.1，意味着在创建其他编辑点之前高度必须大于弦长的 1/10。

#### 分数容差(Fractional Tolerance)

“分数容差”(Fractional Tolerance)值确定原始曲面和插值多边形曲面之间保持的精确度。默认设置为精确到 0.01 单位以内，其中单位是指当前的线性测量单位（默认的测量单位为厘米）。因此，在任何点多边形曲面离原始 NURBS 曲面的距离都不会超过容差距离。

在下一示例中，请注意当把“分数容差”(Fractional Tolerance)值从 1 更改为 0.01时，可以怎样增强多边形曲面的精确度。

![图：“分数容差”(Fractional Tolerance)值确定原始曲面和插值多边形曲面之间保持的精确度。默认设置为精确到…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-95D05AF8-05E6-4EEC-B8C1-7F75CBF7946D.png) <!-- baize:img-hook downloaded=false reason="正文 2717 字 ≥300，非承重" -->

#### 最小边长(Minimal Edge Length)

输入一个值或使用“最小边长”(Minimal Edge Length)滑块来设置创建的三角形或四边形的边的最小长度。

#### 3D 增量(3D Delta)

“3D 增量”(3D Delta)值确定在曲面上组成细分的初始栅格的 U 和 V 等参线的 3D 间距。在以下示例中，“3D 增量”(3D Delta)值从默认值 0.1 更改到 1.0。

![图：“3D 增量”(3D Delta)值确定在曲面上组成细分的初始栅格的 U 和 V 等参线的 3D 间距。在以下示例中，“…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-5CB28147-8B36-405B-B295-C34F934238F5.png) <!-- baize:img-hook downloaded=false reason="正文 2717 字 ≥300，非承重" -->

### 常规(General)

为“常规”(General)设置“细分方法”(Tessellation Method)以显示下列选项。

### 设置初始细分控制

除非“使用弦高”(Use Chord Height)或“使用弦高比”(Use Chord Height Ratio)处于启用状态，否则将执行统一细分操作。每个跨度/曲面拆分为多个多边形的数量取决于设置的“U 向数量”(Number U)和“V 向数量”(Number V)值。

#### U 类型(U Type) / V 类型(U Type)

“U 类型”(U Type)和“V 类型”(V Type)弹出菜单项可以指定是根据跨度所在处（然后拆分每个跨度）拆分曲面，还是基于整个曲面参数化拆分曲面。

![图：“U 类型”(U Type)和“V 类型”(V Type)弹出菜单项可以指定是根据跨度所在处（然后拆分每个跨度）拆分曲面…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-3ADCE7CF-0443-47B1-AD3E-18414A4C59A1.png) <!-- baize:img-hook downloaded=false reason="正文 2717 字 ≥300，非承重" -->

#### U 向数量(Number U) / V 向数量(Number V)

每个跨度或曲面分割为此处指定数量的多边形。

![图：每个跨度或曲面分割为此处指定数量的多边形。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-1603FF78-5B46-4941-B4FE-42B10730CD13.png) <!-- baize:img-hook downloaded=false reason="正文 2717 字 ≥300，非承重" -->

### 指定二级细分控制

如果“使用弦高”(Use Chord Height)或“使用弦高比”(Use Chord Height Ratio)处于启动状态，可以为“弦高”(Chord Height)和“弦高比”(Chord Height Ratio)设置特定的值。如果曲线上的比值大于当前值，大于 0 的值将产生较少的多边形顶点。例如，默认值为 0.1，意味着在创建其他编辑点之前高度必须大于弦长的 1/10。

启用“边交换”(Edge Swap)可以生成和最终的四边形具有相反方向的三角形。

### 计数(Count)

为“计数”(Count)设置“细分方法”(Tessellation Method)以显示下列滑块。

#### “计数”(Count)滑块

使用“计数”(Count)滑块可确定曲面细分成多少多边形。请看以下示例。

![图：使用“计数”(Count)滑块可确定曲面细分成多少多边形。请看以下示例。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-B3D22C3E-718C-4A8B-8A08-54D26ED21A7D.png) <!-- baize:img-hook downloaded=false reason="正文 2717 字 ≥300，非承重" -->

### 控制点(Control Points)

这种细分方法将 NURBS 模型转化成多边形，同时匹配原始 NURBS 曲面的 CV。此操作没有其他选项。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-F0EFD0CF-9BEA-4363-A637-F6B0A3CFA66A.png) <!-- baize:img-hook downloaded=false reason="正文 2717 字 ≥300，非承重" -->

## 注释

当使用“控制点”(Control Points)细分方法(Tessellation Method)”时：

- 设置的“类型”选项被忽略，并且生成的多边形默认为四边形。

- 如果将修剪的 NURBS 曲面转化，曲面将被当做未修剪曲面转化。

当使用“附加多个输出网格”(Attach Multiple Output Meshes)选项，则此操作可能由于多种原因无法附加曲面：

- 如果附着大量曲面，并且某些曲面非常小，容差必须设置为合适小的值，否则附着操作将失败。

- 如果附着多个曲面，所有曲面必须在用户定义的容差范围内连续。分隔区域不能在单个操作中完成附着。在此情况需要多次使用附着操作；每个连续的区域一次。

- 要附着的曲面的法线必须朝向相同的方向，否则附着将失败。
