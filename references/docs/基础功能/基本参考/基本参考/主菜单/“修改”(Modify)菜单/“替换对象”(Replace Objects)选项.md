# “替换对象”(Replace Objects)选项

使用这些选项可设置在选择“修改 > 替换对象”(Modify > Replace Objects)时会发生的状况。

## 要复制的属性(Attributes to copy)

复制的属性是从被替换的原始对象复制到新对象的。

#### 旋转(Rotate)

将“旋转”(Rotate)属性从被替换的原始对象复制到新对象。默认设置为启用。

#### 缩放(Scale)

将“缩放”(Scale)属性从被替换的原始对象复制到新对象。默认设置为启用。

## 复制类型(Type of Copy)

指定如何创建新对象。可以选择“复制”(Copy)、“实例”(Instance)或“引用”(Reference)。

#### 复制(Copy)

新对象是源对象的复制品，具有自己单独的形状节点。这是默认设置。

#### 实例(Instance)

新对象是指定源对象的实例，且共享一个形状节点。当启用“保持最后一个选定对象”(Keep last selected object)时，新对象是源对象的实例，且共享其形状节点。

#### 引用(Reference)

只有源对象是引用时才使用此选项。新对象也将是引用。否则，请使用“复制”(Copy)或“实例”(Instance)选项来将对象替换为被引用的源对象。

**注**

如果尝试使用一个引用替换两个或多个对象，将无法执行“撤消”(Undo)操作。

#### 保持最后一个选定对象(Keep last selected object)

默认情况下会保持源对象。如果要自动删除源对象，请禁用“保持最后一个选定对象”(Keep last selected object)。
