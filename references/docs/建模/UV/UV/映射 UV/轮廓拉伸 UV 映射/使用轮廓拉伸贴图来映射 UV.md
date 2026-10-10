# 使用轮廓拉伸贴图来映射 UV

使用轮廓拉伸贴图来映射 UV

1. 选择要向其应用轮廓拉伸贴图的多边形面。

  该选择必须具有四个可辨别的拐角（即使它不是完美的矩形）和一个清晰的轮廓。

2. 从主菜单中，选择“UV > 轮廓拉伸”(UVs > Contour Stretch) > ![图：从主菜单中，选择“UV 轮廓拉伸”(UVs Contour Stretch) （如果需要设置选项），或在“UV 编辑器”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 447 字 ≥300，非承重" -->（如果需要设置选项），或在“UV 编辑器”(UV Editor)的“UV 工具包”(UV Toolkit)中，转到“创建 > 轮廓拉伸”(Create Contour > Stretch)。

  设置显示的[轮廓拉伸贴图选项](../../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/轮廓拉伸映射选项%28Contour%20Stretch%20Mapping%20options%29.md)，然后单击“投影”(Project)。

3. 如果已启用“用户定义的角顶点”(User defined corner vertices)，则选择四个角顶点，然后按 Enter 键。

  如果禁用“用户定义的角顶点”(User defined corner vertices)，会自动检测该选择的角点。

  轮廓拉伸贴图将应用于该选择。

  **注**

  应用轮廓拉伸 UV 映射后，修改在应用它之前进行的任何拓扑更改将具有戏剧性的且通常不需要的结果。这是因为拓扑更改影响投影用来拉伸多边形选择的轮廓。

## 相关主题

- [轮廓拉伸 UV 映射](../轮廓拉伸%20UV%20映射.md)

- [轮廓拉伸贴图选项](../../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/轮廓拉伸映射选项%28Contour%20Stretch%20Mapping%20options%29.md)
