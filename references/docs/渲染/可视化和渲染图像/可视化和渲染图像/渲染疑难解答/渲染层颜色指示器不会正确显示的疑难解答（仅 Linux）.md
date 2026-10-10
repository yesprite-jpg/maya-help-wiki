# 渲染层颜色指示器不会正确显示的疑难解答（仅 Linux）

若具有已修改的 MayaScheme 文件，则可能在层编辑器中不会看到选定层的正确层指示器颜色（浅蓝色和深蓝色）。同样，您可能无法看见正确的颜色指示器以覆盖层属性（橙色和粗体）。

#### 解决方法

将下列行添加到自定义 MayaScheme 文件：

layerAdjustmentTextForeground: #e56929 *blueSelectBackgroundColor1: #3884c4 *blueSelectBackgroundColor2: #81a7c1
