from django.db import models


class BaseModel(models.Model):
    """为模型类补充字段 """
    # 数据的创建事件
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 数据的更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        # 告诉django这是用来继承的类，不会生成迁移文件
        abstract = True  # 说明是抽象模型类
