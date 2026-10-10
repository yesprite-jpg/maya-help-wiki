# SynColorConfig

SynColorConfig 元素是 SynColor 配置文件的根元素。

## 包含

按任意顺序：

- [SharedHome](SharedHome.md)。必需，仅一个。

- [ReferenceTable](ReferenceTable.md)。必需，仅一个。

## 包含于

- 没有父对象

## 属性

#### version

SynColor 配置文件格式的版本。

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
