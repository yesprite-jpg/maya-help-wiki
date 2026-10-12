# ShaderFX 自定义代码节点

“自定义代码”(Custom Code)节点可以让您编写自定义函数，并将其添加到着色器。

若要创建“自定义代码”(Custom Code)节点，请从 ShaderFX 菜单栏中选择“设置 > 切换高级模式”(Settings > Toggle Advanced Mode)以启用高级模式，然后选择“硬件着色器节点 > 各种 > 自定义代码”(Hw Shader Nodes > Various > Custom Code)。默认情况下，“自定义代码”(Custom Code)节点包含两个输入：“纹理”(Texture)和“采样器状态”(Sampler State)。每个此类输入的方形端口表示它可以接受多个输入。此节点可以让您从纹理读取像素。默认情况下，没有针对节点的输出。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-5B00CB4E-3FAD-4980-A1A8-5D75538FA5CF.png) <!-- baize:img-hook downloaded=false reason="正文 3050 字 ≥300，非承重" -->

按“属性编辑器”(Attribute Editor)中的“编辑”(Edit)，在显示的“自定义代码”(Custom Code)编辑器中输入您的代码。系统提供了一个基本编辑器，但您也可以在任意编辑器中编写代码并在代码完成后将其复制并粘贴到此代码中。系统还为您提供了一个 struct 和一个基本函数定义，便于您着手使用。

第一个 struct 表示输出；默认情况下，它是 float4 color。

```text
struct CustomCode1188Output
{
	float4 color;
};
```

函数定义用于定义输入参数；默认情况下，它是 float inputA。

```text
CustomCode1188Output CustomCode1188Func( float inputA )
```

“自定义代码”(Custom Code) “属性编辑器”(Attribute Editor)列出了“函数名称”(Function Name)：例如 CustomCode1188。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-11780673-96FE-4C60-8084-2FFA0532450B.png) <!-- baize:img-hook downloaded=false reason="正文 3050 字 ≥300，非承重" -->

您可以自定义“函数名称”(Function Name)；但是，struct、函数和“函数名称”(Function Name)都必须相同。

关闭编辑器之后，将会创建 inputA 输入和 color 输出。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-CB8EC51E-B350-493A-9480-1DA923ECCAA0.png) <!-- baize:img-hook downloaded=false reason="正文 3050 字 ≥300，非承重" -->

**注**

通过脚本创建

“自定义代码”(Custom Code)

节点时，必须在更新自定义代码后执行刷新操作，使该节点自我更新。您可以使用带有

edit_action

标志的

shaderfx

命令执行该操作。

## 着色器语言

着色器所用的语言有所不同，具体取决于渲染引擎和平台。

对于 Viewport 2.0：

- SFX_HLSL_5：对于 DirectX 11 模式

- SFX_OGSFX：对于 OpenGL 核心配置模式

- SFX_CGFX_3：对于 OpenGL 模式

对于样例：

- SFX_GLSL_4：对于 Linux/Windows 上的 OpenGL 以及运行 OpenGL 核心配置模式时的所有平台

- SFX_GLSL_1_2：对于 Mac OS X 上的 OpenGL

- SFX_HLSL_5：对于 DirectX 11

- SFX_SWATCH：对于在 ShaderFX 内部渲染样例（当在 Viewport 2.0 内进行渲染时值为 false）

不在 Maya 中使用：

- SFX_HLSL_3：可以导出

- _3DSMAX_：用于 3ds Max

对于 Maya：

- _MAYA_：如果在 Maya 中运行着色器，值为 true

如果打算同时使用 DirectX 和 OpenGL 模式，请确保您的函数支持这两种模式的语言。此外，还要确保您拥有为每种操作系统包含的语言。

## 示例

在此简单的示例中，输出是输入颜色乘以输入颜色。“自定义代码”(Custom Code)样例显示的蓝色比通过 inputA 连接的蓝色要深。

```text
struct CustomCode1181Output
{
    float3 color;
};

CustomCode1181Output CustomCode1181Func( float3 inputA )
{
    CustomCode1181Output OUT;
    OUT.color = float3(inputA*inputA);
    return OUT;
}
```

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-DA89E18E-226F-4A6A-B8E5-F4A678418959.png) <!-- baize:img-hook downloaded=false reason="正文 3050 字 ≥300，非承重" -->

