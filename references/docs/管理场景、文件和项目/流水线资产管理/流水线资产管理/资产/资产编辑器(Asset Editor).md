# 资产编辑器(Asset Editor)

- 若要打开“资产编辑器”(Asset Editor)，请选择“窗口 > 常规编辑器 > 资产编辑器”(Windows > General Editors > Asset Editor)。

“资产编辑器”(Asset Editor)允许从单一窗口管理场景中的所有资产。它包含两个面板。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-21FF9B7B-6EC9-42FE-BD02-B6E2EC805F63.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

类似于“大纲视图”(Outliner)，左侧面板显示一个列表，列出在场景中的所有资产及其属性。在该面板中，可以：

- 查看和排列资产

- 发布和取消发布属性

- 选择要编辑的特定资产

右侧面板显示在左侧面板中选择的资产的模板绑定信息。在右侧面板中，可以：

- 将已发布属性与模板中的已发布名称绑定或取消其绑定

- 发布或取消发布未绑定的属性

- 重命名已发布属性

可以使用“资产编辑器”(Asset Editor)来管理已发布名称和内部节点属性之间的绑定。“资产编辑器”(Asset Editor)也是管理场景中模板的主界面。除了这两个功能，还可以发布/取消发布属性、从资产添加和移除节点、创建“视图”(Views)和“绑定集”(Binding Sets)以及执行其他任何与资产相关的操作。

“资产编辑器”(Asset Editor)有两种操作模式。在“选择资产”模式中，可以快速遍历资产到资产，并显示单个资产的节点内容和属性。

在“已锁定资产”模式中，可以发布或取消发布左侧面板中的属性，并绑定和取消绑定右侧面板中的属性。也可以创建视图和绑定集。

