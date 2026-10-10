# “属性编辑器”(Attribute Editor)菜单

## 列表(List)

使用该菜单可将属性加载到“属性编辑器”(Attribute Editor)中，并定义哪些项目会显示在“选定/对象”(Selected/Object)菜单中。

## 选定/对象 (Selected/Object)

“选定”(Selected)菜单列出场景中当前选定的对象，而“对象”(Object)菜单显示选定类型的场景中的所有对象。

## 关注(Focus)

该菜单显示当“属性编辑器”(Attribute Editor)打开时在场景中已选择的所有节点。最近选择的节点位于列表的顶部。

## 属性(Attributes)

使用该菜单可以为对象或节点添加、编辑和删除附加属性。这些属性显示在“附加属性”(Extra Attributes)区域下。也可以使用“修改”(Modify)菜单来添加、编辑和删除属性。

可从下列选项中选择：

#### 添加属性(Add Attributes)

打开“添加属性”(Add Attributes)窗口。请参见[添加属性(Add Attributes)](../../../../基本参考/基本参考/主菜单/“修改”%28Modify%29菜单/“添加属性”%28Add%20Attribute%29选项.md)。

#### 删除属性(Delete Attributes)

打开“删除属性”(Delete Attributes)窗口。

#### 编辑属性(Edit Attributes)

打开“编辑属性”(Edit Attributes)窗口。请参见[编辑属性(Edit Attributes)](../../../../基本参考/基本参考/主菜单/“修改”%28Modify%29菜单/“编辑属性”%28Edit%20Attribute%29选项.md)。

## 显示(Display)

#### 属性名称

包含若干属性命名选项。“易读”(Nice)显示可读性最强的属性名称，“长”(Long)显示完整的属性名称，“短”(Short)显示缩短的属性名称。长名称和短名称可用于表达式和 MEL 脚本。请参见[属性名称](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F0C690E1-B2F1-4C17-85B2-2EC3E9A317A1)。

## 显示(Show)

#### 按节点类型(By Node Type)

按节点类型显示在“属性编辑器”(Attribute Editor)中的过滤器选项卡。该菜单将显示当前可用的相关节点类型过滤器及其状态的列表。您可以切换各个节点类型过滤器；如果启用一个节点类型过滤器，该类型的节点将从相关的选项卡中过滤掉。

可以从以下全局选项中选择：

- 启用全部(Enable All)：启用所有可用的节点类型过滤器。

- 切换全部(Toggle All)：切换所有可用的节点类型过滤器。

  例如，如果在“按节点类型”(By Node Type)菜单中启用 polyTweak，则 polyTweak 类型的节点将从相关选项卡中过滤掉。选择“切换全部”(Toggle All)将禁用 polyTweak。因此，polyTweak 类型的节点将不再从相关的选项卡中过滤掉。

  如果在“按节点类型”(By Node Type)菜单中禁用 polyTweak，polyTweak 类型的节点将包含在相关选项卡中。选择“切换全部”(Toggle All)将启用 polyTweak。因此，polyTweak 类型的节点将从相关的选项卡中过滤掉。

- 禁用全部(Disable All)：禁用所有可用的节点类型过滤器。

#### 添加新过滤器类型(Add New Filter Type)

打开“定义新过滤器类型”(Define New Filter Type)窗口，使您可以为指定的节点类型创建一个过滤器。

#### 为选定对象添加过滤器类型(Add Filter Types for Selected)

为当前选定的每个节点类型添加新节点过滤器。

**注**

已定义过滤器的节点类型将被忽略。

#### 为相关对象添加过滤器类型(Add Filter Types for Related)

为与当前选择相关的每个节点类型添加新节点过滤器。（即在“属性编辑器”(Attribute Editor)中针对每个节点类型至少显示一个选项卡)。

**注**

已定义过滤器的节点类型将被忽略。

#### 移除过滤器类型(Remove Filter Type)

您可以从“显示”(Show)菜单移除现有的节点类型过滤器。

#### 保存显示预设(Save Show Preset)

打开“保存过滤器类型预设”(Save Filter Type Preset)对话框。输入一个预设名，以便在首选项中保存当前过滤器及其状态。

#### 加载显示预设(Load Show Preset)

通过从此列表中选择名称加载现有的显示过滤器预设。

#### 设置当前视图(Set Current View)

显示可应用于选定节点的视图列表。请参见[应用属性编辑器模板](自定义“属性编辑器”%28Attribute%20Editor%29/自定义“属性编辑器”%28Attribute%20Editor%29模板/应用“属性编辑器”%28Attribute%20Editor%29模板.md)或[刷新“属性编辑器”(Attribute Editor)模板](自定义“属性编辑器”%28Attribute%20Editor%29/自定义“属性编辑器”%28Attribute%20Editor%29模板/刷新“属性编辑器”%28Attribute%20Editor%29模板.md)。

#### 设置全局视图(Set Global View)

显示可应用于具有相同自定义模板视图的所有节点类型的视图列表。请参见[应用属性编辑器模板](自定义“属性编辑器”%28Attribute%20Editor%29/自定义“属性编辑器”%28Attribute%20Editor%29模板/应用“属性编辑器”%28Attribute%20Editor%29模板.md)或[刷新“属性编辑器”(Attribute Editor)模板](自定义“属性编辑器”%28Attribute%20Editor%29/自定义“属性编辑器”%28Attribute%20Editor%29模板/刷新“属性编辑器”%28Attribute%20Editor%29模板.md)。

#### 如果无全局视图，则显示默认视图(Show default if no global view)

启用此选项后，如果节点类型没有在其自定义模板中定义选定的全局视图，“属性编辑器”(Attribute Editor)将还原为默认模板。如果节点类型不具有自定义模板，则“属性编辑器”(Attribute Editor)将使用上一次应用的自定义模板视图。

#### 显示视图标签(Show View Labels)

启用后，该选项将显示当前选定视图的名称及其关联的模板。请参见[应用“属性编辑器”(Attribute Editor)模板](自定义“属性编辑器”%28Attribute%20Editor%29/自定义“属性编辑器”%28Attribute%20Editor%29模板/应用“属性编辑器”%28Attribute%20Editor%29模板.md)。

#### 显示注释(Show Notes)

启用后，此选项将在“属性编辑器”(Attribute Editor)的每个选项卡底部显示一个“注释”(Notes)区域。如果已禁用“显示注释”(Show Notes)，则当您创建新场景或重新启动 Maya 时该选项将保持禁用状态。

#### 显示颜色管理缸(Show Color Managed Pots)

启用颜色控件的颜色管理，包括纯色和渐变。此设置存储在[“颜色管理”(Color Management)首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2D9BBB9D-49F0-44C6-8BFF-B237FD8ED746)中。
