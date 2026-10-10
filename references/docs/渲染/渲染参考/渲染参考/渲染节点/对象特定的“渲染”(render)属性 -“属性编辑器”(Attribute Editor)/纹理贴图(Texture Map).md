# 纹理贴图(Texture Map)

在形状节点下“NURBS”的“属性编辑器”(Attribute Editor)中查找该区域。

## 纹理贴图(Texture Map)

提供了各种可调整的属性，以及使用 2D 纹理在对象上修复纹理扭曲的方法。这点非常有用，例如，像标志一样的波动构造。

#### 修复纹理扭曲(Fix Texture Warp)

纹理贴图属性仅适用于 NURBS 曲面。

**注**

如果曲面使用

“修复纹理扭曲”(Fix Texture Warp)

，则“转化为文件纹理”不支持

“修复纹理扭曲”(Fix Texture Warp)

，且转化材质时会将其忽略

。

为使纹理不依赖 NURBS 对象的 UV 参数化，“修复纹理扭曲”(Fix Texture Warp)会调整纹理的 UV 参数，从而使用 2D 纹理减轻对象上的纹理扭曲。例如，如果要使用“棋盘格”纹理创建标志并为其设置动画，则可以创建要在其上映射“棋盘格”纹理的 NURBS 平面，变换 CV，然后在对象的“属性编辑器”(Attribute Editor)中启用“修复纹理扭曲”(Fix Texture Warp)。

通过移动某些 CV 模拟吹动标志的风来为标志设置动画时，标志上的棋盘格图案会相应地展开和收缩。

![图：纹理贴图属性仅适用于 NURBS 曲面。 注： 如果曲面使用“修复纹理扭曲”(Fix Texture Warp)，则“转…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A6DA4B1C-9080-4A54-AAB4-30EE86E6490F.png) <!-- baize:img-hook downloaded=false reason="正文 1068 字 ≥300，非承重" -->

**注**

提示：

- 若要查看带纹理的曲面更新，必须在“渲染视图”(Render View)（“渲染 > 渲染当前帧”(Render > Render Current Frame)）中进行查看。重新渲染场景以查看修复的纹理。

- 由于计算精确的弧长成本非常高，因此“修复纹理扭曲”(Fix Texture Warp)是用于通过弦长实现间隔恰当的 UV 纹理值的一种折衷办法（其测量在曲面上两个点之间绘制的线的长度）。使用该功能可在不平坦参数化的曲面上更加均匀地应用纹理。

- 基于每个 NURBS 曲面应用“修复纹理扭曲”(Fix Texture Warp)。

#### 设定栅格大小(Setting the grid size)

“修复纹理扭曲”(Fix Texture Warp)处于启用状态时，Maya 纹理将基于曲面上放置的栅格的弦长位 2D NURBS 曲面贴图。可以通过在“每个 U 向跨度的栅格分段”(Grid Division Per Span U)和“每个 V 向跨度的栅格分段”(Grid Division Per Span V)中指定的值以及曲面上对应的跨度数来确定栅格的大小。默认的栅格大小为 4，且结果为 4 的倍数。

#### 每个 U 向跨度的栅格分段(Grid Div Per Span U)

指定 U 参数方向上“弦长”(Chord Length)栅格的每个跨度的分段数。

#### 每个 V 向跨度的栅格分段(Grid Div Per Span V)

指定 V 参数方向上“弦长”(Chord Length)栅格的每个跨度的分段数。
