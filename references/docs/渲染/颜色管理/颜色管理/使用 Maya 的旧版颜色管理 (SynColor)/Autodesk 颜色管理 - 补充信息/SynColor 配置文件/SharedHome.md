# SharedHome

SharedHome 元素指定共享目录的位置。这是存储您自己的自定义变换的有用位置，这些自定义变换可以由使用安装在相同计算机上的 Autodesk 颜色管理的其他应用程序使用。

某些应用程序允许您在其首选项中设置此值。

## 包含

- 无内容。

## 包含于

- [SynColorConfig](SynColorConfig.md)

## 属性

#### dir

共享目录的完整路径。可以位于本地或远程计算机。

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
