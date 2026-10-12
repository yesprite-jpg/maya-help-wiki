# 分层着色器(Layered Shader)

有关分层着色器的详细信息，请参见[创建分层着色器](../../../../关于着色和纹理曲面/创建分层着色器.md)。

在[“创建”(Create)选项卡](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)中找到此材质。

## 分层着色器属性(Layered Shader Attributes)

#### 透明度(Transparency)

设定材质的透明度。默认情况下，材质是半透明的。

#### 合成标志(Compositing Flag)

合成“层着色器”(Layer Shader)节点或“层纹理”(Layer Texture)节点中的层。各个模式计算透明度标志的方式不同。

有关详细信息，请参见[创建分层着色器](../../../../关于着色和纹理曲面/创建分层着色器.md)主题中的“带有‘分层着色器’(Layered Shader)节点的分层纹理”。

#### 层着色器(Layer Shaders)

将颜色和透明度一起进行处理并传递给“层着色器”(Layer Shaders)。换句话说，在将颜色报告给“层着色器”(Layer Shaders)之前，考虑使用透明度修改颜色。

#### 层纹理(Layer Texture)

将颜色和透明度单独传递给分层着色器。换句话说，将颜色报告给“层着色器”(Layer Shaders)，而不考虑透明度设置；透明度作为单独通道传递。然后，合成颜色和透明度。但是，这可能会导致黑色光晕，其中显示 Alpha 通道的负空间。

## 硬件着色属性(Hardware Shading Attributes)

#### 硬件颜色(Hardware Color)

有助于您区分视图中指定给分层着色器的对象。
