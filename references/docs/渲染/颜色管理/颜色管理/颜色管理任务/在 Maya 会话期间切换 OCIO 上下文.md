# 在 Maya 会话期间切换 OCIO 上下文

OCIO 配置文件允许使用上下文，这些上下文本质上是引用颜色变换文件的环境变量。例如，上下文可用于促进每个镜头的颜色分级。

如果使用 OCIO 上下文，您可以在会话期间更改其值，而不重新启动 Maya。要完成此操作，请使用 MEL 或 Python 命令来更改环境变量，然后刷新颜色管理首选项。

例如，假设您的配置文件使用 SHOT 上下文，它当前设置为 abc123.spi1d，但您想要将其更改为 ijk456.spi1d。在这种情况下，您可以在[脚本编辑器(Script Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7C861047-C7E0-4780-ACB5-752CD22AB02E)中运行以下 MEL 行：

```text
putenv "SHOT" "ijk456.spi1d";
colorManagementPrefs -refresh;
```
