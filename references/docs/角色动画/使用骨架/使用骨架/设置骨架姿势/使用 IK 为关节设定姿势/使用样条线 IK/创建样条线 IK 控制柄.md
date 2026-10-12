# 创建样条线 IK 控制柄

样条线 IK 控制柄支持使用 NURBS 曲线控制关节链。由样条线 IK 控制柄驱动的所有关节均遵循该曲线。样条线 IK 控制柄可提供附加属性（如扭曲），允许对关节链中的关节方向进行附加控制。

创建样条线 IK 控制柄并自动创建 IK 样条 NURBS 曲线

1. 选择关节链。

2. 在“装备”(Rigging)菜单集（按 F3 键）中，选择“骨架 > 创建 IK 样条线控制柄”(Skeleton > Create IK Spline Handle) > ![图：在“装备”(Rigging)菜单集（按 F3 键）中，选择“骨架 创建 IK 样条线控制柄”(Skeleton Crea…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 706 字 ≥300，非承重" -->。

3. 在显示的 [IK 样条线控制柄工具](IK%20样条线控制柄工具%28IK%20Spline%20Handle%20Tool%29.md)设置中，启用“自动创建曲线”(Auto Create Curve)。

4. 为 IK 样条曲线指定“跨度数”(Number of Spans)。

5. 单击样条线 IK 控制柄的起始关节。

6. 单击样条线 IK 控制柄的末关节。

  样条线 IK 控制柄和 NURBS 曲线出现在关节链上。

使用已存在 NURBS 曲线创建样条线 IK 控制柄

1. 沿关节链的路径绘制 NURBS 曲线。

  创建没有明晰弯曲的简单曲线以确保为该曲线设置动画时，关节链逐渐移动。

  如果使用较少的 CV 创建曲线，则对该曲线的形状和骨架的移动的控制将不太精确，但您可以更加轻松操纵曲线及其关节链。

  另请参见 [NURBS 曲线的组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3C709643-E723-4518-84B7-45EB07778AD2)。

2. 选择关节链。

3. 在“装备”(Rigging)菜单集（按 F3 键）中，选择“骨架 > 创建 IK 样条线控制柄”(Skeleton > Create IK Spline Handle) > ![图：在“装备”(Rigging)菜单集（按 F3 键）中，选择“骨架 创建 IK 样条线控制柄”(Skeleton Crea…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 706 字 ≥300，非承重" -->。

4. 在 IK 样条线控制柄工具设置中，禁用“自动创建曲线”(Auto Create Curve)。

5. 单击 *开始* 关节的样条线 IK 控制柄。

6. 单击样条线 IK 控制柄的末关节。

7. 选择 NURBS 曲线。

  样条线 IK 控制柄将出现在关节链上。链中的关节随曲线的形状旋转。

## 相关主题

- [使用样条线 IK 控制柄的提示](使用样条线%20IK%20控制柄的提示.md)

- [使用样条线 IK 曲线为关节设定姿势](使用样条线%20IK%20曲线为关节设定姿势.md)

- [样条线 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-B4EF8784-92D1-4D83-9CA5-A692D06607B8.htm)
