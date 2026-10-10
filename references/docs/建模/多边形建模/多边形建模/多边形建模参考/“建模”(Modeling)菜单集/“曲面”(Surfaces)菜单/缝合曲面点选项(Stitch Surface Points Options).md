# 缝合曲面点选项(Stitch Surface Points Options)

使用以下选项可设置在选择“曲面 > 缝合 > 缝合曲面点”(Surfaces > Stitch > Stitch Surface Points)时发生的情况。

#### 保持原始(Keep Original)

如果“保持原始”(Keep Original)处于启用状态，则会在原始输入曲面的顶部创建缝合曲面。可用于在对结果不满意时移动生成的曲面。可以重新缝合一个包含不同选项设置的新曲面。

#### 指定相等权重(Assign Equal Weights)

如果“指定相等权重”(Assign Equal Weights)处于启用状态，则使用平均“NurbsSurfacePoint”节点在位置和法线均执行选定点的加权平均。

如果启用了该选项，则为所有点指定 0.5 的权重。如果禁用了该选项，则为第一个选定点指定 1.0 的权重，而其他点均为 0。默认设置为启用。

#### 层叠缝合节点(Cascade Stitch Node)

如果“层叠缝合节点”(Cascade Stitch Node)处于启用状态，则缝合操作将忽略曲面上之前的任何缝合操作。如果禁用该选项，且曲面已执行了缝合操作，则使用上一个操作的缝合节点。默认设置为启用。

## 相关主题

- [手动缝合曲面点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-16B1BD87-B5CB-49AA-BC83-638BD534001A.htm)
