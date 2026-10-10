# 在 Hypershade 中暂停 Viewport 2.0 和材质查看器

您可以在 Viewport 2.0、“材质查看器”(Material Viewer)以及“UV 编辑器”(UV Editor)等其他编辑器中暂停更新。允许您在场景中进行更改，而不必等待编辑器更新。这特别适用于复杂场景。

单击 Maya 状态行或“材质查看器”(Material Viewer)工具栏中的 ![图：单击 Maya 状态行或“材质查看器”(Material Viewer)工具栏中的 可暂停更新。暂停的编辑器以红色边界显…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A856707B-0550-4DFA-AEB1-590B0FF7D219.png) <!-- baize:img-hook downloaded=false reason="正文 1121 字 ≥300，非承重" --> 可暂停更新。暂停的编辑器以红色边界显示，且文本“暂停”(Paused)指示其暂停状态。如果存在上次缓存渲染的图像，则“材质查看器”(Material Viewer)将显示此图像来代替文本“暂停”(Paused)。

单击 Maya 状态行中的 ![图：单击 Maya 状态行中的 时，所有使用 Viewport 2.0 渲染器的编辑器也会暂停。其中包括：“材质查看器”(M…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A856707B-0550-4DFA-AEB1-590B0FF7D219.png) <!-- baize:img-hook downloaded=false reason="正文 1121 字 ≥300，非承重" --> 时，所有使用 Viewport 2.0 渲染器的编辑器也会暂停。其中包括：“材质查看器”(Material Viewer)（如果设置为使用硬件渲染器）和“UV 编辑器”(UV Editor)。如果“渲染视图”(Render View)设置为使用“硬件 2.0 ”(Hardware 2.0)渲染器，则渲染也将停止。同样，如果在设置为使用硬件渲染器时单击“材质查看器”(Material Viewer)中的 ![图：单击 Maya 状态行中的 时，所有使用 Viewport 2.0 渲染器的编辑器也会暂停。其中包括：“材质查看器”(M…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A856707B-0550-4DFA-AEB1-590B0FF7D219.png) <!-- baize:img-hook downloaded=false reason="正文 1121 字 ≥300，非承重" -->，这些编辑器也会暂停。

再次单击 ![图：再次单击 可解除暂停，并且使用暂停期间进行的所有更改更新场景。每个受影响面板的内容会重新渲染并继续监视场景更新。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A856707B-0550-4DFA-AEB1-590B0FF7D219.png) <!-- baize:img-hook downloaded=false reason="正文 1121 字 ≥300，非承重" --> 可解除暂停，并且使用暂停期间进行的所有更改更新场景。每个受影响面板的内容会重新渲染并继续监视场景更新。

硬件渲染器和插件渲染器分别暂停。暂停 Viewport 2.0 不会影响使用硬件渲染器进行的渲染，其中包括插件渲染器。例如，您仍可在“渲染视图”(Render View)中使用 IPR 进行渲染。在“材质查看器”(Material Viewer)中选择 Arnold for Maya 等插件渲染器作为渲染器时，渲染也可能会独立于 Viewport 2.0 暂停。

当您打开不同的场景时，暂停状态保持不变；但在创建新场景时，将解除暂停。

如果有两个渲染同时发生；例如，“渲染视图”(Render View)和“材质查看器”(Material Viewer)，启动 IPR 渲染将使“材质查看器”(Material Viewer)挂起。一旦停止 IPR 渲染，“材质查看器”(Material Viewer)将重新处于活动状态。但是，必须手动触发重新渲染（例如，通过更改属性值或摄影机角度手动触发）。此行为与单击 ![图：如果有两个渲染同时发生；例如，“渲染视图”(Render View)和“材质查看器”(Material Viewer)，…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A856707B-0550-4DFA-AEB1-590B0FF7D219.png) <!-- baize:img-hook downloaded=false reason="正文 1121 字 ≥300，非承重" --> 略有不同，后者在解除暂停后始终会重新渲染。

若要在启动后暂停 Viewport 2.0，请将环境变量 MAYA_VP2_PAUSE_ON_STARTUP 设置为 1，或者将 optionVar vp2PauseState 设置为 1。

您也可以在“首选项”(Preferences)窗口的“显示”(Display)类别中启用“暂停 Viewport 2.0 (启动)”(Pause Viewport 2.0 (startup))选项。

## 相关主题

- [在 Hypershade 材质查看器中渲染网络](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-FAB13FA2-7068-4169-8D27-016B13E5C930)
