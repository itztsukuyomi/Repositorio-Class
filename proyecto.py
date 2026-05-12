# ══════════════════════════════════════════════════════════════
# proyecto.py · Ficha 3236582 · SENA CTM Itagüí
# Completá con los datos reales de tu proyecto
# ══════════════════════════════════════════════════════════════

nombre_proyecto = "Konyu Motors"           # nombre de tu proyecto
descripcion     = "Compra Venta de Carros"           # qué problema resuelve
tecnologias     = ["React", "HTML", "CSS"]           # ["HTML", "Python", "MySQL"]
integrantes     = ["Juan Manuel Saldarriaga", "Jose Manuel Urrego"]           # ["Nombre 1", "Nombre 2"]
funcionalidades = ["Login", "Registro", "Publicar Venta", "Compra", "Reportes"]           # ["Login", "Registro", "Reportes"]


def mostrar_info():
    print(f"Proyecto:      {nombre_proyecto}")
    print(f"Descripción:   {descripcion}")
    print(f"Equipo:        {', '.join(integrantes)}")
    print(f"Tecnologías:   {', '.join(tecnologias)}")
    print(f"Funcionalidades:")
    for f in funcionalidades:
        print(f"  - {f}")


mostrar_info()