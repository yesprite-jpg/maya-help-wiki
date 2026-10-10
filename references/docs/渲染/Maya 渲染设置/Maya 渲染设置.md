# Maya 渲染设置

![图：另请参见：渲染复杂场景（7 个视频）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-D621FFF0-6D97-4B30-93CC-ED26E2578E70.png) <!-- baize:img-hook downloaded=false reason="正文 1575 字 ≥300，非承重" --> [另请参见：渲染复杂场景（7 个视频）](https://www.youtube.com/playlist?list=PL8hZ6hQCGHMW_4jNxt4zaYW_XzPA6y0sI)

若要设置渲染，可以执行以下操作之一：

  创建**渲染层**。将场景拆分为若干层，然后使用集合填充它们。

  创建**集合**，以便根据要在场景中覆盖的属性对节点进行分组；例如，创建背景对象的集合，以便将其蒙版出角色。

  此外，创建集合以控制对象组的可见性。可以启用或禁用集合，这样只有已启用的集合才会影响层且可见，或者使用“隔离选择”重点处理视口中感兴趣的特定集合。

  集合成员身份基于名称，您可以通过表达式将对象动态添加到集合中。可以重新应用该表达式，动态地适应场景中的更改。请参见[更新场景时更新渲染设置](Maya%20渲染设置/更新场景时更新渲染设置.md)。这可用于轻松管理复杂场景中的数据更改。

  集合自上而下进行解释。因此，如果两个（或更多）集合共享对象且分别处于启用和禁用状态，则列表中排在最下面的集合将确定共享对象是否包含在层中。请参见[控制集合的可见性](Maya%20渲染设置/控制集合的可见性.md)。

  **当您创建覆盖时，系统可能自动创建子集合**。或者，为了更好地进行组织和控制，也可以手动创建子集合。子集合允许覆盖要仅在适用节点上执行的计算，从而更精细地控制哪些对象将接收覆盖，同时提高性能。此外，通过每个集合与子集合上的节点类型指示器，您可以轻松标识已应用覆盖的节点和对象。请参见[创建子集合](Maya%20渲染设置/为渲染层创建集合/创建子集合.md)。

- 为每个集合创建一个或多个**覆盖**，将非破坏性更改应用于场景。创建绝对覆盖可将属性设置为新值，或者创建相对覆盖可倍增原始值和/或添加偏移；例如，将应用于角色的着色器的透明度增加 10%。

  覆盖清楚地列在“特性编辑器”(Property Editor)中，并且可以轻松启用或禁用，以便进行实验和频繁修改。

- 将覆盖应用于层中的灯光。默认情况下，灯光位于层中。

- 可以 .json 文件格式导入或导出渲染设置（渲染层、集合和覆盖）。创建并导出主设定，然后导入并重用它来从序列中构建快照。

- 将渲染层设置为可渲染并进行批渲染。

单击状态行上的 ![图：单击状态行上的 ，可打开“渲染设置”(Render Setup)编辑器。此时将显示“渲染设置”(Render Setup…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-517E1929-F7EC-42AA-A5C2-FD9C91886318.png) <!-- baize:img-hook downloaded=false reason="正文 1575 字 ≥300，非承重" -->，可打开“渲染设置”(Render Setup)编辑器。此时将显示“渲染设置”(Render Setup)窗口，“渲染设置”(Render Setup)编辑器位于左侧，“特性编辑器”(Property Editor)位于右侧。“渲染设置”(Render Setup)编辑器可用于创建层、集合和覆盖，而特性编辑器”(Property Editor)则可用于设置相应的值。此外，“渲染设定”(Render Setup)编辑器可让您通过“场景”(Scene)选项卡访问场景设置。

如果选择“渲染 - 标准”(Rendering - Standard)或“渲染 - 专家”(Rendering - Expert)工作区，则系统会自动停靠“渲染设置”(Render Setup)和“特性编辑器”(Property Editor)窗口。

此渲染设置系统和传统渲染层系统是分离而独立的系统，在给定的 Maya 会话期间只能使用其中一个系统。此外，给定场景只能使用这两个系统之一，无法同时使用二者。若要在系统之间进行切换，请选择“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)以打开“首选项”(Preferences)窗口，然后导航到“渲染”(Rendering)类别。选择“传统渲染层”(Legacy Render Layers)或“渲染设置”(Render Setup)作为“首选渲染设置系统”(Preferred Render Setup system)，然后重新启动 Maya。

**注**

但是，不必切换系统即可对场景文件进行**批渲染**。

在本示例中，第一层具有的集合包含乌贼角色。在着色器的“透明度”(Transparency)属性上应用覆盖；因此系统自动创建了 Killamari_shaders 子集合。第二层具有的集合包含“小黄人”角色的铠甲，一个相对覆盖应用于其“旋转”(Rotate)属性，同时另一个相对覆盖应用于其“平移”(Translate)属性。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-29375B0B-964D-40DF-8CB8-9016FBAC3D5E.png) <!-- baize:img-hook downloaded=false reason="正文 1575 字 ≥300，非承重" -->
