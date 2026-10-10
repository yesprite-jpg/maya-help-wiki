# 自动从最后缓存帧重新启动缓存（仅限 Bifröst 液体）

您可以自动从使用相同设置缓存的最后一帧重新开始缓存 Bifröst 液体模拟。如果在此期间尚未更改任何模拟设置，则可以使用该过程附加到现有缓存。您还可以使用该过程重新启动因任何原因而失败的缓存，而无需手动确定成功缓存的最后一帧。

1. 为要缓存的模拟选择容器。

2. 选择“Bifrost 流体 > 计算并缓存到磁盘”(Bifrost Fluids > Compute and Cache to Disk) > ![图：选择“Bifrost 流体 计算并缓存到磁盘”(Bifrost Fluids Compute and Cache to …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Bifrost/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 321 字 ≥300，非承重" -->。

3. 将“写入模式”(Write Mode)设置为“从最后一个匹配帧写入”(Write from last matching frame)。

4. 确保其他设置符合需要。

5. 单击“创建”(Create)。

  Bifröst 会查找与当前模拟设置匹配的最后一个现有缓存帧，然后计算并保存从该帧开始的用户缓存。