以下示例演示了如何以 Maya 支持的几种语言对纹理进行采样，然后将采样值与输入颜色相乘。if/endif 和 ifdef/endif 语句将与编译时执行的 if 语句交换代码。

```text
struct CustomCode1178Output
{
    float3 color;
};

CustomCode1178Output CustomCode1178Func( float3 inputA, float2 UV )
{
    CustomCode1178Output OUT;

    float3 t = float3(0,0,0);
    #if defined(SFX_CGFX_3) || defined(SFX_HLSL_3)
        t = tex2D( SFX_SAMPLER0, float2(UV.x, 1-UV.y) ).xyz;
    #endif

    #ifdef SFX_HLSL_5
        #if defined(SFX_SWATCH) || defined(_3DSMAX_)
            t = SFX_TEXTURE0.Sample( SFX_SAMPLER0, UV );
        #else
            t = SFX_TEXTURE0.Sample( SFX_SAMPLER0, float2(UV.x, 1-UV.y) );
        #endif
    #endif

    #ifdef SFX_GLSL_4
        t = texture( SFX_TEXTURE0, float2(UV.x, 1-UV.y) ).xyz;
    #endif

    #ifdef SFX_GLSL_1_2
        t = texture2D( SFX_TEXTURE0, float2(UV.x, 1-UV.y) ).xyz;
    #endif

OUT.color = inputA * t;

return OUT;
}
```

在创建“自定义代码”(Custom Code)节点时，将会创建下列节点并按照下图所示进行连接：

- 硬件着色器节点 > 纹理 > 纹理分量(Hw Shader Nodes > Textures > Texture Component)

- 硬件着色器节点 > 纹理 > 采样器状态(Hw Shader Nodes > Textures > Sampler State)

- 硬件着色器节点 > 值 > 颜色(Hw Shader Nodes > Values > Color)

- 硬件着色器节点 > 公共输入 > UV 集(Hw Shader Nodes > Inputs Common > UV Set)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E30857F1-EACD-4E37-9750-DA7C3E80B5D1.png) <!-- baize:img-hook downloaded=false reason="正文 3050 字 ≥300，非承重" -->

现在，当您使用 DirectX 11 时，Viewport 2.0 中的纹理和样例使用 SFX_HLSL_5 代码进行采样。当您使用 OpenGL 时，Viewport 2.0 中的纹理使用 SFX_CGFX_3 代码进行采样，而样例使用 SFX_GLSL_4 代码进行采样（对于 Linux/Windows）。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-11A8B01A-C19B-4CCD-AFBA-31B74606CD45.png) <!-- baize:img-hook downloaded=false reason="正文 3050 字 ≥300，非承重" -->

“自定义代码”(Custom Code)编辑器中的注释还建议您使用 SFX_TEXTURE[n] 或 SFX_SAMPLER[n] 来引用纹理。这样，您就无需对纹理名称（例如，grass_texture_A）进行硬编码。SFX_TEXTURE[n] 和 SFX_SAMPLER[n] 是指连接纹理的顺序。您连接的第一个“纹理分量”(Texture Component)/“采样器状态”(Sampler State)节点对分别是 SFX_TEXTURE[0] 和 SFX_SAMPLER[0]，下一对分别是 SFX_TEXTURE[1] 和 SFX_SAMPLER[1]。在上图中可以发现，从“纹理分量”(Texture Component)和“采样器状态”(Sampler State)节点发出的连接也指示 0。

下面是一个具有两个“纹理分量”(Texture Component)/“采样器状态”(Sampler State)对的示例图。一对的连接指示 0，另一对的连接指示 1。为了更好地进行组织，您可能还需要对节点进行分组。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-DE0A1F28-F520-4C21-A179-143212A65AF7.png) <!-- baize:img-hook downloaded=false reason="正文 3050 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A5E991D8-8397-4406-8A9F-FE6885B3E680.png) <!-- baize:img-hook downloaded=false reason="正文 3050 字 ≥300，非承重" -->
