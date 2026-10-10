# DirectX 11 着色器不显示顶点颜色的疑难解答

如果使用“绘制顶点颜色工具”(Paint Vertex Color Tool)在已应用 DirectX 11 着色器的对象上绘制顶点，且顶点颜色未按预期显示，则可能是因为 DirectX 11 着色器的“曲面数据”(Surface Data)部分中的 Color0 属性未设置为正确的颜色集。默认情况下，Maya 将您创建的第一个顶点颜色集命名为 colorSet1。

以下是可能的解决办法：

- 在 .fx 文件中使用 COLOR1 语义。这对应于 colorSet1。（COLOR0 语义对应于 colorSet。）但是，仅当在 Maya 中使用 .fx 文件时，这才会提供正确的结果。如果 .fx 文件由其他应用程序（如游戏引擎）使用，则可能会遇到意外的结果。

- 在 DirectX 11 着色器的“曲面数据”(Surface Data)部分中，将 Color 0 属性设置为 colorSet1。

- 修改 dx11Shader 插件，以便 COLOR0 语义对应于 colorSet1（而不是 colorSet）。
