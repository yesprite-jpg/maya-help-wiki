# 编写自定义 GLSL 着色器：细分示例

若要编写自定义 GLSL 着色器，请将它另存为 .ogsfx 文件。有关如何编写 GLSL 着色器的示例，请参见 Maya 安装的 ..\presets\GLSL\examples 文件夹中的 TessellationExample.ogsfx 文件。该示例演示了如何编写图形流水线中的细分控制着色器、细分求值着色器和几何体着色器。

在此着色器中，定义了以下两种技术：主技术（它显示着色的视图）和线框技术（它显示说明细分的线框）。若要设置细分的内部级别和外部级别，可以在 Viewport 2.0 中调整“内部级别/100*100 像素”(Inner levels/100*100 pix)（100 x 100 像素区域中的内部级别数）和“外部级别/30 像素”(Outer levels/30 pix)（每 30 像素分段的级别数）设置并查看效果。

## 图形流水线的阶段

线框技术定义包括图形流水线的五个阶段，其顺序如下：

- 顶点着色器

- 细分控制着色器

- 细分求值着色器

- 几何体着色器

- 像素着色器

## 细分着色器

有关如何创建细分控制着色器（它通过操纵控制点 (cp) 生成输出面片，并计算细分级别）的示例，请参见 .ogsfx 文件中的 GLSLShader ShaderTessControl 部分。

有关如何计算由基本体生成器生成的对应域的顶点的示例，请参见 .ogsfx 文件中的 GLSLShader ShaderTessEval 部分。

在 Maya 中执行细分时，细分控制着色器和细分求值着色器要求输入采用 PNAEN18 格式。PNAEN18（使用相邻边法线的点-法线三角形）为具有如下数据的每个三角形创建索引：三角形的顶点索引以及三角形的相邻边和主要边的顶点索引。它为索引数组创建步幅 18。

有关 PNAEN 的详细信息，请参见** Maya 开发人员帮助**的*“Viewport 2.0 API”*部分中的*“自定义着色器的几何数据”*。

必须在技术定义中将输入缓冲区类型指定为 PNAEN18：

```text
string index_buffer_type = "GLSL_PNAEN18";
```

## 几何体着色器

需要有几何体着色器，才能支持线框和细分。细分着色器所创建的新基本体由几何体着色器重新组合到三角形中，像素着色器随后将绘制这些三角形。

## 用于在您的技术中定义着色器的关键字

使用以下关键字可定义着色器：

- VertexShader

- TessControlShader

- TessEvaluationShader

- GeometryShader

- PixelShader

对于每个关键字，提供您的输入和输出参数并将关键字设置为着色器的名称，例如，如下所示：

```text
VertexShader (in APPDATA, out SHADERDATA VS_OUT) = VS;
TessControlShader (in SHADERDATA TCS_IN, out TCSDATA TCS_OUT) = ShaderTessControl;
TessEvaluationShader (in TCSDATA TES_IN, out SHADERDATA2 TES_OUT) = ShaderTessEval;
GeometryShader ( in SHADERDATA2 GEO_IN , out SHADERDATA2 GEO_OUT ) = GS_Wireframe;
PixelShader (in SHADERDATA2 PS_IN, out pixelOut) = PS_Wireframe;
```

输入和输出参数可以是您在 .ogsfx 文件中定义的任何数据类型。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-B6888C5A-42FC-455A-9BD8-8B3E4C5375F5.png) <!-- baize:img-hook downloaded=false reason="正文 1396 字 ≥300，非承重" -->
