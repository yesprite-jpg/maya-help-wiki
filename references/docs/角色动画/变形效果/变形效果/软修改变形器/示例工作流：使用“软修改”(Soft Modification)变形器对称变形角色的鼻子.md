# 示例工作流：使用“软修改”(Soft Modification)变形器对称变形角色的鼻子

该示例显示了如何使用“软修改”(Soft Modification)变形器对称修改角色脸上的鼻子。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-573A4246-2479-4D79-B585-39EBCB211A41.png) <!-- baize:img-hook downloaded=false reason="正文 351 字 ≥300，非承重" -->

1. 在角色鼻子的中心选择单一顶点。

  ![图：在角色鼻子的中心选择单一顶点。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-360C865B-E605-4C74-83F2-8AD75F7DA064.png) <!-- baize:img-hook downloaded=false reason="正文 351 字 ≥300，非承重" -->

2. 在“装备”(Rigging)菜单集中，选择“变形 > 软修改”(Deform > Soft Modification) > ![图：在“装备”(Rigging)菜单集中，选择“变形 软修改”(Deform Soft Modification) ，然后设…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 351 字 ≥300，非承重" -->，然后设置以下内容：

  - 启用“保留历史”(Preserve History)

  - 禁用“未选择遮罩”(Mask Unselected)

  - 启用“在当前选择周围衰减”(Falloff Around Selection)

  然后单击“软修改”(Soft Modification)。

  ![图：在“装备”(Rigging)菜单集中，选择“变形 软修改”(Deform Soft Modification) ，然后设…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-BC7889DE-0710-47CE-ADE1-2F3AE081A120.png) <!-- baize:img-hook downloaded=false reason="正文 351 字 ≥300，非承重" -->

3. 使用操纵器创建一个变形。

  ![图：使用操纵器创建一个变形。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-8D655BF3-5B55-49E3-95E4-E4A3C241991F.png) <!-- baize:img-hook downloaded=false reason="正文 351 字 ≥300，非承重" -->

4. 调整 [softMod](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Nodes/softMod.html) 属性（例如，“衰减半径”(Falloff Radius)、“衰减曲线”(Falloff Curve)）来以交互方式调整变形的效果（例如，将新的鼻子形状平滑地融合到脸的其余部分）。
