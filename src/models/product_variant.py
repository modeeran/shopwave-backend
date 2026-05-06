from sqlalchemy import Column, String, Integer, Numeric, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from src.core.database import Base

class ProductVariant(Base):
    __tablename__ = "product_variants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    sku = Column(String(100), unique=True, nullable=False)
    size = Column(String(50))
    colour = Column(String(50))
    price_override = Column(Numeric(10, 2))
    stock_quantity = Column(Integer, default=0, nullable=False)
    is_active = Column(Boolean, default=True)

    product = relationship("Product", back_populates="variants")
