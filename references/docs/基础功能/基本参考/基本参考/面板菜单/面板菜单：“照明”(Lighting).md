# 面板菜单：“照明”(Lighting)

“照明”(Lighting)菜单显示在场景视图之上，或者显示在具有多个场景视图的布局中每个视图面板之上。

使用此菜单中的项可以选择要在场景中使用的灯光或灯光组。

#### 使用默认照明(Use Default Lighting)

仅在场景视图中启用默认照明；它不影响最终渲染。曲面看起来由视图中的默认灯光完全照明。

另请参见[默认照明](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6D4A0119-5A23-49DF-9D67-C44311BC472B)。

#### 使用所有灯光(Use All Lights)

在场景中至少使用 8 束灯光（取决于图形卡的功能）来为曲面照明。通过此选项，您可以看到渲染图像时灯光的效果*表示形式*。

创建灯光后，您可以在渲染之前交互放置这些灯光并查看场景灯光效果。

#### 使用选定灯光(Use Selected Lights)

使用视图及“渲染视图”(Render View)中的选定灯光为曲面照明。

仅使用选定灯光。如果更改灯光选择，则照明也会随之更改。

#### 使用平面照明(Use Flat Lighting)

将此选项与“Viewport 2.0”或“旧版默认视口”(Legacy Default Viewport)配合使用，以使用环境光着色对象。

**注**

当使用“Viewport 2.0”时，可以选择：物理精确的无灯光模式（选择“照明 > 不使用灯光”(Lighting > Use No Lights)）；或者环境光模式（选择“照明 > 使用平面照明”(Lighting > Use Flat Lighting)），其中对象使用一种默认环境光着色（颜色设置为白色，强度设置为 1）。

#### 不使用灯光(Use No Lights)

将此选项与“Viewport 2.0”或“旧版高质量视口”(Legacy High Quality Viewport)一起选择，可实现物理上精确的无灯光模式。硬件照明已被禁用；不存在环境光，也不会进行着色。

**注**

- 当使用“Viewport 2.0”时，可以选择：物理精确的无灯光模式（选择“照明 > 不使用灯光”(Lighting > Use No Lights)）；或者环境光模式（选择“照明 > 使用平面照明”(Lighting > Use Flat Lighting)），其中对象使用一种默认环境光着色（颜色设置为白色，强度设置为 1）。

- 在 Maya 2014 和更低版本中，“照明 > 不使用灯光”(Lighting > Use No Lights)选项为“旧版默认视口”(Legacy Default Viewport)提供环境光模式。若要实现相同的效果，应使用“使用平面照明”(Use Flat Lighting)选项。

#### 双面照明(Two Sided Lighting)

启用时，会照亮对象的两面。“双面照明”(Two Sided Lighting)在默认情况下处于启用状态。请注意，Maya 的性能在一些系统上可能会降低。

#### 阴影(Shadows)

使用“照明 > 阴影”(Lighting > Shadows)可查看场景视图中的硬件阴影贴图。

几何体（NURBS、多边形、细分曲面）和粒子（仅限点、多点和球体）的定向或现场灯光的硬件阴影贴图可以计算得出，并可以在装有支持 ARB_multitexture 和 EXT_texture_env_combine OpenGL 扩展功能的驱动程序的显卡上显示。

**注**

- 阴影颜色始终为黑色。

- 可以设定“深度贴图分辨率”，但只能使用其中的一个值：1024、512、256、128、64。

- 屏幕刷新可能会变慢，具体取决于灯光投射阴影的数量。
