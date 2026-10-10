# 对光束应用“挡光板”(barn doors)（快门）

如果要创建光穿透半开的门的效果，可应用挡光板。“挡光板”(Barn Doors)是应用于聚光灯光束的快门。“挡光板”(Barn Doors)在默认情况下禁用；必须将其启用并进行调整，才能获得所需的散射光。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A214536E-982F-4BBF-96D6-DE68DDB41046.png) <!-- baize:img-hook downloaded=false reason="正文 938 字 ≥300，非承重" -->

使用“挡光板”(Barn Doors)

1. 选择已显示其操纵器的聚光灯，然后在“属性编辑器”(Attribute Editor)中启用“挡光板”(Barn Doors)。

2. 在聚光灯的“属性编辑器”(Attribute Editor)的“灯光效果”(Light Effects)区域，启用“挡光板”(Barn Doors)。

3. 从视图的“面板”(Panels)菜单中选择“沿选定对象观看”(Look Through Selected)，以沿选定灯光观看。（“挡光板”(Barn Doors)操纵器仅在灯光的视图中可见。）

  将显示四条蓝线。这些线表示聚光灯的矩形边界。没有灯光到达蓝线边界之外的区域。

  ![图：从视图的“面板”(Panels)菜单中选择“沿选定对象观看”(Look Through Selected)，以沿选定灯光…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-21B0A5D2-8CC9-4C6D-8AB9-770E148C5917.png) <!-- baize:img-hook downloaded=false reason="正文 938 字 ≥300，非承重" -->

4. 可以用“移动工具”(Move tool)直接操纵四条线中的每条线来移动边界。（或者，也可以在“属性编辑器”(Attribute Editor)中输入精确数值。）

  将从聚光灯到蓝线边界以度为单位测量属性。例如，对于 80 度的聚光灯，如果边界恰好位于聚光灯边框上，则四条蓝线边界为 40。

  在使用“挡光板”(Barn Doors)设置时，灯光形状采样将在“属性编辑器”(Attribute Editor)顶部发生更改。

  ![图：可以用“移动工具”(Move tool)直接操纵四条线中的每条线来移动边界。（或者，也可以在“属性编辑器”(Attrib…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-7D36086D-03BF-4420-BF06-770C29F3B7B2.png) <!-- baize:img-hook downloaded=false reason="正文 938 字 ≥300，非承重" -->

5. 调整半影值将显示第二个圆。在“属性编辑器”(Attribute Editor)中更改该值或单击“索引操纵器”(Index Manipulator)图标以显示和使用操纵器，然后选择“面板 > 沿选定对象观看”(Panels > Look Through Selected)以查看该圆。

  两个圆之间的区域会产生较柔和的照明。

  ![图：调整半影值将显示第二个圆。在“属性编辑器”(Attribute Editor)中更改该值或单击“索引操纵器”(Index…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A12695C9-105D-4C2F-BF89-7BA5CD65C021.png) <!-- baize:img-hook downloaded=false reason="正文 938 字 ≥300，非承重" -->

6. 如果将半影值设定为 0（默认值）并启用“挡光板”(Barn Doors)，则会产生边缘非常清晰的照明。半影值为非零时，挡光板效果是平滑的场景照明。

  也可以通过在聚光灯的“属性编辑器”(Attribute Editor)顶部查看“灯光形状”(Light Shape)和“强度示例”(Intensity Sample)来验证照明。在更改聚光灯的值时，这些会发生更改。

  ![图：如果将半影值设定为 0（默认值）并启用“挡光板”(Barn Doors)，则会产生边缘非常清晰的照明。半影值为非零时，挡…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-F2078996-0FCF-41CA-9B90-D38D25008AF0.png) <!-- baize:img-hook downloaded=false reason="正文 938 字 ≥300，非承重" -->

7. 若要返回当前视图，请从“面板”(Panel)菜单中选择该视图。
