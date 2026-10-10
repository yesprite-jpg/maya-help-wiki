# Trax 编辑器(Trax Editor)  修改(Modify)菜单

#### 属性编辑器(Attribute Editor)

打开“属性编辑器”(Attribute Editor)并显示选定角色、动画片段、对象或几何缓存片段的节点和属性。

#### 启用/禁用(Enable/Disable)

启用或禁用选定动画片段的动画曲线，或选定的几何缓存片段缓存。请参见[已启用/已禁用的片段](../Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__WS17956D7ADBC6E736475032DC117AE308AAE-7F70)或[启用或禁用几何缓存片段](../../../../几何缓存/几何缓存/创建和编辑几何缓存/使用几何缓存片段/启用或禁用几何缓存片段.md)。

#### 激活/取消激活关键帧(Activate/Deactivate Keys)

*仅用于动画片段*。

启用或禁用选定动画片段的“激活关键帧”(Activate Keys)。“激活关键帧”(Activate Keys)模式用于为片段设置关键帧。请参见[活动/非活动片段](../Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__WS17956D7ADBC6E736475032DC117AE308AAE-7F6F)。

#### 移除空轨迹(Remove Empty Tracks)

*仅用于动画片段*。

移除当前角色的所有空轨迹。

#### 匹配片段(Match Clips)

根据您定义的片段重影根和您设置的“匹配片段选项”(Match Clip Options)对齐片段轨迹。

选择修改 > 匹配片段(Modify > Match Clips) > ![图：选择修改 匹配片段(Modify Match Clips) 以打开匹配片段选项(Match Clip Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1345 字 ≥300，非承重" --> 以打开匹配片段选项(Match Clip Options)。

#### 匹配片段选项

定义的“匹配片段选项”(Match Clip Options)可帮助您更快速地对齐片段并形成平滑动画序列。

例如，可以将行走循环片段与跑步循环片段对齐（每个片段的角色向不同的方向移动），并创建平滑序列，其中角色向相同方向移动，而无需像在行走和跑步片段之间过渡那样滑动或翻转。请参见[匹配姿势和对齐片段](../操纵片段/匹配姿势和对齐片段.md)。

##### 匹配平移(Match Translation)

指定目标（第二个）片段是否移动以匹配源（第一个）片段，以及如何匹配。

如果要在空间中完全对齐片段，设置为完全(Full)。

对于根据由源片段的“平移 X”(Translate X) 和“平移 Z”(Translate Z) 值定义的投影地平面对齐片段的部分匹配，设置为“已投影”(Projected)。

设置为无(None)以在平移时不应用匹配。

##### 匹配旋转(Match Rotation)

指定目标片段是否旋转以匹配源片段，以及如何匹配。

如果在片段的方向需要精确匹配，设置为完全(Full)。此选项将重置目标片段的旋转值以匹配源片段。

对于部分匹配，设置为已投影(Projected)。此选项根据由源片段的“旋转 X”(Rotate X)和“旋转 Z”(Rotate Z)值定义的投影地平面对齐片段。这样，可以保持目标片段的常规方向，但仍然提供一个常规对齐方向。

例如，如果希望在空间中对齐片段但保持目标片段的方向（常规移动方向），请将匹配平移(Match Translation)设置为完全(Full)，而将匹配旋转(Match Rotation)设置为已投影(Projected)。

设置为无(None)以在旋转时不应用匹配。

##### 匹配节点(Match Node)

列出选择用来引导各片段之间的匹配操作的对象。Maya 将使用该对象来确定各片段在空间上的对齐位置。可以使用角色集中包含的对象，或受角色集中所含对象驱动的对象作为“匹配节点”(Match Node)。

具体选择哪个对象取决于两个片段之间的过渡类型。例如，对于行走和跑步片段，由于动作主要集中在脚上，因此最好选择左踝或右踝效应器作为匹配对象。

要更改所列的对象，请选择场景中的某个对象，然后单击 ![图：要更改所列的对象，请选择场景中的某个对象，然后单击 以将其加载为新的“匹配节点”(Match Node)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-10E491C6-8F7E-4610-8015-51D8C014706A.png) <!-- baize:img-hook downloaded=false reason="正文 1345 字 ≥300，非承重" --> 以将其加载为新的“匹配节点”(Match Node)。
