# 晶格工具(Lattice Tool)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-0F6AC744-B248-4B47-90EE-AF500B5CC607.gif) <!-- baize:img-hook downloaded=false reason="正文 713 字 ≥300，非承重" -->

通过允许出于变形目的围绕 UV 创建晶格，将 UV 的布局作为组进行操纵。

若要打开“晶格工具”(Lattice Tool)，请从“UV 工具包”(UV Toolkit)的“变换 > 工具”(Transform > Tools)部分中选择它，或从“UV 编辑器”(UV Editor)菜单中选择“工具 > 晶格”(Tools > Lattice)。

选择“工具 > 晶格”(Tools > Lattice) > ![图：选择“工具 晶格”(Tools Lattice) 时，在“工具设置”(Tool Settings)窗口中将显示以下选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 713 字 ≥300，非承重" -->时，在“工具设置”(Tool Settings)窗口中将显示以下选项。

## 晶格设置(Lattice Settings)

#### 列(Columns)

为当前晶格操纵器指定列数。最小列数为 2，最大列数为 8。

#### 行数(Rows)

为当前晶格操纵器指定行数。最小行数为 2，最大行数为 8。

#### 衰减(Falloff)

指定晶格操纵器的影响级别或衰减值。

#### 使用边界矩形(Use Bounding Rectangle)

如果启用该选项，那么当前晶格操纵器就无法延伸过外部边或目标几何体的边界。

![图：如果启用该选项，那么当前晶格操纵器就无法延伸过外部边或目标几何体的边界。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-EDDEC373-F5C1-4451-B43F-D9321FE2DB11.png) <!-- baize:img-hook downloaded=false reason="正文 713 字 ≥300，非承重" -->

#### 显示移动操纵器(Show move manipulator)

指定选择晶格点时是否显示[“移动”(Move)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9BCE8B23-6DA6-4C7F-B897-7E25D6E8A865)工具操纵器。

## 捕捉设置

晶格捕捉设置与受晶格影响的每个 UV 相关。需要在“UV 编辑器”(UV Editor)中启用“像素捕捉”(Pixel Snap)（“图像 > 像素捕捉”(Image > Pixel Snap)），“UV 晶格工具捕捉设置”(UV Lattice Tool Snap Settings)才会有效果。

#### 放置(Placement)

选择控制点捕捉到的位置。

#### 捕捉角(Snap Corner)

如果启用该选项，UV 晶格变形器的控制点就会捕捉到每个 UV 的角。

#### 捕捉中心(Snap Center)

如果启用该选项，UV 晶格变形器的控制点就会捕捉到每个 UV 的中心。
