# 使用文档

## 1. 环境要求

- Python 3.8 及以上
- pip 包管理器

---

## 2. 安装依赖

项目依赖以下 Python 包：

```bash
pip install flask flask-sqlalchemy flask-login werkzeug
```

| 包名 | 说明 |
|------|------|
| flask | Web 框架核心 |
| flask-sqlalchemy | 数据库 ORM |
| flask-login | 用户登录状态管理 |
| werkzeug | Flask 内置依赖，提供密码哈希工具 |

---

## 3. 启动项目

在项目根目录下执行：

```bash
cd flaskOnlineShop
python run.py
```

**首次运行**时，程序会自动：
1. 在 `instance/` 目录下创建 `shop.db` 数据库文件
2. 创建所有数据表（`user`、`product`、`comment`）
3. 读取 `data/products.json`，将 9 件商品写入数据库

启动成功后终端输出如下：

```
初始化测试商品数据完成，共 9 件。
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

---

## 4. 访问应用

| 场景 | 地址 |
|------|------|
| 本机浏览器 | `http://localhost:5000` |
| 局域网其他设备 | `http://本机IP:5000` |

> 查看本机 IP：Windows 执行 `ipconfig`，找到"IPv4 地址"一栏。

---

## 5. 功能操作指南

### 5.1 浏览商品

1. 打开 `http://localhost:5000`
2. 首页展示所有商品卡片，包含图片、名称、价格
3. 点击**查看详情**进入商品详情页

### 5.2 注册账号

1. 点击导航栏右侧**注册**
2. 填写用户名和密码
3. 点击**注册**按钮
4. 注册成功后自动跳转到登录页

> 用户名不能与已注册用户重复，否则会提示"用户名已存在"。

### 5.3 登录

1. 点击导航栏右侧**登录**
2. 输入注册时的用户名和密码
3. 点击**登录**按钮
4. 登录成功后跳转首页，导航栏显示"你好, 用户名"

### 5.4 发表评论

> 需要先登录才能评论。

1. 进入任意商品详情页
2. 页面下方找到**发表评论**区域
3. 在文本框中输入评论内容
4. 点击**提交评论**
5. 评论立即出现在该商品的评论列表中

未登录时，提交按钮显示为**登录后评论**，点击跳转登录页。

### 5.5 注销登录

点击导航栏右侧**注销**，即退出登录状态，跳转回首页。

---

## 6. 项目文件结构速览

```
flaskOnlineShop/
├── run.py              ← 启动入口，执行 python run.py
├── data/
│   └── products.json   ← 商品初始数据，在此增删改商品
├── app/
│   ├── __init__.py     ← 应用工厂
│   ├── models.py       ← 数据库模型
│   ├── routes/
│   │   ├── auth.py     ← 注册/登录/注销
│   │   └── shop.py     ← 首页/商品详情
│   └── templates/      ← HTML 模板
└── instance/
    └── shop.db         ← 数据库（自动生成）
```

---

## 7. 常见问题

**Q：启动时报 `ModuleNotFoundError: No module named 'flask'`**

未安装依赖，执行：
```bash
pip install flask flask-sqlalchemy flask-login werkzeug
```

---

**Q：修改了数据模型后，启动报数据库错误**

删除旧数据库文件后重新启动：
```bash
# Windows
del instance\shop.db

# 重新启动
python run.py
```

> 注意：删除数据库会清除所有数据，包括注册的用户和评论。

---

**Q：如何新增商品？**

编辑 `data/products.json`，在数组末尾追加一条记录：

```json
{
  "name": "新商品名称",
  "price": 999.00,
  "description": "商品描述文字",
  "image_url": "https://图片地址"
}
```

然后删除数据库并重启：

```bash
del instance\shop.db
python run.py
```

---

**Q：局域网其他设备无法访问**

检查以下两点：
1. 确认 `run.py` 中 `host='0.0.0.0'`（已默认配置）
2. 检查 Windows 防火墙是否放行了 `5000` 端口

---

## 8. 停止服务

在终端中按 `Ctrl + C` 停止开发服务器。
