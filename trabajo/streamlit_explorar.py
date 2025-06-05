# streamlit_explorar.py

import streamlit as st
from db import get_session

# Importa las clases que definiste en clases.py
from generar_base import *


st.set_page_config(page_title="Explorador de objetos SQLAlchemy", layout="wide")


def listar_usuarios():
    """
    Muestra todos los usuarios, en un expander, sus publicaciones y sus reacciones.
    """
    st.header("Usuarios")
    session = get_session()
    usuarios = session.query(Usuario).all()

    if not usuarios:
        st.info("No hay registros en 'usuarios'.")
        session.close()
        return
    for u in usuarios:
        with st.expander(f"ID {u.id} → {u.nombre}", expanded=False):
            st.write(f"**ID:** {u.id}")
            st.write(f"**Nombre:** {u.nombre}")
            if u.publicaciones:
                st.write("**Publicaciones asociadas:**")
                filas = []
                for c in u.publicaciones:
                    filas.append({
                        "ID": c.id,
                        "Contenido": c.publicacion,
                        "ID Usuario": c.usuario_id,
                        "Total Reacciones": len(c.reacciones)
                    })
                st.table(filas)
            else:
                st.write("_No hay publicaciones asociados a este usuario._")


            if u.reacciones:
                st.write("**Reacciones realizadas por el usuario:**")
                filas = []
                for r in u.reacciones:
                    filas.append({
                        "ID Reacción": r.id,
                        "Publicación ID": r.publicacion_id,
                        "Usuario ID": r.usuario_id,
                         "Contenido Publicación": r.publicacion.publicacion if r.publicacion else "No disponible",
                        "Tipo de Emoción": r.tipo_emocion
                    })
                st.table(filas)
            else:
                st.write("_Este usuario no ha reaccionado a ninguna publicación._")
    session.close()

def listar_publicacion():
    """
    Muestra todos las Publicaciones y, en un expander, su autor y sus reacciones.
    """
    st.header("Publicaciones")
    session = get_session()
    publicaciones = session.query(Publicacion).all()
    if not publicaciones:
        st.info("No hay registros en 'publicaciones'.")
        session.close()
        return
    for p in publicaciones:
        with st.expander(f"ID {p.id} → {p.publicacion}", expanded=False):
            st.write(f"**ID:** {p.id}")
            st.write(f"**Publicacion:** {p.publicacion}")
            publi_autor = p.usuario.nombre
            st.write(f"**Autor:** {publi_autor}")
            st.write(f"**Nro. Reacciones:** {len(p.reacciones)}")
            if p.reacciones:
                st.write("**Reacciones asociadas:**")
                filas = []
                for r in p.reacciones:
                    filas.append({
                        "Reaccion ID": r.id,
                        "Usuario ID": r.usuario_id,
                        "Usuario Nombre": r.usuario.nombre,
                        "Tipo Emocion": r.tipo_emocion
                    })
                st.table(filas)
            else:
                st.write("_No hay reacciones asociadas a esta publicacion._")

    session.close()


def listar_reacciones():
    """
    Muestra todos las Reacciones y, en un expander, su usuario autor con la publicacion asociada.
    """
    st.header("Reacciones")
    session = get_session()
    reacciones = session.query(Reaccion).all()
    if not reacciones:
        st.info("No hay registros en 'reaccion'.")
        session.close()
        return
    filas = []
    for r in reacciones:
        filas.append({
            "ID": r.id,
            "Usuario ID": r.usuario_id,
            "Usuario": r.usuario.nombre,
            "Publicacion ID": r.publicacion_id,
            "Publicacion": r.publicacion.publicacion,
            "Tipo Reaccion": r.tipo_emocion
        })
    st.table(filas)
    session.close()
def main():
    st.title("Explorador de objetos SQLAlchemy en Streamlit")
    entidad = st.sidebar.selectbox(
        "Elija la entidad que desea explorar:",
        (
            "Usuario",
            "Publicacion",
            "Reaccion",
        ),
    )
    if entidad == "Usuario":
        listar_usuarios()
    elif entidad == "Publicacion":
        listar_publicacion();
    elif entidad == "Reaccion":
        listar_reacciones();
    


if __name__ == "__main__":
    main()
