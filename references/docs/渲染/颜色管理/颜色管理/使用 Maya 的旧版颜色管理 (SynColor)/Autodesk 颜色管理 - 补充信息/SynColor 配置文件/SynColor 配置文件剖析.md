# SynColor 配置文件剖析

本部分介绍 SynColor 配置文件的一个示例。

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
