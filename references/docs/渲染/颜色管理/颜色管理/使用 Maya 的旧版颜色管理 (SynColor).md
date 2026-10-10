# 使用 Maya 的旧版颜色管理 (SynColor)

若要使用不支持 OCIO v2 的渲染器，必须使用称为 SynColor 的旧版颜色管理系统。

若要使用 SynColor 模式，请在启动 Maya 之前将环境变量 MAYA_COLOR_MANAGEMENT_SYNCOLOR 设置为任意值。请注意：

- 若要在每次启动 Maya 时都使用 SynColor 模式，可以在操作系统的用户或系统变量中设置此模式。

- 若要对特定会话使用 SynColor，可以打开命令 Shell 并直接在命令行中进行设置，然后再从同一 Shell 中启动。

- 如果在 Maya.env 文件中设置环境变量或者通过在 Maya “脚本编辑器”(Script Editor)中使用 putenv 来设置环境变量，则该环境变量将不起作用。

若要还原为使用 OCIO v2 进行颜色管理，请确保该环境变量不再存在，然后再次启动 Maya。
