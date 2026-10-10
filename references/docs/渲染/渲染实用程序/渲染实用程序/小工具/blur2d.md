# blur2d

blur2d 工具根据保存的向量信息对输入图像应用 2D 运动模糊。在 Autodesk® Maya®中，运动向量在渲染时与图像一起保存，方法是启用“渲染设置”(Render Settings)窗口“运动模糊”(Motion Blur)区域中的“保持运动向量”(Keep Motion Vectors)。

使用 blur2d

1. 在 Linux® shell、终端窗口或命令提示中键入：

  ```text
blur2d [-h] [-l blurLength] [-s blurSharpness] [-m smoothValue] [-n start end step] [-f inputFileName]
[-r smoothColor]
```

  | 选项 | 描述 |
  |---|---|
  | -h | 显示帮助文件。 |
  | -l <float> | 模糊长度。该值必须大于 0。默认值为 1。 |
  | -s <float> | 模糊锐度。该值必须大于 0。默认值为 1。 |
  | -m <int> | 平滑值。该值必须大于或等于 0。默认值为 2。 |
  | -r <boolean> | 平滑颜色 (1) 或不平滑颜色 (0)。默认设置为 0。 |
  | -n | 动画开始帧、结束帧和步长。 |
  | -c <string> | 图像文件的名称，例如，picNoBlur.iff |
  | -v <string> | 包含运动向量的文件的名称（不能与 -f 一起使用）。 |
  | -f <string> | 包含图像和向量的文件的名称（不能与 -v 一起使用）。 |
  | -p <int> | 帧填充到前导零的最大数量。默认值为无。 |
  | -o memLimit | 允许的最大内存使用量，以 MB 为单位。 |

  **注**

  当与 -c 和 -v 选项一起使用时，图像文件必须具有相同大小，否则结果可能无法预测。

## 示例

```text
blur2d -f sphere.iff
```

模糊图像保存为 sphere_blur.iff。

```text
blur2d -l 4 -f sphere.iff
```

图像使用模糊长度 4 进行模糊并另存为 sphere_blur.iff。

```text
blur2d -n 1 10 1 -f sphere.iff
```

输入图像序列为 sphere.iff.1 ... sphere.iff.10，输出序列为 sphere_blur.iff.1 ... sphere_blur.iff.10。

若要模糊动画序列，序列文件必须命名为 名称.扩展名.# 或 名称.#。

模糊 名称.扩展名.# 序列的命令是：

```text
blur2d -n start end by -f name.ext
```

模糊 name.# 序列的命令是：

下面的示例使用一个图像的运动路径，然后将其应用于另一个图像。如果要渲染非常大的文件（想不通过渲染运动模糊加快渲染），这将非常有用。该示例以相同的分辨率并在启用运动向量的情况下进行第二次快速渲染（无灯光或纹理，低抗锯齿），并用该方法将模糊应用于非常大的渲染。

**注**

降低抗锯齿质量可能会降低模糊质量。

```text
blur2d -n 1 500 1 -l 2 -f ImageBeautry -v imageVector
```

imageBeauty 是高质量渲染，imageVector 是带有运动向量的低质量渲染。

```text
blur2d -n start end by -f name
```
