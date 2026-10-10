# MASH 编辑器

“MASH 编辑器”(MASH Editor)可用于查看、选择和修改场景中的 MASH 网络。可以通过“动画”(Animation)或“FX”菜单集中的“MASH > MASH 编辑器”(MASH > MASH Editor)，或者通过 MASH 工具架访问该工具。

**注**

MASH 编辑器

与在

Maya

2017 之前创建的 MASH 网络不兼容。

有关功能列表，请参见此图下面的表。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-MotionGraphics/images/GUID-7CC34BD6-724B-4850-90D0-F49D9D2EDE3C.png) <!-- baize:img-hook downloaded=false reason="正文 937 字 ≥300，非承重" -->

| 1 - 添加节点 | 单击此按钮可显示节点的下拉列表。选择一个节点，将其添加到顶层级的 MASH 网络。有关特定节点的详细信息，请参见 [MASH 节点概述](../MASH%20节点概述.md)。 |
|---|---|
| 2 - 添加工具 | 单击此按钮可显示工具的下拉列表。这些工具包括： [添加点节点(Add Points Node)](../MASH%20节点概述/添加工具/点.md) [切换几何体类型(Switch Geometry Type)](../MASH%20菜单.md) [缓存网络(Cache Network)](../MASH%20菜单.md) [从点创建网格(Create Mesh from Points)](../MASH%20菜单.md) |
| 3 - 选择重新投影/实例化器 | 根据 MASH 网络的当前几何体类型，选择[重新投影(Repro)](../MASH%20节点概述/重新投影.md)或[实例化器(Instancer)](../MASH%20节点概述/实例化器.md)节点。 |
| 4 - 切换节点 | 禁用/启用对应的 MASH 节点。单击顶层级按钮时，将影响[分布(Distribute)](../MASH%20节点概述/分布.md)节点。 |
| 5 - 移动节点 | 拖动带有白色虚线控制柄的节点，在堆栈中对其重新排序。节点仅影响其下方的所有对象，因此对节点重新排序时，可能会更改节点在 MASH 网络上的效果。 带有深色实线控制柄的节点无法重新排序。 |
| 更改标签颜色 | 在网络的顶层级上单击鼠标右键，然后选择“标签颜色”(Label Color)。标签颜色有助于快速区分“MASH 编辑器”(MASH Editor)中的不同 MASH 网络。 |
| 复制网络 | 在网络的顶层级上单击鼠标右键，然后选择“复制网络”(Duplicate Network)。 |
| 删除节点或整个网络 | 在节点上单击鼠标右键，然后选择“删除”或“删除网络”(Delete Network)。 注： 如果删除网络，ReproMesh 将保留在场景中。 |
| 更改标签颜色 | 在网络的顶层级上单击鼠标右键，然后选择“标签颜色”(Label Color)。标签颜色有助于快速区分“MASH 编辑器”(MASH Editor)中的不同 MASH 网络。 |
| 创建新的 MASH 网络 | 转到“创建 > 创建 MASH 网络”(Create > Create MASH Network)。 |

## 相关主题

- [MASH 概述](../../使用%20RenderMan%20渲染%20MASH.md)

- [MASH 节点](../MASH%20节点概述.md)
