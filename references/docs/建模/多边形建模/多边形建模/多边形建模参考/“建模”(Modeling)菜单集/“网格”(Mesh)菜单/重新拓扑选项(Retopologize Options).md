# 重新拓扑选项(Retopologize Options)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 951 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-7145F533-FF16-48E5-BC30-22CA59033DA6.png) <!-- baize:img-hook downloaded=false reason="正文 951 字 ≥300，非承重" -->

生成整洁的新拓扑，保留选定网格的曲面特征，同时确保所有面都是四边形。使用以下选项可设置在选择“网格 > 重新拓扑”(Mesh > Retopotalogy)时发生的情况，或在选中 polyRetopo 节点的情况下打开“属性编辑器”(Attribute Editor)时发生的情况。可以在[“输出”(Output)窗口](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D13AA354-01ED-4B20-95A2-E90E03275992)中查看“重新拓扑”(Retopologize)的进度。

若要取消操作，请在操作完成之前按住 Esc 键。

**注**

在大型密集网格上执行此操作时，可能需要较长时间。

#### 保持原始(Keep Original)

指定是重新拓扑选定对象的副本还是重新拓扑对象本身。这仅在“重新拓扑选项”(Retopologize Options)窗口中可用。

#### 保留硬边(Preserve Hard Edges)

指定是否使用模型的硬边（[网格显示 > 硬化边(Mesh Display > Harden Edges)](../网格显示%28Mesh%20Display%29.md)）作为重新拓扑模型的特征边。启用此选项将导致硬边周围的特征更精确地转化为新模型（例如，褶皱、眉毛和嘴唇等）。但是，过多硬边会导致算法运行时间非常长。禁用此选项会将所有边视为软边。这仅在“重新拓扑选项”(Retopologize Options)窗口中可用。

![图：指定是否使用模型的硬边（网格显示 硬化边(Mesh Display Harden Edges)）作为重新拓扑模型的特征边…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-748866DA-E1F6-4120-B19D-7D9E1FC3C1DC.png) <!-- baize:img-hook downloaded=false reason="正文 951 字 ≥300，非承重" -->

#### 目标面数(Target Face Count)

重新拓扑网格的所需面数。这不是硬性计数，而更多的是“重新拓扑”(Retopologize)尝试达到的目标。如果设置为 0，“目标边偏差”(Target Edge Deviation)将控制结果的密度。

#### 容差(%)(Tolerance (%))

“目标面数”(Target Face Count)的可接受误差范围 (%)。非常低的值 (< 10) 可能会导致性能低下。

#### 拓扑规则性(Topology Regularity)

确定结果中奇点（少于 4 条连接边的顶点）的数量。值越低，产生的奇点越少，但可能会平滑精细的细节。

#### 面均匀性(Face Uniformity)

确定允许对生成的网格上的面进行多大程度的挤压或拉伸以适配源曲面形状。较低的值会产生大小不同的四边形，可更加精确地遵循原始网格曲率，而较高的值会产生大小更规则的四边形。

#### 各向异性

值从 0 到 1 表示在圆柱形区域上的贴图拉伸量。较低的值会阻止贴图拉伸，从而生成具有较少矩形元素的更密集网格。较高的值允许贴图拉伸，以生成更加有效但有棱角的网格。

![图：值从 0 到 1 表示在圆柱形区域上的贴图拉伸量。较低的值会阻止贴图拉伸，从而生成具有较少矩形元素的更密集网格。较高的值…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A00844E6-4F85-4F71-988D-B4B697FC3A3F.png) <!-- baize:img-hook downloaded=false reason="正文 951 字 ≥300，非承重" -->
