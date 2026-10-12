# ShaderFX 菜单栏

## File 菜单

#### Export Graph/Export Graph Selection

选择此选项可以导出图表或选定的图表节点，以供在不同的场景中使用。

#### Import Graph

选择此选项可通过导入之前保存的图表网络来替换当前的图表网络。

#### Merge Graph

选择该选项可以导入先前保存的图表网络，并将其与当前的图表合并。

## Edit 菜单

#### Copy/Paste

使用这些复制和粘贴选项可以复制节点。

## Group 菜单

**注**

仅适用于

“Shaderfx 着色器”(Shaderfx Shader)

网络。

#### Create Group

可以创建组，并将一组节点封装在另一节点内。若要创建组，请选择要分组的节点，然后选择此选项。甚至可以对组进行嵌套。有关详细信息，请参见[使用组](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-530D2C81-32BF-47D2-9C4D-95BF8E8F6BBC.htm)。

#### Ungroup

选择组节点，然后选择此菜单选项将封装的节点解组。

#### Make Group Unique

使用此功能可更改组，但仅限于对特定的场景的更改。选择组节点，然后选择此菜单选项。系统将会显示工具提示，表明该组现在是唯一的，并且不引用磁盘上的节点。您现在所做的任何更改将仅应用于当前场景，并且不会保存在磁盘上，也不会传播到其他场景中。

#### Save Group to Disk

将组保存到磁盘，随后便可通过标记菜单提供，并可以添加到任何网络。想要多次重复利用同一组节点和连接时，该功能非常有用。请参见[将 ShaderFX 组节点保存到磁盘](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-FCA7A0F1-D9E2-43BD-8DC9-145711CD9EC4.htm)。

## Tools 菜单

#### Compute Graph

每次更新“ShaderFX”编辑器时，场景视图也将自动更新。

如果您注意到这会影响性能，可以更改设置以在选择手动计算时仅更新场景。

若要执行此操作，请先启用 Settings > Manually Compute Graph，然后在每次要手动更新场景时选择 Tools > Compute Graph。

## Settings 菜单

#### Play Animated Shaders

选择此选项可以显示动画着色器的动画。

#### Manually compute graph

启用此选项可手动更新场景（而不是自动更新）。有关详细信息，请参见[Tools > Compute Graph](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-ED09BF8E-3B80-4F62-AF05-8539B1678151.htm#GUID-ED09BF8E-3B80-4F62-AF05-8539B1678151__SECTION_69199CDC78BE41EC8BCF8F6930A7EE88)。

#### Lock Group to Sides

默认情况下，会将组节点锁定到“ShaderFX”编辑器的四周。禁用该选项可自定义其位置和移动节点。

#### Overwrite System Nodes

默认情况下，您不能覆盖 Maya 附带的节点。若要执行此操作，必须启用该选项。

**注**

不建议覆盖 Maya 提供的系统节点。

#### Use 3dsMax Control Scheme

选择此选项可切换到 3dsMax 鼠标导航模式。

#### Show Property Panel

选择此选项，即在“ShaderFX”编辑器中显示“特性”(Properties)面板。此功能可使您无需使用“属性编辑器”(Attribute Editor)即可更改图表节点的属性。

#### 节点浏览器(Node Browser)

选择此选项以在“ShaderFX”编辑器中显示“节点浏览器”(Node Browser)。“节点浏览器”(Node Browser)为创建节点提供了一个快捷方式：选择要创建的节点，然后将其拖放到工作区。使用搜索字段即可轻松地找到所需的节点。您还可以通过以下方式创建节点：在工作区中单击鼠标右键 (![图：选择此选项以在“ShaderFX”编辑器中显示“节点浏览器”(Node Browser)。“节点浏览器”(Node Br…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-339814BD-5F9D-4AF0-AD24-9C56C81EB765.png) <!-- baize:img-hook downloaded=false reason="正文 1647 字 ≥300，非承重" -->) 并从标记菜单创建节点。

#### 显示样例编译错误(Show Swatch Compile Errors)

如果无法计算渲染样例，选择此选项后，工具提示即会显示在 ShaderFX 编辑器右下角并指明错误。

#### 显示节点 ID(Show Node ID)

选择此选项即可显示每个 ShaderFX 图形节点的唯一节点 ID，这样您便可以将该节点 ID 与其他节点/连接 MEL 命令一起使用。

#### Toggle Advanced Mode

**注**

仅适用于

“Shaderfx 着色器”(Shaderfx Shader)

网络。

选择此选项可打开和关闭高级模式。在高级模式下，可以选择创建更多节点。此外，您可以执行诸如替换默认材质（删除默认的“TraditionalGameSurfaceShader”节点和“材质”(Material)节点，然后创建自己的节点）等任务。
