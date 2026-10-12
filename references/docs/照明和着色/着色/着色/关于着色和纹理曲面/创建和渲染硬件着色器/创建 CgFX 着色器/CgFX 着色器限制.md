# CgFX 着色器限制

Cgfx 着色器基于传统技术，因此不再建议使用。请改用 [GLSL 着色器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-BD177012-56E1-43D0-B7A5-F4B1A70EA846.htm)。

“CgFX 着色器”(CgFX shader)的“已知限制”(Known limitations)包括：

- 仅支持 .cgfx 文件，不支持 .cg

- 前期和后期效果（例如，全屏效果、全局效果、多过程效果）

- 过程脚本编写

- Cg 界面

- 时间语义：在使用随时间移动的着色器时，必须刷新场景才能查看动画（例如，通过翻滚摄影机）。

  CgFX 着色器仅在“OpenGL - 旧版”(OpenGL - Legacy)和“OpenGL - 核心配置(兼容性)”(OpenGL - Core Profile (Compatibility))显示模式下受支持。请参见 [Viewport 2.0 渲染引擎](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BF017019-B89A-47F0-8AB5-106C058AB854#GUID-BF017019-B89A-47F0-8AB5-106C058AB854__SECTION_B04F0E5A1332417DA2CD3FE483F186D4)。

有关 CG 语言的重要信息（包括 CgFX 插件的限制），请访问 nVidia 网站 ([www.developer.nvidia.com](http://www.developer.nvidia.com))，特别是访问 [https://developer.nvidia.com/cg-toolkit](https://developer.nvidia.com/cg-toolkit)。

不支持使几何体变形的着色器。

如果 CgFX 着色器使用 nVidia 特定的剖面，则必须使用 nVidia 显卡。否则，无法在场景视图中预览这些着色器。

**注**

在 Linux 平台上，Maya 硬件工作区不支持远程显示或任何间接渲染设备上的 GLSL 或 Cg 着色语言。
