from sqlalchemy import Table,Column,Integer,String
from app.database.db import meta


Admin_News = Table(
    'admin_news',meta,
    Column("id",Integer,primary_key=True),
    Column("isim_soyisim",String(64)),
    Column("konu",String(255)),
    Column("baslik",String(64)),
    Column("mesaj",String(255)),
    Column("image",String(64)),
    Column("datetime",String(64)),

)
