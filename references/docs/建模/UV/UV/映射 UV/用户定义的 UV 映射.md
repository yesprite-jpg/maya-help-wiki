# 用户定义的 UV 映射

可以映射 UV 纹理坐标，方法是使用“自动映射”(Automatic Mapping)功能中的“加载投影”选项为 UV 投影指定用户定义的平面。

“加载投影”(Load Projection)选项使用从当前 Maya 场景中指定的多边形对象。该对象可以形成围绕对象的框架，或由在其中心彼此相交的单独面组成。在为投影指定用户定义的对象时，“自动映射”(Automatic Mapping)投影操纵器会更新。

## 用户定义的投影对象的条件

- 用作用户定义的投影对象的对象必须具有 UV 纹理坐标。

- 建议投影对象由单独的多边形面组成。即，应先使用“编辑网格 > 提取”(Edit Mesh > Extract)将用作投影对象的多边形基本体分割成单独的网格。对于“加载投影”(Load Projection)，NURBS 曲面和细分曲面不是有效的曲面类型。请参见[提取选项](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/“编辑网格”%28Edit%20Mesh%29菜单/提取选项%28Extract%20Options%29.md)。

此外，最好了解以下操作：

- 投影对象的 UV 确定发生的最终投影映射的形状和位置。

- 可从“加载投影”(Load Projection)对象沿其法线平移任何面，而不对生成的投影产生任何影响。

- 从“加载投影”(Load Projection)对象缩放或旋转任何面将影响生成的最终 UV 投影的方向和比例。发生这种情况时，投影操纵器会更新。

- 可为投影对象指定的多边形面的最大数量为 31。

加载用户定义的多边形对象，以用于“自动映射”(Automatic Mapping)

1. 从场景视图中选择一个要在其上投影 UV 的多边形对象。

2. 选择“UV > UV 编辑器”(UV > UV Editor)以打开“UV 编辑器”(UV Editor)。

  对象的现有 UV 显示在 UV 编辑器的 2D 视图中。

3. 从“建模”(Modeling)菜单集中，选择“UV > 自动”(UV > Automatic) > ![图：从“建模”(Modeling)菜单集中，选择“UV 自动”(UV Automatic) 。 将显示“多边形自动映射选项”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1637 字 ≥300，非承重" -->。

  将显示“多边形自动映射选项”(Polygon Automatic Mapping Options)窗口。

4. 在“多边形自动映射选项”(Polygon Automatic Mapping Options)窗口中，启用“加载投影”(Load Projection)选项，然后执行以下操作之一：

  - 在当前场景中指定要作为投影对象加载的对象，方法是在“投影对象”(Projection Object)框中键入其名称。

  - 在当前场景中选择要作为投影对象加载的对象，然后单击“加载选定项”(Load Selected)。对象的名称出现在“投影对象”(Projection Object)框中。请参见上文的“用户定义的投影对象的条件”。

5. 单击“投影”(Project)或“应用”(Apply)以执行“自动映射”(Automatic Mapping)功能。

  自动映射投影操纵器看起来以场景视图中的对象为中心，且所带的蓝色投影平面在方向上与指定的“加载投影”(Load Projection)对象的平面相对应。也就是说，如果“加载投影”(Load Projection)对象在各种角度的方向上有 8 个平面，则投影操纵器会以类似方式显示。

  **注**

  在某些情况下，

  “加载投影”(Load Projection)

  对象可能会导致自动映射投影操纵器上的平面显示为从在其上进行投影的对象意外偏移或倾斜。该 UV 偏移基于

  “加载投影”(Load Projection)

  对象的原始 UV，并不会影响投影的质量。

  可以在投影前为“加载投影”(Load Projection)对象单位化 UV，以使其 UV 位于 0 到 1 的纹理空间。尽管这将使投影操纵器看起来更加以多边形对象为中心，但它可能无法提供您期望的 UV 映射结果，因为 UV 将以类似于明确指定了重叠功能的方式进行投影。

6. 根据需要平移、旋转或缩放操纵器，以获得所需的 UV 投影。投影的 UV 显示在 UV 编辑器中。只要操纵器在场景视图中移动，就可以看到投影的 UV 在 UV 编辑器中更新。

## 相关主题

- [映射 UV](../映射%20UV.md)

- [自动 UV 映射](自动%20UV%20映射.md)

- [自动映射选项(Automatic Mapping options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/自动映射选项%28Automatic%20Mapping%20options%29.md)

- [平面 UV 映射](平面%20UV%20映射.md)

- [圆柱形映射选项(Cylindrical Mapping options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/圆柱形映射选项%28Cylindrical%20Mapping%20options%29.md)

- [球形映射选项(Spherical Mapping options)](../../../多边形建模/多边形建模/多边形建模参考/“建模”%28Modeling%29菜单集/UV%20菜单/球形映射选项%28Spherical%20Mapping%20options%29.md)
