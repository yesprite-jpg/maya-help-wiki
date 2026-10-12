# GLSL 着色器

通过 glslShader 插件可以加载和可视化自定义 GLSL（OpenGL 着色语言）着色器，在**“OpenGL 核心配置”(OpenGL Core Profile)**模式下运行 Viewport 2.0 时，这些着色器支持照明、纹理、阴影和细分。通过此插件可获取与在 DirectX 11 模式下相同的视觉保真度。

有关如何在“OpenGL 核心配置”(OpenGL Core Profile)模式下运行 Maya 以及如何加载 glslShader 插件的信息，请参见[创建和可视化 GLSL 着色器](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建和可视化%20GLSL%20着色器.md)。

可以使用 .ogsfx 文件格式创建自定义 GLSL 着色器。.ogsfx 文件格式是一种包裹器，允许您为各个着色阶段指定 GLSL 碎片，以处理灯光和纹理绑定，并确定如何在属性编辑器中显示参数。

glslShader 插件支持颜色、阴影和深度过程。

示例 .ogsfx 文件在 Maya 安装的 ..\presets\GLSL\examples 文件夹中提供。这些示例演示如何使用注释指定纹理文件，将 UI 添加到属性编辑器，以及使用指定细分和几何体着色器的过程定义技术。有关这些示例的详细信息，请参见下面的“相关主题”部分。

也可以将 ShaderFX 图表作为 .ogsfx 文件导出，并使用 glslShader 插件加载它。

在 Maya 安装的 ..\presets\GLSL\examples 文件夹中还提供了 UberShader 的 GLSL 版本（名为 AutodeskUberShader.ogsfx）。这相当于用于 dx11Shader 插件的 AutodeskUberShader.fxo（在 ..\presets\HLSL11\examples\ 中提供）和用于 Shaderfx 着色器的 UberShaderGraph.sfx（在 ..\presets\ShaderFX\Scenes 中提供）。

## 相关主题

- [创建和可视化 GLSL 着色器](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建和可视化%20GLSL%20着色器.md)

- [编写自定义 GLSL 着色器：纹理、透明度和照明示例](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建和可视化%20GLSL%20着色器/编写自定义%20GLSL%20着色器：纹理、透明度、照明和硬件选择示例.md)

- [编写自定义 GLSL 着色器：细分示例](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建和可视化%20GLSL%20着色器/编写自定义%20GLSL%20着色器：细分示例.md)

- [使用 ogsfx 文件中的 include 指令加载顶点和碎片着色器](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建和可视化%20GLSL%20着色器/使用%20ogsfx%20文件中的%20include%20指令加载顶点和碎片着色器.md)
