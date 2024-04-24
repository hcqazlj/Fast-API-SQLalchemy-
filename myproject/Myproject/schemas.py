from typing import List, Union
from pydantic import BaseModel

class ItemBase(BaseModel):
    title:str
    description: Union[str,None] = None


#2.ItemCreate 继承自 ItemBase，他们在创建或读取数据时具有共同的属性。
class ItemCreate(ItemBase):
    pass


#3.Item 继承自 ItemCreate，增加 id 和 owner_id 字段
class Item(ItemCreate):
    id: int
    owner_id: int

    class Config:
        orm_mode = True #使其包含关系字段

class UserBase(BaseModel):
    phone: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int 
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True



class ShieldSetting(BaseModel):
    setting_type: str = None
    answer_content: str = None
    set_content: List[str] = None

class Basic(BaseModel):
    basic_title: str = None
    title_content: List[str]

class BasicModel(BaseModel):
    basic_type: str = None
    basic_content: List[ShieldSetting] = None


class WordSame(BaseModel):
    setting_type: str = None
    proper_word: str
    imitation_word: List[str]


class ImageSetting(BaseModel):
    image_name: str = "logo"
    image_route: str
    image_show: List[str]


class UserSetting(BaseModel):
    shield_setting: List[ShieldSetting] = None
    word_same: List[WordSame] = None
