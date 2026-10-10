# 了解 Maya 退出代码

Maya 退出代码通常包含在发生崩溃时显示的消息中：

```text
maya encountered a fatal error

Signal: 11 (Unknown Signal)

Result: /users/<username>/maya/projects/Test/scenes/Test1.ma

Fatal Error. Attempting to save in /usr/tmp/<username>.20120223.1655.ma

// Maya exited with status 139
```

我们可以使用以下信息解释退出代码：

- 介于 1 和 127 之间的退出代码通常由作业自身生成。

- 介于 129 和 255 之间的退出代码表示作业由 UNIX 信号终止。

  每个信号都有一个编号，该编号与 128 相加可创建一个在退出代码中使用的编号。例如，信号 11 用于退出代码 139。

  信号可能会在进程本身中产生，也可以被某外部代理发送到此进程。

**注**

提示：

在许多情况下，您可以使用崩溃错误报告 (CER) 弹出窗口向我们发送有关如何重现崩溃的详细信息。有关详细信息，请参见

http://www.autodesk.com/cer-chs

。

在 Linux 平台上运行 Maya Standalone 时，如果 Maya 在您尝试使用 kill -2 或 kill -2 python-bin 结束 Python 进程时以状态 0 退出，则可设置环境变量 MAYA_DEBUG_NO_SIGINT_HANDLING = 1，使 Maya 以非零状态退出。
