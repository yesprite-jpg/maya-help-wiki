# DirectX 11 着色器支持的图像格式

## 支持的图像格式

Viewport 2.0 中的 DX11 Shader 支持下列图像格式：

- Bmp

- Cals

- DDS

  对于 DX11：请参见 2010 年 6 月版本的 Microsoft DirectX SDK 文档，查看支持的格式列表。

  **注**

  在加载某些

  .dds

  文件时可能会出现错误消息，因为 Maya 软件渲染器无法渲染样例。但是，上面提及的 DirectX SDK 文档上列出的格式会在 Maya 中以 DX11 模式进行渲染。

- Exr

  File 纹理节点可将浮点值映射到 0 到 1 之间的值用于其样例显示和 DG 求值。但是，Viewport 2.0 中可能会直接支持浮点值，而无需色调映射。对于连接到映射到 DirectX 11 Shader 的属性的 File 纹理节点的 .exr 和 .dds 文件，视口会支持浮点位深度。

- Flic

- Gif

- HDR

- Ig4

- Jfif

- Pcx

- Pict

- Png

- PSD

- Rlc

- 聚光灯

- Targa

- TIF

  对于 TIF 文件，仅支持固定点位深度。对于浮点置换贴图，改为使用 EXR 文件。

- 上述未列出的所有其他图像格式在 DirectX 11 Shader 节点中都被读取为固定点位深度。
