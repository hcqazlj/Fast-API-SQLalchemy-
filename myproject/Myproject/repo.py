from sqlalchemy.orm import Session
from sqlalchemy import JSON
from fastapi import Depends
from Myproject import models, schemas, dependency
from typing import List
from Myproject.models import BasicSetting
from Myproject.dependency import get_db

# #使用ID查询
# def get_user(data = Session, user_id: int):
#     return data.query(models.User).filter(models.User.id == user_id).first()


def get_setting(
    shield_type: str = None,
    wordsame_type: str = None,
    db: Session = Depends(),
):
    shield = (
        db.query(BasicSetting).filter(BasicSetting.setting_type == shield_type).first()
    )
    wordsame = (
        db.query(BasicSetting).filter(BasicSetting.setting_type == wordsame_type).first()
    )
    return {"shield_setting": shield, "wordsame": wordsame}


# def get_image(setting_type: str,
#               image_show: str,
#               db = Session,
#               ):
#     return db.query(models.BasicSetting).filter(
#         models.BasicSetting.setting_type == setting_type,
#         ).all()


# #
# #通过电子邮件查询单个用户。
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()

# #查询多个用户
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()

# #查询多个项目
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# #增
# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     #使用数据创建sqlalchemy模型实例
#     db.add(db_item) #增加数据到数据库中
#     db.commit()  # 对数据库十五的提交
#     db.refresh(db_item) #刷新数据库实例，使其包含来自数据库的任何新数据
#     return db_item


def add_basic_setting(
    basic_type_repo: str,
    basic_content_repo: List[dict],
    db: Session = Depends(),
):
    settings_type_repo = basic_type_repo
    settings_content_repo = basic_content_repo
    db_shield_base = BasicSetting(
        setting_type=settings_type_repo,
        setting_content=settings_content_repo,
    )
    db.add(db_shield_base)
    db.commit()
    db.refresh(db_shield_base)
    return db_shield_base


# def add_wordsame_setting(
#     wordsame_type_repo: str,
#     proper_word_repo: str,
#     imitation_word_repo: List[str],
#     #    wordsame_base: schemas.WordSame,
#     db: Session,
# ):
#     settings_type = wordsame_type_repo
#     settings_content_key = proper_word_repo
#     settings_content_value: imitation_word_repo
#     db_wordsame_base = models.BasicSetting(
#         setting_type=settings_type,
#         setting_content={settings_content_key: settings_content_value},
#     )
#     db.add(db_wordsame_base)
#     db.commit()
#     db.refresh(db_wordsame_base)
#     return db_wordsame_base


#改
# def update_item_desc_by_id(db: Session, id: int, desc: str):
#     db_item = db.query(models.Item).filter_by(id=id).first()
#     db_item.description = desc
#     db.commit()
#     db.refresh(db_item)
#     return db_item


def update_basic_setting_repo(
    shield_type_repo: str,
    answer_content_repo: str,
    set_content_repo: List[str],

    db: Session = Depends(),
):
    db_update_shield = db.query(BasicSetting).filter(BasicSetting.setting_type == shield_type_repo).first()
    db_update_shield.setting_content = [{answer_content_repo: set_content_repo}]
    db.commit()
    db.refresh(db_update_shield)
    return db_update_shield

def update_word_setting_repo(
    wordsame_type_repo: str,
    proper_word_repo: str,
    imitation_word_repo: List[str],
    db: Session = Depends(),
):
    db_update_wordsame = db.query(BasicSetting).filter(BasicSetting.setting_type == wordsame_type_repo).first()
    db_update_wordsame.setting_content = [{proper_word_repo: imitation_word_repo}]
    db.commit()
    db.refresh(db_update_wordsame)
    return db_update_wordsame








# {
#     "setting_content": [{"对不起，请重新说": ["美国","日本"]}],
#     "id": 1,
#     "setting_type": "屏蔽词设置"
# }




# #删
# # 批量删除1
# def delete_item_by_ownerId1(db: Session, owner_id: int):
#     db.query(models.Item).filter_by(owner_id=owner_id).delete(synchronize_session=False)
#     db.commit()
#     return True

# # 批量删除2
# def delete_item_by_ownerId2(db: Session, owner_id: int):
#     db_items = db.query(models.Item).filter_by(owner_id=owner_id).all()
#     [db.delete(item) for item in db_items]
#     db.commit()
#     return True
