# 移动并缝合 UV 边选项(Move and Sew UV Edges options)

使用这些选项可设置在选择“UV > 移动并缝合 UV 边”(UV > Move and Sew UV Edges)时发生的情况。

## 设置

#### 限制壳大小(Limit shell size)

禁用该选项时，“移动并缝合 UV”(Move and Sew UVs)仅移动并缝合选定的边。

启用该选项时，“移动并缝合 UV”(Move and Sew UVs)自动移动小于“面数”(Number of Faces)中设定的大小的所有选定边并将它们缝合在一起。

#### 面数(Number of faces)

启用“限制壳大小”时，该设置指定每个壳中的最大面数。数值越大，产生的壳越少。

在执行“移动并缝合”操作后，可以在“通道盒”(Channel Box)中选择历史节点 (polyMapSewMove)，并调整“面数”(Number of Faces)，直到获得理想的结果。

## 相关主题

- [分离和附加 UV 壳](../../../../../编辑%20UV/分离和附加%20UV.md)

- [合并 UV 选项](../../../../../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/合并%20UV%20选项%28Merge%20UVs%20options%29.md)
