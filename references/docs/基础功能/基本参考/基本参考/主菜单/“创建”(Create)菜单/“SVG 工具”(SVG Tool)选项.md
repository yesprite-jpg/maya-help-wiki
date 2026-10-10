# “SVG 工具”(SVG Tool)选项

- 创建 > SVG (Create > SVG)

使用这些选项可控制在使用“创建 > SVG”(Create > SVG)命令创建具有连接到 SVG 节点的默认 SVG（可扩展向量图形）形状的一个多边形网格时发生的情况。可以使用该 SVG 节点从外部源粘贴或导入 SVG 文件。另请参见[从 SVG 创建多边形](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F28EA595-1FA8-496A-A620-A32D1BE2F0E7)。

## SVG 属性

可以在 SVG 节点的属性编辑器中找到 SVG 属性。有四个属性选项卡。

- “SVG”属性控制导入的 SVG 文件的基本外观。

- “几何体”(Geometry)属性控制多边形网格的各个方面。

- “纹理”(Texturing)属性控制网格的着色器指定。

- “动画”(Animation)属性允许您按路径为对象生成动画。

### 公用属性

#### 粘贴(Paste)

单击此按钮可将剪贴板中存储的最近 SVG 路径或代码粘贴到场景中，以替换当前的 SVG 路径。

**注**

如果复制/粘贴操作不起作用，您可能需要将 Illustrator 版本更新为 CC。

#### 导入(Import)

单击此按钮可打开一个文件浏览器窗口，然后浏览到要加载到 SVG 对象中的现有 SVG 文件。

**注**

将 SVG 对象粘贴或导入到具有洞的 Maya 中时，最好首先对周围形状在原始文件中的洞进行分组。否则可能导致在 Maya 中不显示这些洞。开放曲线也可能会导致类似问题，应始终先将其关闭，然后再将对象导入到 Maya 中。有关详细信息，请参见

对 SVG 网格中的洞进行故障排除

。

**注**

要将 SVG 对象颜色保留在 Maya 中作为顶点颜色，来源的 CSS 特性必须设置为表达视图属性。在 Illustrator 中，可以在“另存为”(Save As)菜单中找到该选项。设置此选项后，它将成为所有未来 SVG 对象的默认设置。

### “SVG”选项卡

#### SVG 大小(SVG Size)

指定 SVG 对象的总大小。默认值为 20。

#### “操纵”(Manipulations)选项卡

#### 路径(Path)

指定要根据相应 SVG 路径操纵多边形网格中的哪些对象。

#### 位置 Z 偏移(Position Z Offset)

沿当前“路径”(Path)对象的局部 Z 轴对其进行平移。默认值为 0。

#### 缩放 Z(Scale Z)

沿当前“路径”(Path)对象的局部 Z 轴对其进行缩放。默认值为 1。

#### 全部重置(Reset All)

删除对组成 SVG 对象的所有对象进行的所有“位置 Z 偏移”(Position Z Offset)和“缩放 Z”(Scale Z)操作，使这些对象恢复为默认值。

#### 全局 Z 偏移(Global Z Offset)

立即将组成 SVG 对象的所有对象沿其局部 Z 轴平移。通常，您需要将此值设置为大于 0，因为小于 0 的任何值都可能导致在尝试光线跟踪对象时出现问题。默认值为 0.01。

### “几何体”(Geometry)选项卡

对于与类型工具的“几何体”(Geometry)选项卡重叠的属性，请参见[类型工具](“类型工具”%28Type%20Tool%29选项.md)。请注意，对于 SVG 工具，这些效果将应用到路径。

#### 输出顶点颜色(Output Vertex Colors)

启用后，会在工作空间中显示该网格的逐顶点颜色数据。默认设置为启用。

### “纹理”(Texturing)选项卡

对于与类型工具的“纹理”(Texturing)选项卡重叠的属性，请参见[类型工具](“类型工具”%28Type%20Tool%29选项.md)。请注意，对于 SVG 工具，这些效果将应用到路径。

### “动画”(Animation)选项卡

对于与类型工具的“动画”(Animation)选项卡重叠的属性，请参见[类型工具](“类型工具”%28Type%20Tool%29选项.md)。请注意，对于 SVG 工具，这些效果将应用到路径。

## 相关主题

- [“创建”(Create)菜单](../“创建”%28Create%29菜单.md)

- [从 SVG 创建多边形](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F28EA595-1FA8-496A-A620-A32D1BE2F0E7)