可以旋转一个资产并单击“锁定资产”图标 ![图：可以旋转一个资产并单击“锁定资产”图标 ，以在这些模式之间切换。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-F9B182B8-BA9F-4BAC-9C23-20BF314F9514.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->，以在这些模式之间切换。

在左侧面板中，选定属性将亮显。在右侧面板中，选定属性以箭头图标显示。

## 相关主题

- [资产](../资产.md)

- [资产模板](资产模板.md)

## 大纲视图（选择资产模式）

| 目标 | 操作 |
|---|---|
| 切换到“已锁定资产”模式 | 在左侧面板中选择一个资产，然后单击“锁定资产”图标 ![图：在左侧面板中选择一个资产，然后单击“锁定资产”图标 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-F9B182B8-BA9F-4BAC-9C23-20BF314F9514.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->。 |
| 展开或收拢节点下的级别 | 单击节点名称旁边的加号 ![图：单击节点名称旁边的加号 或减号 图标。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-370190BF-6612-4E4A-AD24-7A5100A32840.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" --> 或减号 ![图：单击节点名称旁边的加号 或减号 图标。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-97F99310-F0E3-49A2-90EB-2A927A31063C.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" --> 图标。 |
| 展开节点下的所有级别 | 按住 Shift 键并单击节点名称旁边的加号 ![图：按住 Shift 键并单击节点名称旁边的加号 图标。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-370190BF-6612-4E4A-AD24-7A5100A32840.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" --> 图标。 |
| 显示或隐藏节点上的属性 | 单击节点名称旁边的加号 (![图：单击节点名称旁边的加号 () 或减号 () 图标。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-CD1F5A9B-A585-4A34-A604-34D3DBEE71CD.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->) 或减号 (![图：单击节点名称旁边的加号 () 或减号 () 图标。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-79A28963-9A0A-4561-A400-42914528DDDB.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->) 图标。 可以进一步展开多值属性。 |
| 重新排序层次中的节点 | 按住鼠标中键并将节点拖动到层次中的新位置。 |
| 将节点从一个资产移动到另一个资产 | 按住鼠标中键并将节点从一个资产拖动到另一个资产。 |
| 使节点成为另一个节点的子对象 | 按住鼠标中键并将节点拖动到要成为其父对象的节点上。 |
| 搜索特定节点 | 在文本字段中输入要寻找节点的完整名称或部分名称，并按 Enter 键。 |

## 大纲视图（已锁定资产模式）

| 目标 | 操作 |
|---|---|
| 发布属性 | 在左侧面板中，选择要发布的属性，然后单击“发布”图标 ![图：在左侧面板中，选择要发布的属性，然后单击“发布”图标 或“发布为”图标 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-1E0CA812-AEB8-43C8-B9AF-707911B90A7C.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" --> 或“发布为”图标 ![图：在左侧面板中，选择要发布的属性，然后单击“发布”图标 或“发布为”图标 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-51B03172-ABA6-48F0-8476-4424B5A310F7.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->。 |
| 取消发布属性 | 在左侧面板中，选择要取消发布的属性，然后单击“曲线分布”图标 ![图：在左侧面板中，选择要取消发布的属性，然后单击“曲线分布”图标 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-28D5F753-E2E8-4E32-9640-B634E7B72822.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->。 |
| 指定模板 | 选择“模板 > 指定”(Template > Assign)并从显示的列表中选择模板，或旋转“指定新模板”(Assign New Template)并从文件浏览器中选择资产。 |
| 将已固定资产的已发布的名称另存为模板 | 选择“模板 > 另存为”(Template > Save As)并输入模板名称和位置。 |
| 选择属性 | 在左侧面板中选择属性名称，或在右侧面板中单击名称旁边包含小箭头的框。 |
| 绑定/取消绑定属性或节点 | 在右侧面板中单击节点名称旁边的“绑定”图标 ![图：在右侧面板中单击节点名称旁边的“绑定”图标 或“取消绑定”图标 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-FBE8085A-7D7F-4950-B2C4-C13C3E776F93.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" --> 或“取消绑定”图标 ![图：在右侧面板中单击节点名称旁边的“绑定”图标 或“取消绑定”图标 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-6524565D-19CA-4226-9DB7-7E197AE08279.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->。 |
| 重命名已发布属性或节点 | 在右侧面板中选择属性或节点，并单击“重命名”图标 ![图：在右侧面板中选择属性或节点，并单击“重命名”图标 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-2364AF92-8D66-4B29-B5EA-0E1A5DA97763.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->。 |
| 将视图添加到当前模板 | 使用当前加载的模板时，选择“视图 > 添加”(View > Add)。 |
| 从当前已发布属性创建绑定集 | 使用当前加载的模板时，选择“模板 > 创建绑定集”。Maya 将添加名为 MayaBinding 的绑定集到模板。 |
| 使用当前已发布属性更新当前绑定集 | 在加载当前的模板后，选择模板 > 更新绑定集。 |
| 移除绑定集 | 在加载当前的模板后，选择模板 > 移除绑定集。Maya 将移除名为“MayaBinding”的绑定集。 |
| 刷新左侧和右侧面板 | 单击“刷新”图标 (![图：单击“刷新”图标 ()。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-251830DD-4F5A-42B6-8C9C-B17A4E15F1BF.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->)。 |

**注**

可以选择多个已发布的名称或属性，方法是按住 Shift 键的同时单击它们。

## 资产编辑器按钮

“资产编辑器”(Asset Editor)按钮控制发布或绑定属性的方式。

#### 锁定/取消锁定资产 ![图：锁定/取消锁定资产](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-F9B182B8-BA9F-4BAC-9C23-20BF314F9514.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

锁定选定的资产进行编辑。“资产编辑器”(Asset Editor)更改为“已锁定资产”模式，同时仅选定资产显示在左侧面板中。在右侧面板中显示已发布绑定和未绑定属性显示用于编辑。

再次单击该图标以取消锁定当前选定资产，并返回到“选择资产”模式。在“选择资产”模式时，所有资产将显示在左侧面板中，同时右面板为空。

#### 选择(Select) ![图：选择(Select)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-FC0E3440-D286-4B10-BAA7-84AA30CE9F9E.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

在右侧面板中选择已发布名称。选择图标以三种颜色显示。

绿色表示已发布名称来自指定模板。

黄色表示有一个模板已指定给资产，但选中已发布名称不源自它。

红色表示没有指定模板给资产。

#### 发布(Publish) ![图：发布(Publish)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-1E0CA812-AEB8-43C8-B9AF-707911B90A7C.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

发布选定属性到封装它的最低级别资产。属性被绑定到匹配属性名称的默认已发布名称。

如果资产上已经存在相同的已发布名称，新的已发布名称将附加有一个数字。

#### 发布为...(Publish As...) ![图：发布为...(Publish As...)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-51B03172-ABA6-48F0-8476-4424B5A310F7.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

发布选定属性到封装它的最低级别资产。属性被绑定到您选择的已发布名称。

#### 取消发布(Unpublish) ![图：取消发布(Unpublish)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-28D5F753-E2E8-4E32-9640-B634E7B72822.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

从其已发布名称取消绑定选定属性，并从资产移除已发布名称。只能取消发布其名称不源自指定模板的属性。

#### 取消绑定选定项(Unbind selected) ![图：取消绑定选定项(Unbind selected)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-6524565D-19CA-4226-9DB7-7E197AE08279.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

从其相应属性取消绑定选定已发布名称。

#### 发布名称(Publish Name) ![图：发布名称(Publish Name)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-1E0CA812-AEB8-43C8-B9AF-707911B90A7C.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

在资产上创建已发布名称而不绑定属性给它。

#### 取消发布名称(Unpublish Name) ![图：取消发布名称(Unpublish Name)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-28D5F753-E2E8-4E32-9640-B634E7B72822.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

从资产移除已发布名称。

只能移除未绑定以及不源自指定模板的已发布名称。

#### 重命名已发布名称(Rename Published Name) ![图：重命名已发布名称(Rename Published Name)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-2364AF92-8D66-4B29-B5EA-0E1A5DA97763.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

重命名已发布的名称。

只能重命名不源自指定模板的属性和节点的已发布名称。

#### 刷新(Refresh) ![图：刷新(Refresh)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-251830DD-4F5A-42B6-8C9C-B17A4E15F1BF.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

更新右侧面板。

#### 绑定(Bind) ![图：绑定(Bind) / 取消绑定(Unbind)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-FBE8085A-7D7F-4950-B2C4-C13C3E776F93.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" --> / 取消绑定(Unbind)![图：绑定(Bind) / 取消绑定(Unbind)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-6524565D-19CA-4226-9DB7-7E197AE08279.png) <!-- baize:img-hook downloaded=false reason="正文 4590 字 ≥300，非承重" -->

从其对应已发布名称绑定或取消绑定选定属性。

## 资产编辑器菜单栏

有关“显示”(Display)和“显示”(Show)菜单的信息，请参见[大纲视图](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4B9A9A3A-83C5-445A-95D5-64104BC47406)。

有关“资产”(Asset)菜单上的信息，请参见[资产](../资产.md)。

有关“传递属性值”(Transfer Attribute Values)的信息，请参见[“传递属性值”(Transfer Attribute Values)选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DB5835DD-C3D4-48A6-855D-3A0A673EB4D3)。

### 模板菜单

“资产编辑器”(Asset Editor)中的“模板”(Template)菜单提供了创建和指定模板到资产的所有选项。

**注**

“模板”(Template)菜单仅在您处于“已锁定资产”模式时可用。

“模板”(Template)菜单包含以下选项：

#### 指定(Assign)

允许您选择和指定模板给当前已锁定资产。

#### 取消指定(Unassign)

断开已锁定资产及其指定模板之间的关联。请参见[从资产取消指定模板](创建资产模板和视图/为资产指定模板.md)。

#### 保存(Save)

从已锁定资产保存已发布名称到模板文件。请参见[保存资产模板](创建资产模板和视图/保存资产模板.md)。

**注**

若要防止模板的其他用户使用

“模板 > 保存”(Template > Save)

覆盖模板文件，建议写保护模板文件。

#### 另存为(Save As)

允许您从已锁定资产创建已发布名称的新模板。请参见[保存资产模板](创建资产模板和视图/保存资产模板.md)。

#### 自动绑定资产(Autobind Asset)

基于绑定集自动发布和绑定模板中的已发布名称给资产中的属性。该选项仅在当前模板具有有效绑定集时可用。

默认情况下，“自动绑定资产”(Autobind Asset)仅考虑未绑定的已发布名称。

#### 全部自动绑定(Autobind All)

启用后，“自动绑定资产”(Autobind Asset)命令将考虑所有已发布名称（绑定和未绑定）。

#### 力(Force)

启用后，“自动绑定资产”(Autobind Asset)命令将完全强制模板的绑定集，以便生成的资产与它匹配。如果未在绑定集中找到现有已发布名称的匹配项，Maya 将强制取消绑定它。

#### 创建绑定集(Create Binding Set)

基于资产的当前已发布属性，在当前模板中创建绑定集条目。

#### 更新绑定集(Update Binding Set)

使用资产的当前已发布属性更新当前已指定模板的绑定集条目。

#### 移除绑定集(Remove Binding Set)

从当前模板移除所有绑定集条目。

#### 重新加载(Reload)

重新加载指定模板。请参见[重新加载资产模板](创建资产模板和视图/重新加载资产模板.md)。

### 视图菜单

“资产编辑器”(Asset Editor)中的“视图”(View)菜单提供了创建自定义资产布局所需的所有选项。

处理视图之前，必须为资产创建模板。有关创建资产模板的详细信息，请参见[创建资产样板](创建资产模板和视图/创建资产模板.md)。

在添加视图到模板后，可以编辑该模板文件以更改视图布局。有关自定义视图的详细信息，请参见[自定义模板视图](创建资产模板和视图/自定义模板视图.md)。

**注**

“视图”(View)

菜单仅在您处于“已锁定资产”模式时可用。

“视图”(View)菜单包含以下选项：

#### 模式(Mode)

允许您从两个默认布局中选择，或使用资产属性的自定义视图布局。从下列选项中进行选择：

#### 平坦(Flat)

在列表中显示资产的已发布属性名称。这是不使用模板的默认视图。

#### 使用模板(Use Template)

基于其当前模板显示资产的已发布属性名称。当选择“使用模板”(Use Template)后，可以从“视图 > 名称”(View > Name)菜单项选择自定义视图。

#### 按节点分组(Group by Node)

基于其绑定的节点，在组中显示资产的已发布属性名称。这是不使用模板的默认视图。

#### 名称(Name)

允许您从可用模板视图中选择。该选项仅在“视图模式”(View Mode)被设定为“使用模板”(Use Template)时可用。

如果模板没有已定义视图，或者如果设定“名称”(Name)为“无”(None)，将以在模板中所定义的顺序显示已发布属性。

#### 添加(Add)

基于默认选项将新视图添加到指定模板。默认情况下，新视图被命名为 viewName。请参见[添加自定义视图到容器模板](创建资产模板和视图/为资产模板添加视图.md)。

#### 名称(Name)

允许您输入视图的名称。这是将显示在“资产编辑器”(Asset Editor)的“视图 > 名称”(View > Name)列表和“属性编辑器”(Attribute Editor)的“视图名称”(View Name)字段的名称。

#### 使资产与模板同步(Sync asset to template)

启用后，Maya 会将来自资产但尚未保存到模板的任何已发布名称添加到模板。任何添加的名称都将被包含在新视图中。

#### 保存模板(Save Template)

启用后，该模板连同新视图将被保存到磁盘上的模板文件中。禁用后，将在内部添加新视图，但不保存模板文件。

#### 切换到新视图(Switch to new view)

启用后，将更新“资产编辑器”(Asset Editor)的右侧面板，以显示组织已发布属性名称的最新创建自定义视图的资产。

#### 展开复合(Expand Compounds)

设定是否将复合属性作为单个条目包含在视图定义中。这会影响视图在 Maya 窗口和编辑器中显示属性的方式。

启用后，子属性将单独包含在视图中，而且它们将与独立的界面控件一起显示。

例如，将为 translateX、translateY 和 translateZ 分别显示滑块和值字段。

**注**

如果

仅

希望显示各个子对象控件（而不显示父组控件），则可以在模板文件中编辑视图定义，然后重新加载模板。请参见

自定义模板视图

和

重新加载容器模板

。

当“展开复合”(Expand Compounds)处于禁用状态时，子属性不会单独列在视图中。使用组控件可以显示父属性（及其子属性）。

#### 布局模式(Layout Mode)

允许您选择平坦或按节点分组作为新视图已发布名称的原始布局。

在添加视图到模板后，可以编辑该模板以更改其布局。请参见[自定义模板视图](创建资产模板和视图/自定义模板视图.md)。
