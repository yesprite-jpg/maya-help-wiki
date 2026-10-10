# Paint Effects 到多边形(Paint Effects to Polygons)、Paint Effects 到 NURBS (Paint Effects to NURBS)和 Paint Effects 到曲线(Paint Effects to Curves)选项

使用以下选项可设置在选择“修改 > 转化 > Paint Effects 到多边形”(Modify > Convert > Paint Effects to Polygons)、“Paint Effects 到 NURBS”(Paint Effects to NURBS)或“Paint Effects 到曲线”(Paint Effects to Curves)时发生的情况。另请参见[将 Paint Effects 转化为几何体](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EFD71EDB-35BA-49B5-B742-6CF36A9B1B5C)。

## “Paint Effects 到多边形”(Paint Effects to Polygons)选项

#### 顶点颜色模式(Vertex Color Mode)

默认值为“无”(None)。其他选项包括“颜色”(Color)和“照明”(Illuminated)。

#### 四边形输出(Quad Output)

启用该选项可输出为四边形。默认设置为禁用，默认输出为三角形。

#### 隐藏笔划(Hide Strokes)

启用该选项可在将“Paint Effects”笔划转化为多边形后隐藏这些笔划。即使隐藏了笔划，仍可以更新其属性，并且此操作将影响多边形网格。默认设置为启用。

#### 多边形限制(Poly Limit)

该值指示将“Paint Effects”笔划转化为多边形时，它应该在达到大约此数量的面后停止。这可以用于避免创建过大的网格，过大的网格可能会导致内存不足。默认值为 100,000。值为 0 指示没有任何限制。

## “Paint Effects 到 NURBS”(Paint Effects to NURBS)选项

#### 隐藏笔划(Hide Strokes)

启用此选项后，可以在“Paint Effects”笔划转化为“NURBS”后隐藏这些笔划。即使笔划处于隐藏状态，其属性仍然可以得到更新，并且将影响“NURBS”几何体。默认设置为启用。

## “Paint Effects 到曲线”(Paint Effects to Curves)选项

#### 隐藏笔划(Hide Strokes)

启用此选项，以在“Paint Effects”笔划转化为曲线后立即隐藏它们。即使笔划被隐藏，仍然可以更新其属性并将影响曲线。
