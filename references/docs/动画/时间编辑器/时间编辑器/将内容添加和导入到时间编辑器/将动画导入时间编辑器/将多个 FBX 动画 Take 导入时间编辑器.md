# 将多个 FBX 动画 Take 导入时间编辑器

Take 是保存在一个文件中的动画实例。Autodesk MotionBuilder 用于将多个动画“Take”保存到单个 FBX 文件。时间编辑器支持通过 FBX 导入的 Take，并允许选择在导入后如何组织它们。

[大纲视图](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4B9A9A3A-83C5-445A-95D5-64104BC47406)将显示已导入场景中的 Take。

将包含多个 Take 的 FBX 文件导入时间编辑器

1. 将 FBX 文件拖动到时间视图中的轨迹上。此时将显示“导入”(Import)窗口。

2. 在“Take 选项”(Take Options)区域中，选择希望 Take 在时间编辑器中如何显示：

  #### 到一个组中(Into a Group)

  所有 Take 成为组片段内包含的单独片段。请参见[将多个片段合并为组片段](../../使用时间编辑器片段/将多个片段合并为组片段.md)。

  ![图：在“Take 选项”(Take Options)区域中，选择希望 Take 在时间编辑器中如何显示： 到一个组中(Int…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F383064B-C18F-4B26-8519-1E6933D8FCED.png) <!-- baize:img-hook downloaded=false reason="正文 448 字 ≥300，非承重" -->

  #### 到多个合成中(Into Multiple Compositions)

  每个 Take 将变为一个片段并插入新合成中。请参见[通过时间编辑器合成创建多个动画故事](../../通过时间编辑器合成创建多个动画故事.md)。

  ![图：在“Take 选项”(Take Options)区域中，选择希望 Take 在时间编辑器中如何显示： 到一个组中(Int…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-9118768F-6DF4-49D9-ACCB-3C6865C7DA15.png) <!-- baize:img-hook downloaded=false reason="正文 448 字 ≥300，非承重" -->

  #### 作为片段序列(As a sequence of clips)

  每个 Take 将变为一个片段并沿动画轨迹并排放置。

  ![图：在“Take 选项”(Take Options)区域中，选择希望 Take 在时间编辑器中如何显示： 到一个组中(Int…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-ACDF9100-78B0-419A-AC7B-053056D9A4C8.png) <!-- baize:img-hook downloaded=false reason="正文 448 字 ≥300，非承重" -->

**注**

仅时间编辑器中的拖动操作支持导入多个 Take。不能使用 Maya 导入功能调入多个 Take。
