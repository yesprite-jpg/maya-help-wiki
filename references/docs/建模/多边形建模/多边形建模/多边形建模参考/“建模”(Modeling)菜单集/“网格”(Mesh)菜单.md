# “网格”(Mesh)菜单

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" -->

- 位于“建模”(Modeling)[菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129)中。

## 结合(Combine)

#### 布尔(Booleans)

布尔运算可用于合并多边形网格以创建新形状。操作依靠交集（即两个网格的共享体积）来确定布尔结果。

#### 并集(union)

合并所选网格的体积。原始的两个对象均保留，并减去交集。

选择“网格 > 布尔 > 并集”(Mesh > Booleans > Union)可设置[“布尔并集选项”(Booleans Union Options)](“网格”%28Mesh%29菜单/布尔并集选项%28Booleans%20Union%20options%29.md)。

#### 差集(Difference)

从第一个选定网格减去第二个（以及后续）选定网格的体积。

选择“网格 > 布尔 > 差集”(Mesh > Booleans > Difference)可设置[“布尔差集选项”(Booleans Difference Options)](“网格”%28Mesh%29菜单/布尔差集选项%28Booleans%20Difference%20Options%29.md)。

**注**

可以通过一次

“差集”(Difference)

运算从第一个选定网格中提取多个网格。

#### 交集(Intersection)

仅保留两个网格的共享体积。

选择“网格 > 布尔 > 交集”(Mesh > Booleans > Intersection)可设置[“布尔交集选项”(Booleans Intersection Options)](“网格”%28Mesh%29菜单/布尔差集选项%28Booleans%20Difference%20Options%29.md)。

#### 结合(Combine)

