# Autodesk 颜色变换集合

Autodesk 颜色管理集合中的变换是基于 Academy/ASC XML 颜色变换格式的 CTF 文件。其中包括多个用于不同目的的类别。

目录位置取决于 Autodesk 产品和操作系统。对于创意后期制作产品：

- Linux：

  ```text
/opt/Autodesk/Synergy/SynColor/<version>/transforms
```

- Mac OS X：

  ```text
/Applications/Autodesk/Synergy/SynColor/<version>/transforms
```

对于 Maya 和 Maya LT：

```text
<install_directory>/synColor/transforms
```

| 类别 | 描述 |
|---|---|
| RRT+ODT | 参考渲染变换 (RRT)（后跟用于 ACES 颜色空间输出的输出设备变换 (ODT)）以及相应的反向变换的各种组合。 |
| bit-depth | 在各种整数和浮点值格式之间转化。 |
| camera | 从各种数字摄影机本地格式转化为 ACES 等其他颜色空间。 |
| display | 将连接空间中的颜色转化为适合各种显示设备的输出空间的颜色（或进行反向转化）。 |
| film | 将扫描胶片颜色空间转化为 ACES（或进行反向转化），或应用各种 1D 对数/线性转化。 |
| gamma | 应用或移除各种常用 Gamma 曲线，包括用于 sRGB 和 Rec. 709 的709. |
| interchange | 将连接空间中的颜色转化为常用于文件输入和输出的空间的颜色（或进行反向转化），例如 AdobeRGB 和 sRGB。 |
| levels | 用于钳制或调整颜色值的各种函数。 |
| misc | 可用于调试或其他用途的各种变换。 |
| primaries | 在使用不同主颜色的线性颜色空间之间进行转化。 |
| tagging | 从主色和编码的各种组合转化为 ACES。 |
| tone-map | 从场景线性转化为视频颜色空间，或者进行反向转化。 |
| view | 用于转化图像以便查看的各种光学传递函数和其他变换。某些变换需要进行额外变换，才能准备要在特定设备上显示的图像。 |
| whitepoint | 转化线性颜色空间的白点。 |
