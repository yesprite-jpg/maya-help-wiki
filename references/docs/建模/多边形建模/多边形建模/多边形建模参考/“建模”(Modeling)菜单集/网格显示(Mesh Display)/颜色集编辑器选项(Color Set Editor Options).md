# 颜色集编辑器选项(Color Set Editor Options)

选择“网格显示 > 颜色集编辑器”(Mesh Display > Color Set Editor)时，可以设置以下选项。有关详细信息，请参见[颜色设置编辑器](../../多边形建模编辑器/颜色集编辑器%28Color%20Set%20Editor%29.md)。

“颜色集编辑器”(Color Set Editor)仅列出当前选定网格的颜色集。如果选定多个网格，则可以使用“颜色集编辑器”(Color Set Editor)对网格上具有相同名称的所有集进行编辑。例如，场景中所有网格可能都有日间和夜间的颜色集。

**注**

“颜色集编辑器”(Color Set Editor)仅列出选定的第一个网格的颜色集（或在一次选择多个网格的情况下仅列出拾取顺序中的第一个网格）。若要编辑多个网格公用的颜色集，请首先选择一个使用所有这些颜色集的网格，然后按住 Shift 键选择其他网格。

#### 新建(New)

为选定曲面创建新的颜色集。

#### 颜色范围(Color Range)

如果“钳制”(Clamped)处于启用状态，则值被钳制到 0 到 1 的范围。

#### 组件类型(Component Type)

仅指定“RGB”、“RGBA”或“A” (alpha)

#### 颜色集共享(Color Set Sharing)

指定是否“共享”(Shared)“逐顶点颜色”(Color Per Vertex)数据、“逐共享实例”(Per Instance Shared)或“逐非共享实例”(Per Instance Unshared)。

#### 重命名(Rename)

通过该选项可以重命名“颜色集编辑器”(Color Set Editor)列表中当前选定的颜色集。

#### 删除(Delete)

从曲面移除选定的颜色集及其数据。将其从“颜色集编辑器”(Color Set Editor)列表中删除。

#### 复制(Copy)

创建选定颜色集的副本。默认情况下，颜色集副本命名为 colorSetName1。

#### 修改(Modify)

从选定颜色集中指定一个 [polyColorMod](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Nodes/polyColorMod.html) 下游节点，以便将全局颜色修改应用到 HSV 颜色空间或 RGBA 颜色通道基础的颜色集。也可以在 polyColorMod 节点上对参数设置动画。

**注**

在

polyColorMod

节点对 HSV 和 RGBA 修改器进行的修改可累积。

#### 合并(Merge)

使用覆盖融合样式合并最顶部选定的颜色集和最底部选定的颜色集。“合并”(Merge)创建一个新的颜色集，将其指定给 [blendColorSets](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Nodes/blendColorSets.html) 节点，然后删除两个原始颜色集。将新合并的颜色集命名为最顶部选择的颜色集的名称。一次只能合并两个颜色集。

#### 融合(Blend)

将一个颜色集与另一个融合，然后将形成的融合创建成一个新的集。默认情况下，在“颜色集编辑器”(Color Set Editor)窗口，将融合颜色集命名为 blendedColorSet。一次只能融合两个颜色集。

#### 覆盖(Over)

将源颜色应用到基础颜色，如贴花。根据以下公式用源颜色的 Alpha 确定贴花的形状：

Blended color set = source color x source alpha + (base color x (1 - source alpha))

Blended color set alpha = 1 - ((1 - base color alpha) x (1 - source color alpha))

#### 相加(Add)

添加源颜色到基础颜色，好比通过滑动投影器将其投影到根部。在基本颜色上应用生成的颜色，并根据以下公式使用源 Alpha 来定义融合颜色集的不透明度：

Blended color set = base color + (source color x source alpha)

Blended color set alpha = base color alpha

#### 相减(Subtract)

从基础颜色中减去源颜色。在基本颜色上应用生成的颜色，并根据以下公式使用源 Alpha 来定义融合颜色集的不透明度：

Blended color set = base color - (source color x source alpha)

Blended color set alpha = base color alpha

#### 相乘(Multiply)

用基础颜色乘以源颜色。在基本颜色上应用生成的颜色，并根据以下公式使用源 Alpha 来定义融合颜色集的不透明度：

Blended color set = base color x (source color x source alpha + 1 - source alpha)

Blended color set alpha = base color alpha

#### 线性(Linear)

将源颜色和基础颜色添加到一起，但是，生成的融合颜色集中每个颜色的数量由“融合权重 A”(Blend Weight A)的值控制。

例如，如果“融合权重 A”(Blend Weight A)为 0.25，则 75% 的基础颜色和 25% 的源颜色将添加到一起，以根据以下公式创建融合颜色集：

Blended color set = (1- primary blend weight) x base color + primary blend weight x source color

Blended color set alpha = (1- primary blend weight) x base color alpha + primary blend weight x source color alpha

#### 双线性(Bilinear)

将源颜色和基础颜色添加到一起或使两者相减，但是，生成的融合颜色集中每个颜色的数量由“融合权重 A”(Blend Weight A)和“融合权重 B”(Blend Weight B)控制。

例如，如果“融合权重 A”(Blend Weight A)为 0.80，“融合权重 B”(Blend Weight B)为 0.80，则 80% 的基础颜色和 80% 的源颜色添加到一起，以创建融合颜色集。如果“融合权重 A”(Blend Weight A)为 1.0，“融合权重 B”(Blend Weight B)为 -1.0，则从 100% 的基础颜色中减去 100% 的源颜色，以根据以下公式创建融合颜色集：

Blended color set = primary blend weight x base color + secondary blend weight x source color

Blended color set alpha = primary blend weight x base color alpha + secondary blend weight x source color alpha

#### 通道(Channels)

将源颜色和基础颜色添加到一起，但是，生成的融合颜色集中每个颜色通道的数量应根据以下公式由“红”(Red)、“绿”(Green)、“蓝”(Blue)和“Alpha 权重”(Alpha Weights)控制：

Blended color set = Red + Blue + Green

Red = weight1 x source red + (1 - weight1) x base red

Green = weight2 x source green + (1-weight2) x base green

Blue = weight3 x source blue + (1-weight3) x base blue

Blended color set alpha = weight x source alpha + (1-weight) x base alpha

#### 上移(Move Up)

在“颜色集编辑器”(Color Set Editor)列表中将选定颜色集上移。

#### 下移(Move Down)

在“颜色集编辑器”(Color Set Editor)列表中将选定颜色集下移。

**注**

“上移”(Move Up)

和

“下移”(Move Down)

不在网格上创建历史。

## “颜色集编辑器”(Color Set Editor)菜单

#### “颜色”(Color)菜单

#### 应用颜色(Apply Color)

请参见[应用颜色选项](应用颜色选项%28Apply%20Color%20Options%29.md)。

#### 绘制顶点颜色工具(Paint Vertex Color Tool)

请参见[绘制顶点颜色工具选项](绘制顶点颜色工具选项%28Paint%20Vertex%20Color%20Tool%20Options%29.md)。

#### “预照明”(Prelight)菜单

请参见[“网格显示 > 预照明(Maya)”(Mesh Display > Prelight (Maya))](预照明选项%28Prelight%20Options%29.md)。

#### “显示”(Display)菜单

通过该菜单可以访问“着色显示”(Shaded Display)中的“颜色”(Color)、“对材质通道上色”(Color Material Channel)和“材质融合设置”(Material Blend Setting)多边形显示设置。
