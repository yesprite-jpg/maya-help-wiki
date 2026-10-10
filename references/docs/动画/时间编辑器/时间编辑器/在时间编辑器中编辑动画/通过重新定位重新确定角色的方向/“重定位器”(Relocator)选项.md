# “重定位器”(Relocator)选项

“重定位器”(Relocator)选项可用于创建或修改自定义重定位器。

打开“重定位器”(Relocator)选项

- 从[“时间编辑器”(Time Editor)菜单栏](../../时间编辑器界面概述/时间编辑器菜单栏.md)或[“时间编辑器”(Time Editor)的“片段”(Clip)上下文菜单](../../使用时间编辑器片段/时间编辑器“片段”%28Clip%29上下文菜单.md)中，选择“重新定位 > 创建”(Relocate > Create)或“编辑”(Edit)。

请参见[通过重新定位重新确定角色的方向](../通过重新定位重新确定角色的方向.md)。

#### 将默认根用于重定位器(Use default root for relocator)

激活此选项可将片段根用于重定位器。

如果动画片段包含多个根，并且您需要重定位器来控制每个根，请禁用此选项，改为启用“从片段根中选择自定义重定位器根”(Choose custom relocator roots from Clip Roots)。

例如，如果片段包含的装备控制器没有层次，但使用一个控制器作为该角色的主控制器（例如，与约束一起使用），则重新定位所有控制器时会导致应用平移两次。这是因为，如果没有层次，每个控制器均被视为根并重新定位。

#### 从片段根中选择自定义重定位器根(Choose custom relocator roots from Clip Roots)

启用此选项可激活“片段根”(Clip Roots)列表，其中将显示场景中的所有根对象。

#### 为自定义定位器选定的根(Selected roots for custom locator)

显示要将多少片段根设置为重定位器。
