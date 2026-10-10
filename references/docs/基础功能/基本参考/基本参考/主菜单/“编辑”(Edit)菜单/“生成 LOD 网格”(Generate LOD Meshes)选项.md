# “生成 LOD 网格”(Generate LOD Meshes)选项

选择“编辑 > LOD (细节级别) > 生成 LOD 网格”(Edit > LOD (Level of Detail) > Generate LOD Meshes) > ![图：选择“编辑 LOD (细节级别) 生成 LOD 网格”(Edit LOD (Level of Detail) Gener…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2331 字 ≥300，非承重" --> 以打开并设置以下选项。另请参见[生成 LOD 网格](../../../../查看场景/查看场景/LOD（细节级别）/生成%20LOD%20网格.md)。

#### 复制蒙皮权重(Copy Skin Weights)

启用时（默认），一个或多个选定网格中的任何蒙皮权重会传递到新生成的 LOD 网格。如果您不希望传递蒙皮权重，请将其禁用。

## 减少方法(Reduction Method)

#### 减少方法(Reduction Method)

可以通过特定值来减少多边形的数量。从下列选项中进行选择：

**注**

“减少”(Reduce)

功能会尝试达到在

“顶点限制”(Vertex limit)

或

“三角形限制”(Triangle limit)

字段中输入的指定数量；但是，如果已启用

“保留四边形”(Preserve quads)

或其他

“功能保留”(Feature Preservation)

选项，减少的网格中的顶点数量或三角形数量可能会与指定的计数不同。

##### 百分比(Percentage)

可以通过使用“百分比”(Percentage)滑块设置原始多边形计数的百分比来减少多边形的数量。

##### 顶点限制(Vertex limit)

可以使用“顶点限制”(Vetex limit)字段来设置输出网格中的顶点数量。

##### 三角形限制(Triangle limit)

可以使用“三角形限制”(Triangle limit)字段来设置输出网格中的三角形数量。

## LOD 级别

#### LOD 级别的数量

选择要生成的网格（级别）的数量（最多九个）。

对于每个级别，将显示复选框和“百分比”(Percentage)、“顶点限制”(Vertex limit)或“三角形限制”(Triangle limit)滑块。（滑块将更新以匹配指定的“减少”(Reduction)方法。）

使用复选框来启用和禁用在该级别上创建网格。

滑块可用于控制为级别减少生成的每个网格的程度。根据“减少”(Reduction)方法，滑块可以控制生成网格时删除的顶点百分比（“百分比”(Percentage)），也可以指定要保留的顶点数或三角形数（“顶点限制”(Vertex limit)或“三角形限制”(Triangle limit)）。

## 形状

#### 保留四边形(Preserve quads)

在网格减少时尝试在网格上保持任何现有的四边形拓扑。滑块范围在 0 到 1 之间。该值越大，最终结果中的四边形就越多。值为 0 相当于禁用此选项。如果减少导致了不需要的形状变更，请减小滑块值。

#### 锐度(Sharpness)

控制保留小巧明细的细节与更大形状之间的平衡。值很小时，相对于对象的常规形状的小巧细节更有可能被收拢。值很大时，它们更可能得到保留。

#### 对称类型(Symmetry type)

可以从以下选项中选择：

**注**

“保留四边形”(Preserve quads)

必须设置为小于 1.0 的值才能使用

“对称类型”(Symmetry type)

选项。

##### 无(None)

禁用对称减少。这是默认设置。

##### 自动(Automatic)

在输出网格中添加对称平面，使减少对称于 Maya 选择的平面。如果选择此选项，Maya 将决定哪个平面（XZ、XY 或 YZ）最为对称。它还会尝试对称于质心，这非常适合未与 X、Y 或 Z 轴对齐的常规形状。

##### 平面(Plane)

在输出网格中添加对称平面，使减少对称于指定的平面。

#### 对称容差(Symmetry tolerance)

控制 Maya 认定两个点相对于对称平面对称的误差范围，值在 0 到 1 之间。

#### 对称平面(Symmetry Plane)

指定对称平面的轴。当“对称类型”(Symmetry Type)设置为“平面”(Planar)时，选择 XZ、XY 或 YZ。

## 功能保留(Feature Preservation)

“功能保留”(Feature Preservation)选项可帮助您在减少过程中保留特定功能。使用滑块可控制为保留不同的边和边界而指定的优先级。

#### 网格边界(Mesh borders)

在减少时尝试保持多边形边界的形状（其他多边形未共享的边）。

**注**

提示：

将

“网格边界”(Mesh borders)

设置为 1 可保留原始选择的边界。

#### UV 边界(UV borders)

在减少时尝试保持 UV 边界的形状。

如果有许多 UV 边界，启用此选项可能产生无法预测的结果。执行减少前，请尝试缝合尽可能多的 UV 片。

**注**

如果多边形曲面上有很多 UV 接缝，而且在

“UV 边界”(UV borders)

启用的情况下执行

“网格 > 减少”(Mesh > Reduce)

操作，对象就很可能会丝毫没有减少，因为减少算法会尝试保持对象上的 UV 边界（接缝）。

如果不介意丢失 UV 接缝，则禁用“UV 边界”(UV borders)以成功减少多边形曲面。

#### 颜色边界(Color borders)

在减少时尝试保持颜色边界的形状。

#### 材质边界(Material borders)

在减少时尝试保持材质边界的形状。

#### 硬边(Hard edges)

在减少时尝试保持标记为“硬”的边的形状。

可以使用“网格显示 > 软化边”(Mesh Display > Soften Edge)或“网格显示 > 硬化边”(Mesh Display > Harden Edge)将网格上的边设置为硬边或软边。标记边为“硬”可能会保持比绘制减少权重更多的形状。

#### 折痕边(Crease edges)

在减少时尝试保留设置了折痕值的边的形状。

您可以使用“折痕工具”(Crease Tool)为网格上的边生成折痕。请参见[为多边形边和顶点生成折痕](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DEB060F9-A4B1-4F73-8B4D-B18A13D0E54B)。

## 高级选项

#### 顶点索引映射(Vertex index map)

可以导出顶点索引映射。若要在原始网格与输出网格的顶点之间建立关系，请在该字段中输入名称以创建新的颜色集。应用颜色集后，您可以观察输出网格中的顶点并根据颜色确定原始网格中的索引。请参见[多边形颜色集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-33C3E67A-A06D-420C-A297-B2830D9E6EAF)。

## 相关主题

- [生成 LOD 网格](../../../../查看场景/查看场景/LOD（细节级别）/生成%20LOD%20网格.md)

- [LOD（细节级别）](../../../../查看场景/查看场景/LOD（细节级别）.md)
