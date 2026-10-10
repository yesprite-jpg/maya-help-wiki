# 光学效果属性(Optical FX Attributes)

“光学效果属性”(Optical FX Attributes)可控制辉光、光晕和镜头光斑的外观。

有关光学效果的详细信息，请参见[辉光、光晕和镜头光斑](../../调整照明/辉光、光晕和镜头光斑.md)。

#### 活动(Active)

启用或禁用光学效果。默认情况下，“活动”(Active)处于启用状态。

#### 镜头光斑(Lens Flare)

模拟照明摄影机镜头的曲面的强光源。光斑强度取决于“[光斑强度](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E2970)”值。光斑圆形的大小与摄影机的视图的场有关。默认情况下，“镜头光斑”(Lens Flare)处于禁用状态。启用“镜头光斑”(Lens Flare)即可访问[镜头光斑属性](光学效果属性%28Optical%20FX%20Attributes%29.md#WS17956D7ADBC6E7361022BC4117AE3252FD-7FB4)。

![图：模拟照明摄影机镜头的曲面的强光源。光斑强度取决于“光斑强度”值。光斑圆形的大小与摄影机的视图的场有关。默认情况下，“镜头…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-FC06F84D-29A2-452B-BF82-4EE2E99C4A7F.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

### 辉光类型(Glow Type)

直接查看时灯光产生的辉光的类型。单击箭头并从下拉列表中访问可用辉光类型。

渲染场景时，灯光不需要辉光来照亮对象，但灯光需要辉光对摄影机可见。默认的“辉光类型”(Glow Type)为“线性”(Linear)。

以下示例显示了一个黄色辉光（[辉光颜色](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E2941)）和默认设置中的其余所有“辉光”(Glow)属性。

#### 无(None)

未出现辉光。

#### 线性(Linear)

辉光从灯光的中心缓慢减弱。

![图：辉光从灯光的中心缓慢减弱。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-08288A15-F399-4526-9F30-E29BDF68B263.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

#### 指数(Exponential)

辉光从灯光的中心快速减弱。

![图：辉光从灯光的中心快速减弱。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-1DBB3ACC-FC9A-4FDE-B250-EDF06BEB1D59.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

#### 球(Ball)

辉光朝着由“辉光扩散”(Glow Spread)值指定的距离（距离灯光中心）快速减弱。

![图：辉光朝着由“辉光扩散”(Glow Spread)值指定的距离（距离灯光中心）快速减弱。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-CC66AC22-F964-4E34-862B-F5BD1565488A.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

#### 镜头光斑(Lens Flare)

模拟照明多个摄影机镜头的曲面的强光源。

![图：模拟照明多个摄影机镜头的曲面的强光源。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-355F9C3B-1A1C-4F64-8F09-C532C5C00552.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

#### 边缘光晕(Rim Halo)

形成具有柔和中心辉光的圆环。环的大小取决于“光晕扩散”(Halo Spread)值（本示例中为 0.75）。

![图：形成具有柔和中心辉光的圆环。环的大小取决于“光晕扩散”(Halo Spread)值（本示例中为 0.75）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-F335AAD1-83D1-4915-A344-A5B7A17BB8CA.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

### 光晕类型(Halo Type)

直接查看时灯光产生的光晕的类型。“光晕”(Halo)类似于“辉光”(Glow)，只不过“光晕”减弱更为缓慢，并且可以使用不同的减弱类型。默认设置为无。单击箭头可访问下拉列表。

接下来将针对不同“辉光”(Halo)类型进行说明：默认[线性](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E28FF)“辉光类型”(Glow Type)，[光晕颜色](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E2961)为红色以及[光晕扩散](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E2968)值为 0.75 的光晕。

#### 无(None)

未出现光晕。

#### 线性(Linear)

光晕从灯光的中心缓慢减弱。

![图：光晕从灯光的中心缓慢减弱。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-82175D4F-2A05-4891-8D2E-15220A2E5022.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

#### 指数(Exponential)

光晕从灯光的中心快速减弱。

![图：光晕从灯光的中心快速减弱。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A6B30386-3589-40AB-9AB4-67BAE2AD2B25.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

#### 球(Ball)

光晕朝着由“光晕扩散”(Halo Spread)值指定的距离（距离灯光中心）快速减弱。

![图：光晕朝着由“光晕扩散”(Halo Spread)值指定的距离（距离灯光中心）快速减弱。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B4E1A249-DFC9-4EAB-AF50-57F7EE35113D.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

#### 镜头光斑(Lens Flare)

模拟照明多个摄影机镜头的曲面的强光源。

![图：模拟照明多个摄影机镜头的曲面的强光源。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-864C8707-410A-4B38-A5E8-D50A4DDF4929.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

#### 边缘光晕(Rim Halo)

形成具有柔和中心辉光的圆环。环的大小取决于“光晕扩散”(Halo Spread)值。

![图：形成具有柔和中心辉光的圆环。环的大小取决于“光晕扩散”(Halo Spread)值。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-0CE33F1C-59F8-422B-AADA-5A758FB97BDC.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

#### 径向频率(Radial Frequency)

控制辉光径向噪波的平滑度（请参见[辉光径向噪波](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E2957)）。滑块范围为 0 到 5，但输入的值可以无穷大。默认值为 0.5。

#### 星形点(Star Points)

表示辉光星形过滤器效果的点数（请参见[辉光星形级别](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E295B)）。以下示例为一个值为 20 的“星形点”(Star Points)和一个可产生类似彗星效果的值为 1 的“星形点”(Star Points)。使用“旋转”(Rotation)属性来调整彗星的尾部。

![图：表示辉光星形过滤器效果的点数（请参见辉光星形级别）。以下示例为一个值为 20 的“星形点”(Star Points)和一…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-971A2FF2-ABC6-42BE-B47A-91FAF29456F3.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

滑块范围为 0 到 10，但输入的值可以无穷大。默认值为 4。

**注**

对于非整数“星形点”(Star Points)值，可以在星形效果的顶部使用接缝或硬线进行渲染。

#### 旋转(Rotation)

围绕灯光的中心旋转辉光噪波和星形效果（[辉光噪波](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E294B)、[辉光径向噪波](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E2957)和[辉光星形级别](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E295B)）。滑块范围为 0 到 360（度），但输入的值可以无穷大。默认值为 0。

#### 忽略灯光(Ignore Light)

如果已启用，则会自动设定着色器辉光的阈值。如果要手动控制场景中辉光的量，则请禁用该选项。

## 辉光属性(Glow Attributes)

#### 辉光颜色(Glow Color)

灯光的辉光的颜色。单击颜色样例可打开“颜色选择器”(Color Chooser)，选择一种颜色（如果需要）。默认设置为白色。

#### 辉光强度(Glow Intensity)

也可以通过材质的“特殊效果”(Special Effects)属性进行访问（请参见[特殊效果(Special Effects)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-426A7F26-4647-4DC4-B390-6380620AD757.htm#WS17956D7ADBC6E73638876AF8117AE33FA94-7FC8)）。控制辉光亮度。随着“辉光强度”(Glow Intensity)值的增加，辉光效果的外观尺寸也会增加。负的“辉光强度”(Glow Intensity)值会使其他辉光减弱。（灯光的“衰退速率”(Decay Rate)可控制辉光亮度如何随距离而降低。）滑块范围为 0 到 10，但输入的值可以无穷大。默认值为 1。

#### 辉光扩散(Glow Spread)

控制辉光效果的大小。负值会有奇怪但有时会有非常有用的效果。滑块范围为 0 至 5。默认值为 1。

#### 辉光噪波(Glow Noise)

控制应用于辉光的 2D 噪波的强度。该噪波是在以灯光位置为中心的平面上生成的，并且始终朝向摄影机。滑块范围为 0 到 1。默认值为 0。

若要在发光的光源周围创建照明烟的幻影，请将“辉光噪波”(Glow Noise)值设定为接近 0.5 的值，并缓慢设置“噪波 U 向偏移”(Noise Uoffset)和“噪波 V 向偏移”(Noise Voffset)值的动画。烟表现为顺着灯光缓慢漂移。

**注**

提示：

通常，如果要创建烟和火的效果，雾照明会比辉光更好，这是因为雾是 3D 效果（例如，对象无法遮挡辉光噪波）。

以下示例显示如何只通过调整一些“辉光属性”(Glow Attributes)来创建令人压抑的夜空<hbreak/>。本示例中使用的“光学效果属性”(Optical FX attributes)如下：

- 辉光类型(Glow Type) = 指数(Exponential)

- “径向频率”(Radial Frequency) = 0

- “星形点”(Star Points) = 2

- “旋转”(Rotation) = 300

  ![图：“旋转”(Rotation) = 300 辉光径向噪波(Glow Radial Noise) 将辉光的扩散随机化，以模拟…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-4CD91C6D-2B7D-48E2-8198-91C3EA3F5F00.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

  #### 辉光径向噪波(Glow Radial Noise)

  将辉光的扩散随机化，以模拟星光和折射灯光的睫毛。滑块范围为 0 到 1。默认值为 0。

  “辉光径向噪波”(Glow Radial Noise)为负值会产生较粗的噪波。使用[径向频率](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E2932)属性控制该效果的平滑度。

  #### 辉光星形级别(Glow Star Level)

  模拟摄影机星形过滤器效果。滑块范围为 0 到 4。默认值为 0。使用[星形点](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E2935)属性设定星形上的点数。使用[旋转](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E293B)属性旋转星形。

  #### 辉光不透明度(Glow Opacity)

  控制灯光的辉光暗显对象的程度。将不透明度视为与透明度相反。滑块范围为 0 到 0.5。默认值为 0。

## 光晕属性(Halo Attributes)

#### 光晕颜色(Halo Color)

光晕的颜色。单击颜色样例以打开“颜色选择器”(Color Chooser)，并选择其他颜色（如果需要）。默认设置为白色。

#### 光晕强度(Halo Intensity)

控制光晕亮度。随着“光晕强度”(Halo Intensity)值的增加，光晕效果的外观尺寸也会增加。（灯光的“衰退速率”(Decay Rate)可控制光晕亮度如何随距离而降低。）滑块范围为 0 至 5。默认值为 1。

#### 光晕扩散(Halo Spread)

控制光晕效果的大小。“光晕扩散”(Halo Spread)和“辉光扩散”(Glow Spread)的值相同时，光晕大小通常大于辉光大小。滑块范围为 0 至 5。默认值为 1。

## 镜头光斑属性(Lens Flare Attributes)

仅当在“光学效果属性”(Optical FX Attributes)中启用“镜头光斑”(Lens Flare)时，才可以使用这些属性。

#### 光斑颜色(Flare Color)

镜头光斑圈的颜色。单击颜色样例，并从“颜色选择器”(Color Chooser)中选择另一种颜色（如果需要）。默认颜色为白色。

#### 光斑强度(Flare Intensity)

控制光斑效果的亮度。（灯光的“衰退速率”(Decay Rate)可控制镜头光斑亮度如何随距离而降低。）有效范围是 0 到无限。滑块范围为 0 到 5。默认值为 1。

#### 光斑圈数(Flare Num Circles)

表示镜头光斑效果中的圈数。有效范围是 0 到无限。滑块范围为 0 到 30。默认值是 20。

如果“光斑圈数”(Flare Num Circles)的值非常大，则渲染时间可能会很长，尤其是在“光斑最小值”(Flare Min Size)和“光斑最大值”(Flare Max Size)的值很大且“光斑颜色”(Flare Color)带纹理时。

#### 光斑最小值(Flare Min Size)、光斑最大值(Flare Max Size)

在这两个值之间随机化圆形大小。有效范围为负无穷到正无穷。滑块范围为 0 到 5。“光斑最小值”(Flare Min Size)的默认值为 0.1，且“光斑最大值”(Flare Max Size)的默认值为 1。

#### 六边形光斑(Hexagon Flare)

生成六边形光斑元素（而不是圆形）。

![图：生成六边形光斑元素（而不是圆形）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-DA7C2D3B-7EC3-4C3D-A4A5-43DA8A0B869D.png) <!-- baize:img-hook downloaded=false reason="正文 4661 字 ≥300，非承重" -->

#### 光斑颜色扩散(Flare Col Spread)

控制基于“光斑颜色”(Flare Color)随机化的各个圆形的色调度。如果“光斑颜色”(Flare Color)不是至少部分饱和（例如，不是白色或灰色），则“光斑颜色扩散”(Flare Col Spread)值没有任何效果。滑块范围为 0 到 1。默认值为 0.5。

#### 光斑聚焦(Flare Focus)

控制圆边的锐度。有效范围为 0（非常模糊）到 1（完全明晰）。默认值为 0.6。

#### 光斑垂直(Flare Vertical)、光斑水平(Flare Horizontal)

相对于图像中心控制光斑效果的轴。如果光源移动，则光斑会表现为围绕该点进行旋转。滑块范围为 -1 到 1。默认值为 1。

#### 光斑长度(Flare Length)

相对于灯光位置控制光斑效果长度。如果“光斑长度”(Flare Length)较小，则所有圆形会与该灯光重叠。如果“光斑长度”(Flare Length)很大，则圆形会扩散到图像之外。如果“光斑垂直”(Flare Vertical)和“光斑水平”(Flare Horizontal)的值都为 0，则“光斑长度”(Flare Length)值没有任何效果。滑块范围为 0 到 1。默认值为 1。

## 噪波属性(Noise Attributes)

请参见[辉光噪波](光学效果属性%28Optical%20FX%20Attributes%29.md#WS1A9193826455F5FF-29C43AA6117B26F372E294B)。

#### 噪波 U 向比例(Noise Uscale)、噪波 V 向比例(Noise Vscale)

在水平方向（“噪波 U 向比例”(Noise Uscale)）和垂直方向（“噪波 V 向比例”(Noise Vscale)）缩放辉光噪波。滑块范围为 0 至 5。默认值为 1。

**注**

提示：

可以使用“噪波 U 向比例”(Noise Uscale)和“噪波 V 向比例”(Noise Vscale)创建分层雾或高火焰。设置“噪波 U 向比例”(Noise Uscale)和“噪波 V 向比例”(Noise Vscale)值从高值到低值的动画，以使噪波表现为像发生爆炸一样飞散开来。

#### 噪波 U 向偏移(Noise Uoffset)、噪波 V 向偏移(Noise Voffset)

在水平方向（“噪波 U 向偏移”(Noise Uoffset)）和垂直方向（“噪波 V 向偏移”(Noise Voffset)）偏移辉光噪波。

例如，可以设置“噪波 U 向偏移”(Noise Uoffset)和“噪波 V 向偏移”(Noise Voffset)值的动画来模拟穿过灯光的烟、雨或雪。噪波在偏移值为 1 后重复。滑块范围为 0 到 1。“噪波 U 向偏移”(Noise Uoffset)的默认值为 1，且“噪波 V 向偏移”(Noise Voffset)的默认值为 0.5。

#### 噪波阈值(Noise Threshold)

噪波的中止值。随着“噪波阈值”(Noise Threshold)的值越来越接接近 0，辉光噪波会分解为较小的面片。滑块范围为 0 到 1。默认值为 0.5。

**注**

提示：

可以使用“噪波阈值”(Noise Threshold)来模拟球状簇、爆炸喷出物、雪和雨效果，尤其是在“噪波 U 向比例”(Noise Uscale)和“噪波 V 向比例”(Noise Vscale)值较高时。还可以将其用于使火焰和烟分布更为不均。
