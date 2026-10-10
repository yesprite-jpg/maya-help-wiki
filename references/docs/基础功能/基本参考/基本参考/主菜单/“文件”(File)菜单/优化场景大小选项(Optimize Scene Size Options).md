# 优化场景大小选项(Optimize Scene Size Options)

使用这些选项可设置在选择“文件 > 优化场景大小”(File > Optimize Scene Size) > ![图：使用这些选项可设置在选择“文件 优化场景大小”(File Optimize Scene Size) 时发生的情况。从主菜…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3057 字 ≥300，非承重" -->时发生的情况。从主菜单栏选择“文件 > 优化场景大小”(File > Optimize Scene Size)或直接单击“立即优化”(Optimize Now)时，通过这些选项可选择要对文件执行的清理操作。另请参见[优化场景大小](../../../../场景管理/场景管理/优化场景大小.md)。

#### 移除无效项目(Remove invalid)

##### NURBS 曲面 + 曲线(NURBS surfaces + curves)

删除 NURBS 曲面和曲线的无效节点。如果一个节点没有连接，则会将该节点视为无效。具体来说，此操作将移除下列无效节点：

- stitchSrf

- rebuildSurface

- insertKnotSurface

- avgNurbsSurfacePoints

#### 移除空项目(Remove empty)

##### 集(Sets)

删除未使用的（空）集。该操作不会移除某些默认集节点。这些集节点如下：

- defaultLightSet

- defaultObjectSet

- initialParticleSE

- initialShadingGroup

##### 划分(Partitions)

删除未使用的（空）划分。如果一个划分与场景中其他部分内的节点无连接，则会将该划分视为未使用。

##### 变换(Transforms)

移除不含相关项或连接且与其他被引用节点不关联的变换节点。

##### “显示层”(Display layers)和“渲染层”(Render layers)

删除未锁定且不是被引用文件一部分的空显示层或渲染层节点。“显示层”(Display layers)或“引用层”(Reference layers)操作无法删除默认层。

#### 移除未使用项目(Remove unused)

##### 动画曲线(Animation curves)

删除与场景中其他节点无连接、未锁定且不是来自被引用文件的 animCurve 节点。

##### 动画片段(Animation clips)

删除未在场景中使用的源动画片段和动画片段节点。如果一个动画片段未与场景中的角色集相关联且未连接到其他任意场景节点，就会将该动画片段视为未使用。如果与源片段链接的场景中未使用动画片段，就会将该源片段节点视为未使用。

##### 姿势(Poses)

删除所有未应用于场景中角色的动画姿势。

##### NURBS 曲线(NURBS curves)

删除与场景中其他节点无连接、未锁定、不是来自被引用文件且父对象未使用的 NURBS 曲线。如果 NURBS 曲线的父对象与其他场景节点有连接，则不会删除该曲线。

##### NURBS 曲面(NURBS Surfaces)

删除与各自的输入 NURBS 曲面相同的 NURBS 曲面。如果一个 NURBS 曲面的唯一输入连接是创建，同时该曲面的输入连接到相同父对象的 NURBS 曲面，而且该曲面形状与输入形状又相同，则该操作会移除该 NURBS 曲面。例如，如果重新构建 NURBS 球体，但重新构建的曲面与原始输入的曲面设置相同，系统就会删除重建的球体。

请注意，若要使用此操作移除 NURBS 曲面，则该曲面不得处于锁定状态或来自被引用文件。

##### 缓存的数据(Cached data)

即使依存关系图的值脏或已计算，这些值还是会临时占用节点内的空间。该清理操作会处理所有可在需要时重新生成的数据，并将其从缓存（数据块）中移除，从而清理内存中的空间。

##### 变形器(Deformers)

删除不含输出连接的未使用变形器，以及不含输出连接的中间对象。

##### 未使用的蒙皮影响(Unused skin influences)

移除对蒙皮无影响的任何关节或影响对象（即所有权重为 0.0）。

##### 表达式(Expressions)

删除所有与自身输出属性无直接连接的表达式节点。具有直接连接的表达式可以在场景中创建出输出属性与输入属性之间的关系。换句话说，系统将删除未链接到场景其余部分的表达式（该表达式是已连接节点组的一部分），因为表达式不会引用与场景相关联的输出属性。不会对另一侧为空的单位节点求值，因此，此操作不会删除单位节点。

此操作仅删除 expression 节点，而不会删除构建到粒子形状中的 dynExpressions 节点。

**注**

注意：

如果执行 MEL 命令的表达式与输出属性没有直接连接（输出连接），则该操作将删除此表达式。

##### GroupID 节点(GroupID nodes)

删除所有与场景中其他节点无连接、未锁定且不是来自被引用文件的 GroupID 节点。

##### 渲染节点(Rendering nodes)

删除所有未使用的渲染节点。该过程分三个阶段进行：

| **阶段 1** | 删除空的着色组以及不含已连接曲面、体积或置换着色器的着色组。 |
|---|---|
| **阶段 2** | 删除所有输出没有任何连接的材质节点（曲面、体积、置换着色器）。来自消息属性的输出连接并不表明节点正在使用中，因此只有具有此类型输出连接的节点才会被删除。请注意，该阶段将删除已提供给空着色组的着色器。阶段 1 删除了空着色组的 shadingEngine 节点，从而使填充到空着色组中的材质处于断开状态。现在将删除这些已断开连接的材质。 |
| **阶段 3** | 删除所有未使用的纹理和工具节点。如果节点没有相关的输出连接，就会将该节点视为未使用。请注意，现在将删除阶段 2 中已提供给材质中的纹理和工具。 |

##### 定位器(Locators)

删除未连接到其形状或变换节点的定位器对象。如果定位器的父对象具有连接，或者定位器的父节点具有多个子节点，就不会删除该定位器此过程仅移除未锁定或不是来自被引用文件的定位器。

##### 约束(Constraints)

删除未约束任何对象的约束。换句话说，此过程不会移除没有驱动任何对象以及不具有任何输出连接的约束。若要使用此过程删除约束，则该约束不得来自被引用文件且不得处于锁定状态。

具体来说，此过程会对场景中的以下节点进行求值，从而确定是否应将其移除：

- pointConstraint

- aimConstraint

- orientConstrain

- parentConstrain

- scaleConstraint

- normalConstraint

- tangentConstraint

- geometryConstraint

##### 对融合(Pair blends)

删除不生成输出或未连接到 input2 的 pairBlends。此过程不会移除已锁定或来自被引用文件的 pairBlends 节点。

##### 快照节点(Snapshot nodes)

删除所有与场景其余部分有一个连接或无连接的快照节点。此过程不会移除已锁定或来自被引用文件的 Snapshot 节点。

##### 单位转化节点(Unit conversion nodes)

删除所有与场景其余部分有一个连接或无连接的单位转化节点。此过程不会移除已锁定或来自被引用文件的单位转化节点。

##### 被引用项目(Referenced items)

删除所有未在场景或场景引用中使用的被引用节点。此操作不会删除只读节点。

##### 笔刷(Brushes)

删除所有未附加到任何笔划的笔刷。此操作可用于清理进行大量导入操作时可能积累的默认笔刷节点。

#### 删除(Remove)

##### 未知节点(Unknown Nodes)

删除下列所有节点类型：

- unknown

- unknownDag

- unknownTransform

#### 删除重复项(Remove duplicate)

##### 着色网络(Shading networks)

将每个着色网络与场景中的着色网络进行比较，并将重复的着色网络收拢为一个着色网络。根据 shadingEngine 的节点名称，按字母顺序删除重复的着色网络。若要将所有重复的网络收拢为一个特定网络，请重命名该网络从而使其位于按字母顺序排序的场景中着色网络列表中的最后一位。

## 相关主题

- [创建自定义“优化场景大小”(Optimize Scene Size)操作](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-436E4642-8436-4FAB-A799-63971FA54DF2)
