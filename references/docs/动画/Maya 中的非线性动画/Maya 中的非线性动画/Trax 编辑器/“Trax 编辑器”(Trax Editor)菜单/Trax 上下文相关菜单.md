# Trax 上下文相关菜单

在摘要、轨迹、动画片段或几何缓存片段上单击鼠标右键时，系统将显示 Trax 上下文相关菜单。显示在该菜单中的选项取决于调用该菜单时鼠标指针所在位置。Trax 上下文菜单中的许多选项也可以在“Trax 编辑器”(Trax Editor)菜单中找到。

## 摘要

*仅用于动画片段*。

#### 粘贴片段(Paste Clip)

将当前存在于系统剪贴板中的片段副本放置到单击的轨迹、组或角色中。

#### 将片段导入角色(Import Clip to Character)

可以将磁盘中的片段导入到单击的角色或组中。打开“导入”(Import)文件浏览器窗口。

## 轨迹

*仅用于动画片段*。

#### 粘贴片段(Paste Clip)

请参见[粘贴](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-10101E33-D78C-4533-91BB-47A96E966C21)。

#### 将片段导入角色(Import Clip to Character)

请参见[将片段导入角色](Trax%20上下文相关菜单.md#GUID-1C252A52-296C-4E17-8BE6-25971040B02D__GUID-0EE20CEF-97D4-428F-B2CB-0EC574387DFD)。

#### 在上面插入轨迹(Insert Track Above)

在单击的轨迹上面创建单个空轨迹。

#### 在下面插入轨迹(Insert Track Below)

在单击的轨迹下面创建单个空轨迹。

#### 移除轨迹(Remove Track)

删除单击的轨迹—包括其中包含所有片段。

## 片段

#### 启用片段(Enable Clip)

可以为单击的动画或几何缓存片段启用或禁用曲线。启用时，选定的片段将处于启用状态。禁用时，选定的片段将处于禁用状态。请参见[已启用/已禁用的片段](../Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__WS17956D7ADBC6E736475032DC117AE308AAE-7F70)或[启用](../../../../动画引用/动画引用/动画节点/cacheFile.md#WS1A9193826455F5FF-6D855556117E9F816D22780)。

#### 将片段设置为相对(Make Clip Relative)

仅当动画片段通道当前设置为混合使用绝对和相对偏移时，才在“Trax”上下文菜单中显示。选择此选项可将所有通道以使用相对偏移的行为。（请参见[绝对和相对通道偏移](../Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__GUID-F4A1A941-729A-4C5B-BB85-94A2854CD4BD)和[偏移片段通道](../操纵片段/偏移片段通道.md)。）

#### 将片段设置为绝对(Make Clip Absolute)

仅当动画片段通道当前设置为混合使用绝对和相对偏移时，才在“Trax”上下文菜单中显示。选择此选项可将所有通道设置为使用绝对偏移行为。

#### 相对片段(Relative Clip)

仅当当前动画片段的*所有*通道是相对或绝对时，才在“Trax”上下文菜单中显示。启用时，所有通道都将设置为相对。禁用时，所有片段通道都将设置为绝对偏移。使用此选项可以将所有通道快速设置为使用相同的偏移。

#### 编辑每通道偏移(Edit Per-Channel Offsets)

为选定的动画层打开“属性编辑器”(Attribute Editor)。展开[“通道偏移”(Channel Offsets)](../../../../动画引用/动画引用/动画节点/animClip.md#GUID-C6BC8B65-4E09-43F2-B578-CEDE01EE5A15__GUID-DAD40086-BA3E-428B-B55A-7DA796856A4A)标题以定义各个通道的偏移行为。请参见[偏移片段通道](../操纵片段/偏移片段通道.md)。

#### 激活关键帧(Activate Keys)

*仅用于动画片段*。

可以激活或取消激活单击的动画片段。启用时，选定的动画片段将处于活动状态。禁用时，选定的动画片段将处于非活动状态。请参见[活动/非活动片段](../Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__WS17956D7ADBC6E736475032DC117AE308AAE-7F6F)。

#### 分组/解组(Group/Ungroup)

*仅用于动画片段*。

请参见[分组](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-BF35C9BF-3A9B-45BA-8C40-1C5BB512B4B8)和[解组](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-4ED349FB-6155-4616-932C-F1425AA1562F)。

#### 剪切片段(Cut Clip)

*仅用于动画片段*。

请参见[剪切](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-3783249B-177D-4F47-8F5B-B77D3D6E95BD)。

#### 复制片段(Copy Clip)

*仅用于动画片段*。

请参见[复制](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-72BAFF88-436A-4B44-BDAE-E3503EF82479)。

#### 粘贴片段(Paste Clip)

*仅用于动画片段*。

请参见[粘贴](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-10101E33-D78C-4533-91BB-47A96E966C21)。

#### 分割片段(Split Clip)

请参见[分割](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-1F21E118-D2BE-4427-9290-898E0217667A)或[分割几何缓存片段](../../../../几何缓存/几何缓存/创建和编辑几何缓存/使用几何缓存片段/分割几何缓存片段.md)。

#### 复制片段(Duplicate Clip)

*仅用于动画片段*。

请参见[复制](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-98B29248-0406-47F6-A46A-1B0B1FDC1ADE)。

#### 匹配片段(Match Clips)

请参见[匹配片段](Trax%20编辑器%28Trax%20Editor%29%20修改%28Modify%29菜单.md#GUID-148B51BC-8792-4950-93F7-2E9404614FE7__GUID-D1F51B76-47A7-4221-B072-0BA6497567B0)。

#### 合并(Merge)

*仅用于动画片段*。

只有在单击循环动画片段或选中两个动画片段后可用。请参见[合并](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-D0206E60-5654-46F4-922E-CF25C479652B)。

#### 剪去前方/剪去后方(Trim Before/Trim After)

请参见[剪去前方](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-FD62DCFA-9C4B-41D4-B2EE-956E935EF18A)或[分割几何缓存片段](../../../../几何缓存/几何缓存/创建和编辑几何缓存/使用几何缓存片段/分割几何缓存片段.md)和[剪去后方](“Trax%20编辑器”%28Trax%20Editor%29%20“编辑”%28Edit%29菜单.md#GUID-C6D15F23-7D7A-4E00-AB3D-6B12110651A5__GUID-D15CEA86-8883-487A-9916-91A5320AE20F)或[修剪几何缓存片段](../../../../几何缓存/几何缓存/创建和编辑几何缓存/使用几何缓存片段/修剪几何缓存片段.md)。

#### 选择几何体(Select Geometry)

*仅用于几何缓存片段*。

在场景视图中选择对象，用于单击的缓存片段。

#### 替换缓存(Replace Cache)

*仅用于几何缓存片段*。

请参见[替换缓存(Replace Cache)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7C183154-EF31-46A0-AB54-F93B5303568B)和[替换几何缓存](../../../../几何缓存/几何缓存/创建和编辑几何缓存/缓存几何体/替换几何缓存.md)。

#### 替换缓存帧(Replace Cache Frame)

仅用于几何缓存片段。请参见[替换缓存帧(Replace Cache Frame)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D4475B13-2962-4014-96B4-0A76625A6828)和[替换几何缓存](../../../../几何缓存/几何缓存/创建和编辑几何缓存/缓存几何体/替换几何缓存.md)。

#### 属性编辑器(Attribute Editor)

打开“属性编辑器”(Attribute Editor)并显示所单击片段的节点和属性。

#### 对权重制图(Graph Weight)

打开“曲线图编辑器”(Graph Editor)并显示所单击片段的权重曲线。仅在片段拥有权重曲线时选择该选项。

#### 选择角色集成员(Select Character Set Members)

*仅用于动画片段*。

在场景视图中选择是所单击角色的成员的所有对象。

#### 在片段中设置关键帧(Key Into Clip)

*仅用于动画片段*。

请参见[在片段中设置关键帧(Key Into Clip)](../Trax%20工具栏.md#GUID-E1C8D9EC-B0FF-46DE-8281-A87E76EE370E__GUID-83BD68AD-CA67-4866-9E8D-F93F21DB214D)，[在片段中设置关键帧](../操纵片段/在片段中设置关键帧.md)。

#### 创建时间扭曲(Create Time Warp)

*仅用于动画片段*。

请参见[时间扭曲](Trax%20编辑器%28Trax%20Editor%29%20创建%28Create%29菜单.md#GUID-C9A3BC4F-42C2-49A7-8265-8C31A58080A8__GUID-05174B59-9C19-4B35-B8F2-C8BFDFFAFDC2)。

#### 创建权重曲线(Create Weight Curve)

为所单击的片段创建权重曲线。可以操纵该切线和对该切线设置关键帧，以创建各种动画和变形效果。请参见[权重](../Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__WS17956D7ADBC6E736475032DC117AE308AAE-7F6C)和[融合和设置几何缓存的权重](../../../../几何缓存/几何缓存/创建和编辑几何缓存/缓存几何体/融合和设置几何缓存的权重.md)。

#### 选择源片段(Select Source Clip)

仅用于动画片段。

选择所单击动画片段的源片段。源片段的属性显示在“通道盒”(Channel Box)中。请参见[编辑源片段](../选择和编辑源片段/编辑源片段.md)。
