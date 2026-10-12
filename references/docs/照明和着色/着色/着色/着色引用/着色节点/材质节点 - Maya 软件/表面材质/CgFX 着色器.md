# CgFX 着色器

**注**

Cgfx 着色器基于传统技术，因此不再建议使用。请改用

GLSL 着色器

。

Maya 中经过编译的 CgFX 插件允许您创建硬件着色器。以前，您可能已从 nVidia® 下载了 Cg/CgFx 库。有关详细信息，请参见[创建和渲染硬件着色器](../../../../关于着色和纹理曲面/创建和渲染硬件着色器.md)。

CgFX 着色器仅在“OpenGL - 旧版”(OpenGL - Legacy)和“OpenGL - 核心配置(兼容性)”(OpenGL - Core Profile (Compatibility))显示模式下受支持。请参见 [Viewport 2.0 渲染引擎](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BF017019-B89A-47F0-8AB5-106C058AB854#GUID-BF017019-B89A-47F0-8AB5-106C058AB854__SECTION_B04F0E5A1332417DA2CD3FE483F186D4)。

有关如何创建 CgFX 着色器的信息，请参见[创建 CgFX 着色器](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建%20CgFX%20着色器.md)。

**注**

该插件使用 Cg 3.0.015 版。Cg 编译器 (cgc) 和所有 dll 均包含在 Maya 的存储箱目录中。

旧效果支持另一不同的语法 .fx (MS) 文件，而当前效果支持：.cgfx。由于 CG 是 HLSL 的超集，因此，CGFX 3.0.015 拥有 Cg 的所有容量（界面和未标注大小的数组）。因此，CgFX 3.0.015 采用名为 .cgfx 的格式，允许开发人员使用 Cg 语言进行编程。

如果已安装 CgFX 的旧版本，则必须先将其卸载，或禁用随安装设定的环境变量。

## 相关主题

- [创建 CgFX 着色器](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建%20CgFX%20着色器.md)

- [编写 CgFX 着色器](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建%20CgFX%20着色器/编写%20CgFX%20着色器.md)

- [CgFX 着色器限制](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建%20CgFX%20着色器/CgFX%20着色器限制.md)

- [CgFX 着色器的纹理坐标系的方向](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建%20CgFX%20着色器/CgFX%20着色器的纹理坐标系的方向.md)

- [CgFX 着色器疑难解答](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建%20CgFX%20着色器/CgFX%20着色器疑难解答.md)
