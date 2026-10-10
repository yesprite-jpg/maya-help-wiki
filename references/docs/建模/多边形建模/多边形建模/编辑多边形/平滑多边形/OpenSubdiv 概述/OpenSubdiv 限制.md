# OpenSubdiv 限制

## OpenSubdiv 的一般限制

- OpenSubdiv 不支持：

  - 非流形网格

    Maya 自动将包含非流形组件的网格默认设置为“Maya Catmull-Clark”。

    当“OpenSubdiv”无法使用时，会在“脚本编辑器”(Script Editor)和 polyShape 节点中显示错误消息，指示“Maya Catmull-Clark”细分方法处于活动状态。

    **注**

    建模操作可以临时生成非流形组件。当非流形网格变为流形网格时，警告消息会消失，并且细分方法会自动切换为

    “OpenSubdiv”

    。

- 由于驱动程序存在问题，OpenSubdiv Catmull-Clark 均匀细分方法的 OpenCL 加速无法在使用 Quadro 4000 显卡的 Mac OS X 系统上正常运行。若要禁用加速，请使用环境变量 MAYA_OPENCL_IGNORE_DRIVER_VERSION = 1。

## OpenSubdiv Catmull-Clark 自适应限制

- “OpenSubdiv Catmull-Clark 自适应”(OpenSubdiv Catmull-Clark Adaptive)不支持：

  - 景深(Depth of field)

  - 使用默认材质(Use Default Material)

  - 深度剥离

  - 通过 MPxShaderOverride 实施的插件着色器

- “OpenSubdiv Catmull-Clark 自适应”(OpenSubdiv Catmull-Clark Adaptive)仅支持 OpenGL 4 和 DirectX11 兼容显卡。

  当 OpenGL 4 或 DirectX11 不受支持时，Maya 将自动默认为“Maya Catmull-Clark”。

## OpenSubdiv 置换预览限制

“OpenSubdiv 置换”(OpenSubdiv Displacement)预览源自“OpenSubdiv Catmull-Clark 自适应”(OpenSubdiv Catmull-Clark Adaptive)，因此共享其限制。

- 此外，“OpenSubdiv 置换”(OpenSubdiv Displacement)预览不支持：

  - 文件纹理节点参数（Alpha 增益等）。

  - 非切线空间向量置换（即，不支持全局空间）。

## 相关主题

- [OpenSubdiv 概述](../OpenSubdiv%20概述.md)
