from dvadmin.utils.json_response import SuccessResponse, ErrorResponse
from dvadmin.utils.viewset import CustomModelViewSet
from plugins import get_all_plugins, install_update_plugins, delete_plugins


class PluginsMarketViewSet(CustomModelViewSet):
    """
    插件市场接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """

    def list(self, request, *args, **kwargs):
        return SuccessResponse(data=get_all_plugins(), msg="获取成功")

    def create(self, request, *args, **kwargs):
        plugins_name = request.data.get('plugins_name', None)
        data = request.data.get('data', None)
        status, msg = install_update_plugins(plugins_name, data)
        return SuccessResponse(data=[], msg="安装成功") if status else ErrorResponse(data=[], msg=f"安装失败，{msg}")

    def update(self, request, *args, **kwargs):
        plugins_name = request.data.get('plugins_name', None)
        update_type = request.data.get('updateType', None)
        data = request.data.get('data', None)
        status, msg = install_update_plugins(plugins_name, data)
        success_msg = "更新"
        if update_type == 'enabled':
            success_msg = "启用" if data.get('enabled') else "禁用"
        return SuccessResponse(data=[], msg=f"{success_msg}成功") if status else ErrorResponse(data=[],
                                                                                             msg=f"{success_msg}失败，{msg}")

    def delete(self, request, *args, **kwargs):
        status, msg = delete_plugins(request.data.get('plugins_name', None))
        return SuccessResponse(data=[], msg="卸载成功") if status else ErrorResponse(data=[], msg=f"卸载失败，{msg}")
