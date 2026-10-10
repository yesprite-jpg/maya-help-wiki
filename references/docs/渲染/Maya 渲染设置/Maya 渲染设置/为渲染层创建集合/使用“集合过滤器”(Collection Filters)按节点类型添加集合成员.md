# 使用“集合过滤器”(Collection Filters)按节点类型添加集合成员

使用“集合过滤器”(Collection Filters)功能可仅向集合添加形状、着色器和集等。此外，您还可以创建自定义过滤器，以添加感兴趣的特定节点类型。

默认情况下，集合仅包含变换节点，这些节点将确定当层可见时您在视口中看到的对象。

但是，对于高级用户，您可能希望将其他类型的节点包含在集合中。例如，您可能希望仅包含着色器、集或着色引擎。这样，您可以仅在特定类型的节点上创建覆盖。

例如，创建仅包含要应用着色器覆盖的着色引擎的集合。再比如，创建要覆盖其属性的集的集合。

单击“特性编辑器”(Property Editor)中的**“集合过滤器”(Collection Filters)**下拉列表，在可用的过滤器之间进行选择。

然后，您可通过执行以下操作之一来填充集合：

- 在集合“特性编辑器”(Property Editor)的“包括”(Include)字段中提供表达式；

- 从视口或“大纲视图”(Outliner)中选择节点，然后在集合“特性编辑器”(Property Editor)中单击“添加”(Add)；

- 结合使用二者。

请参见[为渲染层创建集合](../为渲染层创建集合.md)。

选择过滤器并添加节点或表达式之后，通过在“特性编辑器”(Property Editor)中单击“查看全部”(View All)，您可以验证层成员身份。此时将显示“查看集合对象”(View Collection Objects)窗口，其中包含集合成员的列表。

**注**

- 建议仅高级用户使用“所有”(All)集合过滤器。此外，它可能会影响性能。

- “几何体生成器”(Geometry Generators)过滤器包含历史节点，如 makeNurbCone 和 polySphere。此过滤器以前名为“几何体和 NURBS”(Geometry and NURBS)。

## 使用自定义过滤器添加特定的节点类型

如果提供的“集合过滤器”(Collection Filters)不符合您的特定用途，则可使用“自定义”(Custom)过滤器仅包含所选的特定节点类型，进一步简化集合。从下拉菜单中选择“自定义”(Custom)，然后将节点类型添加到“特性编辑器 集合过滤器 类型”(Property Editor > Collection Filters > Types)属性。若要添加节点类型，请使用鼠标中键将节点从“大纲视图”(Outliner)拖放到“特性编辑器”(Property Editor)，系统会自动识别其节点类型。将识别插件节点类型。

**注**

提示：

除拖放之外，还可以手动键入节点类型的名称（例如，blinn）。

在以下示例中，char*_skin 表达式用于将所有角色蒙皮着色器包含在集合中。现在，使用鼠标中键将 char1_skin 拖动到“特性编辑器”(Property Editor) “类型”(Types)属性时，系统将识别 *blinn* 类型。同样，当您使用鼠标中键将 char2_skin 拖动到“特性编辑器”(Property Editor)时，将识别 *aiStandardSurface* 类型。单击“全选”(Select All)验证成员身份。

**注**

提示：

此外，您还可以通过在特性编辑器中单击

“查看全部”(View All)

来显示集合成员的列表，以验证集合成员。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A9AE97D6-7937-48F5-9D38-ECF80BF5FD87.png) <!-- baize:img-hook downloaded=false reason="正文 1713 字 ≥300，非承重" -->

### 使用分类字符串添加节点类型

在“类型”(Types)字段中输入 *texture/2d* 等分类字符串，可添加文件节点或 2d 纹理节点（例如，“棋盘格”(Checker)）。其他选项包括分类字符串 *utility*，用于添加 bump2d 或 place2dtexture 节点。此字段区分大小写；换句话说，Texture/2d 不会返回任何结果。

每个节点的“节点”文档中提供了有关其分类字符串的信息。有关详细信息，请参见 Maya 帮助中技术文档的“节点”部分。

### 按节点类型减去集合成员

可以使用 - 排除节点类型。例如，以下表达式包含除 Blinn 类型着色器外的所有表面着色器：

```text
shader/surface -blinn
```

此外，您还可以通过分类字符串进行排除。此示例包括所有工具节点，但按 *utility/general/placement/2d* 分类的节点（例如，place2dTexture 节点）除外。

```text
utility -utility/general/placement/2d
```
