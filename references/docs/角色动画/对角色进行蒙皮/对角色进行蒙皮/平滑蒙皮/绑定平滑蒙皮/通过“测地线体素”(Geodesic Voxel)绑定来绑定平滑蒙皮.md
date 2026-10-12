# 通过“测地线体素”(Geodesic Voxel)绑定来绑定平滑蒙皮

“测地线体素”(Geodesic Voxel)绑定方法允许您选择多个网格，将所有形状均视作单一体积并在整个几何体中提供连续权重。请参见[测地线体素绑定](../“测地线体素”%28Geodesic%20Voxel%29绑定.md)。

**注**

为了有效地使用，

“测地线体素”(Geodesic Voxel)

绑定需要满足两个要求。与其他 Maya 绑定方法不同，

“测地线体素”(Geodesic Voxel)

绑定要求所有关节影响均包含在网格体积内。如果未执行此操作，Maya 无法正确计算测地线距离。此外，几何体正面的法线应指向反向。如果在视口中启用背面消隐，并直观地检查结果，就可以检查该要求。

若要使用基于体素的方法设定初始权重和绑定几何体，请执行以下操作：

1. 选择要绑定的关节和网格，然后选择“蒙皮 > 绑定蒙皮”(Skin > Bind Skin) > ![图：选择要绑定的关节和网格，然后选择“蒙皮 绑定蒙皮”(Skin Bind Skin) 。此时将打开“绑定蒙皮选项”(Bin…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 578 字 ≥300，非承重" -->。此时将打开[“绑定蒙皮选项”(Bind Skin Options)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-CF2C698A-44BB-4CA0-BCB9-DB36500DA812.htm)窗口。

2. 将“绑定方法”(Bind Method)设定为“测地线体素”(Geodesic Voxel)。

3. 设置[“衰减”(Falloff)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-CF2C698A-44BB-4CA0-BCB9-DB36500DA812.htm#GUID-CF2C698A-44BB-4CA0-BCB9-DB36500DA812__GUID-01FCCA00-B64B-44C9-A842-7DD77790C352)速率以控制应用到几何体的绑定的刚性程度。

  值 1 可创建更加刚性的绑定，而值 0 会生成更加平滑的绑定。

4. 指定[分辨率(Resolution)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-CF2C698A-44BB-4CA0-BCB9-DB36500DA812.htm#GUID-CF2C698A-44BB-4CA0-BCB9-DB36500DA812__GUID-C57B5D47-B990-4D8D-984F-DD8AF9A18513)以增加绑定的精度。

  分辨率越高，精度就越细，但处理时间也会越长。

5. 单击“绑定蒙皮”(Bind Skin)。

  **注**

  如果网格包含严重

  退化几何体

  ，则

  “测地线体素”(Geodesic Voxel)

  绑定方法可能会出现问题。
