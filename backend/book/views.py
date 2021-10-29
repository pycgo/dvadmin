
# Create your views here.

from book.models import Book
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class BookSerializer(CustomModelSerializer):
    """
    书籍-序列化器
    """

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["id"]


class BookCreateUpdateSerializer(CustomModelSerializer):
    """
    书籍管理 创建/更新时的列化器
    """

    class Meta:
        model = Book
        fields = '__all__'


# class BookTreeSerializer(CustomModelSerializer):
#     """
#     字典表的树形序列化器
#     """
#     children = serializers.SerializerMethodField(read_only=True)
#
#     def get_children(self, instance):
#         queryset = Book.objects.filter(parent=instance.id).filter(status=1)
#         if queryset:
#             serializer = BookTreeSerializer(queryset, many=True)
#             return serializer.data
#         else:
#             return None
#
#     class Meta:
#         model = Book
#         fields = "__all__"
#         read_only_fields = ["id"]


class BookViewSet(CustomModelViewSet):
    """
    书籍管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    extra_filter_backends = []
    permission_classes = []
    search_fields = ['label']
