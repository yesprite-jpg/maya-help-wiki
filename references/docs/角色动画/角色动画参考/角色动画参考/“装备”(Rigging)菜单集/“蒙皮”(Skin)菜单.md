# “蒙皮”(Skin)菜单

位于“装备”(Rigging)[菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A3B6D0BD-9D3B-43AD-8BEC-65144140E915)中。

**注**

已从 Maya 中删除了刚性绑定菜单选项，以简化其他工作流。使用在

刚性蒙皮(Rigid skinning)

主题中提供的脚本命令仍可获得刚性绑定功能。您还可以使用每个顶点 1 个影响的平滑蒙皮获得刚性绑定。

## 绑定

#### 绑定蒙皮(Bind Skin)

将几何体绑定到任意变换节点或节点层次，如空组节点或定位器。例如，可以绑定多边形网格到已连接到样条线曲线 CV 的定位器节点，创建变形效果。

使用“绑定蒙皮选项”(Bind Skin Options)，可以限制影响附近蒙皮点的关节数量，并限制关节的影响范围。

若要打开并更改[绑定蒙皮选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-CF2C698A-44BB-4CA0-BCB9-DB36500DA812.htm)，请选择“蒙皮 > 绑定蒙皮”(Skin > Bind Skin) > ![图：若要打开并更改绑定蒙皮选项，请选择“蒙皮 绑定蒙皮”(Skin Bind Skin) 。 请参见绑定平滑蒙皮。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" -->。

请参见[绑定平滑蒙皮](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/绑定平滑蒙皮.md)。

#### 交互式绑定蒙皮(Interactive Bind Skin)

若要打开并更改[交互式绑定蒙皮选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-B691D8D1-7D8D-4853-86CF-D3B75E835904.htm)，请选择“蒙皮 > 交互式绑定蒙皮”(Skin > Interactive Bind Skin) > ![图：若要打开并更改交互式绑定蒙皮选项，请选择“蒙皮 交互式绑定蒙皮”(Skin Interactive Bind Skin)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" -->。

#### 取消绑定蒙皮(Unbind Skin)

绑定蒙皮后，您可能决定要修改骨架、更改绑定姿势或在蒙皮上执行进一步建模。若要执行这些操作，首先必须从骨架上取消绑定蒙皮，然后再次绑定蒙皮。

若要打开并更改[取消绑定蒙皮选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-4C4597A6-BC0F-401A-96E9-A81AD26C040E.htm)，请选择“蒙皮 > 取消绑定蒙皮”(Skin > Unbind Skin) > ![图：若要打开并更改取消绑定蒙皮选项，请选择“蒙皮 取消绑定蒙皮”(Skin Unbind Skin) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" -->。

#### 转到绑定姿势(Go to Bind Pose)

将骨架返回到其基于选定曲面而设定的绑定姿势所在的位置。请参见[绑定姿势](../../../对角色进行蒙皮/对角色进行蒙皮/绑定姿势.md)。

## 权重贴图

#### 绘制蒙皮权重(Paint Skin Weights)

使用“绘制蒙皮权重工具”(Paint Skin Weights Tool)，可以在当前平滑蒙皮上绘制权重强度值。有关使用“绘制蒙皮权重工具”(Paint Skin Weights Tool)的详细信息，请参见下列主题：

- [绘制蒙皮权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/绘制蒙皮权重.md)

- [绘制平滑蒙皮点权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮.md#GUID-EA1D1658-A32C-4136-8CA6-F7111117DECE__SECTION_EB222F99641149339F7E28CFECC695A0)

请参见 [Artisan 笔刷工具的工作方式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D0A5ACD2-8D10-4B51-ADD3-E261F9337B07)。

**注**

“绘制蒙皮权重工具”(Paint Skin Weights Tool)

禁用了反射。将

“蒙皮 > 镜像蒙皮权重”(Skin > Mirror Skin Weights)

用作反射蒙皮权重的替代方法。

选择“蒙皮 > 绘制蒙皮权重”(Skin > Paint Skin Weights) > ![图：选择“蒙皮 绘制蒙皮权重”(Skin Paint Skin Weights) 以打开绘制蒙皮权重工具。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" --> 以打开[绘制蒙皮权重工具](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-99189E9D-237F-471E-A02C-BE6593B4828B.htm)。

#### 镜像蒙皮权重(Mirror Skin Weights)

可以从一个平滑蒙皮对象到另一个平滑蒙皮对象，或者在同一平滑蒙皮对象内，镜像平滑蒙皮权重。也可以在蒙皮的选定组件上镜像蒙皮权重。

若要打开并更改[镜像蒙皮权重选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-27FE7EDB-4078-473A-B001-C9AFAB3A77A3.htm)，请选择“蒙皮 > 镜像蒙皮权重”(Skin > Mirror Skin Weights) > ![图：若要打开并更改镜像蒙皮权重选项，请选择“蒙皮 镜像蒙皮权重”(Skin Mirror Skin Weights) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" -->。

#### 复制蒙皮权重(Copy Skin Weights)

该工具可将选定源蒙皮的蒙皮权重复制到选定目标蒙皮。有关如何复制平滑蒙皮权重的信息，请参见[复制平滑蒙皮权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/复制平滑蒙皮权重.md)。请参见[复制平滑蒙皮权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮.md#GUID-EA1D1658-A32C-4136-8CA6-F7111117DECE__SECTION_AA4D48D0532747DBA1B89B9E0C7DECD2)。

**注**

提示：

为了在复制平滑蒙皮权重时获得最佳结果，请注意以下事项：

- 使用空间比较复制蒙皮权重时，应该将源蒙皮和目标蒙皮放置在场景中相同的位置。例如，复制权重的目标蒙皮网格和源蒙皮网格应该放置在相同的 X、Y、Z 坐标位置。此外，源蒙皮和目标蒙皮在大小和比例方面应该相似。例如，将平滑蒙皮权重从一个中等大小的两足动物模型复制到另一个中等大小的两足动物模型，产生的效果会比将平滑蒙皮权重从一个小型两足动物模型复制到大型两足动物模型产生的效果好得多。

- 在空间上分隔开或具有差异很大的规模和比例的角色上复制蒙皮权重时，应该使用 UV 空间关联选项。

若要打开并更改[复制蒙皮权重选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-23A76179-A77B-4595-823D-59EA028F0298.htm)，请选择“蒙皮 > 复制蒙皮权重”(Skin > Copy Skin Weights) > ![图：若要打开并更改复制蒙皮权重选项，请选择“蒙皮 复制蒙皮权重”(Skin Copy Skin Weights) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" -->。

#### 平滑蒙皮权重(Smooth Skin Weights)

平滑选定蒙皮对象的蒙皮权重。

若要打开并更改[平滑蒙皮权重选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-566A213B-6D8C-4364-982F-0C7E34307BFF.htm)，请选择“蒙皮 > 平滑蒙皮权重”(Skin > Smooth Skin Weights) > ![图：若要打开并更改平滑蒙皮权重选项，请选择“蒙皮 平滑蒙皮权重”(Skin Smooth Skin Weights) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" -->。

#### 锤式蒙皮权重(Hammer Skin Weights)

为选定顶点指定与其相邻顶点相同的权重值，从而使变形更加平滑。对于因权重导致网格上出现不需要的变形的选定顶点，这是一种快速的修复方式。请参见[修复平滑权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/修复平滑权重.md)。

#### 复制顶点权重(Copy Vertex Weights)

复制选定顶点的权重值。请参见[复制平滑蒙皮权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/复制平滑蒙皮权重.md)。

#### 粘贴顶点权重(Paste Vertex Weights)

将复制的顶点权重值粘贴到其他选定的顶点。

#### 删减小权重(Prune Small Weights)

删减当前关节的小权重。删减小权重可加快处理速度。请参见[删减次要的平滑蒙皮权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/删减次要的平滑蒙皮权重.md)。

#### 删减以下项(Prune Below)

指定权重下限，低于该值的所有小权重都将重置为 0。默认情况下，其余的蒙皮权重都归一化为增加至 1。

#### 重置默认权重(Reset Default Weights)

将选定关节的权重重置为初始默认值。请参见[将蒙皮点权重重置为默认权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/将蒙皮点权重重置为默认权重.md)。

#### 归一化权重(Normalize Weights)

（另请参见[平滑蒙皮权重归一化](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/平滑蒙皮权重归一化.md)。）

从下列选项中选择：

#### 禁用权重归一化(Disable Weight Normalization)

对当前骨架禁用平滑蒙皮权重的自动归一化。

#### 启用权重后期归一化(Enable Weight Post Normalization)

启用平滑权重的自动归一化并将“归一化权重”(Normalize Weights)模式设置为“后期”(Post)。请参见[归一化权重模式](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-2E292C8A-388A-4E77-B42D-165F1C9E1E5F.htm#GUID-2E292C8A-388A-4E77-B42D-165F1C9E1E5F__WS1A9193826455F5FF-3859B43C1215F53D0F3-74A8)(Normalize Weights mode)。

#### 启用权重归一化(Enable Weight Normalization)

为当前骨架启用平滑蒙皮权重的自动归一化。

#### 归一化权重(Normalize Weights)

调整选定骨架的权重，以使所有平滑蒙皮权重加在一起。请参见[设置归一化模式和归一化权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/设置归一化模式和归一化权重.md)。

#### 导出权重贴图(Export Weight Maps)

打开“写入映射”(Write Map)文件浏览器，以便您可以指定用于存放贴图文件的文件夹（或目录）的路径和名称。若要首先打开并更改[导出权重贴图选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-6B15F365-A53A-4518-8035-29A7CA05A2FA.htm)，请选择“蒙皮 > 导出权重贴图”(Skin > Export Weight Maps) > ![图：打开“写入映射”(Write Map)文件浏览器，以便您可以指定用于存放贴图文件的文件夹（或目录）的路径和名称。若要首先…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" -->。另请参见[导出蒙皮权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/导出权重.md)。

**注**

默认情况下，

Maya

将指定的文件夹名称置于当前项目的

sourceimages

文件夹下。

当平滑蒙皮曲面时，Maya 将在每个关节创建一个权重贴图。使用“导出权重贴图”(Export Weight Maps)菜单项，可以同时导出所有权重贴图。

#### 导入权重贴图(Import Weight Maps)

启动“导入”(Import)文件浏览器，从而可以将蒙皮权重贴图导入到场景中。请参见[导入蒙皮权重](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/导入权重.md)了解有关将权重导入另一个场景中的角色，或导入回原始角色的信息。

## 其他

#### 交互式蒙皮绑定工具(Interactive Skin Bind Tool)

可用于通过修改体积操纵器的形状和位置，快速设置选定网格的初始权重。操纵器针对网格上每个对象的影响为您提供了视觉指示。请参见[平滑蒙皮的交互式绑定](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/平滑蒙皮的交互式绑定.md)。

若要打开并更改[交互式蒙皮绑定工具](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-005CE3E3-831B-4DCE-95DE-5E255C7C83AD.htm)设置，请参见“蒙皮 > 交互式蒙皮绑定工具”(Skin > Interactive Skin Bind Tool) > ![图：若要打开并更改交互式蒙皮绑定工具设置，请参见“蒙皮 交互式蒙皮绑定工具”(Skin Interactive Skin B…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" -->。

#### 移动蒙皮关节(Move Skinned Joints)

使“移动蒙皮关节工具”(Move Skinned Joints Tool)成为当前工具。

若要打开并更改[移动蒙皮关节工具](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-27EB7E9A-A5E4-45D3-8FEA-DA52B3DF7404.htm)设置，请选择“蒙皮 > 移动蒙皮关节”(Skin > Move Skinned Joints) > ![图：若要打开并更改移动蒙皮关节工具设置，请选择“蒙皮 移动蒙皮关节”(Skin Move Skinned Joints) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" -->。

#### 将权重移动到影响(Move Weights to Influences)

将选定顶点的权重值从其当前影响移动到选定影响。

第一个选定影响将作为源影响，其他所有选定影响都作为目标。如果在“绘制蒙皮权重工具”(Paint Skin Weights Tool)或“组件编辑器”(Component Editor)中锁定了一个影响，则该影响不会接收从邻近影响移动的权重。

该菜单项也作为“绘制蒙皮权重工具”(Paint Skin Weights Tool)中的一个按钮 ![图：该菜单项也作为“绘制蒙皮权重工具”(Paint Skin Weights Tool)中的一个按钮 提供。请参见移动权重和…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-133C86A9-CDFE-4B3D-9F11-78B88A5B7D9A.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" --> 提供。请参见[移动权重](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-99189E9D-237F-471E-A02C-BE6593B4828B.htm#WS1A9193826455F5FF-4855151011E4FD543C6-3212)和[将权重移到其他影响](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/将权重移到其他影响.md)以获得更多信息。

#### 编辑影响(Edit Influences)

打开[“编辑影响”(Edit Influences)菜单](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-9B2EF2CB-25AF-431D-8A53-62311A08B9ED.htm)。

#### 替换几何体(Substitute Geometry)

使用“替换几何体”(Substitute Geometry)，可将一个未绑定的几何体与您角色的已绑定几何体交换，并将所有平滑蒙皮权重都传递给它。另请参见[将绑定几何体替换为未绑定的几何体](../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/将绑定几何体替换为未绑定的几何体.md)。

若要打开并更改[替换几何体选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E9069302-F010-41E0-986A-27BF11BB1C57.htm)，请选择“蒙皮 > 替换几何体”(Skin > Substitute Geometry) > ![图：若要打开并更改替换几何体选项，请选择“蒙皮 替换几何体”(Skin Substitute Geometry) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3591 字 ≥300，非承重" -->。

#### 烘焙变形到蒙皮权重(Bake Deformation to Skin Weights)

打开“烘焙变形器工具”(Bake Deformer Tool)，用于从任意变形器创建变形，以便将复杂装备导出到具有有限变形器支持的应用程序。它允许 Maya 使用计算“更智能的”权重值的方法（而非其他绑定方法）将网格绑定到骨架。有关窗口中各选项的描述，请参见[烘焙变形器工具(Bake Deformer Tool)](../../../变形效果/变形效果/变形器参考/变形器工具/烘焙变形器工具%28Bake%20Deformer%20Tool%29.md)。
