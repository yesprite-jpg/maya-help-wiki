# 使用多个 UV 集在硬件渲染器中显示分层纹理

可以在硬件渲染器中显示分层纹理并为每个不同的纹理创建多个 UV 集。这样可以根据需要在场景中定位纹理。

## 在硬件渲染器中显示分层纹理

该功能可与“Blinn”、“Lambert”“Phong”和“Phong E”着色器结合使用，并可用于*“最多两个层”(up to two layers)*（当分层纹理连接到着色器上的“颜色”(Color)属性时）。

在分层纹理的每层中，可以选择应用任何 2D 纹理，或者“环境球”(Env Ball)纹理或“环境立方体”(Env cube)纹理。该功能仅支持 2D“法线”(Normal)贴图方法。投影贴图和蒙板贴图方法不受支持。

若要显示分层纹理，可以在多个融合模式中选择，例如，“覆盖”(Over)、“相加”(Add)或“相乘”(Multiply)。下拉列表中的所有融合模式均受支持。有关融合模式的详细信息，请参见[融合模式](../../../../着色引用/着色节点/纹理节点概述/分层纹理%28Layered%20texture%29.md#WS17956D7ADBC6E73638876AF8117AE33FA94-7F39)。

使用 “Alpha” 属性可以调整两个层之间的 Alpha 融合。

[该功能支持Alpha 为亮度](../../../../着色引用/着色节点/纹理节点概述/分层纹理%28Layered%20texture%29.md#WS73099CC142F48755-3D114B7511812357EFE-5FE7)。启用该属性，以使 Alpha 为“输出颜色”(Out Color)的亮度。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-64280537-5AF8-4645-9370-0D049D9928EF.png) <!-- baize:img-hook downloaded=false reason="正文 906 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B73FCB37-8865-4760-A839-917BB996A096.png) <!-- baize:img-hook downloaded=false reason="正文 906 字 ≥300，非承重" -->

## 支持不同纹理使用多个 UV 集

现在，可以对场景中的不同纹理使用多个 UV 集。这允许每个纹理使用不同放置。可以使用各种 UV 编辑工具以及当前纹理节点移动纹理。

## 配置

“Maya 硬件”(Maya Hardware)渲染器使用的“环境立方体/环境球”(Env Cube/Env Ball)贴图配置不同于“Maya 软件”(Maya Software)渲染器。可以从“渲染设置”(Render Settings):“Maya 硬件”(Maya Hardware)选项卡中的“硬件环境查找”(Hardware Environment Lookup Attribute)属性选择您喜欢的配置。

此外，“环境立方体/环境球”(Env Cube/Env Ball)贴图的解释也不同，具体取决于“环境立方体/环境球”(Env Cube/Env Ball)映射到“颜色”(Color)属性还是映射到“反射的颜色”(Reflected Color)属性。大多数情况下，映射到“反射的颜色”(Reflected Color)可创建有光泽的曲面，映射到“颜色”(Color)可查找信息（例如，光照贴图）。
