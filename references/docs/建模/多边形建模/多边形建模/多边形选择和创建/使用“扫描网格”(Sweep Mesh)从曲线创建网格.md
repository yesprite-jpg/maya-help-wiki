# 使用“扫描网格”(Sweep Mesh)从曲线创建网格

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 1251 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-CCCE6953-1CBB-48CE-BF21-E41F40112F2A.gif) <!-- baize:img-hook downloaded=false reason="正文 1251 字 ≥300，非承重" -->

使用“扫描网格”(Sweep Mesh)工具可以基于直线或简单曲线创建多边形网格。

基于曲线创建网格

1. 创建曲线。 （在[“创建”(Create)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-AF592D59-02CB-4B97-9C57-37795C8B1D8A)菜单中选择**“曲线工具”(Curves Tools)**，或使用“曲线/曲面”(Curves / Surfaces)工具架）。

2. 选择曲线后，从“多边形建模”(Poly Modeling)工具架中选择“扫描网格”(Sweep Mesh)，或者选择“创建 > 扫描网格”(Create > Sweep Mesh)。

  ![图：选择曲线后，从“多边形建模”(Poly Modeling)工具架中选择“扫描网格”(Sweep Mesh)，或者选择“创…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-18DA4D59-01A7-48A4-AF9B-CD8292AED473.png) <!-- baize:img-hook downloaded=false reason="正文 1251 字 ≥300，非承重" -->

  “多边形建模”(Poly Modeling)工具架中的“扫描网格”(Sweep Mesh)

  将使用默认的“多边形”(Poly)扫描剖面，从曲线路径创建网格。也会创建 [sweepMeshCreator 输入节点](../多边形建模参考/多边形节点/sweepMeshCreator.md)。

3. 从扫描剖面中选择形状。

  ![图：从扫描剖面中选择形状。 注： 如果选择“自定义”(Custom)，请参见使用“扫描网格”(Sweep Mesh)创建自定…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-0D8DECD5-9B46-4B74-A1B3-F0D6B5E8644C.png) <!-- baize:img-hook downloaded=false reason="正文 1251 字 ≥300，非承重" -->

  **注**

  如果选择

  “自定义”(Custom)

  ，请参见

  使用“扫描网格”(Sweep Mesh)创建自定义网格

  的过程。

4. 使用[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)中**“sweepMeshCreator”选项卡**下的[“扫描网格”(Sweep Mesh)选项](../多边形建模参考/多边形建模工具/“扫描网格”%28Sweep%20Mesh%29工具/“扫描网格”%28Sweep%20Mesh%29选项.md)修改曲线网格。

5. 有关其中每个选项的说明，请参见[“扫描网格”(Sweep Mesh)选项](../多边形建模参考/多边形建模工具/“扫描网格”%28Sweep%20Mesh%29工具/“扫描网格”%28Sweep%20Mesh%29选项.md)。

从多条曲线创建网格

如果要将“扫描网格”(Sweep Mesh)应用于**多条曲线**，但要单独处理每条曲线（例如，在头发卡片中），请按照以下步骤操作：

1. 创建多条曲线后，将其全部选中。

2. 选择“创建 > 扫描网格”(Create > Sweep Mesh) > ![图：选择“创建 扫描网格”(Create Sweep Mesh) 。 此时将出现一个窗口，询问您是要为一条曲线还是多条曲线创…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1251 字 ≥300，非承重" -->。 此时将出现一个窗口，询问您是要为一条曲线还是多条曲线创建节点。

  ![图：选择“创建 扫描网格”(Create Sweep Mesh) 。 此时将出现一个窗口，询问您是要为一条曲线还是多条曲线创…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-0CB95F95-387D-467E-96FA-05DB3DAA1141.gif) <!-- baize:img-hook downloaded=false reason="正文 1251 字 ≥300，非承重" -->

3. 选择**“每条曲线对应一个节点”(One node for each curves)**，以便选定曲线由单独的节点控制（即，可以将“扫描网格”(Sweep Mesh)设置应用于选定组中的各条曲线）。

  **注**

  在“属性编辑器”(Attribute Editor)中，将为每条曲线创建

  SweepMeshCreator

  <

  **x**

  >（其中

  x

  是曲线名称或编号）选项卡。还会为每条曲线创建

  sweepMeshCreator 输入节点

  。

3. 使用默认的“多边形”(Poly)扫描剖面均匀创建网格。

4. 使用[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)中相应**“sweepMeshCreator”选项卡**下的[“扫描网格”(Sweep Mesh)选项](../多边形建模参考/多边形建模工具/“扫描网格”%28Sweep%20Mesh%29工具/“扫描网格”%28Sweep%20Mesh%29选项.md)，分别选择每条曲线以修改曲线网格。

  有关其中每个选项的说明，请参见[“扫描网格”(Sweep Mesh)选项](../多边形建模参考/多边形建模工具/“扫描网格”%28Sweep%20Mesh%29工具/“扫描网格”%28Sweep%20Mesh%29选项.md)。

  **注**

  如果选择

  “自定义”(Custom)

  ，请参见

  使用“扫描网格”(Sweep Mesh)创建自定义网格

  的过程。

不使用曲线创建网格

在[创建(Create)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-AF592D59-02CB-4B97-9C57-37795C8B1D8A)菜单中选择“创建 > 扫描网格”(Create > Sweep Mesh)，或使用“曲线/曲面”(Curves / Surfaces)工具架。使用默认设置时，基于直线创建网格。使用[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)中**“sweepMeshCreator”选项卡**下的[“扫描网格”(Sweep Mesh)选项](../多边形建模参考/多边形建模工具/“扫描网格”%28Sweep%20Mesh%29工具/“扫描网格”%28Sweep%20Mesh%29选项.md)修改曲线网格。

请参见[扫描网格示例工作流：开瓶器](使用“扫描网格”%28Sweep%20Mesh%29从曲线创建网格/扫描网格示例工作流：开瓶器.md)、[扫描网格示例工作流：框架](使用“扫描网格”%28Sweep%20Mesh%29从曲线创建网格/扫描网格示例工作流：框架.md)和[扫描网格示例工作流：动画曲线](使用“扫描网格”%28Sweep%20Mesh%29从曲线创建网格/扫描网格示例工作流：动画曲线.md)，了解一些示例项目。
