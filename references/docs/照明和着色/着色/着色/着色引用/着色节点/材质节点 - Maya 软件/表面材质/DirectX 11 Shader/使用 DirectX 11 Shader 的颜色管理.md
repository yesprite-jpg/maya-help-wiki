# 使用 DirectX 11 Shader 的颜色管理

如果启用“颜色管理”(Color Management)（在“首选项”(Preferences)窗口的“颜色管理”(Color Management)部分下），并使用属性编辑器在 dx11Shader 中启用“线性空间照明”(Linear Space Lighting)，则 Gamma 仅应用一次且着色将正确渲染。

如果 Gamma 已在视口中启用，您可以使用语义 MayaGammaCorrection 进行查询。
