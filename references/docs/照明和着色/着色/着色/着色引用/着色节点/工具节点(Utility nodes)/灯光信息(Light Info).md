# 灯光信息(Light Info)

与[采样器信息](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-5134339F-6F76-4193-9F94-713D0A88AAC2.htm)节点类似，“灯光信息”(Light info)提供灯光信息而非曲面特性信息。可以使用“灯光信息”(Light Info)工具节点可以获取灯光相对于纹理的位置的信息。当纹理上每个点都着色后，“灯光信息”(Light Info)的属性可以确定从灯光到着色点的精确距离。

“灯光信息”(Light Info)节点提供以下信息：

- 灯光在世界空间的位置。

- 灯光照射的方向（如果它不是点光源）。

- 从灯光到着色点的距离。

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用灯光信息工具](../../../渲染节点工具/使用“灯光信息”%28Light%20Info%29工具.md)。灯光信息属性位于连接编辑器中。

#### 灯光位置(Light Position)

已连接灯光在世界空间中的位置。已连接灯光是其“世界矩阵”(World Matrix)属性连接到该节点的“世界矩阵”(World Matrix)属性的灯光。

#### 灯光方向(Light Direction)

已连接灯光的照射方向。点光源照射所有方向。

#### 采样距离(Sample Distance)

已连接灯光和曲面上的着色点之间的世界空间距离。可用不同方法计算它。详细信息请参见[仅灯光方向](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-B28C5B86-685B-471B-8C03-D8AF27462DD6.htm#WS73099CC142F48755-3D114B7511812357EFE-5AC4)。

#### 世界矩阵(World Matrix)

将灯光或其他对象的输出“世界矩阵”(World Matrix)属性连接到该属性。该过程必须在该节点的输出尚不可用时完成。

#### 仅灯光方向(Light Direction Only)

控制如何计算“采样距离”(Sample Distance)属性。如果禁用，则“采样距离”(Sample Distance)是灯光到采样点的世界空间距离。

如果启用，则“采样距离”(Sample Distance)是沿灯光方向向量从最近点到采样点的距离。

用数学语言来说，它将“光源到对象”向量的投影长度返回到灯光方向向量上。

![图：控制如何计算“采样距离”(Sample Distance)属性。如果禁用，则“采样距离”(Sample Distance…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-D9CC8492-D90B-4A20-869F-B02325108A96.png) <!-- baize:img-hook downloaded=false reason="正文 831 字 ≥300，非承重" -->

**注**

“灯光数据”(Light Data)属性使用摄影机空间中的灯光信息，而“灯光信息”(Light Info)工具的“灯光方向”(Light Direction)属性使用世界空间中的灯光信息。
