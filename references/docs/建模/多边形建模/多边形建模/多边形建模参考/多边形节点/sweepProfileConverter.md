# sweepProfileConverter

**sweepProfileConverter** 节点是 [sweepMeshCreator](sweepMeshCreator.md) 节点的辅助节点，在您使用“自定义扫描剖面”(Custom Sweep Profile)形状时会创建此节点。请参见[使用“扫描网格”(Sweep Mesh)创建自定义网格](../../多边形选择和创建/使用“扫描网格”%28Sweep%20Mesh%29从曲线创建网格/使用“扫描网格”%28Sweep%20Mesh%29创建自定义网格.md)和[“扫描网格”(Sweep Mesh)选项](../多边形建模工具/“扫描网格”%28Sweep%20Mesh%29工具/“扫描网格”%28Sweep%20Mesh%29选项.md)。

您可以使用 **sweepProfileConverter** 移除现有剖面对象或组件。当设置为**“曲线对象”(Curve Object)**时，也可以用于定义网格相对于剖面曲线的细节。

您可以调整**“曲线精度”(Curve Precision)**属性，以增加或减少跨路径宽度的细分数。

您可以启用**“曲线优化”(Curve Optimize)**属性以基于曲率控制扫描网格沿剖面的密度：平直截面的分段较少，曲线型截面的细节较多。
