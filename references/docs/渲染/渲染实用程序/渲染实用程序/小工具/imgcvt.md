# imgcvt

Imgcvt 工具将图像或图像序列从一种图像格式转化为其他格式。

在 Shell 窗口输入 imgcvt，后面加上要转化图像的名称。输入和输出图像格式通常由文件扩展名或图像内容决定。然而，当输入或输出图像没有扩展名或无法识别时，可以使用 -f 和 -t 选项来指示所需格式。可以使用以下选项：

```text
imgcvt <options> input_image output_image
```

## 示例 1

```text
imgcvt -f sgi -t tiff input_image output_image
```

该命令将名为 input_image 的“Silicon Graphics”格式图像转化为 TIFF 格式，并以其他名称 output_image 保存该图像。

## 示例 2

```text
imgcvt -f tiff -t iff input_image output_image
```

该命令将 TIFF 图像转化为 IFF 文件格式。

## 选项

| 命令行选项 | 描述 |
|---|---|
| -f input_image_extension | 识别要转化的特定图像格式。例如： -f sgi 这表示只将匹配“Silicon Graphics”图像格式的文件视为输入。 |
| -t output_image_extension | 识别要转化到的特定图像格式。例如： -t tiff 这表示文件将只被转化为 TIFF 图像格式。有关可能的扩展名列表，请参见[图像扩展名](imgcvt.md#WS17956D7ADBC6E73658A86F82117AE33C1F0-7FFD)。 |
| -n start end step | 是输入图像序列的开始、结束和步长（只接受整数）。 |
| -N start end step | 是输出图像序列的开始、结束和步长（只接受整数）。 |
| -r range | 在输入图像序列中，选择要转化的图像范围。例如： imgcvt -r 1-5 ... imgcvt -r 1-5x2 ... imgcvt -r 1-5,10-20x2,50 ... 序列说明符是由逗号或斜线隔开的单独帧或范围的列表。对于每个范围，均可在 x 之后指定可选步长。 可以反转序列，也可以将偏移添加到输入或输出帧编号： imgcvt -r 100-1 -R 1-100 in.#.rgb out.#.rla imgcvt -r 1-100 in.#.rgb out.#+100.rla 这些是单独的连续编号图像文件。 |
| -R range | 在输出图像序列中，选择要转化到的图像范围。 |
| -h | 提供每个选项的简短描述。 |
| -s | 无提示模式。 |
| -v | 详细模式。 |
| -V pal/ntsc | yuv 文件的视频模式。 |
| -C compress | TIFF 压缩类型：LZW（默认）或 NONE。 |
| -q N | JPEG 质量（0...100；默认为 75）。 |
| -m | 浏览映射格式。 |

在处理一个图像序列时，可以使用 # 和 @ 符号来引用当前帧编号。井号 (#) 表示一个四位填充式数字，而 @ 符号表示一个非填充式数字。以下示例将转化一个 100 帧序列：

```text
imgcvt -n 1 100 1 image_in.iff.@ image_out.#.rla
```

要对帧编号格式进行更加精确的控制，请使用多个 @ 符号来设定一个特定填充，或使用标准 printf (3S) 表示法：

```text
imgcvt -n 1 100 1 image_in.@@@.rgb image_out.#.rla
imgcvt -n 1 100 1 image_in.%03d.rgb image_out.#.rla
imgcvt -n 1 100 1 image_in.%.2f.rgb image_out.#.rla
```

## 图像扩展名

使用以下扩展名将图像从一种图像格式转化为其他格式。在 -f 选项中，指定要转化的图像格式的扩展名。在 -t 选项中，指定要转化到的图像格式扩展名。

| 图像格式 | 扩展名 |
|---|---|
| Abekas NTSC 或 PAL | .yuv |
| Alias | .als |
| 浏览 |  |
| GIF | .gif |
| JPEG | .jpg |
| Kodak Cineon | .cin |
| Lucas Film | .lff |
| Pixibox PXB 和 SCN | .pxb 或 .scn |
| PPM raw/ascii | .ppm |
| Prisms | .pri |
| Quantel | .qtl |
| SGI | .rgb、.sgi 或 .bw |
| Avid®Softimage® | .pic |
| Targa RGB/BW | .tga |
| TIFF 6.0 | .tif 或 .tiff |
| Vista | .vst |
| Wavefront RLA | .rla |
