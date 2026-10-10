# 编辑 LOD 阈值的值

+

您可以使用“通道盒”(Channel Box)或“属性编辑器”(Attribute Editor)更改切换级别的阈值。可用的设置会更改，具体取决于是否将 LOD 组设置为使用基于阈值的“屏幕高度百分比”(Screen Height Percentage)或“距离”(Distance)。

**注**

您可以在创建 LOD 组时或在

“通道盒”(Channel Box)

中（如果 LOD 组基于透视摄影机）设置

“阈值类型”(Threshold Type)

。对于正交摄影机，无法在创建 LOD 组之后更改

“阈值类型”(Threshold Type)

。

更改级别阈值的值的步骤

1. 在“Hypergraph”或“大纲视图”(Outliner)中选择细节级别组节点。

  [细节级别属性](“细节级别”%28Level%20of%20Detail%29属性.md)显示在“通道盒”(Channel Box)中。

2. 编辑要更改其阈值的对象的“LOD*n* 开始”(LODn Start)的值，然后按 Enter 键。

  **注**

  对于基于

  “屏幕高度百分比”(Screen Height Percentage)

  的 LOD 组，属性将标签为

  “LOD_

  n

  开始百分比”(LOD_n Start Percentage)

  。对于基于

  “距离”(Distance)

  的 LOD 组，

  “开始”(Start)

  属性的标签为

  “LOD_

  n

  开始距离”(LOD_n Start Distance)

  。

3. 当您修改级别的“开始”(Start)值时，放大和缩小场景视图以测试您的更改。

## 相关主题

- [创建 LOD 组](创建%20LOD%20组.md)
