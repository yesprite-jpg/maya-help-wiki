# “展开 UV 工具”(Unfold UV Tool)和“优化 UV 工具”(Optimize UV Tool)

若要打开“展开 UV 工具”(Unfold UV Tool)或“优化 UV 工具”(Optimize UV Tool)，请从“UV 工具包”(UV Toolkit)中的“展开”(Unfold)部分选择它，或者从“UV 编辑器”(UV Editor)菜单中选择“工具 > 展开”(Tools > Unfold)或“工具 > 优化”(Tools > Optimize)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-12BA58C6-1468-4173-8D88-542239693089.gif) <!-- baize:img-hook downloaded=false reason="正文 787 字 ≥300，非承重" -->

使用“展开 UV 工具”(Unfold UV Tool)，可以通过交互方式展开多边形对象的 UV 网格，同时尽量确保 UV 不重叠。展开 UV 有助于优化 UV 坐标的位置以便它们更准确地反映原始多边形网格，从而最大程度地减小有机多边形网格上纹理贴图的扭曲。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-71DABCA5-FB35-4318-9B47-1EF4D3250F78.gif) <!-- baize:img-hook downloaded=false reason="正文 787 字 ≥300，非承重" -->

“优化 UV 工具”(Optimize UV Tool)用于平均分配 UV 在网格上的间距并修复扭曲的区域（重叠 UV）。

选择“工具 > 展开”(Tools > Unfold) > ![图：选择“工具 展开”(Tools Unfold) 或“工具 优化”(Tools Optimize) 时，在“工具设置”(T…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 787 字 ≥300，非承重" --> 或“工具 > 优化”(Tools > Optimize) > ![图：选择“工具 展开”(Tools Unfold) 或“工具 优化”(Tools Optimize) 时，在“工具设置”(T…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 787 字 ≥300，非承重" --> 时，在“工具设置”(Tool Settings)窗口中将显示以下选项。

## Unfold3D 笔刷选项(Unfold3DBrush Options)

#### 模式(Mode)

在“展开”(Unfold)和“优化”(Optimize)工具之间切换。

#### 笔刷大小(Brush Size)

设置工具的半径。

热键：按住 B 键并向左/向右拖动可调整笔刷大小。

#### 笔刷压力(Brush Pressure)

确定工具影响曲面的程度。

热键：按住 M 键并向上/向下拖动可调整笔刷强度。

#### 迭代次数(Iterations)

指定在展开过程完成后执行“优化”(Optimize)算法的次数（例如，值为 0 将展开网格，但不进行任何优化）。

**注**

非常高的迭代次数(Iterations)可能会产生意外的结果。

#### 曲面角度(Surface Angle)

控制曲面的强度和角度优化，从而最大限度地减少 UV 贴图中的拉伸和角度错误。默认值为 1。

**注**

此选项只有在选择了

“优化”(Optimize)

时才可用。
