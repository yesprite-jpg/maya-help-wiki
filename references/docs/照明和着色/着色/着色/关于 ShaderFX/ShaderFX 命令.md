# ShaderFX 命令

ShaderFX 命令使您可以查询有关“ShaderFX”图形的信息（例如图表中节点数、节点中特性的列表），以及执行各种操作（例如添加或删除节点，创建或断开连接，以及指定正使用的 ShaderFX 着色器的 DAG 路径）。

有关 ShaderFX 命令的详细信息以及对其标志的描述，请在 MEL 命令行中输入 shaderfx – help。

shaderfx 命令可用于 ShaderFX 着色器图表和 Stingray PBS 图表。使用 -sfxnode 标志指定“Shaderfx 着色器”(Shaderfx Shader)或 Stingray PBS 节点。但是，只有适用于 Stingray PBS 图表的标志才能用于后者。例如，可以使用 -getNodeCount 标志，但是不能使用 -addGroup 标志。

例如：

```text
shaderfx -sfxnode "StingrayPBS1" -getNodeCount
```
