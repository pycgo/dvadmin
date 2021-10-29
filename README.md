# Django-Vue-Admin-Pro



个人学习 dvadmin项目  





## 前端♝

### 	开发🦗

```bash
# 克隆项目
git clone https://gitee.com/dvadmin/django-vue-admin-pro.git

# 进入项目目录
cd web

# 安装依赖
npm install --registry=https://registry.npm.taobao.org

# 启动服务
npm run dev
# 浏览器访问 http://localhost:8080
# .env.development 文件中可配置启动端口等参数
```

### 	发布♗

```bash
# 构建测试环境
npm run build:stage

# 构建生产环境
npm run build:prod
```



## 后端💈

~~~bash
1. 进入项目目录 cd backend
2. 在项目根目录中，复制 ./conf/env.example.py 文件为一份新的到 ./conf 文件夹下，并重命名为 env.py
3. 在 env.py 中配置数据库信息
	mysql数据库版本建议：8.0
	mysql数据库字符集：utf8mb4
4. 安装依赖环境
	pip3 install -r requirements.txt
5. 执行迁移命令：
	python3 manage.py makemigrations
	python3 manage.py migrate
6. 初始化数据
	python3 manage.py init
7. 启动项目
	python3 manage.py runserver 127.0.0.1:8000
或使用 daphne :
  daphne -b 0.0.0.0 -8000 application.asgi:application
初始账号：superadmin 密码：admin123456
后端接口文档地址：http://127.0.0.1:8000/swagger






