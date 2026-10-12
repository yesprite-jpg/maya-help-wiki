# 表面着色器(Surface Shader)

是作为包裹器节点的材质（着色器），这意味着您可以将任何可设定关键帧属性连接到该着色组，然后将该着色组连接到对象。例如，您可以将某个对象的平移位置连接到“曲面着色器”(Surface Shader)的“输出颜色”(Out Color)属性，以通过对象的位置确定对象的颜色。

在[“创建”(Create)选项卡](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)中找到此材质。

## 表面着色器属性(Surface Shader Attributes)

#### 输出颜色(Out Color)

材质的颜色。默认为黑色。

#### 输出透明度(Out Transparency)

材质的透明度。默认为黑色（不透明）。

#### 输出辉光颜色(Out Glow Color)

材质的辉光颜色。默认为黑色，无辉光。

#### 输出蒙版不透明度(Out Matte Opacity)

将其他属性连接到该选项以控制材质的蒙版 (Alpha) 通道的不透明度。
