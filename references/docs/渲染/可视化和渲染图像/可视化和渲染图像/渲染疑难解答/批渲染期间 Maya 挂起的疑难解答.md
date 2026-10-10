# 批渲染期间 Maya 挂起的疑难解答

在某些情况下（例如，批渲染），解析网络名称期间 Maya 可能会挂起。如果发生这种情况，请验证网络设置，并确保操作系统能够将 localhost 解析为当前计算机。

如果您使用的是 Mac OS X 平台，请参考适用于您所用操作系统的文档，了解有关如何解决 Mac OS X 无法解析 localhost 这一情况的信息。

通常，您可以尝试编辑系统文件 /etc/hosts 并更新行条目：

```text
127.0.0.1 localhost enterHostNameHere
```

其中，enterHostNameHere 是主机计算机的名称，即 Mac OS X 命令的输出：hostname。
