# 角色映射器(Character Mapper)

- 关键帧 > 角色映射器(Key > Character Mapper)（从“动画”(Animation)菜单集中）。

使用“角色映射器”(Character Mapper)窗口，可以将动画从一个角色（源）映射到另一个（目标）角色。使用“角色映射器”(Character Mapper)可在源角色和目标角色的节点或属性之间建立关系，使您能够在“Trax 编辑器”(Trax Editor)中已映射的角色之间导入和导出或复制和粘贴动画片段。

可以使用四种不同的方式查看“角色映射器”(Character Mapper)中角色的已映射和未映射节点或属性：“按字母顺序”(Alphabetical)、“层次”(Hierarchical)、“显示节点名称”(Display Node Names)和“显示通道名称”(Display Channel Names)视图。请参见[显示菜单](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-20015023-4D8F-4D09-8F82-15D3A80A1554.htm#WS17956D7ADBC6E736D9592B5117AE30E3AC-7FFD)。这些视图有助于更好地导航长节点或属性列表（“层次”或“按字母顺序”视图），并隔离特定节点（显示节点名称(Display Node Names)视图）或动画通道（“显示通道名称”(Display Channel Names)视图）。

如果需要将动画从一个类似的角色映射到另一个角色，则最好使用“角色映射器”(Character Mapper)。例如，将动画从一个两足动物角色的 translateX 通道映射到另一个两足动物角色的 translateZ 通道。

## “显示”(Show)菜单

#### 按字母顺序(Alphabetical)

从 A 开始，按字母顺序在“已映射”(Mapped)和“未映射”(Unmapped)列中列出节点或属性。

#### 层次(Hierarchical)

按层次关系在“已映射”(Mapped)和“未映射”(Unmapped)列中列出节点或属性。这意味着节点或属性将从根开始，按父子顺序显示。默认情况下，此选项处于启用状态。

#### 显示节点名称(Display Node Names)

在“已映射”(Mapped)和“未映射”(Unmapped)列中显示所有角色集的节点。使用该选项，可以将动画从源角色节点映射到目标角色节点。节点视图的格式如下所示：

SourceJoint -----> TargetJoint

#### 显示通道名称(Display Channel Names)

在“已映射”(Mapped)和“未映射”(Unmapped)列中显示所有角色集的可设定关键帧通道。如果需要将动画从特定的源角色通道映射到特定的目标角色通道，请使用该选项。例如，如果需要将源角色左肩的 X 旋转通道中的动画映射到目标角色左肩的 Z 旋转通道，请使用该选项。通道视图的格式如下所示：

SourceNode.SourceChannel -----> TargetNode.TargetChannel

## “编辑”(Edit)菜单

#### 取消映射(Unmap)

断开“已映射”(Mapped)列中选定的节点或属性对之间的链接。

#### 全部取消映射(Unmap All)

断开当前已在“角色映射器”(Character Mapper)中加载的源角色和目标角色的节点或属性之间的所有链接。源角色和目标角色的节点或属性之间的这些链接或关系将显示在“已映射”(Mapped)列中。

#### 清除全部(Clear All)

清除“未映射”(Unmapped)和“已映射”(Mapped)列的当前内容。

#### 刷新(Refresh)

“刷新”(Refreshes)“已映射”(Mapped)和“未映射”(Unmapped)列，以显示最新（当前）的内容版本。

#### 根据节点名称映射(Map based on node names)

根据节点或属性名称映射源角色和目标角色。如果源角色和目标角色的节点或属性名称相同，请选择该菜单项。例如：

lshoulder -----> lshoulder

lelbow -----> lelbow

lhand -----> lhand

#### 根据层次映射(Map based on hierarchy)

根据层次结构映射源角色和目标角色。如果需要自动映射角色中的不同节点层次，请选择该菜单项。

可以使用以下两种方式根据源角色和目标角色的层次映射动画：

- 可以自动映射源角色和目标角色的所有节点和属性。如果在“未映射”(Unmapped)列中未选择任何节点或属性，则“角色映射器”(Character Mapper)将搜索源角色和目标角色的根，并且稍后将相应地穿越和映射其层次。

- 您可以自动映射角色层次的指定分段的节点或属性（例如，肢体到肢体）。通过在分段层次的顶部选择单个源以及单个目标的节点或属性，您可以指定要映射的分段。“角色映射器”(Character Mapper)将根据选定的节点或属性向下映射每个角色层次的分段。

请参见[将一个角色映射到另一个角色](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-47CB74C4-4031-4A99-BB06-65D0D148FFC4.htm)。

#### 根据顺序映射(Map based on order)

根据节点或属性的层次顺序（降序）映射源角色和目标角色。如果源角色和目标角色的节点或属性具有相同的基本层次，请选择该菜单项。例如：

joint3 -----> 3joint

joint2 -----> 2joint

joint1 -----> 1joint

## 字段

#### 来自:(From:)

显示源角色的名称。源角色集包含重映射到目标角色集的骨架的动画数据。

#### 至:(To:)

显示目标角色的名称。目标角色集的骨架将接收源角色集中重映射的动画数据。

## 按钮

#### “加载源”(Load Source)按钮

将所有节点或属性名称从选定的角色加载到左侧（源）列。

#### “加载目标”(Load Target)按钮

将所有节点或属性名称从选定的角色加载到右侧（目标）列。

#### 映射按钮

在选定的源节点或属性（左侧“未映射”(Unmapped)列）到目标节点或属性（右侧“未映射”(Unmapped)列）的动画之间创建对应关系。例如，如果需要将源角色的 node1 映射到目标角色的 node2，则该节点对或关系将按以下方式出现在“已映射”(Mapped)列中：

node1 -----> node2

#### “关闭”(Close)按钮

关闭“角色映射器”(Character Mapper)窗口。

## 列

#### “已映射”(Mapped)列

显示源角色集和目标角色集之间的所有节点或属性关系。通过在源（左侧）和目标（右侧）“未映射”(Unmapped)列中单击节点或属性、以此将它们链接在一起之后，链接对将出现在“已映射”(Mapped)列中。

#### “未映射”(Unmapped)列

左侧“未映射”(Unmapped)列将列出源角色集骨架中的所有节点或属性，右侧“未映射”(Unmapped)列则将列出目标角色集骨架中的所有节点或属性。若要链接节点或属性对，请参见[将一个角色映射到另一个角色](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-47CB74C4-4031-4A99-BB06-65D0D148FFC4.htm)。
