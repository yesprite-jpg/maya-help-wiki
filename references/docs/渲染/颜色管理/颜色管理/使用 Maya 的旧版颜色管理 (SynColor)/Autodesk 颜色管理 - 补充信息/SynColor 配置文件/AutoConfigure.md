# AutoConfigure

AutoConfigure 元素确定某些选项是否在启动支持 Autodesk 颜色管理的应用程序时自动配置。

当前这只适用于 Mac OS X 上的 Autodesk Smoke。

## 包含

- 无内容。

## 包含于

- [SynColorConfig](SynColorConfig.md)

## 属性

#### graphicsMonitor

将操作系统首选项中设置的 ICC 配置文件用作 graphicsMonitor 别名。

## 示例

```text
<?xml version="1.0" encoding="UTF-8"?>
<SynColorConfig version="1.0">
   <AutoConfigure graphicsMonitor="true" />
   <SharedHome dir="/Applications/Autodesk/Synergy/SynColor/Shared/transforms" />
   <ReferenceTable>
      <Ref alias="broadcastMonitor" path="/Applications/Autodesk/Synergy/SynColor/2013.3/transforms/display/broadcast/CIE-XYZ_to_HD-video.ctf" />
      <Ref alias="defaultLook" path="/Applications/Autodesk/Synergy/SynColor/2013.3/transforms/misc/identity.ctf" />
      <Ref alias="graphicsMonitor" path="/Library/ColorSync/Profiles/Displays/Color LCD-00000610-0000-9CCF-0000-0000042733C0.icc" />
   </ReferenceTable>
</SynColorConfig>
```
