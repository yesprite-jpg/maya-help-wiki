# Ref

Ref 元素为 CTF 文件定义别名，以便在其他 CTF 文件中轻松地引用该文件。

某些应用程序允许用户在其首选项中设置特定别名，如 graphicsMonitor。

如果别名发生更改，使用该别名的引用直到重新启动应用程序后才会更新。

## 包含

- 无内容。

## 包含于

- [ReferenceTable](../ReferenceTable.md)

## 属性

#### alias

别名的唯一名称。必需。

#### path

相应 CTF 文件的路径和文件名。必需。

#### basePath

作为 path 属性值前缀以完整解析文件或位置的基本路径。可选。

如果使用此属性，path 属性将被解释为相对于基本路径的相对路径。否则，path 属性将被解释为绝对路径。

## 示例

```text
<?xml version="1.0" encoding="UTF-8"?>
<SynColorConfig version="1.0">
   <SharedHome dir="/opt/Autodesk/Synergy/SynColor/Shared/transforms"/>
   <ReferenceTable>
      <Ref alias="broadcastMonitor" path="/opt/Autodesk/Synergy/SynColor/2013.3/transforms/display/broadcast/CIE-XYZ_to_HD-video.ctf" />
      <Ref alias="defaultLook" path="/opt/Autodesk/Synergy/SynColor/2013.3/transforms/misc/identity.ctf" />
      <Ref alias="graphicsMonitor" path="/opt/Autodesk/Synergy/SynColor/2013.1/transforms/display/Eizo/CIE-XYZ_to_CG245W.ctf"/>
   </ReferenceTable>
</SynColorConfig>
```
