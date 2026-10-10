# “发送到 Mudbox”(Send to Mudbox)相关问题疑难解答

## 文件(File)菜单中缺少发送到 Mudbox (Send to Mudbox)

仅当具有 Maya 和 Mudbox 的匹配版本时，“发送到 Mudbox”(Send to Mudbox)才在“文件”(File)菜单中可用。（Maya 2016 和 Mudbox 2016 是匹配版本。）

如果安装了相应的 Mudbox 版本，但是“文件”(File)菜单中缺少“发送到 Mudbox”(Send to Mudbox)，请检查并确保已使用“插件管理器”(Plug-in Manager)（“窗口 > 设置/首选项 > 插件管理器”(Window > Settings/Preferences > Plug-in Manager)）加载 OneClick.mll 插件。

## 在导入的网格中检测到问题

某些情况下，当您从 Maya 发送对象时，Mudbox 会检测到网格存在问题。当您发送网格时可能会显示以下任一警告。

- 高边价顶点(High-valence vertex)

- UV 面与平铺边界交叉(UV Faces Crossing Tile Boundaries)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-E834D83B-AD05-48B5-8CA9-4E7D0A048584.png) <!-- baize:img-hook downloaded=false reason="正文 793 字 ≥300，非承重" -->

在 Maya 中，这两个问题都可以进行更正。

更正“高边价顶点”(High-valence vertex)问题

**注**

该问题通常与球形对象关联。

1. 在 Maya 中选择对象。

2. 打开[属性编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)并为多边形对象选择“历史”(History)选项卡。

3. 将“轴向细分数”(Subdivisions Axis)和“高度细分数”(Subdivisions Height)的值更改为 15。

更正“UV 面与平铺边界交叉”(UV Faces Crossing Tile Boundaries)问题

1. 打开 [UV 纹理编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-73BF7546-3BF2-44F3-9192-15A024CEC173)并选择“移动 UV 壳”(Move UV Shell)工具。

2. 减小对象的大小，使其不会接触到 UV 壳边界。

**注**

Mudbox 中不支持同一网格上存在多种材质。如果将具有多种材质的网格从

Maya

发送到 Mudbox，则只有应用于网格的第一个面 (ID 0) 的材质才会显示在 Mudbox 中。
