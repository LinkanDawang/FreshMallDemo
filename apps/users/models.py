from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from itsdangerous.timed import TimestampSigner
from itsdangerous.url_safe import URLSafeTimedSerializer

# from apps.goods.models import GoodsSKU
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from utils.models import BaseModel


class TimedSignSerializer(URLSafeTimedSerializer):
    default_signer = TimestampSigner

    def __init__(
        self,
        secret_key=settings.SECRET_KEY,
        salt=b"encodeForUserActivateToken",
        serializer=None,
        serializer_kwargs=None,
        signer=None,
        signer_kwargs=None,
        fallback_signers=None,
    ):
        super(TimedSignSerializer, self).__init__(
            secret_key,
            salt=salt,
            serializer=serializer,
            serializer_kwargs=serializer_kwargs,
            signer=signer,
            signer_kwargs=signer_kwargs,
            fallback_signers=fallback_signers,
        )
        self._signer = self.make_signer()

    def validate(self, signed_value, max_age=None) -> bool:
        return self._signer.validate(signed_value, max_age=max_age)


class User(AbstractUser, BaseModel):
    """用户"""
    class Meta:
        db_table = "df_users"

    def generate_active_token(self):
        """生成激活令牌"""
        # 参数1:混淆用户id的盐  参数2:超时时间
        # SECRET_KEY = '_7hu3*$_suy+)x=1fui7p*#kvz*u(g&&sjv5awidt6s$z_jc_@'
        serializer = TimedSignSerializer(settings.SECRET_KEY, 3600)
        token = serializer.dumps({"confirm": self.id})  # 返回bytes类型
        return token.decode()


class Address(BaseModel):
    """地址"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="所属用户")
    receiver_name = models.CharField(max_length=20, verbose_name="收件人")
    receiver_mobile = models.CharField(max_length=11, verbose_name="联系电话")
    detail_addr = models.CharField(max_length=256, verbose_name="详细地址")
    zip_code = models.CharField(max_length=6, verbose_name="邮政编码")

    class Meta:
        db_table = "df_address"



