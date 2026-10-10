# 绘制顶点颜色工具选项(Paint Vertex Color Tool Options)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 1370 字 ≥300，非承重" -->

使用以下选项可设置在选择“网格显示 > 绘制顶点颜色工具”(Mesh Display > Paint Vertex Color Tool)时发生的情况。在下面的“颜色”(Color)部分中会介绍“绘制顶点颜色工具”(Paint Vertex Color Tool)的独特属性。

有关所有其他区域中的所有其他属性的介绍，请参见 [Artisan 工具设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B8F095-4A0E-4BAE-938C-CB41B3EBD533)。

## 颜色(Color)

#### 运算(Operation)

选择为顶点上色的方法。

#### 替换(Replace)

使用指定颜色替换现有颜色。

#### 平滑(Smooth)

平均化笔刷下的颜色。特别是，笔刷下的顶点会获得四个周围的顶点的平均颜色。

#### 删除(Remove)

通过每个笔刷笔划逐渐移除现有颜色。

#### 添加(Add)

通过每个笔刷笔划逐渐添加颜色。

#### Subtract

通过每个笔刷笔划逐渐减去颜色。

#### 缩放(Scale)

通过每个笔刷笔划逐渐缩放颜色值和不透明度。

#### 绘制(Paint)

选择要上色的组件。

#### 顶点(Vertex)

与绘制的顶点连接的所有面都会获得该颜色。

#### 顶点面(Vertex face)

仅为该面的内部上色。会保持顶点为非共享，这样它们在边的任一侧上可能会有不同的颜色值。

#### 面(Face)

会为附加到面的所有顶点上色。颜色会溢出面的边。

#### 通道(Channels)

选择进行上色要使用的颜色通道。

#### RGB

绘制顶点会应用“颜色值”(Color value)。

#### RGBA

绘制顶点会应用“颜色值”(Color value)（颜色）和“Alpha 值”(Alpha value)（透明度）。

#### 颜色值(Color value)

绘制的颜色将应用到顶点。

#### Alpha 值(Alpha value)

当“通道”(Channels)是 RGBA 时，绘制的 Alpha 值将应用到顶点。“Alpha 值”(Alpha value)的范围在 0（透明）和 1（不透明）之间。请参见下面的“Alpha 工具”(Alpha Tools)。

#### 绘制钳制(Paint clamp)

尤其是对于“相加”(Add)、“相减”(Subtract)和“缩放”(Scale)运算，您可能需要将“颜色值”(Color value)的应用范围限制于重复的笔刷笔划。如果是这样，请使用复选框并将数值“钳制值”(Clamp values)指定为介于 0 和 1 之间，以设置“颜色值”(Color value)的“下限”(Lower)和/或“上限”(Upper)。

#### Alpha 工具(Alpha Tools)

与“绘制钳制”(Paint clamp)一样，如果要限制“Alpha 值”(Alpha value)设置的范围，请使用该区域将“Alpha 最小值/最大值”(Alpha min/max value)设置为介于 0 和 1 之间，或者指定“Alpha 钳制值”(Alpha clamp values)，然后选择“下限”(Lower)和/或“上限”(Upper)。

#### 泛洪(Flood)

将所有顶点设定为当前“颜色值”(Color Value)（和“颜色 Alpha”(Color Alpha)，如果“通道”(Channels)是“RGBA”）。

#### 显示(Display)

#### 通道(Channels)

![图：在对象曲面上仅显示特定颜色通道。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1370 字 ≥300，非承重" --> 在对象曲面上仅显示特定颜色通道。

#### 以灰度显示 Alpha(Display alpha as greyscale)

![图：在对象上仅显示以灰度而不是透明度呈现的 Alpha 通道。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1370 字 ≥300，非承重" --> 在对象上仅显示以灰度而不是透明度呈现的 Alpha 通道。

## 相关主题

- [使顶点颜色可见](../../../多边形上色/使顶点颜色可见.md)

- [通过绘制为多边形顶点指定颜色](../../../多边形上色/通过绘制为多边形顶点指定颜色.md)

- [Artisan 笔刷工具的工作方式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D0A5ACD2-8D10-4B51-ADD3-E261F9337B07)
