# 环境铬(Env Chrome)

模拟陈列室环境。纹理由平面和天空平面（具有荧光灯矩形）组成，并提供了简单但有效的环境模拟铬表面的反射。

“环境铬属性”(Environment Chrome Attributes)控制“环境铬”(Env Chrome)纹理中模拟荧光灯的大小和位置。（这些“灯光”可在表面产生反射，但它们实际上不照亮表面。）

在[“创建”(Create)选项卡](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)中找到此纹理。

#### 灯光宽度(Light Width)、灯光深度(Light Depth)

每个灯光的宽度和深度。这些参数也确定灯光之间的间距。有效/滑块范围为 0 到 1。默认“灯光宽度”(Light Width)值为 0.5，默认“灯光深度”(Light Depth)值为 0.1。

#### 灯光宽度增益(Light Width Gain)、灯光宽度偏移(Light Width Offset)

每单位长度灯光的数目。有效/滑块范围为 0 到 1。默认“灯光宽度增益”(Light Width Gain)值为 1，默认“灯光宽度偏移”(Light Width Offset)值为 0。

#### 灯光深度增益(Light Depth Gain)、灯光深度偏移(Light Depth Offset)

灯光置换。滑块范围为 0 到 1。默认“灯光深度增益”(Light Depth Gain)值为 1，默认“灯光深度偏移”(Light Depth Offset)为 0。

## 天空属性(Sky Attributes)

#### 天空颜色(Sky Color)

地平线处天空的颜色。将使用“天空颜色”(Sky Color)和“天顶颜色”(Zenith Color)之间的颜色对整体天空颜色进行线性插值。

#### 天顶颜色(Zenith Color)

天顶（笔直向上）处天空的颜色。将使用“天空颜色”(Sky Color)和“天顶颜色”(Zenith Color)之间的颜色对整体天空颜色进行线性插值。

#### 灯光颜色(Light Color)

模拟荧光灯的颜色。这些“灯光”可在表面产生反射，但它们实际上不照亮表面。

## 地面属性(Floor Attributes)

#### 地面颜色(Floor Color)、地平线颜色(Horizon Color)、栅格颜色(Grid Color)

地面、地面水平线和地面栅格的颜色。

#### 真实地板(Real Floor)

如果“真实地板”(Real Floor)处于禁用状态，则环境的地板位于无限远处，因此移动的对象上的反射和，或从移动的摄影机查看到的反射都是不正确的。

如果“真实地板”(Real Floor)处于启用状态，则地板的位置相对于栅格平面（基于“地面海拔高度”(Floor Altitude)值），因此移动的对象上的反射和，或从移动的摄影机查看到的反射都是正确的。如果“真实地板”(Real Floor)处于启用状态，请确保表面和、或摄影机不会低于栅格平面。默认情况下“真实地板”(Real Floor)处于启用状态。

#### 地面海拔高度(Floor Altitude)

地面相对于栅格平面的高度。如果“真实地板”(Real Floor)处于禁用状态，则“地面海拔高度”(Floor Altitude)无效果。滑块范围为 -1 到 1。默认值为 -1。

**注**

如果“地面海拔高度”(Floor Altitude)设定得太高，纹理样例将变为红色，表示摄影机在地面下方观看，而您可能不希望发生这种情况。降低“地面海拔高度”(Floor Altitude)，直到红色消失。

## 栅格放置(Grid Placement)

#### 栅格宽度(Grid Width)、栅格深度(Grid Depth)

栅格线的宽度和深度。这些属性也可确定栅格线之间的间距。有效/滑块范围为 0 到 1。默认值为 0.1。

#### 栅格宽度增益(Grid Width Gain)、栅格深度增益(Grid Depth Gain)

每单位长度栅格单元的数目。有效/滑块范围为 0 到 1。默认值为 1。

#### 栅格宽度偏移(Grid Width Offset)、栅格深度偏移(Grid Depth Offset)

栅格置换。滑块范围为 0 到 1。默认值为 0。
