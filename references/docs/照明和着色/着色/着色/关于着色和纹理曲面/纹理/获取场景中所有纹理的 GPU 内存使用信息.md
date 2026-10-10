# 获取场景中所有纹理的 GPU 内存使用信息

若要获取场景中所有纹理的列表以及用于每个纹理的 GPU 内存，请使用带有 dt 标志和 gpu 标志的 ogs 命令。若要列出场景中的所有文件纹理，请将 dt 标志设置为值 full。若要仅列出已用纹理内存的总量，请将 dt 标志设置为值 total。

```text
ogs -gpu -dt full
```

```text
ogs -gpu -dt total
```
