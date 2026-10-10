# “映射边界”(Map Border)选项

使用这些选项可设置选择“UV > 映射 UV 边界”(UV > Map UV Border)时发生的情况。

## 设置

#### 边界目标形状(Border target shape)

选择要映射 UV 边界的形状类型（“方形”(Square)或“圆形”(Circle)）。

#### 自动(Automatic)

启用“自动”(Automatic)以自动映射 UV 边界为最佳使用纹理空间的形状，同时保持边之间的世界空间关系。

#### 保持原始形状(Preserve original shape)

确定边界映射匹配选定“边界目标形状”(Border Target Shape)的程度。使用滑块或输入介于 0 和 1 的值，以使用指定“边界目标形状”(Border Target Shape)控制现有 UV 边界。值为 0 时会生成最接近指定目标形状（“圆形”(Circle)或“方形”(Square)）的 UV 边界映射。值为 1 时会生成接近代表边之间的世界空间关系的边界，但会导致沿边界的凹面区域 — 一旦松弛，这将会产生重叠的内部 UV。

![图：确定边界映射匹配选定“边界目标形状”(Border Target Shape)的程度。使用滑块或输入介于 0 和 1 的…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-FA48B9BC-8AEB-45A4-95A5-94F0022CDBEB.png) <!-- baize:img-hook downloaded=false reason="正文 662 字 ≥300，非承重" -->

**注**

“映射 UV 边界”(Map UV Border)

可能无法找到一个带非流形几何体的唯一边界。

如果您有一块非流形几何体，任何特定 UV 可能在不止一个边界/壳中，因此它不会唯一确定要松弛网格的平坦片。“映射 UV 边界”(Map UV Border)将查找边界并映射它，但是无法控制它会获得哪个。

若要解决该问题，可以沿非流形边切割 UV，以确保它们是“平坦的”，或使用“清除”以首先消除非流形区域。

## 相关主题

- [将边界 UV 映射到方形或圆形](../../../../../编辑%20UV/将边界%20UV%20映射到方形或圆形.md)

- [拉直 UV 边界选项(Straighten UV Border options)](“拉直边界”%28Straighten%20Border%29选项.md)

- [松弛和解开 UV](../../../../../编辑%20UV/优化%20UV%20间距.md)
