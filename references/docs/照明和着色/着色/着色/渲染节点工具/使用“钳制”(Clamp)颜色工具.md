# 使用“钳制”(Clamp)颜色工具

有关“钳制”(Clamp)颜色工具的描述，请参见[钳制](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-75A0D963-24A0-4DAB-8073-903734443E03.htm)。

使用“钳制”(Clamp)工具钳制颜色

1. 将一个复杂纹理（如“大理石”(Marble)）映射到材质的“颜色”(Color)。

2. 在纹理的特性编辑器中，将“钳制”(Clamp)映射到纹理的其中一个颜色。

3. 在特性编辑器中选择“钳制”(Clamp)并调整“最小值”(Min)和“最大值”(Max)属性。

  “最小值”(Min)和“最大值”(Max)这两个属性决定了显示的“红”(Red)、“绿”(Green)或“蓝”(Blue)颜色的量。

  在以下示例中，“钳制”(Clamp)节点已连接到“大理石”(Marble)纹理的“脉络颜色”(Vein Color)。由于 R 和 B 的“最小值”(Min)和“最大值”(Max)设置得比 G 的高，因此“大理石”(Marble)纹理的脉络看起来更红和更蓝。

  ![图：在特性编辑器中选择“钳制”(Clamp)并调整“最小值”(Min)和“最大值”(Max)属性。 “最小值”(Min)和“…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-7138D3C9-9268-4879-8AD0-C07BA36C6BCC.png) <!-- baize:img-hook downloaded=false reason="正文 358 字 ≥300，非承重" -->
