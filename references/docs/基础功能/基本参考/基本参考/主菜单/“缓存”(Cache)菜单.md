# “缓存”(Cache)菜单

#### Alembic 缓存

在 Maya 中使用 Alembic 缓存可在产品级流水线的各个阶段之间传递资产。Alembic 缓存文件的内容作为 Maya 几何体进行求值，并且可以使用多边形、NURBS 和细分曲面编辑工具进行修改。

必须先加载 AbcImport.mll 和 AbcExport.mll 插件，“缓存”(Cache)菜单才能显示在 Maya 主菜单中。

详细信息请参见[“Alembic 缓存”(Alembic Cache)子菜单](“缓存”%28Cache%29菜单/“Alembic%20缓存”%28Alembic%20Cache%29子菜单.md)。

#### 几何缓存

使用几何缓存可通过将对象的变形缓存到几何缓存，将多边形网格、NURBS（包含曲线）曲面和细分曲面变形（蒙皮和非蒙皮）保存到服务器或本地硬盘驱动器。几何缓存是存储顶点变换数据的特殊 Maya 文件。

当在播放或渲染包含许多变形对象的场景，并希望减少 Maya 要执行的计算数量时，这将非常有用，此外它们还允许您以直观的非线性方式轻松混合和编辑对象的变形。

详细信息请参见[“几何缓存”(Geometry Cache)子菜单](“缓存”%28Cache%29菜单/“几何缓存”%28Geometry%20Cache%29子菜单.md)。

#### GPU 缓存

GPU 缓存是基于 Alembic 的的文件，为了在 Maya 中实现快速播放性能而优化。根据对 GPU 缓存文件进行求值的方式来实现性能提升。GPU 缓存节点直接将缓存的数据路由到系统显卡，以处理、忽略 Maya 依存关系图求值。可以按与 Alembic 缓存相同的方式使用 GPU 缓存。

必须先加载 gpuCache.mll 插件，“GPU 缓存”(GPU Cache)才能显示在“缓存”(Cache)菜单中。

详细信息请参见[“GPU 缓存”(GPU Cache)子菜单](“缓存”%28Cache%29菜单/“GPU%20缓存”%28GPU%20Cache%29子菜单.md)。
