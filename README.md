Supabase是一个开源的Firebase替代品，提供了数据库、认证、实时订阅等功能。下面是一个Supabase快速开始指南，帮助你快速启动一个项目。

Supabase的网址是https://supabase.com

## 创建Supabase项目

1. 访问Supabase官网并创建一个新的组织和项目。选择最适合你的地区以优化性能。例如，如果你在欧盟，可以选择西欧（爱尔兰）作为服务器位置[3]。
2. 创建项目后，你需要记录下项目URL和匿名公钥。这两个信息在设置中的API部分可以找到，它们对于连接你的项目至Supabase至关重要[3]。

## 设置数据库

1. 在Supabase Dashboard中创建一个新的Supabase项目后，你可以使用Table界面或SQL编辑器创建一个`todos`表。例如，使用以下SQL片段创建一个`todos`表：

   ```sql
   create table todos (
     id serial primary key,
     task text
   );
   ```

2. 创建表后，可以通过行级安全性（RLS）来保护它，并使用Supabase客户端库设置对更改的订阅[2]。

## 初始化本地Supabase环境

1. 使用Supabase CLI在应用的根目录中初始化Supabase：

   ```bash
   supabase init
   ```

2. 创建一个迁移文件来管理数据库更改：

   ```bash
   supabase migration new init
   ```

3. 使用Supabase CLI将你的本地仓库与Supabase项目链接，并启动本地开发设置。在进行本地更改之前，记得从Dashboard拉取任何架构更改[2]。

## 开发应用

1. 在你的JavaScript项目中安装Supabase客户端：

   ```bash
   npm i @supabase/supabase-js
   ```

   或者如果你使用Yarn：

   ```bash
   yarn add @supabase/supabase-js
   ```

2. 创建一个Supabase对象，以便在需要与Supabase交互时引用它。例如，获取`drinks`表中的所有记录：

   ```javascript
   supabase
     .from('drinks')
     .select('*')
     .order('name')
     .limit(15)
     .then(...)
   ```

   这段代码首先指定要连接的表（`drinks`），然后选择要选择的列（使用`*`表示所有列），接着按名称排序，并限制结果为前15个元素[3]。

通过遵循上述步骤，你可以快速开始使用Supabase来构建你的应用。Supabase提供了丰富的文档和指南，帮助你深入了解如何使用其各种功能，包括数据库、认证、存储等[1][2][3][4][5][6][7][8]。

Citations:
[1] https://github.com/supabase/supabase/issues/21519
[2] https://www.restack.io/docs/supabase-knowledge-supabase-quickstart-guide
[3] https://dev.to/wagenrace/getting-started-with-supabase-8n4
[4] https://supabase.com/docs/guides/getting-started/tutorials/with-nextjs
[5] https://supabase.com/docs/guides/getting-started/tutorials/with-react
[6] https://supabase.com/docs/guides/api/quickstart
[7] https://supabase.com/docs/guides/getting-started
[8] https://supabase.com/docs/guides/storage/quickstart
