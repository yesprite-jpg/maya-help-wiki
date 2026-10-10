# ReferenceTable

ReferenceTable 元素是定义 CTF 文件别名或简称的 Ref 元素的容器。

## 包含

- [Ref](ReferenceTable/Ref.md)。可选，任意数量。

  但是，如果没有用来定义以下别名的 Ref 元素，那么一些 Autodesk 提供的变换将不可用：

  - graphicsMonitor 别名应设置为适合在工作站显示器上显示的变换。

  - broadcastMonitor 别名应设置为适合在广播显示器上显示的变换。

  - defaultLook 别名应设置为用来重新创建在现场使用的外观的变换。

  用户可以根据自己的需要为其他变换文件定义其他别名。

## 包含于

- [SynColorConfig](SynColorConfig.md)

## 属性

无。

## 示例

```text
<?xml version="1.0" encoding="UTF-8"?>
<SynColorConfig version="1.0">
   <SharedHome dir="/opt/Autodesk/Synergy/SynColor/Shared/transforms"/>
  <ReferenceTable>
      <Ref alias="broadcastMonitor" path="/opt/Autodesk/Synergy/SynColor/2013.3/transforms/display/broadcast/CIE-XYZ_to_HD-video.ctf" />
      <Ref alias="defaultLook" path="/opt/Autodesk/Synergy/SynColor/2013.3/transforms/misc/identity.ctf" />
      <Ref alias="graphicsMonitor" path="/opt/Autodesk/Synergy/SynColor/2013.3/transforms/display/Eizo/CIE-XYZ_to_CG245W.ctf" />
   </ReferenceTable>
</SynColorConfig>
```
