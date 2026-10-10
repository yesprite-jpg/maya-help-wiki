# 工具动画演示 XML 文件的组成部分

ToolClips.xml 文件存储在以下位置：

- Windows：C:\Program Files\Autodesk\Maya<版本>\resources\builtin.toolclips

- Mac OS X：/Applications/Autodesk/maya<版本>/Maya.app/Contents/Resources/builtin.toolclips

- Linux：/usr/autodesk/maya<版本>-x64/resources/builtin.toolclips

工具动画演示可以包含两个级别的数据。本主题将此文件分为以下部分：

- [主元素](工具动画演示%20XML%20文件的组成部分.md#GUID-4E471D1E-3562-4EE2-8B7E-1BD81D9C8F00__SECTION_1A99086B1BBF4DE1A0CDDFF2AE1F28C1)

- [级别 1 工具动画演示部分](工具动画演示%20XML%20文件的组成部分.md#GUID-4E471D1E-3562-4EE2-8B7E-1BD81D9C8F00__SECTION_C22DF182E23243E88C43EC92539FC291)

- [级别 2 工具动画演示部分](工具动画演示%20XML%20文件的组成部分.md#GUID-4E471D1E-3562-4EE2-8B7E-1BD81D9C8F00__SECTION_DF11AD90EE6C4ADE8A8904C332C4C67E)

## 主元素

XML 文件的主体由一个 <toolclips> 元素定义。

下表介绍了 <toolclips> 元素的属性。

| 属性 | 说明 |
|---|---|
| <ui> | 指定 QML 描述的位置。该文件描述默认工具动画演示窗口的布局。默认情况下，ToolClipUI.qml 文件位于 builtin.toolclips\ui 目录中。 |
| <simple> | 指定简化 QML UI 描述的位置。此文件描述当在[“帮助”首选项](../../../首选项/首选项/“首选项”%28Preferences%29窗口/“帮助”%28Help%29首选项.md#GUID-2B90FD26-20F6-4CF6-8A68-2DD4AD6CF334__WS73099CC142F487553B93539F117EA10CE8F2FB4)中启用“仅显示工具名称和快捷方式”(Display tool name and shortcut only)时，工具动画演示的显示方式。默认情况下，SimpleTooltip.qml 文件位于 builtin.toolclips\ui 目录中。 |
| <locale> | 指定 ToolClips.xml 文件中包含的工具动画演示语言区域设置。默认属性值为 en_US（英语）。 提示： 如果要将工具动画演示本地化为日语或简体中文，可以使用 ja_JP 或 zh_CN 作为属性值。 |

示例代码：

```text
xml version="1.0" encoding="utf-8"
<toolclips ui="ui/ToolClipUI.qml" simple="ui/SimpleTooltip.qml" locale="en_US”>
... </toolclips>
```

## 级别 1 工具动画演示

所有工具动画演示都包含一个级别 1 窗口。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-4FBC1F59-12B0-4A5B-A04C-839519B52AE0.png) <!-- baize:img-hook downloaded=false reason="正文 2379 字 ≥300，非承重" -->

下表介绍了定义级别 1 工具动画演示各部分的属性。

| 属性 | 说明 |
|---|---|
| <toolclip> | 包含所有级别 1 和级别 2 工具动画演示元素。 |
| <key> | 用于请求工具动画演示的关键帧名称。请参见[创建工具动画演示](创建工具动画演示.md#GUID-690C8663-30A7-49DA-B0DB-14BCAB1E6A9F__GUID-EB0325B0-A494-4A5B-A247-0AE1BB6F66DB)。 注： 如果某一关键帧名称存在于工具动画演示搜索路径内的两个 ToolClip.xml 文件中，Maya 将使用第一次遇到的关键帧名称。 |
| <help> | （可选）指定当级别 2 工具动画演示不存在时，工具动画演示窗口中所含帮助链接的位置。该位置可以是一个 URL 或内部帮助字符串（如以下示例代码所示）。如果未指定位置，帮助链接将默认为“帮助”主页。 |
| <title> | 显示在工具动画演示窗口中的工具标题。 |
| <shortcut> | （可选）默认的键盘快捷键。键盘快捷键在 Maya 中是自动分配的，但您可以使用此属性覆盖工具动画演示窗口中的显示内容。 |
| <text> | 显示在工具动画演示窗口中的摘要文本。 |

示例代码：

```text
<toolclip key="moveTool" help="files/MoveTool.htm" title="Move Tool" shortcut="W">
     <text>Move selected objects or components by dragging the transform manipulator.</text>
...</toolclip>
```

## 级别 2 工具动画演示

级别 2 工具动画演示是可选的，在存在其他学习内容时使用。如果存在级别 2 工具动画演示，级别 1 工具动画演示中会显示“更多(More)”按钮。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-6741B2A6-F219-4701-AC40-72739D7CDCE9.png) <!-- baize:img-hook downloaded=false reason="正文 2379 字 ≥300，非承重" -->

下表介绍了定义级别 2 工具动画演示各部分的属性。

| 属性 | 说明 |
|---|---|
| <expanded> | 包含所有级别 2 工具动画演示数据。如果工具动画演示包含展开区域，级别 1 工具动画演示窗口中会显示“更多”(More)按钮。 |
| <default-resource> | （可选）指定当打开级别 2 工具动画演示时，可以将工具动画演示资源列表中的特定视频或图像资源载入查看器/播放器中。<index> 属性决定将载入查看器或播放器中的资源列表项。例如，值设置为 2 时，将显示列表中的第二项。默认情况下，<index> 属性设置为 1。 |
| <resourcelist> | 指定要显示在级别 2 工具动画演示窗口中的资源列表。可以包含视频、图像和/或外部资源的链接。 |
| <video> | 将视频添加到资源列表中。使用 <location> 属性指示显示在工具动画演示窗口中的文件名称和标题。当创建自定义工具动画演示时，所有视频必须采用 WebM 格式，并且位于 users.toolclips\Resources 或 <自定义目录>\Resources 子目录中。 |
| <image> | 将图像添加到资源列表中。使用 <location> 属性指示显示在工具动画演示窗口中的文件名称和标题。当创建自定义工具动画演示时，所有图像必须采用 JPEG 或 PNG 格式，并且位于 users.toolclips\Resources 或 <自定义目录>\Resources 子目录中。 |
| <link> | 将外部链接添加到资源列表中。使用 location 属性指示链接位置和显示在工具动画演示窗口中的标题。该位置可以是完全限定的 URL 或内部帮助字符串（如以下示例代码所示）。 |

示例代码：

```text
    <expanded>
       <default-resource index=”1”/>
        <resourcelist>
            <video location="MoveTool.webm">Move Objects</video>
            <image location=”MoveTool.jpg”>Show Objects</image>
            <link location="files/MoveTool.htm">Using the Move Tool</link>
        </resourcelist>
    </expanded>
```

## 相关主题

- [自定义工具动画演示](../自定义工具动画演示.md)
