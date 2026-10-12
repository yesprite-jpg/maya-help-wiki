# HLSL 着色器

HLSL（高级着色语言）着色器节点可以在 Maya 中创建和配置本地 HLSL 硬件着色器。HLSL 是 Direct X 的原生着色语言，因此对于许多基于 Direct X 的目标应用程序是首选的着色语言，包括适用于 XBOX 系列控制台的游戏。与 Maya 中的上一个 HLSL 支持不同，HLSL 着色器提供本地 Direct X 编译渲染。

有关如何创建 HLSL 着色器的信息，请参见[创建 HLSL 着色器](../../../../关于着色和纹理曲面/创建和渲染硬件着色器/创建%20HLSL%20着色器.md)。

**注**

dx11Shader.mll 是用于创建 Direct X 着色器的首选插件。因此，不再随标准 Maya 安装提供 HLSL 插件。

为了向后兼容，可以从 Maya Bonus Tools 软件包（从 Maya 菜单中选择“帮助 > Maya 资源和工具 > 下载 Bonus Tools”(Help > Maya Resources and Tools > Download Bonus Tools)）下载 hlslShader.mll，或者从 [Autodesk Developer Network](https://www.autodesk.com/developmaya) 上的开发人员工具包中下载 *hlslShader* 插件示例。

该功能需要安装 2007 年 2 月版的 Direct X。

若要将旧的 .FX 文件转换为新的 .cgfx 格式，请使用 NVIDIA 提供的转换工具。Cg 和 CgFX 还提供了大量文档。请参见 [www.developer.nvidia.com](http://www.developer.nvidia.com)。

## HLSL 限制和其他注释

HLSL 着色器当前仅受默认 Maya 场景视图支持。当前，不支持高质量渲染器或外部渲染器。

不能在 Maya 中使用包含某些效果的 HLSL 着色器：

- 全局效果

- 多过程效果

HLSL 插件当前不支持可以使几何体变形的着色器。将可以看到这些效果，但在将 DX 和 GL 场景元素合成在一起时可能会存在瑕疵。

**注**

在 Linux 平台上，Maya 硬件工作区不支持远程显示或任何间接渲染设备上的 GLSL 或 Cg 着色语言。
