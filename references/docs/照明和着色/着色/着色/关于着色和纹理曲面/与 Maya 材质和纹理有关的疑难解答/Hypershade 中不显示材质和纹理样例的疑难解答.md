# Hypershade 中不显示材质和纹理样例的疑难解答

## 无法在 Hypershade 中渲染样例

- 用于在启动时渲染样例的选项可能已禁用。

  在“首选项”(Preferences)窗口（“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)）中的[显示(Display)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BF017019-B89A-47F0-8AB5-106C058AB854)部分，确保“渲染样例(启动)”(Render swatches (startup))已启用。

- 可能在 Hypershade 中暂停了样例渲染。

  如果暂停材质和纹理样例生成按钮设置为 ![图：如果暂停材质和纹理样例生成按钮设置为 ，则将该按钮切换为 以启用样例渲染。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A194F9D7-F3E4-4E37-8FA8-21F1DA8E0329.png) <!-- baize:img-hook downloaded=false reason="正文 558 字 ≥300，非承重" -->，则将该按钮切换为 ![图：如果暂停材质和纹理样例生成按钮设置为 ，则将该按钮切换为 以启用样例渲染。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E877B724-DC07-4153-8B4B-E4B3661E9311.png) <!-- baize:img-hook downloaded=false reason="正文 558 字 ≥300，非承重" --> 以启用样例渲染。

- 文件纹理的分辨率高于渲染样例的最大分辨率设置。

  增加样例的最大分辨率设置。在“首选项”(Preferences)窗口中的[显示(Display)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BF017019-B89A-47F0-8AB5-106C058AB854)部分，从“样例的 最大分辨率”(Max res. for swatches)下拉列表中选择更高的分辨率。

  也可以通过右键单击样例，然后从标记菜单中选择“刷新样例”(Refresh Swatch)渲染单个样例。

## 样例无法显示在 Hypershade 浏览器中

可能在[浏览器工具栏](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-5B48E281-2DCB-4C65-9DCA-52CBA26A7BBA.htm)中启用了过滤器。单击“显示”(Show)按钮，然后选择“对象”(Objects)以检查过滤器设置。单击“清除以下项”(Clear Below)以清除所有过滤器。此外，验证您尚未在过滤器文本框中输入任何文字。有关详细信息，请参见 [Hypershade 浏览器工具栏](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-5B48E281-2DCB-4C65-9DCA-52CBA26A7BBA.htm)。
