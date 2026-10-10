# 使用渲染设置创建 AOV 覆盖

创建覆盖可启用或禁用每个渲染层上的不同 AOV，或者导出 AOV 并将其导入其他场景中。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1301 字 ≥300，非承重" -->

通过“渲染设置”(Render Settings)窗口的 Arnold for Maya“AOV”(AOVs)选项卡创建 AOV。然后，可以按照下列步骤在每个渲染层上创建覆盖。

创建覆盖以禁用 AOV

1. 在要创建覆盖的渲染层上单击 ![图：在要创建覆盖的渲染层上单击 ，将该层设置为可见。 注： 请确保您未在渲染层中选择任何集合。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-8FE3D3FC-212F-4816-99B0-C3DBB08C8AF5.png) <!-- baize:img-hook downloaded=false reason="正文 1301 字 ≥300，非承重" -->，将该层设置为可见。

  **注**

  请确保您未在渲染层中选择任何集合。

2. 双击“渲染设置”(Render Setup)编辑器的“场景”(Scene)设置中的 AOV 选项卡可打开“渲染设置”(Render Settings)窗口。

  **注**

  提示：

  ![图：也可以通过“渲染设置”(Render Setup)编辑器菜单中的“首选项 AOV”(Preferences AOVs)访…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1301 字 ≥300，非承重" --> 也可以通过“渲染设置”(Render Setup)编辑器菜单中的“首选项 > AOV”(Preferences > AOVs)访问 AOV 选项卡。

  在“AOV”(AOVs)选项卡中，在 AOV 名称旁边的复选框上单击鼠标右键，然后选择“为可见层创建绝对覆盖”(Create Absolute Override for Visible Layer)。

  此时会创建“AOV”(AOVs)集合，以及 <AOV 名称> 子集合和启用覆盖。

4. 选择此启用覆盖，然后在“特性编辑器”(Property Editor)中将其禁用。

覆盖过滤器或驱动者属性

1. 在要创建覆盖的渲染层上单击 ![图：在要创建覆盖的渲染层上单击 ，将该层设置为可见。 注： 请确保您未在渲染层中选择任何集合。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-8FE3D3FC-212F-4816-99B0-C3DBB08C8AF5.png) <!-- baize:img-hook downloaded=false reason="正文 1301 字 ≥300，非承重" -->，将该层设置为可见。

  **注**

  请确保您未在渲染层中选择任何集合。

2. 双击“渲染设置”(Render Setup)编辑器的“场景”(Scene)设置中的 AOV 选项卡可打开“渲染设置”(Render Settings)窗口。

  **注**

  提示：

  ![图：也可以通过“渲染设置”(Render Setup)编辑器菜单中的“首选项 AOV”(Preferences AOVs)访…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1301 字 ≥300，非承重" --> 也可以通过“渲染设置”(Render Setup)编辑器菜单中的“首选项 > AOV”(Preferences > AOVs)访问 AOV 选项卡。

3. 在 AOV 选项卡中，在 AOV 条目旁边的 ![图：在 AOV 选项卡中，在 AOV 条目旁边的 图标上单击鼠标左键，然后选择“选择驱动者”(Select Driver)以…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-B3673DA8-6639-4D95-ABC3-DDBE68FB5081.png) <!-- baize:img-hook downloaded=false reason="正文 1301 字 ≥300，非承重" --> 图标上单击鼠标左键，然后选择“选择驱动者”(Select Driver)以显示 AOV 驱动者节点的“属性编辑器”(Attribute Editor)（或者，选择“选择过滤器”(Select Filter)以显示过滤器节点的“属性编辑器”(Attribute Editor)）。

4. 在要覆盖的属性上单击鼠标右键，然后选择“为可见层创建绝对覆盖”(Create Absolute Override for Visible Layer)或“为可见层创建相对覆盖”(Create Relative Override for Visible Layer)。

**注**

默认过滤器和驱动者节点带有 < > 标志，例如 <exr>。覆盖默认过滤器或驱动者节点的属性时，将在

“渲染设置”(Render Settings)

集合下面创建一个覆盖。否则，覆盖非默认过滤器或驱动者节点的属性时，将改为在

“AOV”(AOVs)

集合下面创建一个覆盖。

**注**

您可以剪切、复制和粘贴以下内容：

- 将“AOV”(AOVs)集合从一个渲染层剪切/复制/粘贴到另一个渲染层

- 将 <AOV_name> 子集合（如 *diffuse* 或 *opacity*）从一个 AOV 集合剪切/复制/粘贴到另一个 AOV 集合（或在同一 AOV 集合中执行相关操作）

- 将 AOV 覆盖（如 *enabled* 或 *mergeAOVs*）从一个子集合剪切/复制/粘贴到另一个子集合（或在同一子集合中执行相关操作）

## 导出和导入 AOV

请参见[导出和导入 AOV](导出渲染设置/导出和导入%20AOV.md)。
