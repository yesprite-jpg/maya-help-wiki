# 显示 UV 的子集

默认情况下，选择曲面网格时，Maya 会在“UV 编辑器”(UV Editor)中显示该网格的所有 UV。

可以在显示当前集的所有 UV 和仅显示隔离的选定子集之间切换 UV 编辑器。这样一来，可以更轻松地处理部分模型，而不影响或意外选择其他 UV。

隔离特定的 UV 子集

1. 选择要隔离的 UV。

2. 单击工具栏上的“隔离”(Isolate)按钮，或选择“视图 > 隔离选择 > 查看选定对象”(View > Isolate Select > View Selected)，或按 **Ctrl** + **1**。

  仅显示集中的 UV。HUD 将在“UV 编辑器”(UV Editor)的底部指示您处于“隔离选择”(Isolated Selection)模式。

  **注**

  若要切换回显示所有 UV，请再次单击

  “切换隔离”(Toggle isolation)

  ，或禁用

  “视图 > 隔离选择 > 查看选定对象”(View > Isolate Select > View Selected)

  菜单项，或按

  Ctrl

  +

  i

  。

添加到已隔离的 UV 子集

1. 在“UV 编辑器”(UV Editor)中，单击工具栏上的“隔离”(Isolate)按钮，以切换回显示所有 UV。

  或者，选择“视图 > 隔离选择 > 查看选定对象”(View > Isolate Select > View Selected)。

2. 选择要添加到已隔离子集的 UV。

3. 选择“视图 > 隔离选择 > 添加选定对象”(View > Isolate Select > Add Selected)。

从已隔离的子集中移除 UV

1. 在 UV 编辑器中，选择要从已隔离的子集中移除的 UV。

2. 选择“视图 > 隔离选择 > 移除选定对象”(View > Isolate Select > Remove Selected)。

仅显示已指定当前图像的 UV

1. 显示纹理（在 UV 编辑器中，选择“图像 > 显示图像”(Image > Display Image)）。如果多个纹理与网格相关联，请使用“纹理”(Textures)菜单选择要处理的纹理。

  处于组件选择模式下时，“纹理”(Textures)菜单将列出指定给选定组件的着色组。处于对象选择模式下时，该菜单将列出指定给整个网格的所有着色组。

2. 若要仅显示已指定当前图像的面，请在“UV 编辑器”(UV Editor)中启用“视图 > 过滤器选择 > 查看选定图像的面”(View > Filter Selection > View Faces of Selected Images)。

3. 若要再次显示所有面，请禁用“选择 > 过滤器选择 > 查看选定图像的面”(Select > Filter Selection > View Faces of Selected Images)。

仅显示选定 UV 或边内部的面

1. 选择 UV 或边以定义边界。

2. 在“UV 编辑器”(UV Editor)中，启用“选择 > 过滤器选择 > 查看包含的面”(Select > Filter Selection > View Contained Faces)。

3. 若要再次显示所有面，请禁用“选择 > 过滤器选择 > 查看包含的面”(Select > Filter Selection > View Contained Faces)。

仅显示共享选定 UV 或边的面

1. 选择 UV 或边。

2. 在“UV 编辑器”(UV Editor)中，启用“选择 > 过滤器选择 > 查看连接面”(Select > Filter Selection > View Connected Faces)。

3. 若要再次显示所有面，请禁用“选择 > 过滤器选择 > 查看连接面”(Select > Filter Selection > View Connected Faces)。
