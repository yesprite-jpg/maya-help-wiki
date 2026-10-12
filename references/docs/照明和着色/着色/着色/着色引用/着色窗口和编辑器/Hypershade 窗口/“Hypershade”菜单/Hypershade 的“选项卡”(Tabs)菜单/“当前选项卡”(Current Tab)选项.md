# “当前选项卡”(Current Tab)选项

有关 Hypershade 选项卡的详细信息，请参见 [Hypershade 浏览器](../../Hypershade%20浏览器.md)。

当您选择“选项卡 > 当前选项卡”(Tabs > Current Tab)时，如果当前选项卡是磁盘选项卡或默认的“项目”(Projects)选项卡，则下列选项可用：

#### 仅显示目录(Show Directories Only)

该选项卡仅显示目录列表。

#### 仅显示文件(Show Files Only)

选项卡仅显示文件图标。

#### 显示二者(Show Both)

该选项卡在分割面板中显示目录列表和文件图标。

#### 刷新文件列表(Refresh File Listing)

选项卡刷新列表显示。

#### 刷新选定样例(Refresh Selected Swatches)

选项卡刷新选定的样例。该选项适用于“Hypershade”中的磁盘选项卡。

#### 刷新所有样例(Refresh All Swatches)

选项卡刷新所有的样例。该选项适用于“Hypershade”中的磁盘选项卡。

**注**

提示：

在“Hypershade”中的“项目”(Project)和自定义磁盘选项卡中，可以在一个文件上单击鼠标右键，然后选择“刷新样例”(Refresh Swatch)来刷新该文件样例。

#### 为当前图像生成样例文件(Generate Swatch Files for Current Images)

当导航到在磁盘选项卡（例如，默认的“项目”(Projects)选项卡）中包含图像的目录时，“Hypershade”从磁盘读取每个图像文件，并显示代表该图像文件的一个样例。读取每个图像文件，然后创建一个样例比较花费时间，特别是当目录包含较大的图像文件和/或多个图像文件或包含网络图像文件时。

创建并显示图像文件的样例后，可以使用为当前图像生成样例文件菜单项来将其保存。现在，每次导航到“Hypershade”中的同一目录，显示更新会快得多，因为“Hypershade”可以读取保存的样例，而不再需要读取每个图像文件。

样例文件被保存在包含图像的目录的 .mayaSwatches 子目录中，样例文件的名称对应于图像文件的名称。例如，对于名称为 earth.tif 的图像文件，.mayaSwatches 子目录中包含一个名称为 earth.tif.swatch 的文件。

**注**

- 由于样例文件保存在子目录中，若要成功地为当前图像生成样例文件，需要具有目录的写权限。

- 由于磁盘/网络的访问时间，刷新样例可能需要一些处理时间。
