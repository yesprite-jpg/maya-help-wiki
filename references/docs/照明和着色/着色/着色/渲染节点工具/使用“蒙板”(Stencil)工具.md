# 使用“蒙板”(Stencil)工具

有关“蒙板”(Stencil)工具的描述，请参见[蒙板](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-783942EF-DD42-49FD-9076-805CF9BB2BF0.htm)。

将“蒙板”(Stencil)映射到对象

1. 在材质的“属性编辑器”(Attribute Editor)中，将“蒙板”(Stencil)工具映射到“颜色”(Color)属性。

2. 在“蒙板”(Stencil)的“属性编辑器”(Attribute Editor)中，将 2D 纹理映射到“图像”(Image)属性。

3. 将材质指定给对象，并在必要时调整“蒙板”(Stencil)属性。

  **注**

  提示：

  IPR 渲染以在调整属性时查看结果。

使用“关键帧遮罩”(Key Masking)属性

1. 启用“关键帧遮罩”(Key Masking)。由于“颜色关键帧”(Color Key)属性的默认颜色为黑色和“蒙板”(Stencil)的“默认颜色”(Default Color)，因此 Maya 仅遮罩出包含大部分黑色的区域。

  ![图：启用“关键帧遮罩”(Key Masking)。由于“颜色关键帧”(Color Key)属性的默认颜色为黑色和“蒙板”(S…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-3ACA282E-070C-407D-B290-8701CB0C535E.png) <!-- baize:img-hook downloaded=false reason="正文 545 字 ≥300，非承重" -->

2. 在“颜色选择器”(Color Chooser)中更改“颜色关键帧”(Color Key)。在以下示例中，Maya 遮罩了包含红色或粉红色的所有颜色，将其替换为“蒙板”(Stencil)的“颜色平衡”(Color Balance)默认颜色。

  ![图：在“颜色选择器”(Color Chooser)中更改“颜色关键帧”(Color Key)。在以下示例中，Maya 遮罩了…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-EEA65C60-C52B-4AB6-962F-E2FD7C935D71.png) <!-- baize:img-hook downloaded=false reason="正文 545 字 ≥300，非承重" -->

  **注**

  当凹凸映射“蒙板”(Stencil)纹理时，必须进行手动的显式连接。凹凸贴图纹理，然后将“bumpValue”手动连接到蒙板“outAlpha”。
