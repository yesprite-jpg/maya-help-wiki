# dump_object 节点

# dump_object 节点

将 Amino::Object 的内容转储到文件中。

## 输入

### object [in]

要转储的 Amino::Object。它按原样穿过。

### filename [in]

转储文件的名称。

### folder [in]

用于保存日志文件的可选文件夹。如果未指定，则文件将写入临时目录。

### sample_size [in]

如果大于 0，则为每个组件转储指定大小的数据采样。

### rtServices [in]

运行时服务

## 输出

### out_object [out]

未更改的 Amino::Object 输入。

### log_file_path [out]

完整日志文件路径。

**父页面:** [bif](https://help.autodesk.com/cloudhelp/2022/CHS/Bifrost-Common/files/reference/Bifrost_Common_reference_bif_html.html)
