# 面板编辑器(Panel Editor)

打开面板编辑器

- 在主菜单栏中：“窗口 > 设置/首选项 > 面板编辑器”(Windows > Settings/Preferences > Panel Editor)

- 在场景视图中：“面板 > >面板编辑器”(Panels > Panel Editor)

- 在任意[快速布局按钮](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-693FBB4C-4010-4D55-8215-67FBE19114E7)上单击鼠标右键，然后选择“编辑布局”(Edit Layouts)

## 选项卡

### 面板(Panels)

显示可以重命名或删除的现有 Maya UI 面板。

- 选择一个面板并编辑“标签”(Label)字段可将其重命名。您无法重命名“顶视图”、“侧视图”、“前视图”或“透视视图”面板。

- 选择一个面板并单击“删除”(Delete)可将其从列表中移除。

  ![图：选择一个面板并单击“删除”(Delete)可将其从列表中移除。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-37842407-8CE7-49D1-9B60-DF584AD9A671.png) <!-- baize:img-hook downloaded=false reason="正文 1087 字 ≥300，非承重" -->

### 新建面板(New Panel)

包含用于创建新面板类型的控件。

- [将新面板添加到可用面板列表](创建面板的多个实例.md)

  ![图：将新面板添加到可用面板列表](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-91A69450-0949-4C81-A160-1DB6E8EC028A.png) <!-- baize:img-hook downloaded=false reason="正文 1087 字 ≥300，非承重" -->

### 布局(Layouts)

显示现有面板布局。

- 单击“新建布局”(New Layout)可向列表中添加项目。

- 单击一个布局并单击“编辑布局”(Edit Layouts)选项卡可对其进行编辑。

- 若要删除布局，请在列表中单击它，再单击“删除”(Delete)。

### 编辑布局(Edit Layouts)

显示当前面板布局以进行编辑。

- [创建自定义面板布局](创建自定义面板布局.md)

  #### 配置(Configurations)

  使用该选项卡可更改布局的配置和比例。

  从下拉列表中，选择所需的面板布局。

  通过在布局的缩略图中拖动边框来调整窗格大小。主窗口将更改，以反映您所做的更改。

  ![图：使用该选项卡可更改布局的配置和比例。 从下拉列表中，选择所需的面板布局。 通过在布局的缩略图中拖动边框来调整窗格大小。主…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-629430BA-74FD-4970-A77E-9F6B4CC84DC4.png) <!-- baize:img-hook downloaded=false reason="正文 1087 字 ≥300，非承重" -->

  #### 内容(Contents)

  使用该选项卡可更改在布局中显示哪些面板内容。

  #### 与场景无关(Scene Independent)

  与场景无关的布局可用于所有场景。它们的内容由面板类型定义。

  如果在一个场景中具有多个相同类型的面板，则无法确定在您选择布局时会显示哪些面板。在大多数情况下，这不是问题；但是，如果在特定场景中的工作非常多，则可能希望开发布局以专门与该场景一起保存。

  #### 与场景关联(Associated with Scene)

  这些布局仅在当前场景中可用。如果您具有多个相同类型的面板，则可以指定一个特定面板。

  ![图：这些布局仅在当前场景中可用。如果您具有多个相同类型的面板，则可以指定一个特定面板。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-94A82BBD-2830-40BC-9456-3150D3228B4F.png) <!-- baize:img-hook downloaded=false reason="正文 1087 字 ≥300，非承重" -->

### 历史(History)

显示使用过的面板的历史。

Maya 会记录面板布局更改。这使您可以向前或向后浏览每个视图。如果要在两个布局之间切换，但是不记得它们的名称，这非常有帮助。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-84D6F87D-17EF-4980-B82B-8EF870504800.png) <!-- baize:img-hook downloaded=false reason="正文 1087 字 ≥300，非承重" -->

#### 历史深度(History Depth)

指定您希望存储在历史中的配置数。

#### 包裹历史(Wrap History)

开启该选项可在您达到记录历史的末尾时返回到第一个视图或最新视图配置。

#### 清空历史(Clear History)

删除使用过的所有面板的记录。

#### 上一个布局(Previous Layout)

向后浏览面板布局。

#### 下一个布局(Next Layout)

向前浏览面板布局。

## 相关主题

- [快速布局按钮](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-693FBB4C-4010-4D55-8215-67FBE19114E7)
