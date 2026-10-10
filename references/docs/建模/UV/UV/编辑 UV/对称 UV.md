# 对称 UV

处理对称网格或特定区域中存在对称特性的网格时，可以使用[对称 UV 工具](../UV%20参考/UV%20工具/对称%20UV%20工具%28Symmetrize%20UV%20Tool%29.md)沿 U 轴或 V 轴镜像对应组件。这样，您可以快速将在网格一侧生成的组件布局与另一侧相匹配，甚至是整理整个 UV 布局来简化纹理映射。

**注**

对称 UV 工具

不能创建新的 UV。由于它使用几何体的总体对称进行引导，因此只能处理现有 UV。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-248E77C1-0D75-45F0-8523-DB49FB2253B2.gif) <!-- baize:img-hook downloaded=false reason="正文 597 字 ≥300，非承重" -->

使 UV 网格上的组件对称

1. 在“UV 编辑器”(UV Editor)中，预先排布要沿 U 向线或 V 向线（不一定要是中心线）用作对称基础的网格区域。

2. 通过转到“工具 > 对称”(Tools > Symmetrize)，或者通过“UV 工具包”(UV Toolkit)的“变换 > 工具 > 对称”(Transform > Tools > Symmetrize)，选择“对称 UV 工具”(Symmetrize UV Tool)。

3. 单击网格上的某条边以定义拓扑对称线。

4. 根据需要调整笔刷设置。特别地，请确保通过调整相应属性或在“UV 编辑器”(UV Editor)窗口中使用鼠标中键拖动粗体轴来设置“镜像轴位置”(Mirror Axis Position)，使其正确表示 UV 空间中要沿其镜像组件的线。

5. 沿网格的一侧进行绘制以使其组件对称。

或者，您可以先选择 UV，然后使用“修改 > 对称”(Modify > Symmetrize)命令或“UV 工具包”(UV Toolkit)中的“对称”(Symmetrize)图标 (![图：或者，您可以先选择 UV，然后使用“修改 对称”(Modify Symmetrize)命令或“UV 工具包”(UV To…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4BA930E5-89E6-4365-BF02-C16CB4471511.png) <!-- baize:img-hook downloaded=false reason="正文 597 字 ≥300，非承重" -->) 一次性将其全部对称（系统仍会提示您选择网格上的对称边）。

## 相关主题

- [对称 UV 工具](../UV%20参考/UV%20工具/对称%20UV%20工具%28Symmetrize%20UV%20Tool%29.md)
