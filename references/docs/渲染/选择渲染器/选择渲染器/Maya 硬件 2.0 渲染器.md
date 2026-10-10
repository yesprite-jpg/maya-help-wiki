# Maya 硬件 2.0 渲染器

使用 Maya 硬件 2.0 渲染器执行“Viewport 2.0”命令行渲染或批渲染到磁盘或“渲染视图”(Render View)。

可以使用以下方法选择 Maya 硬件 2.0 渲染器：

- [渲染视图](../../渲染参考/渲染参考/渲染窗口和编辑器/渲染视图%28Render%20View%29.md)窗口

- [渲染设置窗口](../../渲染参考/渲染参考/渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)

- 渲染 > 批渲染(Render > Batch Render)（有关信息，请参见[批渲染选项](../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/批渲染选项%28Batch%20Render%20Options%29.md)）

- 在命令行中使用 Render 命令

- 通过提示模式的命令行 (-prompt)

- 通过批处理模式的命令行 (-batch)

- 通过脚本编辑器的 MEL 选项卡 (ogsRender)

**注**

在

“渲染视图”(Render View)

窗口中使用 Maya 硬件 2.0 渲染器或在脚本编辑器中使用 ogsRender 命令进行渲染前，必须先在面板菜单中选择

“渲染器 > Viewport 2.0”(Renderer > Viewport 2.0)

。

支持的功能

- 支持“渲染设置”(Render Settings)窗口的“公用”(Common)选项卡中的“文件输出”(File Output)设置。

- 支持来自不同摄影机类型（包括立体摄影机）的渲染。

硬件 2.0 渲染器的限制

- 在“渲染视图”(Render View)窗口中：

  - 不支持渲染区域。

  - 不支持 IPR。

- 不支持渲染层。

- 仅支持颜色输出。目前不支持深度通道。

## 相关主题

- [使用 Viewport 2.0](../../使用%20Viewport%202.0/使用%20Viewport%202.0.md)
