import json

import sqlalchemy as sa
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite://", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    computers = orm.relationship("Computer", back_populates="owner", uselist=True)


class Computer(Base):
    __tablename__ = "computers"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    owner_id = Column(ForeignKey(Person.id))
    owner = orm.relationship("Person", back_populates="computers", uselist=False)

    parts = orm.relationship("Part", back_populates="computer", uselist=True)


class Part(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True)
    part_no = Column(String)

    computer_id = Column(ForeignKey(Computer.id))
    computer = orm.relationship(Computer, back_populates="parts", uselist=False)


Base.metadata.create_all(engine)

bob = Person(name="Bob")
alice = Person(name="Alice")

computer1 = Computer(title="Computer 1", owner=bob)
computer2 = Computer(title="Computer 2", owner=bob)
computer3 = Computer(title="Computer 3", owner=alice)
computer4 = Computer(title="Computer 4", owner=alice)

for c in [computer1, computer2]:
    for _ in range(4):
        c.parts.append(Part(part_no=str(_)))
    session.add(c)
for c in [computer3, computer4]:
    for _ in range(5, 10):
        c.parts.append(Part(part_no=str(_)))
    session.add(c)

session.commit()

data = [_[0] for _ in session.execute(sa.select(Computer)).all()]


from marshmallow_jsonapi import Schema, fields


class PersonSchema(Schema):
    class Meta:
        type_ = "person"
        self_url = "/persons/{id}"
        self_url_kwargs = {"id": "<id>"}
        self_url_many = "/persons/"

    id = fields.Str(dump_only=True)
    name = fields.Str()

    computers = fields.Relationship(
        self_url="/person/{id}/relationships/computers",
        self_url_kwargs={"id": "<id>"},
        related_url="/parts?filter[owner_id]={person_id}",
        related_url_kwargs={"person_id": "<id>"},
        schema="ComputerSchema",
        many=True,
        type_="computer",
    )


class ComputerSchema(Schema):
    class Meta:
        type_ = "computer"
        self_url = "/computers/{id}"
        self_url_kwargs = {"id": "<id>"}
        self_url_many = "/computers/"

    id = fields.Str(dump_only=True)
    title = fields.Str()
    owner_id = fields.Integer(as_string=True)

    owner = fields.Relationship(
        self_url="/computers/{id}/relationships/owner",
        self_url_kwargs={"id": "<id>"},
        related_url="/persons/{person_id}",
        related_url_kwargs={"person_id": "<owner_id>"},
        schema="PersonSchema",
        type_="person",
    )
    parts = fields.Relationship(
        self_url="/computer/{id}/relationships/parts",
        self_url_kwargs={"id": "<id>"},
        related_url="/parts?filter[computer_id]={computer_id}",
        related_url_kwargs={"computer_id": "<id>"},
        schema="PartSchema",
        many=True,
        type_="part",
    )


class PartSchema(Schema):
    class Meta:
        type_ = "part"
        self_url = "/parts/{id}"
        self_url_kwargs = {"id": "<id>"}
        self_url_many = "/parts/"

    id = fields.Str(dump_only=True)
    part_no = fields.Str()
    computer_id = fields.Integer(as_string=True)
    computer = fields.Relationship(
        self_url="/parts/{id}/relationships/computer",
        self_url_kwargs={"id": "<id>"},
        related_url="/computers/{computer_id}",
        related_url_kwargs={"computer_id": "<computer_id>"},
        schema="ComputerSchema",
        type_="computer",
    )


filter_json = {
    "filters": [
        {
            "name": "nabave",
            "op": "any",
            "val": {
                "name": "verifikacije",
                "op": "any",
                "val": {"name": "datum_prihvacanja", "op": "le", "val": "2013-09-16"},
            },
        },
        {
            "or": [
                {
                    "name": "nabave",
                    "op": "any",
                    "val": {
                        "name": "verifikacije",
                        "op": "any",
                        "val": {
                            "name": "datum_prihvacanja",
                            "op": "ge",
                            "val": "2013-09-16",
                        },
                    },
                },
                {
                    "name": "nabave",
                    "op": "any",
                    "val": {
                        "name": "verifikacije",
                        "op": "any",
                        "val": {
                            "name": "datum_primitka",
                            "op": "ge",
                            "val": "2013-08-30",
                        },
                    },
                },
            ]
        },
        {
            "comment": [
                "won't work because filtering DSL doesn't split on '.' but on '__'. ",
                "`include` DSL on the other hand splits on '.' and not on '__'.",
            ],
            "name": "nabave.verifikacije",
            "op": "any",
            "val": {
                "or": [
                    {
                        "name": "datum_prihvacanja",
                        "op": "ge",
                        "val": "2013-09-16",
                    },
                    {
                        "name": "datum_primitka",
                        "op": "ge",
                        "val": "2013-08-30",
                    },
                ]
            },
        },
        {
            "comment": [
                "Won't work because `__` split is not recursive and following filter "
                "will try to compare `nabava.verifikacije >= '2013-09-16'` "
            ],
            "or": [
                {
                    "name": "nabave__verifikacije__datum_prihvacanja",
                    "op": "ge",
                    "val": "2013-09-16",
                },
                {
                    "name": "nabave__verifikacije__datum_primitka",
                    "op": "ge",
                    "val": "2013-08-30",
                },
            ],
        },
    ]
}


ids_str = "1,5,6,2,8,9,10,12,14,16,17,18,21,22,25,26,30,34,35,36,40,43,47,48,55,4,59,69,70,68,67,66,65,64,63,62,61,60,58,57,54,53,52,51,50,49,46,45,44,42,41,39,38,37,33,32,31,29,28,27,24,23,20,19,15,13,7"
f2 = {
    "and": [
        {"name": "za_godinu", "op": "eq", "val": 2022},
        {"name": "id", "op": "in", "val": ids_str},
     ]
}
