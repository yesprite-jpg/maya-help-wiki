# “细分曲面到多边形”(Subdiv to Polygons)选项

使用以下选项可设置在选择“修改 > 转化 > 细分曲面到多边形”(Modify > Convert > Subdiv to Polygons)时发生的情况。

### 细分方法(Tessellation Method)

选择以下一种细分方法。

#### 一致(Uniform)

“一致”(Uniform)细分生成的多边形在每个细分曲面的基础网格面上都具有相同数量的面（级别 0 的面）。

#### 多边形计数(Polygon Count)

“多边形计数”(Polygon Count)方法与“一致”(Uniform)方法基本相同，只是具有阈值，超出该阈值转化将会失败。使用“最大多边形数”(Maximum Number Polygons)设置该值。生成的多边形最多有该数量的多边形，但不能保证数量精确。

#### 自适应(Adaptive)

“自适应”(Adaptive)细分生成的多边形在细分曲面的每个最精细级别面上具有相同数量的面。某个细分曲面区域的细化程度越高，生成的多边形在该区域中的面就越多。使用“每个面的分段数”(Divisions Per Face)可控制对于每个最精细级别的面生成的面数。

#### 顶点(Vertices)

生成匹配细分曲面上顶点的多边形。多边形匹配顶点的级别在“级别”(Level)选项中指定。

#### 级别(Level)

如果使用“一致”(Uniform)选项，设置级别可以确定细分中使用的面数。例如，“级别”(Level)为 3，则细分中将使用级别 3 上的面。

#### 每个面的分段数(Divisions Per Face)

指定执行“一致”(Uniform)或“自适应”(Adaptive)细分时每个面应分割的次数。增加该值将平滑多边形曲面。

#### 最大多边形数(Maximum Number Polygons)

设置“多边形计数”(Polygon Count)细分使用的多边形数量阈值。

### 原始对象(Original Object)

选择细分后要对原始选定对象进行的操作。使用“原始对象”(Original Object)设置可以维护某种形式的构建历史，因为这些设置将覆盖全局构建历史设置。

#### 替换(Replace)

创建多边形曲面后删除细分曲面。这是默认设置。

#### 隐藏(Hide)

“隐藏”(Hide)将保留细分曲面，但会在创建多边形曲面时隐藏该细分曲面。可以在“Hypergraph”和“大纲视图”(Outliner)中查看源对象（选择“输入和输出连接”(Input and Output Connections)），并且使用“显示 > 显示”(Display > Show)>“显示当前选择”(Show Selection)或“全部”(All)可以使源对象在建模视图中可见。

#### 显示

“显示”将保留细分曲面并使其在建模视图中可见。

#### 共享 UV (Share UVs)

启用该选项后，生成的多边形将保留原有 UV 网格边界。如果禁用该选项，则将为每个多边形面创建 UV 边界。
