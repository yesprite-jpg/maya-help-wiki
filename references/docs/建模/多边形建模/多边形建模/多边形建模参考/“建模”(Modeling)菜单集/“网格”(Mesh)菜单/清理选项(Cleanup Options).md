# 清理选项(Cleanup Options)

使用以下选项可设置在选择“网格 > 清理”(Mesh > Cleanup)时发生的情况。

## 清理效果(Cleanup Effect)

使用这些选项，以指定要清理的多边形几何体的部分。可以仅使用“清理”(Cleanup)功能标识匹配指定标准的多边形，或自动使用此功能移除或修改不匹配指定标准的多边形。

#### 运算(Operation)

选择是要清理多边形还是仅将其选中。

#### 清理匹配多边形(Cleanup matching polygons)

使用此选项来重复清理选定的多边形几何体（使用相同的选项设置）。这是默认设置。

#### 选择匹配多边形(Select matching polygons)

使用此选项选择符合设置标准的任何多边形，但不执行清除。

#### 范围(Scope)

选择要清理的对象范围。

#### 应用于选定对象(Apply to selected objects)

启用此选项，以仅在场景中清理选定的多边形。这是默认设置。

#### 应用于所有多边形对象(Apply to all polygonal objects)

启用此选项，以清理场景中所有多边形对象。

#### 保持构建历史(Keep construction history)

启用此选项，以保持与选择的多边形几何体相关的构建历史。

## 通过镶嵌细分修复(Fix by Tessellation)

可以使用一些多边形编辑操作修改多边形网格，并且生成具有不需要的属性的的多边形面。例如，四边面、包含四条以上边的面、凹面、带孔的面和非平面的面。这些选项可以通过镶嵌细分（三角化）不精细的面来清理这些问题。

以下插图显示了多边形面可能会遇到的各种问题。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-00A69E63-B4E0-4328-A273-E8937EDC1C60.png) <!-- baize:img-hook downloaded=false reason="正文 2090 字 ≥300，非承重" -->

## 移除几何体(Remove Geometry)

指定在清理操作期间要移除的几何体，以及要移除的下落几何体中的容差。可以使用以下方式移除：

#### 层状体面(Lamina faces)

“层状体面”(Lamina faces)共享其所有边。如果选择用于移除的“层状体面”(Lamina faces)，则 Maya 移除共享所有边的面。通过移除这些类型的面，可以避免不必要的处理时间，特别是当将模型导出到游戏控制台时。

例如，假定您在“单独的重复面”(Separate Duplicate Faces)选项禁用时执行“编辑网格 > 复制”(Edit Mesh > Duplicate)。具有两个在各自顶部的面。如果之后合并两个面的顶点，则它们会共享相同的边。可以使用“层状体面”(Lamina faces)处于启动状态时的“清理”(Cleanup)移除额外的面。

#### 非流形几何体(Nonmanifold geometry)

启用此选项以清理非流形几何体。选择以下选项之一，以控制结果法线的情况。有关非流形几何体的详细信息，请参见[双流形和非流形多边形几何体](../../../双流形和非流形多边形几何体.md)。

#### 法线和几何体(Normals and Geometry)

清理非流形顶点或边时，启用此选项以使法线一致。

#### 仅几何体(Geometry only)

清理非流形几何体，而无需更改结果法线。

**注**

因为

“清理”(Cleanup)

功能可以合并顶点并收拢零长度边，所以可能存在

“清理”(Cleanup)

功能可以输出非流形几何体的情况。

使用层叠方式设置“清理”(Cleanup)选项以在网格上执行多个清理操作时会产生此情况。

如果这种情况很有可能发生，建议您多次运行“清理”(Cleanup)功能，然后仅在上一次迭代的“移除几何体”(Remove Geometry)菜单中启用“非流形几何体”(Non-Manifold geometry)选项。

#### 具有零长度的边(Edges with a zero length)

当您选择移除具有零长度的边，非常短边将在指定的容差内被删除。

#### 长度容差(Length tolerance)

“具有零长度的边”(Edges with a zero length)设置处于启动状态时，指定要移除的边的最小长度。

#### 包含零几何体区域的面(Faces with zero geometry area)

当您选择移除具有零几何体区域的面（例如，移除面积介于 0 和 0.0001 的面）时，会通过合并顶点移除面。要确保此操作移除在定义的容差内区域的面，必须为进行合并的边顶点设置长度容差。如果不要移除长度容差内的边，可以在设置容差后禁用零长度边选项。

#### 区域容差(Area tolerance)

包含零几何体区域的面处于启动状态时，指定要删除的面的最小区域。

![图：包含零几何体区域的面处于启动状态时，指定要删除的面的最小区域。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-1B8275FE-5F62-4DD0-8DCE-6F71E4335FD6.png) <!-- baize:img-hook downloaded=false reason="正文 2090 字 ≥300，非承重" -->

#### 具有零贴图区域的面(Faces with a zero map area)

选择移除具有零贴图区域的面时，检查面的相关 UV 纹理坐标，并移除 UV 不符合指定的容差范围内的面。

#### 区域容差(Area tolerance)

当“具有零贴图区域的面”(Faces with a zero map area)设置处于打开状态时，指定要将其删除的面的最小区域。

**注**

同时应用到对象及其实例时，意外的“清理”(Cleanup)行为。这通常会在“应用到所有多边形对象”(Apply to all polygon objects)已启用时发生。合理的工作流程是仅清理原始对象；实例以及结果将被清理。

#### 无效组件(Invalid Components)

移除选定对象上的孤立边、顶点和 UV。

## 相关主题

- [清理、简化或验证网格](../../../编辑多边形/删除和简化多边形/清理、简化或验证网格.md)

- [复制面选项(Duplicate Faces Options)](../“编辑网格”%28Edit%20Mesh%29菜单/复制面选项%28Duplicate%20Faces%20Options%29.md)
