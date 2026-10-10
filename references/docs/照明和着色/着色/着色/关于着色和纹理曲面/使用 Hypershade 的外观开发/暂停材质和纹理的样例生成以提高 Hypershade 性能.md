# 暂停材质和纹理的样例生成以提高 Hypershade 性能

如果场景中有许多材质和纹理，则通过启用和禁用样例生成，可以避免等待样例进行渲染。

可以在以下区域中启用 (![图：可以在以下区域中启用 () 和禁用 () 样例生成：](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E877B724-DC07-4153-8B4B-E4B3661E9311.png) <!-- baize:img-hook downloaded=false reason="正文 888 字 ≥300，非承重" -->) 和禁用 (![图：可以在以下区域中启用 () 和禁用 () 样例生成：](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A194F9D7-F3E4-4E37-8FA8-21F1DA8E0329.png) <!-- baize:img-hook downloaded=false reason="正文 888 字 ≥300，非承重" -->) 样例生成：

- Hypershade 浏览器中的“材质”(Materials)和“纹理”(Textures)选项卡

- 属性编辑器(Attribute Editor)

- Hypershade 工作区的着色器图表中的节点

材质查看器不受此设置的影响。

切换的状态将与首选项一起保存，且在启动新场景时和重新启动 Maya 时保持不变。

仅渲染等于或低于最大分辨率的样例。可以在“首选项”(Preferences)窗口中设置样例的最大分辨率。（在“显示”(Display)类别中，设置“样例的最大分辨率”(Max res. for swatches)首选项。）

## 使用 Hypershade 图标暂停样例生成

若要启用和禁用所有节点的样例生成，请单击 Hypershade 工具栏中的 ![图：若要启用和禁用所有节点的样例生成，请单击 Hypershade 工具栏中的 和 按钮。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E877B724-DC07-4153-8B4B-E4B3661E9311.png) <!-- baize:img-hook downloaded=false reason="正文 888 字 ≥300，非承重" --> 和 ![图：若要启用和禁用所有节点的样例生成，请单击 Hypershade 工具栏中的 和 按钮。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A194F9D7-F3E4-4E37-8FA8-21F1DA8E0329.png) <!-- baize:img-hook downloaded=false reason="正文 888 字 ≥300，非承重" --> 按钮。

样例生成处于禁用状态时，通过单击鼠标右键并从标记菜单中选择“刷新样例”(Refresh Swatch)，可以对着色器图表中的特定节点启用样例渲染。

## 使用脚本暂停样例生成

通过将 renderThumbnailUpdate 命令设置为 true 或 false，也可以启用和禁用样例渲染。通过使用 -forceUpdate 标志指定节点名称，刷新特定节点的样例。

详细信息请参见 renderThumbnailUpdate 命令文档。

## 启动 Maya 时禁用样例渲染

启动 Maya 时可以禁用样例生成，以便在节点编辑器、Hypershade 和属性编辑器中均不渲染样例。

1. 选择窗口 > 设置/首选项 > 首选项(Window > Settings/Preferences > Preferences)以打开“首选项”(Preferences)窗口。

2. 在“显示”(Display)类别下，禁用“渲染样例(启动)”(Render swatches (startup))。

  如果禁用此设置，则在启动 Maya 时 Hypershade 中的切换样例生成设置将设为 ![图：如果禁用此设置，则在启动 Maya 时 Hypershade 中的切换样例生成设置将设为 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A194F9D7-F3E4-4E37-8FA8-21F1DA8E0329.png) <!-- baize:img-hook downloaded=false reason="正文 888 字 ≥300，非承重" -->。

  如果启用此设置，则 Hypershade 中的切换样例生成图标将设置为其上次保存的状态。

## 相关主题

- [Hypershade 中不显示材质和纹理样例的疑难解答](../与%20Maya%20材质和纹理有关的疑难解答/Hypershade%20中不显示材质和纹理样例的疑难解答.md)
