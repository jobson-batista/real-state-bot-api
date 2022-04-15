from ..database.database import Base
from sqlalchemy import Column, Integer, Text, Float, String

class Announcement(Base):
    __tablename__ = 'announcement'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    location = Column(Text, nullable=False)
    image = Column(Text, nullable=False)
    date = Column(Text, nullable=False)

    def __init__(self, title, url, price, location, image, date):
        self.title = title
        self.url = url
        self.price = price
        self.location = location
        self.image = image
        self.date = date
    
    def __repr__(self):
        ad = {}
        ad['id'] = self.id
        ad['title'] = self.title
        ad['url'] = self.url
        ad['price'] = self.price
        ad['location'] = self.location
        ad['image'] = self.image
        ad['date'] = self.date
        return ad

class Search(Base):
    __tablename__ = 'searchs'
    id = Column(Integer, primary_key=True)
    city = Column(String(50), nullable=False)
    districts = Column(Text, nullable=False)

    def __init__(self, city, districts):
        self.city = city
        self.districts = districts
    
    def __repr__(self):
        search = {}
        search['id'] = self.id
        search['city'] = self.city
        search['districts'] = self.districts
        return search
