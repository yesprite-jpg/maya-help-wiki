# 使用“属性编辑器”(Attribute Editor)

将属性加载到“属性编辑器”(Attribute Editor)中会使其可供查看或编辑。有几种方法可以加载对象属性：

- 选择对象时自动加载

- 手动

- 从“属性编辑器”(Attribute Editor) “选定”(Selected)菜单中选择对象

- 从“聚焦”(Focus)菜单中选择对象

自动加载选定对象的属性

选择某个对象时，会自动将其属性加载到“属性编辑器”(Attribute Editor)中，可以在属性编辑器中查看和编辑这些属性。选定对象的每个节点将自动显示为一个选项卡。这是默认方法。

1. 在“属性编辑器”(Attribute Editor)中，选择“列表 > 自动加载选定属性”(List > Auto Load Selected Attributes)以启用该选项。

  **注**

  如果选择多个项目，Maya 自动更新最近选择的项目（即，拾取列表中最新的项目）。

手动加载选定对象的属性

1. 单击“属性编辑器”(Attribute Editor)底部的“加载属性”(Load Attributes)按钮。

  **注**

  如果禁用了

  “自动加载选定属性”(Auto Load Selected Attributes)

  ，那么在选择对象之后，必须手动将对象的属性加载到

  “属性编辑器”(Attribute Editor)

  中以查看和编辑这些属性。

## “属性编辑器”(Attribute Editor)颜色

属性框的颜色会根据其状态而变化。有关详细信息，请参见[通道盒颜色](../通道盒%28Channel%20Box%29.md#GUID-4C954FB2-8B6A-4BBD-9695-DF432616D0D2__WS17956D7ADBC6E736-4CE538CA117AE30C631-7FF9)。

## “属性编辑器”(Attribute editor)图形控件

对于某些属性，在“属性编辑器”(Attribute Editor)中会显示两个常用的图形控件：渐变和图表。

### 渐变(Ramp)

渐变中的每个颜色条目在渐变上方都有一个圆形颜色控制柄，在渐变的下方都有一个方形颜色图标。活动颜色在其颜色控制柄和图标周围具有白色边界。渐变可以用于多种类型的渐变，包括透明度、颜色等。

有关如何通过添加额外的颜色项目自定义渐变的详细信息，请参见[使用渐变设置属性](../使用渐变设置属性.md#GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B__SECTION_D18F4FBF38B94659837688094068CAF0)。

有关高级渐变功能的详细信息，请参见[渐变着色器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-022F69B8-B1A3-46A3-9917-0D9CBDBB6733)。

### 图表(Graph)

图表控件包含控制柄，可在图表区域中拖动这些控制柄来设定位置-值对。活动点在其控制柄和图标周围具有白色边界。图表可以用于多种类型的属性，在这些属性中，值会按位置改变，包括 Paint Effects 设置、流体设置等等。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-9EBE1668-F3AA-43D0-BFEE-D813DB834B10.png) <!-- baize:img-hook downloaded=false reason="正文 1222 字 ≥300，非承重" -->

## 在单独的窗口中打开渐变和图表控件

单击控件右侧的箭头可在更大的窗口中打开渐变或图表控件。

对于图表控件，可以编辑插值方法、选定值和选定位置。对于渐变控件，可以编辑插值方法、选定颜色和颜色条目。另外，还可以启用/禁用“垂直”以在垂直布局或水平布局之间切换。

选中垂直框会改变渐变的大小。选中垂直框后，渐变或图表将自动调整为合适的大小。

保存场景时，Maya 还会保存已为控件选择的布局。

## 相关主题

- [节点和属性概述](../../../节点和属性.md)

- [在属性编辑器(Attribute Editor)或通道盒(Channel Box)中更改属性值](../在“属性编辑器”%28Attribute%20Editor%29或“通道盒”%28Channel%20Box%29中更改属性值.md)

- [保存和重用属性预设](../保存和重用属性预设.md)

- [锁定属性值](../锁定属性值.md)

- [创建、编辑或删除自定义属性](../创建、编辑或删除自定义属性.md)

- [打开多个属性编辑器](打开多个“属性编辑器”%28Attribute%20Editor%29.md)

- [通道盒](../通道盒%28Channel%20Box%29.md)
