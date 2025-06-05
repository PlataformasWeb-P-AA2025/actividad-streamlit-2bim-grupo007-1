from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Base = declarative_base()

class Usuario(Base):
    __tablename__= "usuario"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))

    publicaciones = relationship("Publicacion", back_populates="usuario")
    reacciones = relationship("Reaccion", back_populates="usuario")

    def __repr__(self):
        return "Usuario: publicacion=%s\n reaccion=%s\n"% (
                          self.publicacion,
                          self.reaccion)


class Publicacion(Base):
    __tablename__= "publicacion" 
    id = Column(Integer, primary_key=True)
    publicacion = Column(String())
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    usuario = relationship("Usuario", back_populates="publicaciones")
    reacciones = relationship("Reaccion", back_populates="publicacion")

    def __repr__(self):
        return "Publicacion: publicacion=%s"% (
                          self.publicacion)

      
    

class Reaccion(Base):
    __tablename__= "reaccion"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    publicacion_id = Column(Integer, ForeignKey('publicacion.id'))
    tipo_emocion = Column(String())


    publicacion = relationship("Publicacion", back_populates="reacciones")
    usuario = relationship("Usuario", back_populates="reacciones")

    def __repr__(self):
        return "Reaccion: publicacion=%s\n reaccion=%s\n"% (
                          self.publicacion,
                          self.reaccion)

Base.metadata.create_all(engine)