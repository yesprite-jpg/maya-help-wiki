# NURBS 选项

使用“Display > NURBS”(Display > NURBS)子菜单上的选项可控制哪些特征显示在场景中的选定 NURBS 曲面上以及这些曲面的平滑度。

#### CV

显示选定曲面的控制顶点 (CV)。

#### 编辑点(Edit Points)

显示选定曲面的编辑点。

#### 壳线(Hulls)

显示选定曲面的壳线。

#### 法线(着色模式) (Normals (Shaded Mode))

显示选定曲面的法线。法线仅在着色模式（热键：5）下显示。

#### 面片中心(Patch Centers)

在面片中心显示小方形。

#### 曲面原点(Surface Origins)

显示曲面的原点曲线。

![图：显示曲面的原点曲线。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-33848928-6420-4330-9FDC-8B80E727041E.png) <!-- baize:img-hook downloaded=false reason="正文 1351 字 ≥300，非承重" -->

#### 自定义(Custom)

允许您通过同时设置多个选项自定义显示。还可以使用“范围”(Scope)下拉列表指定哪些 NURBS 对象显示选定选项：“活动对象”(Active objects)、“所有对象”(All objects)、“新曲线”(New curves)或“新曲面”(New surfaces)。

#### 壳线(Hull)

设置这些选项可控制壳线平滑度，从而设置 U 和 V 的数值。您可以将设置应用于“活动对象”(Active objects)或“所有对象”(All objects)。

#### 粗糙/中等/精细(Rough/Medium/Fine)

以预设质量级别显示对象。选择“中等”或“精细”会减慢显示，降低交互式性能，但会提高图像精度。

这些选择的选项允许您将设置应用于“活动对象”(Active objects)对象或“所有对象”(All objects)对象。

**注**

这些设置的热键是：1（“粗糙”）、2（“中等”）和 3（“精细”）。

#### 自定义平滑度(Custom Smoothness)

用于自定义显示质量。

下图中，对象的平滑度已从默认的中等质量级别更改为自定义的壳线质量级别。

![图：用于自定义显示质量。 下图中，对象的平滑度已从默认的中等质量级别更改为自定义的壳线质量级别。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-BCA37515-0DCE-4BA9-AAA3-4AE0BA58199D.png) <!-- baize:img-hook downloaded=false reason="正文 1351 字 ≥300，非承重" -->

## NURBS 平滑度(自定义)选项(NURBS Smoothness (Custom) options)

#### 受影响的对象(Objects Affected)

将选项应用于“活动对象”(Active objects)对象或“所有对象”(All objects)对象。

#### 几何体(Geometry)

若要显示所有几何体，请选择“完全”(Full)。若要仅显示壳线，请选择“壳线”(Hull)。

## 线框(Wireframe)

#### 每个 U 向跨度的曲面分段(Surface Div per Span U)、每个 V 向跨度的曲面分段(Surface Div per Span V)

这两个设置都是细分 NURBS 面片，实现以更精细的网格外观显示面片的目的。范围在 0 到 32 之间。

#### 每个跨度的曲线分段(Curve Div per Span)

指定每个跨度的曲线分段数，以更粗糙或更平滑的外观显示曲线。范围在 1 到 128 之间。

## 着色(Shaded)

#### 显示渲染细分几何体(Display Render Tessellation Geometry)

启用后可以查看渲染器将用于曲面的细分图案。必须在着色模式下才能查看该图案。

#### 每个跨度的曲面分段(Surface Div per Span)

指定着色模式下每个跨度的曲面分段数。范围在 0 到 32 之间。

## 壳线(Hull)

#### U 向壳线简化(Hull Simplification U)、V 向壳线简化(Hull Simplification V)

如果已将“几何体”(Geometry)设置为“壳线”(Hull)，则可以使用这些设置控制显示的壳线分段数。
