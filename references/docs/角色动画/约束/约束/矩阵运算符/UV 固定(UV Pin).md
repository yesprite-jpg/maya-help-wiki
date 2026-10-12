# UV 固定(UV Pin)

“UV 固定”(UV Pin)节点用于跟踪变形曲面上的位置，类似于[“接近度固定”(Proximity Pin)节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-8A5E153C-8D06-408D-9D72-D82AC39D1288.htm)。顾名思义，“UV 固定”(UV Pin)从 UV 坐标派生位置，因此可以为固定指定精确的坐标位置。

若要了解如何将“UV 固定”(UV Pin)添加到几何体，请参见[创建 UV 固定](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-AADA4417-39D1-4EE0-84DB-2DCEE2F72B1F.htm)。

“UV 固定”(UV Pin)非常适用于干净 UV；它不太适用于重复或可疑的 UV。“UV 固定”(UV Pin)节点可用于在“属性编辑器”(Attribute Editor)中拖动 UV 值，以在对象的整个曲面上移动“UV 固定”(UV Pin)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-B761E1F8-9A0C-4659-BBF0-D021F75731D0.png) <!-- baize:img-hook downloaded=false reason="正文 343 字 ≥300，非承重" -->

将 UV 固定添加到 NURBS 几何体

当需要进行精确定位时，非常适合使用“UV 固定”(UV Pin)节点，例如，如果要在置换贴图中对齐特征（其中需要了解 UV 的精确位置），或者要跨曲面设置动画。
