# 分层纹理(Layered texture)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1577 字 ≥300，非承重" -->

有关分层纹理的详细信息，请参见[分层纹理](../../../关于着色和纹理曲面/纹理/2D%20和%203D%20纹理.md#WS17956D7ADBC6E736-51D3585C117AE33DCFA-7FE4)。

在[“创建”(Create)选项卡](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-76B10C8D-EC19-4AFE-8433-743326C49DBE.htm)中找到此纹理。

#### 层可见(Layer is Visible)

指定在计算分层纹理的结果颜色和 Alpha 的过程中，是否应该考虑层。如果禁用，就好像层不存在一样。如果需要隔离特定层以查看它本身的外观时，请使用该选项。

![图：指定在计算分层纹理的结果颜色和 Alpha 的过程中，是否应该考虑层。如果禁用，就好像层不存在一样。如果需要隔离特定层以…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-527D82D2-67C7-4CB4-8EF3-FA22C47DCC2D.png) <!-- baize:img-hook downloaded=false reason="正文 1577 字 ≥300，非承重" -->

#### Alpha 为亮度(Alpha is Luminance)

用于确定“Alpha”是否应该像其他 2D 纹理（如“文件”(File)纹理）一样，是“输出颜色”(Out Color)的亮度。

## “文件”(File)和“分层纹理”(Layered Texture)节点的自动Alpha

#### 硬件颜色(Hardware Color)

指定在硬件着色模式（而不是硬件纹理模式）下时，哪些颜色对象在视图中使用该纹理显示。

#### 融合模式(Blend modes)

使用“分层纹理”(Layered Texture)的“属性编辑器”(Attribute Editor)中的“纹理融合”(Texture Blend)属性，可以将层与其下的内容融合。“融合模式”(Blend Mode)指定选定层如何与其下的内容融合。下面列出了融合模式。

**注**

有关这些融合模式的详细信息（包括其技术定义），请参见“Maya 帮助”中的“技术文档 > 节点 > layeredTexture”。

#### 无(None)

编辑或绘制每个像素以使其成为结果颜色。这是默认设置。（处理位映射或索引颜色图像时，法线模式称为“阈值”(Threshold)。）

#### 覆盖(Over)

会将顶部层像贴花一样应用到下面的层。贴花的形状是由顶部 Alpha 确定的。

#### 内部(In)

在前景 Alpha 的形状中，会剪切背景纹理。

#### 输出(Out)

结果与“内部”(In)相反。这就好像是已将前景层的形状从背景 Alpha 中裁切掉一样。

#### 相加(Add)

结果颜色是将前景色添加到背景色的结果，就好像通过幻灯机投影到背景上一样。接着会使用前景 Alpha 在背景色上应用结果颜色，以定义结果的不透明度。

#### 相减(Subtract)

结果颜色是从背景色减去前景色。接着会使用前景 Alpha 在背景色上应用结果颜色，以定义结果的不透明度。

#### 相乘(Multiply)

查看每个层中的颜色信息，并将底色乘以融合颜色。结果颜色始终是较暗的颜色。任何颜色与黑色相乘会产生黑色。任何颜色与白色相乘会保留该颜色不变。

#### 差集(Difference)

查看每个层中的颜色信息，然后从底色减去融合颜色或从融合颜色减去底色，具体取决于哪种颜色具有最大的亮度值。与白色融合会反转底色值；与黑色融合不会产生任何改变。

#### 变亮(Lighten)

查看每个层中的颜色信息，然后选择底色或融合颜色中较浅的颜色作为结果颜色。会替换比融合颜色暗的像素，比融合颜色亮的像素不会改变。

#### 变暗(Darken)

查看每个层中的颜色信息，然后选择底色或融合颜色中较暗的颜色作为结果颜色。会替换比融合颜色亮的像素，比融合颜色暗的像素不会改变。

#### 饱和度(Saturate)

使用底色的亮度和色调以及融合颜色的饱和度创建结果颜色。

#### 降低饱和度(De-saturate)

结果颜色是饱和度降低的背景色，降低的程度与由前景 Alpha 调整的前景色成比例。例如，如果前景色为红色，则产生的颜色为包含不饱和红色的背景色。

#### 照明(Illuminate)

使用底色的色调和饱和度以及融合颜色的亮度创建结果颜色。该模式会创建与“颜色”(Color)模式相反的效果。

#### CPV 调制(CPV Modulate)

![图：在此模式下，将基于活动的逐顶点颜色和 Alpha 值 (CPV) 按每个组件 (RGBA) 融合层。 选择此模式将断开 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-57E9DA6F-DB97-48FB-859F-5FA7A7471DF8.png) <!-- baize:img-hook downloaded=false reason="正文 1577 字 ≥300，非承重" -->

在此模式下，将基于活动的逐顶点颜色和 Alpha 值 (CPV) 按每个组件 (RGBA) 融合层。

选择此模式将断开 CPV 组件与指定材质上的颜色通道的连接。因此，将忽略“网格显示 > 材质融合设置”(Mesh Display > Material Blend Setting)和“网格显示 > 对材质通道上色”(Mesh Display > Color Material Channel)设置。
