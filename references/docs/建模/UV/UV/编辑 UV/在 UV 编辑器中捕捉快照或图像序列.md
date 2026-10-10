# 在 UV 编辑器中捕捉快照或图像序列

使用 textureWindow 命令的 -capture 标志，可以在 UV 编辑器中拍摄快照或捕捉图像序列，然后将图像或图像序列保存到磁盘。

## 捕捉快照

若要捕捉单帧快照，请执行以下操作：

```text
textureWindow -e -capture "fileName" panelName;
```

在以下示例中，捕捉 UV 编辑器的当前快照，并将它保存到 testSnapshot.iff 文件。

```text
textureWindow -e -capture "testSnapshot.iff" polyTexturePlacementPanel1;
```

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A7B7CDFB-2C02-42F0-B1D8-5D36751DDBEA.png) <!-- baize:img-hook downloaded=false reason="正文 708 字 ≥300，非承重" -->

## 捕捉图像序列

还可以捕捉图像序列。在禁用捕捉之前，每次刷新编辑器时都会保存图像。

若要捕捉图像序列，请使用 -captureSequenceNumber 标志（短名称为 -csn）并指定序列号 #。序列号必须为正，图像序列按以下模式保存：fileName.#.ext。必须将 -capture 与 -captureSequenceNumber 一起使用。

以下示例保存图像序列 testSnapshotSequence.1.iff、testSnapshotSequence.2.iff 等，直到您选择禁用步骤。每次刷新时都会拍摄快照，且序列号与帧号或时间轴中的时间无关。

```text
textureWindow -e -csn 1 -capture "testSnapshotSequence.iff" polyTexturePlacementPanel1;
```

若要禁用捕捉，请将序列号设置为 -1；或者，将文件名设置为空字符串 ""。

例如：

```text
textureWindow -e -capture "" polyTexturePlacementPanel1;
```

然后可以在 FCheck 中播放图像序列；例如：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-EFC48F5E-7FAC-4165-B873-F8510F1FF8A7.png) <!-- baize:img-hook downloaded=false reason="正文 708 字 ≥300，非承重" -->
