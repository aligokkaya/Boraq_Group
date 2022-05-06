from pydantic import BaseModel


class Admin_News(BaseModel):
    isim_soyisim:str = None
    konu:str = None
    baslik:str = None
    mesaj:str = None
    image:str = None
    datetime:str = None