# 预照明选项(Prelight Options)

使用以下选项可设置在选择“网格显示 > 预照明(Maya)”(Mesh Display > Prelight (Maya))时发生的情况。

## 相关主题

- [预照明多边形](../../../多边形上色/预照明多边形.md)

- [使用预照明将颜色指定给多边形的顶点](../../../多边形上色/使用预照明将颜色指定给多边形的顶点.md)

- [从多边形顶点移除颜色或预照明](../../../多边形上色/从多边形顶点移除颜色或预照明.md)

默认情况下，所有选项都已禁用，且“采样比例因子”(Sample scale factor)设置为 1.0。

#### 仅对选定面采样(Sample selected faces only)

您可以选择对象和/或对象的任何类型的多边形组件。其中包括顶点、边、面和 UV/贴图组件类型。默认情况下，Maya 检查每个组件类型以确定已经选中的顶点，然后将对选定的顶点进行采样。

如果启用“仅对选定面采样”(Sample selected faces only)，Maya 将检查每个组件类型以确定选中的完整面。然后对选定的面采样。

例如，假设一个面有四个顶点，而只选中了其中三个：

- 如果“仅对选定面采样”(Sample selected faces only)禁用，则将对三个顶点采样。

- 如果启用了“仅对选定面采样”(Sample selected faces only)，则不进行采样，因为该面被认为是只有部分选中。

#### 使用面法线采样(Sample using face normals)

无论“仅对选定面采样”(Sample selected faces only)是否禁用，也无论是硬边还是软边，该选项都使用相应的面法线进行采样。

#### 计算阴影贴图(Compute shadow maps)

如果要计算阴影，请启用该选项。将发生软件渲染“阴影过程”(Shadow Pass)，它会输出一组深度阴影贴图，然后在采样求值过程中使用这些贴图。

它等效于在 Maya 渲染中执行下列操作：

- 将“属性编辑器”(Attribute Editor)中“renderGlobals”选项卡的“阴影过程”(Shadow Pass)设定为打开状态。通过打开“大纲视图”(Outliner)并关闭“显示 > 仅 DAG 对象”(Display > DAG Objects Only)，您可以选择该选项卡。

- 选择每个灯光并启用“属性编辑器”(Attribute Editor)中的“使用深度贴图阴影”(Use Depth Map Shadows)。

- 选择每个灯光并且将“基于磁盘的深度贴图”(Disk Based Dmaps)贴图转为“覆盖现有深度贴图”(Overwrite Existing Dmap(s))。

- 用当前活动视图摄影机执行软件渲染。

- 选择每个灯光并关闭“基于磁盘的深度贴图”(Disk Based Dmaps)。

- 在阴影贴图中读取，并在采样期间使用。

#### 强制为灯光使用阴影贴图(Force shadow map usage on lights)

仅当“计算阴影贴图”(Compute shadow maps)启用时，该选项才可用。当启用“强制为灯光使用阴影贴图”(Force shadow map usage on lights)时，即使“使用深度贴图阴影”(Use Depth Map Shadows)对灯光禁用，该选项也会计算每个灯光的阴影。

#### 重用计算的阴影贴图(Reuse computed shadow maps)

若要重用计算阴影贴图，请启用“计算阴影贴图”(Compute shadow maps)。启用该选项以跳过“阴影过程”(Shadow Pass)计算（上面的“计算阴影贴图”(Compute Shadow maps)）。这允许您使用静态创建的阴影，和/或为预照明操作的将来调整或软件渲染一次性计算阴影。

#### 忽略表面着色器上已映射的通道(Ignore mapped channels on surface shaders)

启用该选项以对曲面着色器的每个通道启用“渲染时忽略”。

#### 仅“对传入照明采样”(Sample incoming illumination)

如果选中该选项，将仅计算传入照明。该选项有助于您使用该信息计算自己的着色。它也有助于采样照明效果，例如当灯光的颜色已映射时。

请注意，场景中的灯光必须具有“衰退速率”(Decay Rate)，该选项才能生效。

#### 置换几何体(Displace geometry)

使用采样着色值置换几何体不是预照明效果，但与使用采样数据修改对象的几何体上的属性相关。要采样的选定顶点的位置会沿其法线被采样数据值的量置换。用于置换的法线就是用于渲染的顶点法线。

您可以通过启用“顶点法线”(Vertex Normals)选项（选择[“显示 > 多边形”(Display > Polygons)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B7F70ACE-0F3F-483B-83B5-D9711D6CBAAC) > 顶点法线(Vertex Normals)）在透视视图中查看该法线。

**注**

- 当启用该选项时，“使用面法线采样”会禁用。这是因为无法对顶点的每个面执行置换（如果“使用面法线采样”可用，可能尝试该操作）。

- 修改 > 转化 > 置换到多边形(Modify > Convert > Displacement to Polygons)可以实现相同的效果（尽管只能应用于整个对象）。

#### 忽略双面(Ignore double sided)

在预照明网格时忽略网格的形状节点上的双面属性。默认设置为启用。

#### 存储共享值(Store shared values)

如果选中了多个顶点，则启用该选项值会对各顶点求平均值并存储该平均值。

#### 采样比例因子(Sample scale factor)

如果要在存储前使颜色变亮或变暗，或者调整要执行的置换量，则比例因子很有用。

在将采样应用到几何体之前可以对其进行缩放（即，可以存储颜色或置换点）。对于颜色，会忽略负比例因子。对于几何置换，则考虑比例因子，无论是正因子还是负因子。

**注**

通常对采样的每个通道应用介于 0.0 和 1.0 之间的值，但也可以使用大于 1.0 的值。

#### 钳制最小 RGBA 值(Clamp minimum RGBA value)、钳制最大 RGBA 值(Clamp maximum RGBA value)

启用这些选项可钳制最小和最大 RGBA 值，从而强制使这些值在设定的范围中。

#### 颜色融合(Color blending)、Alpha 融合(Alpha blending)

控制新计算的颜色和透明度值如何影响顶点上的当前颜色/透明度。

运算后应用最小和最大钳制选项。

#### 覆盖(Overwrite)

新值替换当前值。

#### 相加(Add)、相减(Subtract)、相乘(Multiply)、相除(Divide)

用数学运算将当前值和新值结合使用。

#### 平均(Average)

求当前值和新值的平均值。

#### 不要覆盖(Don’t Overwrite)

如果顶点有当前值，则不会保存新值。
