# MASH 菜单

MASH 工具是一组可在 MASH 网络上运行或由 MASH 网络辅助的有用工具。通过转到“动画”(Animation)或“FX”菜单集中的“MASH > 工具”(MASH > Utilities)，可以访问这些工具。其中的大多数工具也可通过 MASH 工具架获得。

#### 创建 MASH 网络

从选定对象以及 [Waiter](MASH%20节点概述/Waiter.md) 和[分布(Distribute)](MASH%20节点概述/分布.md)节点中创建新的 MASH 网络。根据当前的“几何体类型”(Geometry Type)自动添加其他节点。

也可以通过 [MASH 编辑器](MASH%20窗口和编辑器/MASH%20编辑器.md)或 MASH 工具架进行访问。

#### MASH 编辑器

打开 [MASH 编辑器](MASH%20窗口和编辑器/MASH%20编辑器.md)。

#### 工具

包含许多与 MASH 相关的工具和实用程序。

#### 缓存 MASH 网络(Cache MASH network)

使用 Alembic 缓存来缓存 MASH 网络效果。与使用“缓存 > Alembic 缓存 > 将当前选择导出到 Alembic”(Cache > Alembic Cache > Export Selection to Alembic)选项的功能相同。有关详细信息，请参见[缓存 MASH 网络进行渲染](../缓存%20MASH%20网络进行渲染.md)。

#### 创建 MASH 变形器(Create MASH Deformer)

根据 MASH 网络中的点使顶点或面变形。有关详细信息，请参见 [MASH 变形器](MASH%20菜单/MASH%20变形器.md)。

#### 创建融合变形器(Create Blend Deformer)

从网格的一个版本过渡到相同网格的另一个版本。但与常规“融合变形器”(Blend Deformer)不同，此融合可与 MASH 衰减对象、贴图等进行交互。有关详细信息，请参见 [MASH 融合变形器](MASH%20菜单/MASH%20融合变形器.md)。

#### 创建抖动变形器(Create Jiggle Deformer)

使网格上的点在移动时振动。但与常规“抖动变形器”(Jiggle Deformer)不同，此抖动可与 MASH 衰减对象、贴图等进行交互。有关详细信息，请参见 [MASH 抖动变形器](MASH%20菜单/MASH%20抖动变形器.md)。

#### 从点创建网格(Create Mesh from Points)

通过将当前选定 MASH 节点的点接合形成一个三角形，可创建新网格。如果要将对象分布到蒙皮角色的体积中，则此选项对于设置顶点分布非常有用。

#### 将 MASH 连接到类型/SVG(Connect MASH to Type/SVG)

将选定类型/SVG 网格中的角色连接到选定 MASH 网络中的点。有关详细信息，请参见[创建多边形文本](../../../创建多边形文字/创建多边形文字.md)。

**注**

为获得最准确的结果，请将“类型”(Type)网格的

“字距微调比例”(Kerning Scale)

设置为 0。

#### 切换 MASH 几何体类型(Switch MASH Geometry Type)

将选定 MASH 网格的实例更改为重新投影节点，反之亦然。

#### 将实例化器烘焙到对象(Bake Instancer to objects)

用于将 MASH 实例烘焙到实际对象（包括动画）。有关详细信息，请参见[烘焙实例化器工具(Bake Instancer Tool)](MASH%20窗口和编辑器/烘焙实例化器工具.md)。

#### 创建实例化器枢轴(Create Instancer Pivot)

创建新定位器，充当所有实例的枢轴。

#### 动力学(Dynamics)

包含与 MASH 动力学相关的工具和实用程序。

#### 添加壳动力学(Add Shell Dynamics)

将 MASH 动力学添加到所有选定的多边形壳（每个壳用作动力学对象）。

**注**

如果在将网格设置为动力学壳之后对其进行编辑，则需要重置动力学节点的

初始状态

。

#### 添加解算器(Add Solver)

创建新的 [BulletSolver](MASH%20节点概述/BulletSolver.md) 节点。

#### 指定解算器(Assign Solver)

将选定的 [BulletSolver](MASH%20节点概述/BulletSolver.md) 节点指定给选定的 MASH 网络（按住 Shift 键并选择二者）。

## 相关主题

- [MASH 节点](MASH%20节点概述.md)
