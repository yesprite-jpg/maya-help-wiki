# 线工具(Wire Tool)

- 在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 > (创建)[线](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-7FBC7D21-E325-435F-AC29-6F22CFF81AF7.htm)”(Deform > (Create) Wire) > ![图：在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 (创建)线”(Deform (Create…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" -->

- 在“动画”(Animation)菜单集中：“动画变形 > 打开完整的变形菜单 > (创建)[线](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-7FBC7D21-E325-435F-AC29-6F22CFF81AF7.htm)”(Anim Deform > Open Full Deform Menu > (Create) Wire) > ![图：在“动画”(Animation)菜单集中：“动画变形 打开完整的变形菜单 (创建)线”(Anim Deform Open…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" -->

若要创建线变形器，请使用“线工具”(Wire Tool)。所创建的线变形器的特性取决于“线工具”(Wire Tool)的工具设置。默认情况下，会将“线工具”(Wire Tool)设定为创建不包含限制曲线的线变形器。

请参见[线变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-F45EC3DD-F268-4790-B069-DD1E6DF4484D.htm)和[绘制线变形器权重](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-DF0CCC32-C8BC-4C46-A0E3-4E349E738982.htm)。

### 线设置(Wire Settings)

#### 限制曲线(Holders)

如果启用该选项，则会创建包含限制曲线的线变形器。如果禁用该选项，则会创建不包含限制曲线的线变形器。限制曲线是可用于限制变形区域的曲线。默认设置为禁用。

#### 封套(Envelope)

指定变形比例因子。使用滑块从 0.0000 到 2.0000 的范围内选择值。值为 0 未指定任何变形效果。默认值为 1.0000。

#### 交叉效果(Crossing Effect)

指定在变形器的其中两影响线相交的位置上变形效果的振幅。使用滑块从 0.0000 到 2.0000 的范围内选择值。默认值为 0.0000，它指定平滑的、不能相加的效果。

#### 局部影响(Local Influence)

指定在局部应用两条或更多影响线的变形效果。使用滑块从 0.0000 到 2.0000 的范围内选择值。默认值为 0.0000。

#### 衰减距离(Dropoff Distance)

指定每条影响线的影响范围。使用滑块从 0.0000 到 10.0000 的范围内选择值。默认值为 1.0000。

变形顺序(Deformation Order)

指定在可变形对象的历史中变形器节点的放置。放置选择包括：“默认”(Default)、“之前”(Before)、“之后”(After)、“分割”(Split)或“平行”(Parallel)。

#### 默认(Default)

将变形器放置在当前最终形状节点之前并紧邻该形状节点。

#### 之前(Before)

将变形器放置在当前最终形状节点之前并紧邻该形状节点。“默认”(Default)和“之前”(Before)通常提供相同的放置方式。

#### 之后(After)

作为当前最终形状节点的输出放置变形器，并创建一个新的最终形状节点。

#### 分割(Split)

将输入变形历史“分割”(Splits)为两个单独的变形链，从而提供源自同一可变形对象的两个最终形状。

#### 并行(Parallel)

创建一个最终形状，该最终形状会融合对象的当前输入历史，使之与新变形器平行。

#### 排除(Exclusive)

指定变形器集是否将处于某个划分中。如果变形器集处于某个划分中，那么该集中的点不能位于任何其他集中。结果是仅将要创建的变形器可能会影响这些点。如果启用该选项，那么“独占划分”(Exclusive Partition)和“现有划分”(Existing Partitions)选项会变得可用。默认情况下，“排除(Exclusive)”处于禁用状态。

#### 独占划分(Exclusive Partition)

指定划分的名称。默认名称为“deformPartition”。仅当启用“排除”(Exclusive)时可用。

#### 现有划分(Existing Partitions)

指定一个现有划分。默认的现有划分为“characterPartition”。仅当启用“排除”(Exclusive)时可用。

## 属性编辑器

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" -->

您可以在“属性编辑器”(Attribute Editor)的“线”(Wire)选项卡中找到用于线变形器的其他控件。

#### 绑定到原始几何体(Bind to Original Geometry)

可用于将某个单独的网格指定为线变形器的变形的绑定几何体。在网格已经变形（例如，通过簇变形器）但您希望将线绑定到其变形前的形状时，这很有用。 （有关原始几何体属性的说明，请参见[原始几何体](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-EEF323A6-8692-4D74-8EAA-5481BF437D42.htm)。）

在下面的示例中，我们选用了一个多边形平面，对其应用簇变形器。然后，在此之上应用线变形器

| 绑定到原始几何体(Bind to Original Geometry)：禁用(Off) |  | 绑定到原始几何体(Bind to Original Geometry)：启用(On) |
|---|---|---|
| 线变形器将在簇变形的平面 (D) 上对新点进行采样。 将得到一个更接近线的平面，而曲面上的顶点偏移以匹配簇。 如果要左右移动基础簇变形器，顶点将沿凸起的曲面来回滑动，同时大致保持相同的整体形状。 ![图：如果要左右移动基础簇变形器，顶点将沿凸起的曲面来回滑动，同时大致保持相同的整体形状。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-38A4F943-C4AF-41B3-BE4E-41BE365E2187.gif) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" --> | ![图：在下面的示例中，我们选用了一个多边形平面，对其应用簇变形器。然后，在此之上应用线变形器 绑定到原始几何体(Bind to…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-44B535E8-FF41-4330-94C6-C8C42C5D51F6.png) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" --> | 线变形器将忽略簇变形的平面，并直接从提供的网格 (M2) 对点进行采样。 提供的网格与变形几何体必须具有相同拓扑。通常，它将是变形前的基础网格（在此示例中为我们的平面）的副本。 将得到一个按照原始网格的顶点变形的平面，因此，形状不仅接近线，而且也接近基础簇变形器。 如果要左右移动基础簇变形器，凸起会一起移动。 ![图：如果要左右移动基础簇变形器，凸起会一起移动。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-3031C577-35D3-40CF-B47F-2385ACAF80C8.gif) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" --> 注： 启用此选项还可以提高性能。因此，在两种结果相同的情况下，建议启用此选项。 |

将线变形器连接到基础网格

1. （可选）在对基础网格应用任何变形器之前复制该基础网格。

  **注**

  可以将线节点绑定到拓扑相同的任何网格，但通常情况下，您会希望使用基础网格的副本。

2. 将线变形器应用于对象（以及任何其他变形器）。

3. 在“属性编辑器”(Attribute Editor)的“线”(Wire)选项卡中，启用“绑定到原始几何体”(Bind to Original Geometry)。

4. 将基础网格副本的“输出网格”(Out Mesh)属性连接到线条变形器的[原始几何体(Original Geometry)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-EEF323A6-8692-4D74-8EAA-5481BF437D42.htm)属性，方法是通过[节点编辑器(Node Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C6E5588F-40A4-4B1E-9C02-A29DA9A4650F)、[连接编辑器(Connection Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-92F35EC2-35BF-49AB-8CDE-9DE922EA85A1)，或通过使用以下 MEL 脚本：connectAttr -f <对象名称>.outMesh <线条变形器名称>.originalGeometry[0]

  ![图：将基础网格副本的“输出网格”(Out Mesh)属性连接到线条变形器的原始几何体(Original Geometry)属…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-36B2E1C8-45EC-480B-B000-FC0CD87B3474.jpg) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" -->
