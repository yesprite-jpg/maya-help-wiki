# 使用 ogsfx 文件中的 include 指令加载顶点和碎片着色器

在 Maya 安装的 presets\GLSL\examples 文件夹中提供了一个示例，演示如何使用 .ogsfx 文件中的 #include 指令加载顶点和碎片着色器。

使用 #include 指令，可以保留现有的 GLSL 着色器代码，而不必将它全部组合到一个 .ogsfx 文件中。这样，就可以在不同的应用程序之间共享同一 GLSL 片段。

示例包含以下文件：

- Brix.ogsfx

- Brix.glslf

- Brix.glslv

## 统一参数的定义

.ogsfx 文件从定义统一参数开始。

HIDE_OGSFX_UNIFORMS 设置为 0，#include 指令用于导入 Brix.glslf 和 Brix.glslv 着色器文件。

Brix.glslf 和 Brix.glslv 着色器文件中包裹在 #if !HIDE_OGSFX_UNIFORMS 和 #endif 内的代码（由预处理器）插入到已扩展的中间临时 .ogsfx 文件中，然后对它进行编译。仅在已完全预处理原始的 .ogsfx 文件后，才会编译此临时 .ogsfx 文件。

在 #if !HIDE_OGSFX_UNIFORMS 和 #endif 包裹器内，#if OGSFX 和 #endif 语句用于包裹 OGSFX 特定的代码。

使用 #if 和 #endif 包裹器内的 #else 可为使用 GLSL 的其他第三方应用程序定义统一参数。

在 OGSFX 统一参数定义中，诸如 World 和 WorldInverseTranspose 之类的语义用于向 Maya 指示统一参数的含义。

例如：

```text
uniform mat4 gWorldITXf : WorldInverseTranspose < string UIWidget="None"; >;
```

向 Maya 指示 gWorldITXf 是矩阵 4，它包含 World 变换信息（已反转并转置）。

有关 Maya Viewport 2.0 支持的语义列表，请参见 Maya 开发人员帮助的“Viewport 2.0 API”部分中的“Viewport 2.0 支持的着色器语义”。

光特定的语义（如 DIRECTION 和 AMBIENT）允许光由 Maya 驱动。例如，AMBIENT 允许用户在 Maya 属性编辑器中设置环境光颜色。

Maya 中的 GLSL 着色器支持在 [Viewport 2.0 中 dx11Shader 插件支持的语义和注释](../Viewport%202.0%20中%20dx11Shader%20和%20glslShader%20插件所支持的语义和注释.md)上列出的所有语义。

## 输入流和输出流的定义

然后 .ogsfx 文件定义输入流和输出流。

HIDE_OGSFX_STREAMS 设置为 0，#include 指令用于导入 Brix.glslf 和 Brix.glslv 着色器文件。

编译了顶点和碎片着色器文件中包裹在 #if !HIDE_OGSFX_STREAMS 和 #endif 内的代码。

在 #if !HIDE_OGSFX_STREAMS 和 #endif 包裹器内，#if OGSFX 和 #endif 语句将再次用于包裹 OGSFX 特定的代码。

## 实现顶点和碎片着色器的主要功能

然后 .ogsfx 文件实现顶点和碎片着色器的 main() 函数。

例如，HIDE_OGSFX_CODE 设置为 0，使用 #include 指令在单独的 GLSLShader 块内加载顶点和碎片着色器，如下所示：

```text
GLSLShader VS
{
#include "Brix.glslv"
}
```

编译了顶点和碎片着色器中包裹在 #if !HIDE_OGSFX_CODE 和 #endif 语句内的 main() 函数。只需要一个 main() 函数，但是 main() 可以定义和调用其他函数。

## 技术的定义

一个技术可以包含一个或多个过程。每个过程定义渲染对象的特定方式，并指定应该使用的顶点着色器和像素着色器。

您可以指定多个技术，如果具有多个顶点着色器和/或多个碎片着色器，则可以指定要将哪个着色器用于每个技术。在此示例中，仅定义了一个主技术。

在代码处理部分中，Brix.glslv 已加载并定义为 VS。

```text
GLSLShader VS
{
#include "Brix.glslv"
}
```

此处，在技术定义中，使用 VS 标识相同的顶点着色器文件：

```text
VertexShader (in appdata, out brixVertexOutput) = VS;
```

请确保在指定顶点和碎片着色器时列出的输入和输出参数与在顶点着色器和碎片着色器文件中定义的参数一致。

例如，在 Brix.glslv 中必须有名为 appdata 的匹配输入和名为 brixVertexOutput 的匹配输出。

```text
VertexShader (in appdata, out brixVertexOutput) = VS;
```
