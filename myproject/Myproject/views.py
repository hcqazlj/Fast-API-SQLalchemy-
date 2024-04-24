# from fastapi import FastAPI
# import uvicorn


# app = FastAPI()

# @app.get("/items/{item_id}")

# async def root_item(item_id):
#     return {"ssdfa": item_id}

# @app.get("/items/item_id")

# async def root_item(item_id):
#     return {"ssdfa": "item_idsadfasd"}


## 枚举类型

# from fastapi import FastAPI
# from enum import Enum

# class ModelName(str, Enum):
#     a = 'abcd'
#     b = 'cds'
#     c = 'kkkfa'

# app = FastAPI()

# @app.get("/enum/{enums}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.a:
#         return {"a_num":model_name,"meass": "sadfasdfggg!"}
#     if model_name.value == "cds":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#     return {"model_name": model_name, "message": "Have some residuals"}


# from fastapi import FastAPI

# app = FastAPI()

# item_db = [{"item_name": "Null"},{"item_name": "Fast"},{"item_name": "Yes"}]

# @app.get("/items/")
# ## 0和10是查询参数的默认值
# async def read_item(a: int = 0,limit: int = 10):
#     return item_db[a: a+limit]


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# from typing import Union
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/user/{user_id}/items/{items_id}")
# async def read_user_item(
#     user_id: int ,item_id = int, a: Union[str, None] = None,short: bool = False
# ):
#     item = {"item_ids": item_id,"user_ids": user_id}
#     if a:
#         item.update({"a": a})
#     if not short:
#         item.update({"description":"a big"})
#     return item

# @app.get("/items/{item_id}")
# async def read_user_item(
#     item_id: str, needy: str,skip: int = 0,limit: Union[int,None] = None
# ):
#     item = {"item_id":item_id,"needy": needy,"skip": skip,"limit":limit}
#     return item


# ## 请求体
# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float | None = None

# app = FastAPI()

# @app.post("/items/")
# async def create_item(item: Item):
#     return item


# from fastapi import FastAPI
# from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# app = FastAPI()


# @app.post("/items/")
# async def create_item(item:Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax":price_with_tax})
#     return item_dict


# from typing import Union
# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Union[str, None] = Query(default=None,max_length=50)):
#     ## Query中的内容作为默认值
#     results = {"items": [{"item_id":"foo"},{"item_id":"Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results


# from typing import List, Union
# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: List[str] = Query(default=["foo", "bar"])):
#     query_times = {"q":q}
#     return query_times


# from fastapi import FastAPI, Path
# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(*,item_id: int = Path(title="The ID of the item to get"), q: str):
#     results = {"item_id": item_id}
#     if  q:
#         results.update({"q":q})
#     return results


# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class User(BaseModel):
#     username: str
#     full_name: str | None = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user":user}
#     return results


# from typing import Annotated

# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     ## 会在请求体外多一个键item
#     results = {"item_id": item_id, "item": item}
#     return results


# from typing import Annotated

# from fastapi import Body, FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300
#     )
#     price: float = Field(gt=0, description="The price must be greater than zero")
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results


# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# @app.post("/user/")
# async def create_user(user: UserIn) -> UserIn:
#     return user

# @app.post("/users/", response_model=schemas.User)
# def create_user(user:schemas.UserCreate, data_session: Session = Depends(get_db)):
#     db_user = repo.get_user_by_email(data_session, phone = user.phone)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return repo.create_user(db=data_session, user=user)


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return repo.create_user_item(db=db, item=item, user_id=user_id)

# 预先创建数据库表
# models.Base.metadata.create_all(bind=engine)

# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = repo.get_items(db, skip=skip, limit=limit)
#     return items
# @app.put("/update_item/{item_id}/")
# def update_item(item_id: int,desc: str, db: Session = Depends(get_db)):
#     db_item = repo.update_item_desc_by_id(db, id=item_id, desc=desc)
#     return db_item

## 连接数据库
from typing import List
from fastapi import APIRouter
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import JSON
from sqlalchemy.orm import Session

# import repo as repo, schemas as schemas,models as models
from .dependency import get_db
from .models import BasicSetting
from Myproject import schemas, repo

app1 = APIRouter()


@app1.get("/settings/basic_setting")
def get_user_setting(
    shield_name: str = "屏蔽设置",
    wordsame_name: str = "同音设置",
    db: Session = Depends(get_db),
):
    db_user_setting = repo.get_setting(
        shield_type=shield_name,
        wordsame_type=wordsame_name,
        db=db,
    )
    return db_user_setting


# @app1.get("/settings/basic_setting")
# def get_user_setting(
#     shield_type:str,
#     wordsame_type: str,
#     db: Session = Depends(get_db),
#     ):
#     query_shield = db.query(BasicSetting).filter(BasicSetting.setting_type == shield_type).first()
#     query_wordsame = db.query(BasicSetting).filter(BasicSetting.setting_type == wordsame_type).first()
#     print(query_shield)
#     print(query_wordsame)
#     return {"shield_setting":query_shield,"wordsame":query_wordsame}


@app1.post(
    "/settings/creat_basic_setting",
    response_model=None,
)
def create_basic_setting(
    basic_setting_type: str,
    set_content: List[dict],
    db: Session = Depends(get_db),
):
    create_basic = repo.add_basic_setting(
        basic_type_repo=basic_setting_type,
        basic_content_repo=set_content,
        db=db,
    )
    return {"creat_basic_setting": create_basic}


@app1.put(
    "/settings/update_basic_setting",
    response_model=None,
)
def update_basic_setting(
    shield_setting_type: str,
    answer_content: str,
    set_content: List[str],

    wordsame_setting_type: str,
    proper_word: str,
    imitation_word: List[str],
    db: Session = Depends(get_db),
):
    db_basic_setting = repo.update_basic_setting_repo(
        shield_type_repo=shield_setting_type,
        answer_content_repo=answer_content,
        set_content_repo=set_content,
        db=db,
    )
    db_wordsame = repo.update_word_setting_repo(
        wordsame_type_repo=wordsame_setting_type,
        proper_word_repo=proper_word,
        imitation_word_repo=imitation_word,
        db=db
    )
    return db_basic_setting,db_wordsame


# @app.delete("/delete_item/{owner_id}/")
# def delete_item(owner_id: int, db: Session = Depends(get_db)):
#     result = repo.delete_item_by_ownerId2(db, owner_id=owner_id)
#     return result
