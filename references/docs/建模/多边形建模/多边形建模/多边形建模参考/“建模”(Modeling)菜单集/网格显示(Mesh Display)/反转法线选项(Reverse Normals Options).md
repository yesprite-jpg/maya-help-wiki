# 反转法线选项(Reverse Normals Options)

使用这些选项可设置在选择“网格显示 > 反转”(Mesh Display > Reverse)时发生的情况。

#### 在以下项上反转法线(Reverse normals on)

指定反转哪些元素的法线。

#### 选定面(Selected faces)

Maya 反转选定面上的法线。这是默认设置。

#### 选择面后进行提取(Selected faces, then extract)

Maya 反转选定面上的法线，然后提取或分割顶点。

**注**

“反转”(Reverse)

选项可生成非流形几何体，该几何体中共享一条边的多边形拥有反转法线。某些工具不能用于非流形几何体。请参见

清理、简化或验证网格

。

若要避免创建非流形几何体，请使用“选择面”(Select faces)，然后提取选项。该选项将分割顶点，以便不创建非流形几何体。

#### 壳中的所有面(All faces in the shell)

Maya 反转壳中所有（选中或未选中）面上的法线。

#### 用户法线(User Normals)

指定用户定义的法线是否受“反转”(Reverse)操作影响。

#### 保持用户法线方向(Preserve user normals direction)

指定使用“反转”(Reverse)功能时不反转用户定义的法线。默认设置为禁用。

#### 反转用户法线(Reverse user normals)

指定使用“反转”(Reverse)功能时反转用户定义的法线。这是默认设置。

## 相关主题

- [多边形法线](../../../多边形法线.md)

- [编辑顶点法线以影响多边形着色](../../../编辑多边形/编辑多边形法线/使用顶点法线硬化或软化多边形着色.md)