![图：将选定的网格组合到单个多边形网格中。一旦多个多边形被组合到同一网格中，就只能在两个单独的网格壳之间执行其编辑操作。 如果…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" -->

将选定的网格组合到单个多边形网格中。一旦多个多边形被组合到同一网格中，就只能在两个单独的网格壳之间执行其编辑操作。

如果任何组合网格上有您希望在合并网格的[“组件标记”(Component Tags)表](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1D7D6E5A-2E20-42F7-91D2-8C18A878919A)中可用的[组件标记](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3F9B8FA5-82C0-483C-840E-86784CA4F548)，请在[节点编辑器(Node Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-23277302-6665-465F-8579-9BC734228F69)中选择 [polyUnite](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2C2EC5C2-91C2-445E-A1B3-4C226E962886) 节点，以在“属性编辑器”(Attribute Editor)中打开“polyUnite”选项卡。在此处，可以单击“添加新项目”(Add New Item)以输入要包含在组合网格的“组件标记”(Component Tags)表中的组件标记的名称。

选择“网格 > 结合”(Mesh > Combine) > ![图：选择“网格 结合”(Mesh Combine) 可设置“组合选项”(Combine Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[“组合选项”(Combine Options)](“网格”%28Mesh%29菜单/组合选项%28Combine%20Options%29.md)。

**注**

在

“构建历史”(Construction History)

处于禁用状态时使用

“网格 > 结合”(Mesh > Combine)

，以便清除多个蒙皮项目的历史记录，并形成单个干净蒙皮的网格。（在

“构建历史”(Construction History)

已关闭的情况下，您仍可以使用

“网格 > 结合”(Mesh > Combine)

。）

#### 分离(Separate)

将网格中断开的壳分离为单独的网格。可以立即分离所有壳，或者可以通过在选择网格 > 分离(Mesh > Separate)之前首先选择要分离的壳上的某些面，指定要分离的壳。

## 重新划分网格(Remesh)

#### 一致(Conform)

将一个对象的顶点折绕到另一个对象的曲面。请参见[使顶点与曲面保持一致](../../编辑多边形/变换多边形组件/使顶点与曲面保持一致.md)。

选择“网格 > 一致”(Mesh > Conform) > ![图：选择“网格 一致”(Mesh Conform) 可设置一致选项(Conform Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[一致选项(Conform Options)](“网格”%28Mesh%29菜单/一致选项%28Conform%20Options%29.md)。

#### 填充洞(Fill Hole)

您可以通过“填充洞”(Fill Hole)功能填充多边形网格中不存在多边形的区域，前提是该区域以三个或更多的多边形边为边界。“填充洞”(Fill Hole)可创建具有三个或多个边的多边形来填充选定的区域。

#### 减少(Reduce)

减少多边形网格中选定区域的多边形数，也可以在选择要减少区域的时候考虑 UV 和顶点颜色。当需要在多边形网格的特定区域减少多边形数时，“减少”(Reduce)选项将非常有用。多边形减少量将通过创建的“polyReduce 节点”(polyReduce node)进行控制。通过此功能，可以尝试不同量的融合减少，并在希望多边形网格恢复为其原始减少前状态时将所有减少完全删除。还可以保持原始顶点位置，尽可能降低因减少导致的网格整体形变。可选择使用[网格工具 > 绘制减少权重工具(Mesh Tools > Paint Reduce Weights Tool)](“网格工具”%28Mesh%20Tools%29菜单/绘制减少权重工具选项%28Paint%20Reduce%20Weights%20Tool%20Options%29.md)绘制多边形减少量。

选择“网格 > 减少”(Mesh > Reduce) > ![图：选择“网格 减少”(Mesh Reduce) 可设置“减少选项”(Reduce Options )。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[“减少选项”(Reduce Options )](“网格”%28Mesh%29菜单/减少选项%28Reduce%20Options%29.md)。

#### 平滑(Smooth)

通过向网格上的多边形添加分段来平滑选定多边形网格。

选择“网格 > 平滑”(Mesh > Smooth) > ![图：选择“网格 平滑”(Mesh Smooth) 可设置“平滑选项”(Smooth Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[“平滑选项”(Smooth Options)](“网格”%28Mesh%29菜单/平滑选项%28Smooth%20Options%29.md)。

#### 三角化(Triangulate)

将现有多边形选择转化为三角形。

#### 四边形化(Quadrangulate)

将现有多边形选择转换为四边形。

选择“网格 > 四边形化”(Mesh > Quadrangulate) > ![图：选择“网格 四边形化”(Mesh Quadrangulate) 可设置“四边形化选项”(Quadrangulate Op…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[“四边形化选项”(Quadrangulate Options)](“网格”%28Mesh%29菜单/四边形化选项%28Quadrangulate%20Options%29.md)。

#### 重新划分网格(Remesh)

![图：通过将非三角形面分割成三角形，重新定义网格或选定组件的拓扑。使用“重新划分网格”(Remesh)创建均匀细分的三角形网格…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" -->

通过将非三角形面分割成三角形，重新定义网格或选定组件的拓扑。使用“重新划分网格”(Remesh)创建均匀细分的三角形网格或将细节添加到曲面的特定区域。

选择“网格 > 重新划分网格”(Mesh > Remesh)> ![图：选择“网格 重新划分网格”(Mesh Remesh) ，以设置重新划分网格选项(Remesh Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" -->，以设置[重新划分网格选项(Remesh Options)](“网格”%28Mesh%29菜单/重新划分网格选项%28Remesh%20Options%29.md)。

#### 重新拓扑(Retopologize)

![图：生成整洁的新拓扑，保留选定网格的曲面特征，同时确保所有面都是四边形。若要取消操作，请在操作完成之前按住 Esc 键。 注…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" -->

生成整洁的新拓扑，保留选定网格的曲面特征，同时确保所有面都是四边形。若要取消操作，请在操作完成之前按住 Esc 键。

**注**

为获得最佳结果，请先尝试对几何体运行

“重新划分网格”(Remesh)

，然后再执行

“重新拓扑”(Retopologize)

。此外，如果场景文件包含 Maya 2020 之前的

polyRetopo

节点，则应先删除网格上的历史，然后再执行其他

“重新拓扑”(Retopologize)

。

选择“网格 > 重新拓扑”(Mesh > Retopologize)> ![图：选择“网格 重新拓扑”(Mesh Retopologize) ，以设置重新拓扑选项(Retopologize Optio…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" -->，以设置[重新拓扑选项(Retopologize Options)](“网格”%28Mesh%29菜单/重新拓扑选项%28Retopologize%20Options%29.md)。

## 镜像(Mirror)

#### 镜像(Mirror)

跨对称轴镜像选定对象。选择“网格 > 镜像”(Mesh > Mirror) > ![图：跨对称轴镜像选定对象。选择“网格 镜像”(Mesh Mirror) 可设置镜像选项(Mirror Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[镜像选项(Mirror Options)](“网格”%28Mesh%29菜单/镜像选项%28Mirror%20Options%29.md)。

#### 对称(Symmetrize)

如果启用了拓扑对称，“对称”(Symmetrize)将跨对称轴复制选定的网格拓扑。请参见[将不对称的组件进行对称](../../编辑多边形/对称编辑/将不对称的组件进行对称.md)。

## 传递(Transfer)

#### 剪贴板操作(Clipboard Actions)

#### 复制属性(Copy Attributes)

允许您通过将属性复制到临时剪贴板来将 UV、着色器和逐顶点颜色属性从一个多边形网格复制到另一个多边形网格。可以设定复制功能，使其复制一个属性或同时复制所有三个属性。可以在多边形网格之间复制的属性选项如下所述。

选择“网格 > 剪贴板操作 > 复制属性”(Mesh > Clipboard Actions > Copy Attributes) > ![图：选择“网格 剪贴板操作 复制属性”(Mesh Clipboard Actions Copy Attributes) 可设…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[“复制属性选项”(Copy Attributes Options)](“网格”%28Mesh%29菜单/复制属性选项%28Copy%20Attributes%20Options%29.md)。

#### 粘贴属性(Paste Attributes)

允许您将以前从另一个多边形网格复制的任何“UV”、“着色器”(shader)和逐顶点“颜色”(color)属性粘贴到临时剪贴板。可以将粘贴功能设定为粘贴一个属性，或已作为复制操作结果而复制的三个属性中的任何一个。

#### 清空剪贴板(Clear Clipboard)

“清空剪贴板”(Clear Clipboard)会清空所有保存的多边形属性的剪贴板，以便随后可以在多边形网格之间复制和粘贴新属性。

选择此菜单项时，请使用“清空剪贴板选项”(Clear Clipboard Options)来指定要清空的属性（每个顶点的“UV”、“着色器”(Shader)和“颜色”(Color)）。

#### 传递属性(Transfer Attributes)

“传递属性”(Transfer Attributes)会在具有不同拓扑的网格间传递 UV、逐顶点颜色 (CPV) 和顶点位置信息（即，网格具有不同的形状，且顶点和边都不相同）。

“传递属性”(Transfer Attributes)通过对源网格上的顶点信息进行采样来传递顶点数据，然后根据基于空间的比较将信息传递给指定的目标网格。从而实现对目标网格的修改。

选择“网格 > 传递属性”(Mesh > Transfer Attributes) > ![图：选择“网格 传递属性”(Mesh Transfer Attributes) 可设置“传递属性选项”(Transfer A…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[“传递属性选项”(Transfer Attributes Options)](“网格”%28Mesh%29菜单/传递属性选项%28Transfer%20Attributes%20Options%29.md)。

#### 传递着色集(Transfer Shading Sets)

使用“传递着色集”(Transfer Shading Sets)工具，您可以在具有不同拓扑的两个对象之间传递着色指定数据。例如，您可以将着色指定数据从立方体传递到球体。类似位置的面会被指定相同的着色数据。

选择“网格 > 传递着色集”(Mesh > Transfer Shading Sets) > ![图：选择“网格 传递着色集”(Mesh Transfer Shading Sets) 可设置“传递着色集选项”(Transf…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[“传递着色集选项”(Transfer Shading Sets Options)](“网格”%28Mesh%29菜单/传递着色集选项%28Transfer%20Shading%20Sets%20Options%29.md)。

#### 传递顶点顺序(Transfer Vertex Order)

“传递顶点顺序”(Transfer Vertex Order)可用于将顶点 ID 顺序从一个对象传递到另一个对象。有关详细信息，请参见[修改或传递顶点顺序](../../编辑多边形/修改多边形网格/修改或传递顶点顺序.md)。

## 优化

#### 清理(Cleanup)

在选择上执行各种操作，以标识和移除无关且无效的多边形几何体。

选择“网格 > 清理”(Mesh > Cleanup) > ![图：选择“网格 清理”(Mesh Cleanup) 以设置清理选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 以设置[清理选项](“网格”%28Mesh%29菜单/清理选项%28Cleanup%20Options%29.md)。

#### 平滑代理(Smooth Proxy)

#### 细分曲面代理(Subdiv Proxy)

“细分曲面代理”(Subdiv Proxy)通过添加多边形平滑选定多边形，并将原始未平滑网格作为代理。此时会在代理和平滑版本的网格之间建立节点连接，这样对代理形状或拓扑所做的更改会更新到平滑版本的网格中。在对较粗糙版本的多边形模型（需要关注的组件较少）重新定形和/或设定动画并同时查看平滑版本的外观时，“细分曲面代理”(Subdiv Proxy)非常有用。

选择“网格 > 平滑代理 > 细分曲面代理”(Mesh > Smooth Proxy > Subdiv Proxy) > ![图：选择“网格 平滑代理 细分曲面代理”(Mesh Smooth Proxy Subdiv Proxy) 可设置“细分曲面代…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[“细分曲面代理选项”(Subdiv Proxy Options)](“网格”%28Mesh%29菜单/细分曲面代理选项%28Subdiv%20Proxy%20Options%29.md)。

#### 移除细分曲面代理镜像(Remove Subdiv Proxy Mirror)

移除由“平滑代理 > 细分曲面代理”(Smooth Proxy > Subdiv Proxy)（“镜像行为”(Mirror Behavior)设置为“完全”(Full)）创建的平滑网格，并将代理网格的两半（原始网格和镜像网格）组合为单个网格（与在原始网格上使用“网格 > 镜像几何体”(Mesh > Mirror Geometry)类似）。对网格的一半进行的调整将不再自动镜像到另一半上。使用“网格 > 平滑代理 > 细分曲面代理”(Mesh > Smooth Proxy > Subdiv Proxy)（并且将“镜像行为”(Mirror Behavior)设置为“完全”(Full)）创建对称模型后，使用“细分曲面代理镜像”(Subdiv Proxy Mirror)移除平滑网格。然后使用“平滑代理 > 细分曲面代理”(Smooth Proxy > Subdiv Proxy)（并且将“镜像行为”(Mirror Behavior)设置为“无”(None)）创建通过非对称方式设置动画的平滑网格。

选择“网格 > 平滑代理 > 移除细分曲面代理镜像”(Mesh > Smooth Proxy > Remove Subdiv Proxy Mirror) > ![图：选择“网格 平滑代理 移除细分曲面代理镜像”(Mesh Smooth Proxy Remove Subdiv Proxy…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4775 字 ≥300，非承重" --> 可设置[“移除细分曲面代理镜像选项”(Remove Subdiv Proxy Mirror Options)](“网格”%28Mesh%29菜单/移除细分曲面代理镜像选项%28Remove%20Subdiv%20Proxy%20Mirror%20Options%29.md)。

#### 折痕工具(Crease Tool)

**“折痕工具”(Crease Tool)**存在于两个位置（**“网格 > 平滑代理 > 折痕工具”(Mesh > Smooth Proxy > Crease Tool)**和网格工具 > 折痕工具(Mesh Tools > Crease Tool)）。有关详细信息，请参见[使多边形的边和顶点起折痕](../../编辑多边形/修改多边形网格/为多边形边和顶点生成折痕.md)。

#### 切换代理显示(Toggle Proxy Display)

在法线多边形显示和平滑细分曲面代理版本之间切换细分曲面代理对象的显示。对多边形曲面建模并希望在任一模式之间快速切换以预览您的工作时，在细分曲面代理和法线多边形显示模式之间切换很有用。也可以使用 Ctrl + ' 热键切换此显示模式。

#### 代理和细分曲面同时显示(Both Proxy and Subdiv Display)

同时显示代理网格和细分曲面网格。还可以使用 ~ 热键控制该显示模式。
