# 缓存 MASH 网络进行渲染

由于某些 MASH 节点具备程序特性，因此通常建议在渲染时缓存使用这些节点以快速获得可预测结果的所有网络。这对模拟类型节点而言最重要，其中包括：

- [飞行(Flight)](MASH%20参考/MASH%20节点概述/飞行.md)

- [弹簧(Spring)](MASH%20参考/MASH%20节点概述/弹簧.md)

- [轨迹(Trails)](MASH%20参考/MASH%20节点概述/添加工具/轨迹.md)

- 任何基于“速度”(Velocity)的效果（默认为在[颜色(Color)](MASH%20参考/MASH%20节点概述/颜色.md)和[时间(Time)](MASH%20参考/MASH%20节点概述/时间.md)节点中，但也可通过自定义的 [Python](MASH%20参考/MASH%20节点概述/Python.md) 脚本访问此属性）

- 当“添加”(Add)模式由[衰减(Falloff)](MASH%20参考/MASH%20节点概述/衰减.md)节点使用的任何时候

缓存 MASH 网络的过程因当前的“几何体类型”(Geometry Type)而异。

在使用实例化器时缓存 MASH 网络

1. 打开 [Waiter](MASH%20参考/MASH%20节点概述/Waiter.md) 节点的“属性编辑器”(Attribute Editor)。

2. 在“缓存”(Caching)部分中，打开[缓存创建器(Cache Creator)](MASH%20参考/MASH%20窗口和编辑器/缓存创建器.md)。

3. 设置相应的选项，然后单击“创建缓存”(Create Caches)。

在使用重新投影网格时缓存 MASH 网络

1. 选择重新投影网格，然后选择“缓存 > Alembic 缓存 > 将当前选择导出到 Alembic”(Cache > Alembic Cache > Export Selection to Alembic)，以便将网格导出到 Alembic 缓存。

2. 将 Alembic 缓存重新导入到场景中（“缓存 > Alembic 缓存 > 导入 Alembic”(Cache > Alembic Cache > Import Alembic)）。

3. 删除或禁用 MASH 网络的其余部分。

**注**

作为步骤 3 和 4 的替代方法，您可以使用 Vray Proxies 等第三方渲染工具直接渲染缓存。
