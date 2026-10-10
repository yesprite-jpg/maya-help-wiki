# 折痕集编辑器(Crease Set Editor)菜单

## 编辑菜单

#### 从选定对象中选择折痕集(Select Crease Sets from Selection)

亮显“折痕集编辑器”(Crease Set Editor)中与选定折痕组件关联的折痕集。仅当已选择网格或组件时可用。

#### 将折痕值烘焙到网格(Bake Crease Values to Mesh)

将折痕集中的折痕值直接传递到网格，并从折痕集中移除边和顶点。仅当已选择网格或折痕集时可用。

#### 从网格创建折痕集(Create Crease Sets from Mesh)

将现有网格折痕值转化为具有相同值的折痕集。仅当已选择网格时可用。

#### 细分基础网格(Subdivide Base Mesh)

将基础网格细化一个细分级别，并将折痕值减少一。生成的细分网格与原始网格相同，但基础网格面数更多。仅当已选择网格或折痕集时可用。

#### 从折痕值设置边的硬度(Set Edge Hardness from Crease Values)

硬化或软化网格中的边以匹配当前折痕集值。仅当已选择网格或折痕集时可用。

## 显示(Display)

选择网格或折痕集后，以下选项将可用：

#### 最佳网格细分级别(Optimal Mesh Subdivision Level)

调整网格形状节点的“预览分段级别”(Preview Division Levels)属性（位于“属性编辑器”(Attribute Editor)的“平滑网格 > 细分级别”(Smooth Mesh > Subdivision Levels)区域），以使其值大于网格的最大[“折痕”(Crease)](“折痕集编辑器”%28Crease%20Set%20Editor%29列表和操作按钮.md)值。这显示了对所生成细分曲面应用折痕值的完整效果。

#### 默认网格细分级别(Default Mesh Subdivision Level)

将网格形状节点的“预览分段级别”(Preview Division Levels)属性（位于“属性编辑器”(Attribute Editor)的“平滑网格 > 细分级别”(Smooth Mesh > Subdivision Levels)区域中）设置为其默认值 2。

#### 创建/更新折痕颜色集(Create/Update Crease Color Set)

创建或更新用于表示网格折痕值的颜色集。值的范围从蓝色（无折痕）到红色（折痕值大于 4）。详细信息请参见[多边形颜色集](../../../多边形上色/多边形颜色集.md)。

**注**

提示：

若要查看颜色集，对象必须处于着色模式（

“着色 > 对所有项目进行平滑着色处理”(Shading > Smooth Shade All)

）。

#### 显示/隐藏折痕颜色集(Show/Hide Crease Color Set)

显示或隐藏以前计算的网格折痕颜色集。

## 设置菜单

#### 折痕级别拖动增量(Crease Level Drag Increment)

用于设置当您在“折痕”(Crease)字段中使用鼠标中键拖动以增加或减少折痕值时所依据的增量。

#### 默认折痕集名称(Default Crease Set name)

用于设置折痕集的命名约定。创建折痕集时，默认名称为 creaseSet#。

## 相关主题

- [折痕集编辑器(Crease Set Editor)](../折痕集编辑器%28Crease%20Set%20Editor%29.md)

- [“折痕集编辑器”(Crease Set Editor)上下文相关菜单](“折痕集编辑器”%28Crease%20Set%20Editor%29上下文相关菜单.md)
