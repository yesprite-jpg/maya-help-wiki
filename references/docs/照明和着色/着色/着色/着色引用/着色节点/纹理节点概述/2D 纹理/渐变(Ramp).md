# 渐变(Ramp)

通过一系列颜色创建渐变。使用该纹理：

- 创建不同类型的效果，如条纹、几何图案或杂色曲面

- 作为 2D 背景

- 作为环境球体纹理的源文件来模拟天空和地平线

- 作为投影纹理的源文件来模拟木材颗粒、大理石或岩石

在[“创建”(Create)选项卡](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)中找到此纹理。若要应用该纹理为纹理贴图，请参见[映射 2D 或 3D 纹理](../../../../关于着色和纹理曲面/纹理/纹理映射/将%202D%20或%203D%20纹理映射到材质.md)。

**注**

动画期间，非常复制的渐变纹理可能会出现锯齿。如果出现此情况，请将渐变纹理转化为一个图像文件（有关详细信息，请参见[将纹理或着色网络转化为文件纹理](../../../../关于着色和纹理曲面/纹理/纹理映射/将纹理或着色网络转化为文件纹理.md)）。

#### 类型(Type)

颜色渐变的方向。默认为“V 向渐变”(V Ramp)。以下介绍了选择“圆形类型”(Circular Type)并在“属性编辑器”(Attribute Editor)中调整“渐变”(Ramp)的颜色时会发生的情况（请参见下文的渐变）。

![图：颜色渐变的方向。默认为“V 向渐变”(V Ramp)。以下介绍了选择“圆形类型”(Circular Type)并在“属性…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-6D97D30C-313B-4F8D-AD67-A51AECA1DCB0.png) <!-- baize:img-hook downloaded=false reason="正文 1442 字 ≥300，非承重" -->

#### 插值(Interpolation)

有关详细信息，请参见[插值](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B#GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B__SECTION_A26BB5B0120C4D1797A3AA77DBA8E0B9)。

#### 渐变(Ramp)

默认情况下，渐变设置为黑色和白色（从黑色到白色）。

![图：默认情况下，渐变设置为黑色和白色（从黑色到白色）。 您可以切换到彩虹渐变，方法是选择“预设 彩虹”(Presets Ra…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-1C7EEC1E-71AD-45B2-9F9D-8153231E86F1.png) <!-- baize:img-hook downloaded=false reason="正文 1442 字 ≥300，非承重" -->

您可以切换到彩虹渐变，方法是选择“预设 > 彩虹”(Presets > Rainbow)。若要还原为默认值，请选择“预设 > BlackToWhite”(Presets > BlackToWhite)。另一个可用选项是“预设 > WhiteToBlack”(Presets > WhiteToBlack)。

有关如何通过添加颜色条目来自定义渐变的详细信息，请参见[颜色渐变](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B#GUID-6C102F00-86AC-4EA6-9357-A0C13A4BBB3B__SECTION_D18F4FBF38B94659837688094068CAF0)。

**注**

仅在

“插值”(Interpolation)

、

“选定位置”(Selected Position)

、和

“选定颜色”(Selected Color)

中的更改会显示在渐变中。对所有属性的更改都将显示在 Hypershade 样例中。

存在高级渐变功能。有关详细信息，请参见[渐变着色器](../../材质节点%20-%20Maya%20软件/表面材质/渐变着色器%28Ramp%20Shader%29.md)。

#### 选定颜色(Selected Color)

活动的颜色组件。该属性仅适用于活动颜色。

#### 选定位置(Selected Position)

渐变中的活动颜色组件的位置。该属性仅适用于活动颜色。范围为 0（渐变底部）到 1（渐变顶部）。

#### U 向波(U Wave)、V 向波(V Wave)

控制 U 和 V 方向中的纹理的正弦偏移振幅.增加“U 向波”(U Wave)或“V 向波”(V Wave)会增加纹理波纹的显示。范围为 0（无波浪）到 1。默认值为 0。

**注**

提示：

若要增加纹理中的波浪数，请在 2D 纹理放置节点中增加[UV 向重复](../../工具节点%28Utility%20nodes%29/2D%20放置%282d%20Placement%29.md#GUID-94070C7E-C550-42FD-AFC9-FBE82B173B1D__WS1A9193826455F5FF-4F542F6211C79DEA861-1775)值。

#### 噪波(Noise)

2D 噪波在 U 和 V 方向的偏移量。如果该纹理重复（[UV 向重复](../../工具节点%28Utility%20nodes%29/2D%20放置%282d%20Placement%29.md#GUID-94070C7E-C550-42FD-AFC9-FBE82B173B1D__WS1A9193826455F5FF-4F542F6211C79DEA861-1775)值大于 1），则噪波不会重复（该纹理的每个实例是唯一）。范围为 0（无噪波）到 1。默认值为 0。

#### 噪波频率(Noise Freq)

控制噪波粒度（如果以上的“噪波”(Noise)值上方是非零）。范围为 0 到 1。默认值为 0.5。

## HSV 颜色噪波(HSV Color Noise)

使用三个会影响颜色“色调”(Hue)、“饱和度”(Saturation)和“明度”(Value)的单独 2D 噪波来随机化“渐变”(Ramp)纹理的颜色。

#### 色调噪波(Hue Noise)

偏移颜色色调。用于标记带不同颜色斑点的颜色。范围为 0 到 1。默认值为 0。

#### 饱和度噪波(Sat Noise)

偏移颜色饱和度（或白度）。用于创建风化外观。范围为 0 到 1。默认值为 0。

#### 明度噪波(Val Noise)

偏移颜色值（或黑度）。范围为 0 到 1。默认值为 0。

#### 色调噪波频率(Hue Noise Freq)、饱和度噪波频率(Sat Noise Freq)、明度噪波频率(Val Noise Freq)

控制色调、饱和度和明度噪波的粒度。范围为 0 到 1。默认值为 0.5。（对于每个非零频率值，附加计算可能会降低渲染速度。）
