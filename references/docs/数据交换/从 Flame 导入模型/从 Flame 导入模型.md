# 从 Flame 导入模型

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 929 字 ≥300，非承重" -->

确保 Flame 中的模型是 Action 节点中的几何体对象。

在 Flame 中

1. 在 Action 节点中，选择要发送的几何体对象。

2. 从 Action 上下文菜单中，选择“发送到 Maya > 发送选定对象作为新场景”(Send to Maya > Send Selected as New Scene)。

  “发送到”(Send To)命令将在 Flame 和 Maya 之间建立连接。建立连接之后，应用程序之间将共享数据。若要断开连接，只需关闭场景或退出其中一个应用程序即可。

  **注**

  重要：

  必须安装了另一个应用程序的同等主版本，才能查看“发送到”(Send To)命令选项。例如，如果您运行的是 Flame 2020.3 和 Maya 2020（“发送到 Maya”(Send To Maya)在 Flame 2020.3 中已可用），则**“发送到 Maya”(Send to Maya)**选项可用。

将几何体从 Flame 发送到 Maya 时，请考虑以下事项：

- 在与几何体一起发送材质和纹理贴图时，Maya 不支持 Substance 纹理：不同贴图最终烘焙在单个 Maya 材质中。

- Maya 不支持 PBR 渲染：视口渲染在 Flame 和 Maya 中看起来不同。

- 如果计划在 Maya 中绘制几何体，请确保已将材质节点附加到 Flame 中的几何体。

- Maya 非常适合处理四边形网格。

## 从不同版本的 Flame 导入模型

建议使用**“发送到 Maya”(Send to Maya)**功能在 Flame 和 Maya 之间共享数据。但是，如果尝试在不同主版本的软件（例如 Flame 2020.3 和 Maya 2019）之间共享数据，则“发送到 Maya”(Send to Maya)功能不可用。请改为尝试：

- **FBX**：可以使用 Autodesk FBX® 文件格式将 Flame 中的数据导出到 Maya 中。有关详细信息，请参见[将 FBX 文件导入到 Maya](../Maya%20FBX%20插件/Maya%20FBX%20插件/FBX%20导入/将%20FBX%20文件导入到%20Maya.md)。

- 在 Action 示意图中，从上下文菜单中选择“导出...”(Export...)。

在 Maya 中，根据您的要求，选择“文件 > 打开”(File > Open)或“文件 > 导入”(File > Import)，然后选择从 Flame 导出的模型。可以设置导入选项，有关信息，请参见[导入选项(Import options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-37B31221-7BBC-40DA-AB33-47C333EF4E14)主题。

## 相关主题

- [将对象发送到 Flame](../将对象发送到%20Flame/将对象发送到%20Flame.md)

- [发送到 Flame 选项(Send to Flame options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4475498E-3321-417A-9A77-B7A9FDB0B154)
