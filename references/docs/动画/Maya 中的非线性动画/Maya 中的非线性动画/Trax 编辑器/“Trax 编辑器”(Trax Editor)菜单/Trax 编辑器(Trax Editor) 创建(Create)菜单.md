# Trax 编辑器(Trax Editor)  创建(Create)菜单

#### 动画片段(Animation Clip)

创建当前角色的动画片段。选择“动画片段”(Animation Clip) > ![图：创建当前角色的动画片段。选择“动画片段”(Animation Clip) 以访问创建片段选项(Create Clip O…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->以访问[创建片段选项(Create Clip Options)](Trax%20编辑器%28Trax%20Editor%29%20创建%28Create%29菜单/“创建片段”%28Create%20Clip%29选项.md)。

#### 约束片段(Constraint Clip)

“创建约束片段选项”(Create Constraint Clip Options)窗口中的选项与“创建片段选项”(Create Clip Options)窗口中的选项一样，不同之处在于“创建约束片段选项”(Create Constraint Clip Options)窗口不包含“时间范围动画曲线”(Time Range Animation Curve)选项。有关“创建约束片段选项”(Create Constraint Clip Options)窗口中选项的信息，请参见[创建片段选项](Trax%20编辑器%28Trax%20Editor%29%20创建%28Create%29菜单/“创建片段”%28Create%20Clip%29选项.md)。

#### 表达式片段(Expression Clip)

“创建表达式片段选项”(Create Expression Clip Options)窗口中的选项与“创建片段选项”(Create Clip Options)窗口中的选项一样，不同之处在于““创建表达式片段选项”(Create Expression Clip Options)窗口不包含“时间范围动画曲线”(Time Range Animation Curve)选项。有关“创建表达式片段选项”(Create Expression Clip Options)窗口中选项的信息，请参见[创建片段选项](Trax%20编辑器%28Trax%20Editor%29%20创建%28Create%29菜单/“创建片段”%28Create%20Clip%29选项.md)。

#### 姿势(Pose)

为当前角色创建一个姿势。请参见 [Trax 中的姿势](../Trax%20中的非线性动画组件/Trax%20中的姿势.md)和[创建姿势](../创建片段和姿势/创建姿势.md)。选择“创建姿势”(Create Pose) > ![图：为当前角色创建一个姿势。请参见 Trax 中的姿势和创建姿势。选择“创建姿势”(Create Pose) ，以显示“创建…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->，以显示[“创建姿势选项”(Create Pose Options)](Trax%20编辑器%28Trax%20Editor%29%20创建%28Create%29菜单/“创建姿势”%28Create%20Pose%29选项.md)窗口。

“创建姿势选项”(Create Pose Options)窗口中的“名称”(Name)文本框定义姿势的名称，与在 Visor 中显示的名称相同。

#### 融合(Blend)

*仅用于动画片段。*

融合选定的动画片段。一次只能创建两个动画片段之间的融合。请参见[融合](../Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__WS17956D7ADBC6E736475032DC117AE308AAE-7F6E)和[创建和编辑融合](../操纵片段/创建和编辑融合.md)。

在创建融合之前，请选择“创建 > 融合”(Create > Blend) > ![图：在创建融合之前，请选择“创建 融合”(Create Blend) 以设置“融合片段选项”(Blend Clip Opti…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->以设置“融合片段选项”(Blend Clip Options)。

#### 融合片段选项(Blend Clip Options)

设定下列选项：

##### 初始权重曲线(Initial Weight Curve)

设定如何在动画片段的开始、中间和结束部分对融合进行插值。

##### 线性(Linear)

以恒定速率更改从片段开始到结束的属性值。

##### 缓入(Ease In)

在开始时缓慢更改属性值，在结束时快速更改属性值。

##### 缓出(Ease Out)

在开始时快速更改属性值，在结束时缓慢更改属性值。

##### 缓入缓出(Ease In Out)

在开始和结束时缓慢更改属性值，在中间时快速更改属性值。

#### 旋转插值(Rotation Interpolation)

指定如何在动画片段的旋转之间进行融合。

##### 四元数(Quaternion)

（默认）在融合时使用四元数插值从第一个片段旋转到第二个片段。在大多数情况下，四元数插值跟随两个方向之间的最短圆弧，生成更佳的融合效果。

##### Euler

在片段之间使用 Euler 插值，创建以恒定速率融合值的线性插值。

#### 角色集(Character Set)

创建当前对象的角色集。请参见[角色、组和子角色](../Trax%20中的非线性动画组件/角色、组和子角色.md)。

有关[“创建角色集选项”(Create Character Set Options)](../../../../动画引用/动画引用/“动画”%28Animation%29菜单集/“关键帧”%28Key%29菜单/创建角色集选项%28Create%20Character%20Set%20Options%29.md)窗口的详细信息，请参见[“关键帧”(Key)菜单](../../../../动画引用/动画引用/“动画”%28Animation%29菜单集/“关键帧”%28Key%29菜单.md)中的“创建角色集”(Create Character Set) > ![图：有关“创建角色集选项”(Create Character Set Options)窗口的详细信息，请参见“关键帧”(Ke…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" -->。

#### 时间扭曲(Time Warp)

*仅用于动画片段*

创建当前动画片段的时间扭曲曲线。请参见[时间扭曲](../Trax%20中的非线性动画组件/Trax%20中的片段/片段状态.md#GUID-968254A9-1044-4887-8197-63A41D0DE05A__WS17956D7ADBC6E736475032DC117AE308AAE-7F6D)和[创建和编辑时间扭曲](../操纵片段/使用%20Trax%20创建和编辑时间扭曲.md)。

选择“时间扭曲”(Time Warp) > ![图：选择“时间扭曲”(Time Warp) 可打开“片段时间扭曲选项”(Clip Time Warp Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1892 字 ≥300，非承重" --> 可打开“片段时间扭曲选项”(Clip Time Warp Options)。

##### 已启用时间扭曲曲线(Enabled Time Warp Curve)

激活当前动画片段的时间扭曲曲线。

##### 已禁用时间扭曲曲线(Disabled Time Warp Curve)

取消激活当前动画片段的时间扭曲曲线。

#### 快速选择集(Quick Select Set)

创建当前动画或几何缓存片段的“快速选择集”(Quick Select Set)。“快速选择集”(Quick Select Set)用于为来自各种片段和角色的多个片段创建选择集。使用该选项创建的选择集显示在 Trax 菜单栏的“编辑 > 快速选择集”(Edit > Quick Select Sets)下。

可以使用“关系编辑器”(Relationship Editor)编辑现有快速选择集的成员身份。请参见[关系编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3DA58150-A73D-403E-A988-798DED4956BD)。

#### 几何缓存(Geometry Cache)

创建当前对象的几何缓存片段。请参见[创建新缓存(选项Create New Cache Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-CD67781F-A091-479C-B11F-A4801E203536)和[创建和编辑几何缓存](../../../../几何缓存/几何缓存/创建和编辑几何缓存.md)。
