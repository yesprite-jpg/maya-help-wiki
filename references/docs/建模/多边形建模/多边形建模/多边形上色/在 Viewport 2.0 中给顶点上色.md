# 在 Viewport 2.0 中给顶点上色

可以根据影响或颜色集给顶点上色。

## 根据影响给顶点上色

将几何体绑定到骨架或关节并选择“显示 > 多边形 > 顶点”(Display > Polygons > Vertices)后，顶点将根据影响进行上色。

在几何体形状节点“属性编辑器”(Attribute Editor)中，“网格控制 > 顶点颜色源”(Mesh Controls > Vertex Color Source)将自动设置为“影响颜色”(Influence Colors)。

## 根据颜色集给顶点上色

1. 例如，通过使用“绘制顶点颜色工具”(Paint Vertex Color Tool)，将绘制添加到几何体。

2. 在几何体的形状节点“属性编辑器”(Attribute Editor)中的“网格控制”(Mesh Controls)下，将“顶点颜色源”(Vertex Color Source)设置为“当前颜色集”(Current Color Set)。

3. 顶点组件现在将在当前颜色集上拾取。

**注**

选择

“显示 > 多边形 > 顶点”(Display > Polygons > Vertices)

以显示顶点的上色情况。
