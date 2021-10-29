# 初始化
import os

import django

from dvadmin.utils.core_initialize import CoreInitialize

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
django.setup()

from dvadmin.system.models import Menu, MenuButton


class Initialize(CoreInitialize):
    creator_id = "456b688c-8ad5-46de-bc2e-d41d8047bd42"

    def init_menu(self):
        """
        初始化菜单表
        """
        self.menu_data = [
            {"id": "b2f96606-faf3-4b7c-89b6-30d461ec98a9", "name": "插件市场", "sort": 0, "web_path": "/pluginsMarket",
             "icon": "briefcase", "parent_id": "",
             "component": "dvadmin_plugins/plugins_market_web/pluginsMarket",
             "component_name": "pluginsMarket"}
        ]
        self.save(Menu, self.menu_data, "菜单表")

    def init_menu_button(self):
        """
        初始化菜单权限表
        """
        self.menu_button_data = [
            {'id': '30bcce50-17d6-4255-96a4-30e42f85bc7d', 'menu_id': 'b2f96606-faf3-4b7c-89b6-30d461ec98a9',
             'name': '查询', 'value': 'Search', 'api': '/api/plugins_market/plugins/',
             'method': 0},
            {'id': '343758bb-7800-4fe6-9b60-5238b0b91271', 'menu_id': 'b2f96606-faf3-4b7c-89b6-30d461ec98a9',
             'name': '新增', 'value': 'Create', 'api': '/api/plugins_market/plugins/',
             'method': 1},
            {'id': '3256fa34-0fb3-4006-84c8-740ae82c1bb2', 'menu_id': 'b2f96606-faf3-4b7c-89b6-30d461ec98a9',
             'name': '编辑', 'value': 'Update', 'api': '/api/plugins_market/plugins/{id}/',
             'method': 2},
            {'id': '964be8bc-7d0c-4ccc-a9de-894f78b28b13', 'menu_id': 'b2f96606-faf3-4b7c-89b6-30d461ec98a9',
             'name': '删除', 'value': 'Delete', 'api': '/api/plugins_market/plugins/{id}/',
             'method': 3},
            {'id': '7a37976e-8688-44e1-b408-a832c6b2c9af', 'menu_id': 'b2f96606-faf3-4b7c-89b6-30d461ec98a9',
             'name': '单例', 'value': 'Retrieve', 'api': '/api/plugins_market/plugins/{id}/',
             'method': 0},
            {'id': '306a3168-5923-43eb-9ffa-0a01209fbd62', 'menu_id': 'ab5efc83-47de-4944-a813-e26067be836c',
             'name': '查询', 'value': 'Search', 'api': '/api/plugins_market/plugins_details/',
             'method': 0},
            {'id': '3f1b367e-28ce-404e-9c26-8e9a30564952', 'menu_id': 'ab5efc83-47de-4944-a813-e26067be836c',
             'name': '新增', 'value': 'Create', 'api': '/api/plugins_market/plugins_details/',
             'method': 1},
            {'id': '0b79d634-9c68-46b1-b7ea-7dd4b279c6f8', 'menu_id': 'ab5efc83-47de-4944-a813-e26067be836c',
             'name': '编辑', 'value': 'Update', 'api': '/api/plugins_market/plugins_details/{id}/',
             'method': 2},
            {'id': '5cd1c89d-06bc-4cf2-a085-4307511e5560', 'menu_id': 'ab5efc83-47de-4944-a813-e26067be836c',
             'name': '删除', 'value': 'Delete', 'api': '/api/plugins_market/plugins_details/{id}/',
             'method': 3},
            {'id': '87d871dc-d1da-4686-bf6b-5d4d4ea47a0e', 'menu_id': 'ab5efc83-47de-4944-a813-e26067be836c',
             'name': '单例', 'value': 'Retrieve', 'api': '/api/plugins_market/plugins_details/{id}/',
             'method': 0}]

        self.save(MenuButton, self.menu_button_data, "菜单权限表")

    def run(self):
        self.init_menu()
        self.init_menu_button()


# 项目init 初始化，默认会执行 main 方法进行初始化
def main(reset=False):
    Initialize(reset).run()
    pass


if __name__ == '__main__':
    main()
