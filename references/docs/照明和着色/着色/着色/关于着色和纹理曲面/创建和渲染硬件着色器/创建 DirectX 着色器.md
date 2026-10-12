# 创建 DirectX 着色器

1. 选择“窗口 > 渲染编辑器 > Hypershade”(Window > Rendering Editors > Hypershade)，以打开“Hypershade”窗口。

2. 在“创建”(Create)选项卡中，选择“Maya > 曲面 > DirectX 11 Shader”(Maya > Surface > DirectX 11 Shader)。

  将创建 DirectX 11 Shader，同时自动加载 AutodeskUberShader.fxo。

3. 按 6 以获得纹理模式，按 7 以使用场景照明。

**注**

提示：

纹理和非纹理模式均受支持，且所有灯光模式（

“使用所有灯光”(Use All Lights)

、

“使用选定灯光”(Use Selected Lights)

、

“不使用灯光”(Use No Lights)

和

“使用默认照明”(Use Default Lighting)

）均受支持。

**注**

加载 .fx 文件时，如果 DX11 着色器中的任何参数与您先前已加载的 .fx 文件中的参数名称和类型匹配，则这些参数将使用现有场景值，而不是新文件中的默认值。

例如，如果您有两个效果文件，其中 effect1.fx 的 gAmbient 参数默认值为“绿色”(green)，effect2.fx 的 gAmbient 参数默认值为“红色”(red)，您先加载第一个 effect1，然后再加载 effct2，加载 effect2 后，gAmbient 参数值仍为“绿色”(green)。此外，如果您加载 effect1，稍后将 gAmbient 颜色更改为“蓝色”(blue)并加载 effect2，则由于系统保留当前值，因此 gAmbient 仍为“蓝色”(blue)

这允许您从简单的效果切换至更复杂的效果，而不影响环境光和其他共享参数的当前场景值。

## 相关主题

- [在 DirectX 11 模式下运行 Viewport 2.0](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-EE108A86-9830-455E-BF2F-64A4075E8303)
