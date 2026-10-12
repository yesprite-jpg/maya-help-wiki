# 公用“体积”(Volumetric)材质属性

下列属性对“环境雾”(Environment Fog)和“灯光雾体积”(Light fog Volumetric)材质是公用的，请执行以下操作：

## 蒙版不透明度(Matte Opacity)

可以控制单个对象的遮罩值。请参见“蒙版不透明度”(Matte Opacity)。

“蒙版不透明度”(Matt Opacity)属性可用于“各向异性”(Anisotropic)、“Blinn”、“Lambert”、“分层着色器”(Layered Shader)、“Phong”、“PhongE”、“着色贴图”(Shading Map)和“使用背景”(Use Background)材质类型。

## 蒙版不透明度模式(Matte Opacity Mode)

从下拉列表中单击以显示三个“蒙版不透明度模式”(Matte Opacity Modes)。

#### 不透明度增益(Opacity Gain)

默认“蒙版不透明度模式”(Matte Opacity Mode)。“不透明度增益”(Opacity Gain)值用作在材质的常用蒙版值贡献的增益控件。

蒙版通道将首先计算此方法 — 不透明曲面的值为 1.0 能完全覆盖像素，少于 1.0 的值则说明它覆盖了部分像素。将为透明对象适当减少该值，然后乘以指定“蒙版不透明度”(Matte Opacity)值。

“蒙版不透明度模式”(Matte Opacity Mode)值也可设定关键帧。“不透明度增益”(Opacity Gain)范围是从完全透明到无效果（和平常一样渲染）。

#### 匀值蒙版(Solid Matte)

使这些曲面覆盖的所有像素的蒙版通道的值不变。使用指定在“蒙版不透明度”(Matte Opacity)滑块的值。

#### 黑洞(Black Hole)

即使对象为透明，对象所覆盖的所有像素的蒙版通道设置为 0（完全透明），而不管对象透明时后面的内容。这将创建一个对象位于图像中的黑洞，以击打蒙版。在此模式下，“蒙版不透明度”(Matte Opacity)滑块处于禁用状态，并且将忽略其值。

**注**

对于“不透明度增益”(Opacity Gain)和“匀值蒙版”(Solid Matte)模式，如果对象具有非零的“透明度”，则后面的对象通常为蒙版通道的值作出贡献。这是在这些模式中将“蒙版不透明度”(Matte Opacity)设置为 0.0，并选择“黑洞”(Black Hole)模式的区别。

## 蒙版不透明度(Matte Opacity)

此值基于选定的“蒙版不透明度模式”(Matte Opacity Mode)（“不透明度增益”(Opacity Gain)或“匀值蒙版”(Solid Matte)）采用不同方式工作。

例如，对于“不透明度增益”(Opacity Gain)模式，“蒙版不透明度”(Matte Opacity)滑块值表示 Alpha 通道的透明倍增数量。默认值为 1，即，任何不透明对象注册了完整的 Alpha 值。

如果“蒙版不透明度”(Matte Opacity)值为 1，则 0 Alpha 值已注册。任何 0 到 1 之间的值作为 Alpha 通道值的倍增，以获得新的 alpha 值。
