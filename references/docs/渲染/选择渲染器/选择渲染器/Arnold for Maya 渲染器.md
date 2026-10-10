# Arnold for Maya 渲染器

**有关 MtoA 插件的综合文档，请访问 [Arnold for Maya 用户手册](https://docs.arnoldrenderer.com/display/A5AFMUGCHS/Arnold+for+Maya+User+Guide)**。

通过 mtoa.mll 插件默认安装 Maya 时，将随附提供 Arnold for Maya。此插件将自动加载，且 Arnold 将设置为 Maya 中的首选渲染器。

如果默认情况下未加载 Arnold，则可通过“插件管理器”(Plug-in Manager)（“窗口 > 设置/首选项 > 插件管理器”(Windows > Settings/Preferences > Plug-in Manager)）启用 mtoa.mll，手动进行加载。

## 在不安装 Arnold 的情况下安装 Maya

您可以选择在安装过程中禁用 Arnold for Maya 选项，退出 Arnold 安装。

## 结合使用现有的 Arnold 许可证与 Arnold for Maya

仅当您需要以不带水印的方式进行渲染时（例如，在批渲染过程中），才使用已存在的 Arnold 许可证。这些许可证不用于通过 Maya 进行交互式渲染。

## 将非原生 Arnold 着色器转换为最新版 Arnold for Maya

从 Maya 菜单中选择“Arnold > 工具 > 将着色器转换为 Arnold”(Arnold > Utilities > Convert Shaders to Arnold)。

## Arnold for Maya 与 Arnold 之间的区别

该本地版本的 Arnold for Maya 仅在 Maya 中以交互方式运行。您可渲染单帧或[以交互方式渲染帧序列](../../可视化和渲染图像/可视化和渲染图像/渲染场景/以交互方式渲染帧序列.md)；但是，无法进行批渲染或从 mayabatch.exe 调用，并且图像在显示时将带有水印。若要以不带水印的方式渲染图像，请从 [Solid Angle](https://www.autodesk.com.cn/products/arnold/subscribe) 购买 Arnold 批渲染节点。
