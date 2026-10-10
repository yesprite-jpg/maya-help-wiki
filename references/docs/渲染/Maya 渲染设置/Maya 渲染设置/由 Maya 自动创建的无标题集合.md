# 由 Maya 自动创建的无标题集合

如果您在位于活动的渲染层（此层是除场景层设置为可见以外的层）中时创建了一个对象，则将自动创建一个名为 _untitled_ 的集合，其中包含该对象。

您在位于渲染层中时创建的其他对象也会添加到 _untitled_ 集合。

可以重命名 _untitled_ 集合。但重命名该集合之后，如果您在位于活动渲染层中时创建了其他对象，则将再次创建**新的** _untitled_ 集合。

其他 _untitled_ 集合（在其他渲染层中创建）命名为 _untitled_1、_untitled_2，依此类推。

## 避免创建无标题集合

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 700 字 ≥300，非承重" -->

禁用**“选项 > 创建新对象后启用‘untitled’集合”(Options > Enable untitled collections when new objects are created)**可避免向活动渲染层添加新对象时创建无标题集合。

您可以随时禁用此选项，即使场景中存在无标题集合以及即使当前渲染层中存在无标题集合也是如此。在后一种情况下，您创建的任何其他新对象不会添加到现有的无标题集合中。

此设置与首选项一起保存在选项变量 renderSetup_useUntitledCollections 中，并在重新启动 Maya 时保留。

还可以通过设置环境变量 MAYA_RENDER_SETUP_USE_UNTITLED_COLLECTIONS 控制此选项。值为 0 时禁用该选项，值为 1 时启用该选项。该环境变量优先于首选项。设置该环境变量后，“选项 > 创建新对象后启用‘untitled’集合”(Options > Enable untitled collections when new objects are created)菜单选项将灰显，系统将应用该环境变量值。
