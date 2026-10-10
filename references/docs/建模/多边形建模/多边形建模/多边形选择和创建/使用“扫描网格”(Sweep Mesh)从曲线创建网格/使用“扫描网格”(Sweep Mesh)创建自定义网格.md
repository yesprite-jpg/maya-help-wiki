# 使用“扫描网格”(Sweep Mesh)创建自定义网格

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 790 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-E969DC25-346E-4BF2-8020-7940D8163C77.gif) <!-- baize:img-hook downloaded=false reason="正文 790 字 ≥300，非承重" -->

可以使用自己的剖面创建网格，而不是[使用“扫描网格”(Sweep Mesh)从曲线创建网格](../使用“扫描网格”%28Sweep%20Mesh%29从曲线创建网格.md)中的默认剖面，但过程略有不同。

有关自定义扫描网格工作流示例，请参见[扫描网格示例工作流：框架](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-374194A8-C9FE-4B69-BA63-82E073D4482F)。

使用“扫描网格”(Sweep Mesh)创建自定义网格

1. 创建球体。（创建 > 多边形基本体 > 球体(Create > Polygon Primitives > Sphere)）

2. 创建曲线路径。

3. 在曲线仍处于选定状态的情况下，从“多边形建模”(Poly Modeling)工具架中选择“扫描网格”(Sweep Mesh) ![图：在曲线仍处于选定状态的情况下，从“多边形建模”(Poly Modeling)工具架中选择“扫描网格”(Sweep Mes…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-DC8543C9-FAAD-453D-9063-8EAD87CC1BD1.png) <!-- baize:img-hook downloaded=false reason="正文 790 字 ≥300，非承重" -->，或者从菜单栏中选择“创建 > 扫描网格”(Create > Sweep Mesh)。

4. 在[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED) 的“sweepMeshCreator1”选项卡中，从**“扫描剖面”(Sweep Profiles)**中选择**“自定义”(Custom)** ![图：在属性编辑器(Attribute Editor) 的“sweepMeshCreator1”选项卡中，从“扫描剖面”(Sw…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-11C0BD86-CFEA-4F27-952B-F65FA54EF974.png) <!-- baize:img-hook downloaded=false reason="正文 790 字 ≥300，非承重" -->。此时将显示“自定义扫描剖面”(Custom Sweep Profile)对话框。

  ![图：在属性编辑器(Attribute Editor) 的“sweepMeshCreator1”选项卡中，从“扫描剖面”(Sw…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-2AD15CE0-9A65-4852-B922-DA1C9195B4F5.png) <!-- baize:img-hook downloaded=false reason="正文 790 字 ≥300，非承重" -->

5. 在“自定义扫描剖面”(Custom Sweep Profile)对话框中，将**“类型”(Type)**设置为**“多边形面”(Poly Face)**，然后在球体上选择一个面。该面将沿曲线扫描。

  在[“扫描网格”(Sweep Mesh)选项](../../多边形建模参考/多边形建模工具/“扫描网格”%28Sweep%20Mesh%29工具/“扫描网格”%28Sweep%20Mesh%29选项.md)中调整设置。

6. 单击“确定”(OK)将所选内容设置为自定义剖面。

  **注**

  提示：

  平坦或平面形状效果最佳；像球体或圆环这样的体积形状不能用作“多边形对象”(Poly Object)自定义剖面。只要总的来说是平坦的，曲线就可以在任何方向上起作用。

**注**

提示：

若要从多条曲线创建自定义网格，请先对曲线进行分组选择，然后选择

“创建 > 扫描网格”(Create > Sweep Mesh) > ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 790 字 ≥300，非承重" -->

，再从显示的

“扫描网格选项”(Sweep Mesh Options)

窗口中选择

“每条曲线对应一个节点”(One node for each curve)

。有关多条曲线的步骤，请参见

使用“扫描网格”(Sweep Mesh)从曲线创建网格

。
