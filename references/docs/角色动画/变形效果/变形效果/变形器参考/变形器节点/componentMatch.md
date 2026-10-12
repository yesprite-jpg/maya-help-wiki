# componentMatch

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 539 字 ≥300，非承重" -->

当在[变形变形器选项](../../变形变形器/变形选项%28Morph%20Options%29.md)中激活“使用组件查找”(Use Component Lookup)时，将使用比较几何体的算法创建 *componentMatch* 节点，构建顶点之间的相关性，然后生成预配置的查找表。这个自动生成的查找表会提供给组件列表，因此您无需创建自己的顶点表。

若要了解如何使用 componentMatch 节点创建查找表，请参见[使用 componentMatch 节点创建顶点查找表](../../修改变形器/变形器衰减/使用%20componentMatch%20节点创建顶点查找表.md)。

生成的查找表将使用此信息而不是顶点 ID，这样您便可以轻松地执行复杂操作，例如让部分驱动整体或整体驱动部分。可以使用 componentMatch 节点驱动其他变形器。

componentMatch 节点提供最近点的匹配模式，因此它会比较顶点并匹配它们。

**注**

重要：

如果要在不使用

componentMatch

节点的情况下创建自己的顶点查找表，请不要在

变形选项(Morph Options)

中激活

“使用组件查找”(Use Component Lookup)

选项。

#### 输入

要变形的几何体。与输入几何体对齐。

#### 目标(Target)

要提供给输入的对象。

#### 查找表格

输出结果。

#### 使用组件查找(Use Component Lookup)

使用拓扑映射。

#### componentLookupList

拓扑映射列表。

#### componentLookup

变形变形器的顶点查找。
