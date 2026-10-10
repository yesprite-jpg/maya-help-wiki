# Viewport 2.0 的内部纹理烘焙

Viewport 2.0 中不支持的以下纹理类型将在内部烘焙：

支持以下着色器为已烘焙：

- 布朗(Brownian)

- 云(Cloud)

- 凹陷

- 花岗岩

- 皮革

- 大理石

- 岩石(Rock)

- 匀值分形(Solid Fractal)

- 灰泥(Stucco)

- 体积噪波(Volume Noise)

- 水

- 木材

- 3D 程序凹凸贴图

若要提高性能并避免对这些纹理进行长时间烘焙，请降低其烘焙分辨率。

若要提高渲染中已烘焙纹理的质量，请提高其烘焙分辨率。

若要修改这些内部烘焙纹理的分辨率，请执行以下操作：

1. 从面板菜单中，选择“渲染器 > Viewport 2.0”(Renderer > Viewport 2.0) > ![图：从面板菜单中，选择“渲染器 Viewport 2.0”(Renderer Viewport 2.0) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 558 字 ≥300，非承重" -->。

2. 在“硬件渲染器 2.0 设置”(Hardware Renderer 2.0 Settings)下，展开“不支持的纹理类型的烘焙分辨率”(Bake Resolution for Unsupported Texture Types)标题（在“性能”(Performance)下）。

3. 修改“颜色纹理”(Color Textures)值。例如，将它增至 2048 以渲染具有更高质量的纹理；或者，将它减至 32 以提高性能。

4. 单击“重新烘焙所有纹理”(Rebake All Textures)以查看更改的效果。

**注**

烘焙纹理的执行速度可能会变慢，具体取决于烘焙分辨率。此外，如果烘焙分辨率设置得太低，烘焙纹理可能会以低质量渲染。
