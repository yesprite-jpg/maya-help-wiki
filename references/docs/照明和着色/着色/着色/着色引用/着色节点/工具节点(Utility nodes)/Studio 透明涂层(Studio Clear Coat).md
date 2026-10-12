# Studio 透明涂层(Studio Clear Coat)

该工具是插件 (studioImport.mll)。您可以在以下情况中使用该节点：特定材质（如车漆）根据查看方向和曲面方向之间的关系会以不同方式反射灯光。

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用 Studio 透明涂层工具](../../../渲染节点工具/使用“Studio%20透明涂层”%28Studio%20Clear%20Coat%29工具.md)。

studioClearCoat 是单独节点。在 Maya 中，复杂的着色网络可以使用多个较小节点构建，但因为 studioClearCoat 是其自己的节点，所以可以将其应用于任何材质（甚至插件材质）。将 studioClearCoat 节点的输出连接到材质的“反射率”(Reflectivity)。

您可以使用 IPR 调节 studioClearCoat 属性。将 studioClearCoat 节点的输出应用于“表面着色器”(Surface Shader)节点的颜色时，该功能非常强大。

下图中，白色显示了最大反射率，黑色显示了最小反射率。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-32C00901-35A9-46F7-8EC3-7AD781133108.png) <!-- baize:img-hook downloaded=false reason="正文 769 字 ≥300，非承重" -->

如果满意 studioClearCoat 设置，可以将输出连接回材质的“反射率”属性并确信结果。

下图是使用 studioClearCoat 插件生成的。请注意汽车引擎盖和顶部的反射率是如何高于汽车前部和侧面的。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-F29727D3-5485-4E66-A50F-A65E6FEA36F5.png) <!-- baize:img-hook downloaded=false reason="正文 769 字 ≥300，非承重" -->

除了常规的“缓存”(Caching)和“节点状态”(Node State)操作，studioClearCoat 还包含以下属性：

#### 折射率(Index)

描述材质的折射特性。

#### 缩放(Scale)

简单的最终结果倍增器。

#### 偏移(Bias)

控制对比度调整的中间点，并添加到最终结果。增加“偏移”(Bias)可以向上移动中间点（因为对比度增加，更多的纹理变暗）。减小“偏移”(Bias)可以向下移动中间点（因为对比度增加，更多的纹理变亮）

计算是：

最终结果= f（折射率）* 缩放 + 偏移

其中 f（折射率）是将折射率作为输入的 studioClearCoat 计算。
