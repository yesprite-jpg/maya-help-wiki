# “ViewCube”首选项

**注**

ViewCube 仅适用于旧版视口。若要切换到旧版视口，您可以从

渲染器(Renderer)

面板菜单选择

“旧版默认视口”(Legacy Default Viewport)

或

“旧版高质量视口”(Legacy High Quality Viewport)

选项。

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“ViewCube”类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

#### 显示 ViewCube (Show the ViewCube)

控制在视图中显示还是隐藏 ViewCube。如果该设置已启用，则“ViewCube”会显示为视图右上角的一个平视显示仪。

### 显示(Display)

#### 屏幕上的位置(On-screen position)

控制“ViewCube”在场景视图内的放置。

通过从下拉菜单中选择某个预设（“右上”、“右下”、“左上”或“左下”），可以将“ViewCube”设定为显示在视图的任一角。根据“ViewCube”所占据的角，会自动重新定位其他控件（主视图按钮、弯箭头）。默认设置为“右上”。

#### ViewCube 大小(ViewCube Size)

控制“ViewCube”的大小。

设置选项有“小”、“正常”和“大”。显示多个视图时，“小”设置很有用。默认设置为“正常”。调整场景视图的大小时，“ViewCube”不会更改大小。

#### 非活动不透明度(Inactive Opacity)

控制鼠标光标不在“ViewCube”的附近时“ViewCube”和其他控件的不透明度级别。

设置选项有“0%”、“25%”、“50%”、“75%”和“100%”。如果设定为“0%”，则将鼠标光标移离“ViewCube”时，它将消失。如果设定为“100%”，则不管鼠标光标在什么位置，都会显示“ViewCube”。默认设置为“50%”。

### 在 ViewCube 上拖动时(When Dragging on the ViewCube)

下列设置控制在“ViewCube”上单击然后拖动以更改场景视图时“ViewCube”的行为。

#### 捕捉到最近视图(Snap to closest view)

控制在每当单击“ViewCube”并将其拖动到某个固定视图附近的某个位置时，ViewCube 是否自动捕捉到任何预定义的观察角度。默认设置为启用。

#### 在过渡过程中保持场景向上(Preserve scene up during transitions)

控制每当场景视图更改时该视图是否自动保持正立位置。

默认设置为启用。如果禁用该选项，视图更改将不会保持默认正立位置。

### 在 ViewCube 上单击时(When Clicking on the ViewCube)

下列设置控制在“ViewCube”上单击以更改场景视图时“ViewCube”的行为。

#### 在视图更改时适配到视图(Fit-to-view on view change)

控制每当场景视图更改时该视图是否自动重新框显场景视图以适配新视图内的 3D 场景的内容。

默认设置为启用。如果禁用该选项，则视图会更改，并会发生动画过渡，而不会自动重新框显视图。

#### 切换视图时使用动画过渡(Use animated transitions when switching views)

控制每当视图更改时是否发生动画过渡。

动画过渡设置会在视图更改过程中设置摄影机位置的动画，以从视觉上帮助确定现有视图和新视图之间的关系。默认设置为启用。如果 3D 场景的内容很大，那么为了提高使用“ViewCube”时视图更改的速度，可能会希望禁用该设置。

### 指南针

#### 在 ViewCube 下显示指南针

启用该选项时，会在 ViewCube 下显示指南针以确定地理背景中视图的方向。

#### 北方角度（度）

用于指定指南针的方向。例如，要将指南针顺时针旋转四分之一，则可将“北方角度”设置为 **90.0**。
