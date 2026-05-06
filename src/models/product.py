from sqlalchemy import Column, String, Numeric, Integer, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from src.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    slug = Column(String(300), unique=True, nullable=False)
    description = Column(String, nullable=True)
    base_price = Column(Numeric(10, 2), nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"))
    brand = Column(String(100))
    tags = Column(JSON, default=list)

    variants = relationship("ProductVariant", back_populates="product")
    images = relationship("ProductImage", back_populates="product")
