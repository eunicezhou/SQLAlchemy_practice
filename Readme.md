# 什麼是 ORM ?
ORM（對象關係映射）是指將資料庫表格映射到 Python 對象的過程，讓我們得以透過操作 Python 對象來操作資料庫。

# 關於 ORM 的一些基本概念:
__類(Model Class):__ 在 SQLAlchemy 中，類是用來表示資料庫表格的 Python 類別，每個類都會對應資料庫中的一個表格

__列(Column):__ 列是類中的屬性，用來表示資料庫表格中的列。在 SQLAlchemy 中，可以使用 Column 類別來定義列、指定列的類型和約束等等資訊

__關係(Relationship):__ 關係是用來描述類之間的關聯關係，例如一對多、多對一、一對一等等。在 SQLAlchemy 中，可以使用 relationship 函數來定義關係，指定外鍵信息

__會話(Session):__ 會話是用來管理與資料庫的交互，物件導向程式可以透過會話執行查詢、添加、修改、刪除等等操作，並將這些操作同步到資料庫中

__映射(Mapping):__ 映射是指將類和資料庫表格進行對應關聯的過程。在 SQLAlchemy 中，這個過程式自動完成的，透過定義類和使用類的方式，SQLAlchemy 可以根據類自動生成與之對應的資料庫表格結構

# 使用 SQLAlchemy 的基本步驟
__Step 1 定義類(Model Class):__