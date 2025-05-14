from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class Inversor_DB:
    __tablename__ = 'inversores'
    
    inversor_id: Mapped[int] = mapped_column(primary_key=True)#(1)!
    potencia_ativa_watt: Mapped[float]  
    temperatura_celsius: Mapped[float]
    data_original: Mapped[datetime] = mapped_column(primary_key=True)#(1)!
    data_formatada: Mapped[str] 
    #created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now()  )

@table_registry.mapped_as_dataclass    
class Usina_DB:
    __tablename__ = 'usinas'

    usina_id: Mapped[int] = mapped_column( primary_key=True)
    inversor_id: Mapped[int] = mapped_column( primary_key=True)
    data_original: Mapped[datetime] = mapped_column(primary_key=True)
    data_formatada: Mapped[str]
    #created_at: Mapped[datetime] = mapped_column(init=True, server_default=func.now())

usi = Usina_DB(
    usina_id=1,
    inversor_id=1,
    data_original=datetime.strptime('01-01-2025', '%d-%m-%Y'),
    data_formatada='08-01-2025'
)

inver = Inversor_DB(
    inversor_id=5,
    potencia_ativa_watt=0.0,
    temperatura_celsius=0.0,
    data_original=datetime.strptime('01-01-2025', '%d-%m-%Y'),
    data_formatada='01-01-2025'
)
