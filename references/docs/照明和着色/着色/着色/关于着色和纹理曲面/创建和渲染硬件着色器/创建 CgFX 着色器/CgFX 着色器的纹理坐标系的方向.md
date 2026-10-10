# CgFX 着色器的纹理坐标系的方向

在编译 CgFX 着色器时，CgFX 插件会将编译宏 MAYA_TEXCOORD_ORIENTATION_OPENGL 或 MAYA_TEXCOORD_ORIENTATION_DIRECTX 设置为 1，以指定用于纹理坐标系的方向。

将 MAYA_TEXCOORD_ORIENTATION 环境变量设定为 OPENGL 或 DIRECTX，以分别定义 MAYA_TEXCOORD_ORIENTATION_OPENGL 或 MAYA_TEXCOORD_ORIENTATION_DIRECTX 宏。定义宏之后，该宏将设定为 1。

#### OPENGL

指定使用 OpenGL 约定。在该约定中，纹理的原点位于纹理的左下角。

#### DIRECTX

指定使用 DirectX 约定。在该约定中，纹理的原点位于纹理的左上角。

对于 Maya 2011 和较低版本，上述两个宏均未定义，且着色器应采用 DirectX 纹理坐标系的方向。

对于 Maya 2012 和更高版本，默认情况下，MAYA_TEXCOORD_ORIENTATION_OPENGL 宏设置为 1。在启动 Maya 之前，通过将环境变量 MAYA_TEXCOORD_ORIENTATION 设定为 DirectX，可以更改默认设置。

将默认渲染器或硬件渲染器与着色器（指为 Maya 先前版本编写、且尚未经过修改、无法支持 OPENGL 纹理坐标方向的着色器）一起使用时，将 MAYA_TEXCOORD_ORIENTATION 环境变量设定为 DirectX 十分有用。在 MAYA_TEXCOORD_ORIENTATION 环境变量设置为 DirectX 时，将出现以下情况：

- 着色器将使用设定为 1 的 MAYA_TEXCOORD_ORIENTATION_DIRECTX 宏进行编译。

- 纹理将使用 DirectX 方向进行加载。

- 默认渲染器和硬件渲染器将使用 DirectX 方向生成 UV 坐标。

- 但是，使用 OpenGL 方向存在限制，它将导致 Viewport 2.0 仍然生成 UV 坐标。这可能会导致使用 Viewport 2.0 时纹理将沿 V 轴翻转渲染。

这将会更改 UV 坐标的生成和纹理图像的加载，如果着色器使用 UV 坐标采样纹理，则渲染的图像在两个坐标系中均相同。但是，当使用着色器以程序方式生成的 UV（相对于由 Maya 生成的、来自于 UV 源流中的 UV）对纹理进行采样时，插件必须能够控制两种约定。$ (MAYA_ROOT) /presets/CgFX/example 中包含的 brix.cgfx 示例举例说明了上述运行方式：

```text
/******************** pixel shader *********************/
#ifdef MAYA_TEXCOORD_ORIENTATION_OPENGL
     float GBalanceCorr = 1.0f - GBalance;
 #else
     float GBalanceCorr = GBalance;
#endif

    float v = ((float4)tex2D(stripeSampler,float2(IN.BrickUV.x,0.5))).x;
    float4 dColor1 = lerp(SurfColor1,SurfColor2,v);
    v = ((float4)tex2D(stripeSampler,float2(IN.BrickUV.x*2,GBalanceCorr))).x;
    dColor1 = lerp(GroutColor,dColor1,v);
    v = ((float4)tex2D(stripeSampler,float2(IN.BrickUV.x+0.25,0.5))).x;
    float4 dColor2 = lerp(SurfColor1,SurfColor2,v);
    v = ((float4)tex2D(stripeSampler,float2((IN.BrickUV.x+0.25)*2,GBalanceCorr))).x;
    dColor2 = lerp(GroutColor,dColor2,v);
    v = ((float4)tex2D(stripeSampler,float2(IN.BrickUV.y,0.5))).x;
    float4 brix = lerp(dColor1,dColor2,v);
    v = ((float4)tex2D(stripeSampler,float2(IN.BrickUV.y*2,GBalanceCorr))).x;
    brix = lerp(GroutColor,brix,v);
       return IN.DCol * brix;
}
```
