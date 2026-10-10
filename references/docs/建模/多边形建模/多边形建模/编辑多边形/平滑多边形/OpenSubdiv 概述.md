# OpenSubdiv 概述

OpenSubdiv 是由 Pixar 开发的开源细分方法，通过此方法，您可以在保证高精度和高速度的情况下使用高保真模型表示。作为动画行业的专业标准，OpenSubdiv 在各种软件包中实施，当模型在应用程序之间传递时可产生相同的结果，从而提高了互操作性。在 Maya 中，预览平滑网格、使用“网格 > 平滑”(Mesh > Smooth)平滑网格或创建细分曲面代理时，OpenSubdiv 是默认的细分方法。

OpenSubdiv 是对旧版“Maya Catmull-Clark”细分方法的改进替代方法。例如，OpenSubidv 利用平行 GPU 和 CPU 结构，通过较高的细分级别提高了网格的视口性能。此外，在[平滑网格](../../多边形建模参考/多边形节点/平滑网格%28Smooth%20Mesh%29.md#GUID-FF35F773-1FC0-4EBA-A64C-6199375F489A__GUID-2EA84CBD-5246-4233-9349-A20EB450DF66)属性中，可以启用置换预览(Displacement Preview)来以交互方式可视化置换贴图，而无需进行渲染（请参见[在视口中预览置换结果](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-50A6338F-ACBE-472C-9C81-D1820CD61048)）。

您可以选择以下 OpenSubdiv 细分方法之一：

- OpenSubdiv Catmull-Clark 一致(OpenSubdiv Catmull-Clark Uniform)：对网格面应用统一的细化方案。整个网格会收到相同级别的细分。

- OpenSubdiv Catmull-Clark 自适应(OpenSubdiv Catmull-Clark Adaptive)：对不规则的网格部分应用逐步细化方案。自适应细分仅细化需要其他细节的网格拓扑。细化级别由网格拓扑和摄影机视图决定。例如，接近摄影机的网格拓扑比同一网格上较远的拓扑更精细。在当前实现中，自适应细分可以提高网格的平滑度，而无需增加其细分级别。在 [OpenSubdiv 控件(OpenSubdiv Controls)](../../多边形建模参考/多边形节点/平滑网格%28Smooth%20Mesh%29.md#GUID-FF35F773-1FC0-4EBA-A64C-6199375F489A__SECTION_AEC2592F09DA47ACBB9901F1310E01E9)中将“自适应细分级别”(Adaptive Tessellation Level)设置为一个较高的值以查看结果，而不影响场景的性能。

  **注**

  仅 OpenGL 4 和 DirectX11 兼容显卡支持“OpenSubdiv Catmull-Clark 自适应”(OpenSubdiv Catmull-Clark Adaptive)

  。
