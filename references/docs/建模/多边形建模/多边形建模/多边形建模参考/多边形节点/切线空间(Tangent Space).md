# 切线空间(Tangent Space)

您可以控制 Maya 如何在场景中设置多边形模型的切线空间。在网格的 polyShape 节点上的“切线空间”(Tangent Space)区域内设置“切线空间”(Tangent Space)属性。

#### 坐标系(Coordinate System)

默认情况下，Maya 使用右手切线空间。即，法线、切线和 Binormal 形成右手坐标系。

但是，如果在需要左手切线空间的环境中工作（例如，您所使用的游戏引擎要求使用左手系统，或者您正在将法线贴图合并到来自其他基于左手系统的应用程序的场景），那么将该选项设置为左手可确保计算切线空间后，使法线、切线和 Binormal 始终形成左手坐标系。

![图：默认情况下，Maya 使用右手切线空间。即，法线、切线和 Binormal 形成右手坐标系。 但是，如果在需要左手切线空…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-892F2F73-2719-4041-A988-68D1124BE8E0.png) <!-- baize:img-hook downloaded=false reason="正文 1382 字 ≥300，非承重" -->

**注**

默认情况下，Autodesk® 3ds Max® 使用左手切线空间。因此，合并来自 3ds Max 的法线贴图时，应确保在多边形网格的“属性编辑器”(Attribute Editor)中选择“左手”(Left Handed)选项。或者，也可以转到“窗口 > 设置/首选项 > 首选项 > 建模 > 多边形切线空间”(Windows > Settings/Preferences > Preferences > Modeling > Polygon Tangent Space)，然后将“默认坐标系”(Default co-ordinate system)设置为“左手”(Left handed)，以便所有的新网格均默认使用左手贴图。

#### UV 缠绕顺序(UV Winding Order)

有关“UV 缠绕顺序”(UV winding order)的描述，请参见手册的“映射 UV”部分中的[显示 UV 缠绕顺序](../../../../UV/UV/显示和选择%20UV/显示%20UV%20缠绕顺序.md)。

在面的“UV 缠绕顺序”(UV winding order)反转（即逆时针）的情况下，简单的左手或右手切线计算将得出翻转 Binormal。

![图：有关“UV 缠绕顺序”(UV winding order)的描述，请参见手册的“映射 UV”部分中的显示 UV 缠绕顺序…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-723280AE-C668-4BCC-A250-02DAC7F13F16.png) <!-- baize:img-hook downloaded=false reason="正文 1382 字 ≥300，非承重" -->

通过在“UV 缠绕顺序”(UV Winding Order Detect)字段中选择“检测”选项，Maya 将基于 UV 映射的 V 方向计算 Binormal。

![图：有关“UV 缠绕顺序”(UV winding order)的描述，请参见手册的“映射 UV”部分中的显示 UV 缠绕顺序…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-39080644-6D6D-4C68-B86D-225ECAADA2A6.png) <!-- baize:img-hook downloaded=false reason="正文 1382 字 ≥300，非承重" -->

**注**

提示：

默认情况下，会为创建的任何新网格设定

“UV 缠绕顺序”(UV Winding Order Detect)

字段中的“检测”选项。在大多数情况下，该选项可使法线贴图和凹凸贴图正确显示。

通过选择“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)，并选择“建模”(Modeling)类别可修改默认首选项。在“多边形切线空间”(Polygon Tangent Space)部分中，可设置 Maya 用于多边形网格的默认坐标系和缠绕顺序。

#### 切线平滑角度(Tangent Smoothing Angle)

指定对切线进行平滑的角度上限。默认设置 0 会使沿 UV 边界和镜像边的切线空间不平滑。增加该值可以平滑这些区域，其有助于移除凹凸贴图、法线贴图及其他由切线空间接缝引起的高级照明模型中的瑕疵。

#### 切线法线阈值(Tangent Normal Threshold)

指定计算切线空间时将法线视为等效的角度上限。默认设置 0 可确保所有硬边形成切线空间接缝。增加该值有助于当顶点法线未在边中共享时消除硬接缝。

**注**

无论何时变形多边形网格，都会在 Maya 中基于每一帧动态重新计算切线空间。这可能会导致切线空间平滑随着网格变形而发生变化。

许多使用切线空间的交互式游戏/交互式应用程序会导出网格处于绑定姿势或静止姿势时的一个切线数据快照，并根据该数据变形。因此，不会在最终游戏中显示引入的任何瑕疵。
