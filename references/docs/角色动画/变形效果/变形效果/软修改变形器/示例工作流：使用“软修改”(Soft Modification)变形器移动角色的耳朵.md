# 示例工作流：使用“软修改”(Soft Modification)变形器移动角色的耳朵

该示例显示了如何移动角色的耳朵，使耳朵周围的蒙皮发生调整以适应耳朵的新位置。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-B02A0994-CC30-42A6-8917-0BC6D9A6C73F.png) <!-- baize:img-hook downloaded=false reason="正文 387 字 ≥300，非承重" -->

1. 选择要移动的耳朵顶点和周围蒙皮。请确保选择头部两侧的耳朵顶点，以便使变形对称。

  （选择周围的区域将发生变形，使移动的顶点自然融合到周围区域中。）

  ![图：选择要移动的耳朵顶点和周围蒙皮。请确保选择头部两侧的耳朵顶点，以便使变形对称。 （选择周围的区域将发生变形，使移动的顶点…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-36A67EA3-13B4-4040-92CE-BAF117E6DDA2.png) <!-- baize:img-hook downloaded=false reason="正文 387 字 ≥300，非承重" -->

2. 在“装备”(Rigging)菜单集中，选择“变形 > 软修改”(Deform > Soft Modification) > ![图：在“装备”(Rigging)菜单集中，选择“变形 软修改”(Deform Soft Modification) ，然后设…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 387 字 ≥300，非承重" -->，然后设置以下内容：

  - 启用“保留历史”(Preserve History)

  - 禁用“未选择遮罩”(Mask Unselected)

  - 启用“在当前选择周围衰减”(Falloff Around Selection)

  然后单击“软修改”(Soft Modification)。

3. 使用操纵器移动耳朵（例如，向上）。

  ![图：使用操纵器移动耳朵（例如，向上）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-B0E88855-F2BA-4EFE-97FF-D878DF785D5D.png) <!-- baize:img-hook downloaded=false reason="正文 387 字 ≥300，非承重" -->

4. 调整 [softMod](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Nodes/softMod.html) 属性（例如，“衰减半径”(Falloff Radius)、“衰减曲线”(Falloff Curve)）以交互式调整新耳朵位置融合到周围蒙皮中的方式。
