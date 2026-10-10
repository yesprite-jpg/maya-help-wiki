# 节点行为(Node behavior)

若要更改节点行为，请选择节点，然后展开“属性编辑器”(Attribute Editor)的“节点行为”(Node Behavior)部分。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-0A61F080-31FC-4CFB-B1C8-1F6844DDDF43.gif) <!-- baize:img-hook downloaded=false reason="正文 1099 字 ≥300，非承重" -->

选择一个节点，然后展开“属性编辑器”(Attribute Editor)的“节点行为”(Node Behavior)部分

#### 缓存(Caching)

启用“缓存”(Caching)可以在缓存中暂时存储输入节点解算。在 Maya 需要这些解算（作为节点输入）时，Maya 将使用存储在缓存中的信息，而不是重新解算输入节点。如果未对节点做出过更改，则重画速度将更高。缓存将在您编辑属性时毁坏。请注意，缓存会使用更多内存，这可能将影响 Maya 性能。

#### 冻结(Frozen)

启用“冻结”(Frozen)可暂时对选定节点禁用[解算管理器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-190D97E7-9AC0-4D67-8A07-1AF3A9DBAF15)。有问题的节点会导致播放速度减慢，禁用它们可提高性能。请参见[从解算中排除节点](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F69C44F3-1037-46DF-A1BE-56B96EA6ED43)。

#### 节点状态(Node State)

更改节点状态可以提高性能。可以选择以下三种节点状态之一：

#### 正常(Normal)

根据定义的设置和效果，使节点行为正常。这是默认设置。

#### 无效果(HasNoEffect)

禁用节点上的任何效果，使重画时所需计算更少。“节点状态”(Node State)重置回“正常”(Normal)后，效果才会渲染。Maya 会解算节点历史中的节点，而不是节点本身。

例如，转换簇，使几何体变形，然后将簇节点的“节点状态”设置为“无效果”，则几何体将显示为未变形状态，好像转换尚未发生一般。若要查看该效果，请将“节点状态”改回“正常”(Normal)。

#### 阻塞(Blocking)

暂时隐藏节点，不显示节点任何输入（输入解算）的结果。这可以加快重画。如果在场景复杂的情况下想只编辑节点的一个方面，这也将非常有用。阻塞的节点不渲染。

例如，在旋转曲面复杂时想编辑曲线，但不想等待曲线重画，则选择“阻塞”，然后编辑曲线。若要显示修改的旋转曲面，请将“节点状态”重置为“正常”。

#### “等待-正常”(Waiting-Normal)、“等待-无效果”(Waiting-HasNoEffect)和“等待-阻塞”(Waiting-Blocking)

这三个选项仅供内部使用。在交互（例如操纵）期间，它们会临时关闭图表的某些部分。请注意，操作完成后，将适当重置状态，例如，**“等待-阻塞”(Waiting-Blocking)**将重置为**“阻塞”(Blocking)**。

## 注释

- “无效果”(HasNoEffect)状态对于每个节点类型有不同的含义。某些节点类型不实现状态，在这种情况下，状态就如同“正常”一样。

- “等待”节点状态由 Maya 在内部用于跟踪“Hypergraph”中等待视图更新的节点。通常不应该将节点设置为“等待”状态。
