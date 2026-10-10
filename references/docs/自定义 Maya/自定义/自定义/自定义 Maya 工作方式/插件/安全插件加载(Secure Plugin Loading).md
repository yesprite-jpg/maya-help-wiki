# 安全插件加载(Secure Plugin Loading)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 783 字 ≥300，非承重" -->

在加载源自不受信任源（如 Internet 网站或论坛）的插件之前，我们建议在[首选项(Preferences)](../../../../首选项/首选项/“首选项”%28Preferences%29窗口.md)中启用“安全插件加载”(Secure Plugin Loading)。此功能处于活动状态时，在您不知情的情况下，Maya 将阻止加载位于不受信任的位置（即，Maya 的默认受信任位置以外的位置以及用户指定的位置）的插件：询问您是否允许继续加载，或者完全拒绝加载插件。

**注**

默认情况下，

“安全文件加载”(Secure File Loading)

处于启用状态。

启用/禁用“安全插件加载”(Secure Plugin Loading)

1. 转到[“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)](../../../../首选项/首选项/“首选项”%28Preferences%29窗口/“安全”%28Security%29首选项.md)。

2. 单击“安全 > 插件”(Security > Plugins)部分。

3. 启用/禁用“安全插件加载”(Secure Plugin Loading)。

4. （可选）设置所需的“不受信任位置的默认操作”(Default action for untrusted locations)，以确定在尝试从不受信任的位置加载插件时 Maya 如何反应。

添加/移除受信任的位置

1. 转到[“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)](../../../../首选项/首选项/“首选项”%28Preferences%29窗口/“安全”%28Security%29首选项.md)。

2. 单击“安全 > 插件”(Security > Plugins)部分。

  - 单击“我的受信任插件位置”(My trusted plugin locations)旁边的“添加”(Add)按钮，然后输入文件路径以进行添加。

  - 在“我的受信任插件位置”(My trusted plugin locations)列表中单击受信任的位置，然后单击“移除”(Remove)按钮以将其移除。

  **注**

  Maya 还有一个默认的受信任插件位置列表，这些位置不显示在此列表中。

## 相关主题

- [安全首选项](../../../../首选项/首选项/“首选项”%28Preferences%29窗口/“安全”%28Security%29首选项.md)

- [安全文件加载(Secure File Loading)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D554C4DA-7706-4B93-AD0F-FB9769C022F9)
