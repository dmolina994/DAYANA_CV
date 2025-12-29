from django.shortcuts import render
from .models import (
    DatosPersonales,
    CursoRealizado,
    ExperienciaLaboral,
    ProductoAcademico,
    ProductoLaboral,
    Reconocimiento,
    VentaGarage
)

# 🏠 HOME
def home(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    return render(request, "home.html", {"perfil": perfil})


# 📌 PANEL
def panel(request):
    # También se lo pasamos por si el panel hereda de base.html
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    return render(request, "panel.html", {"perfil": perfil})


# 📚 CURSOS REALIZADOS
def cursos(request):
    # 1. Buscamos el perfil para la barra lateral
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    
    # 2. Buscamos los cursos
    cursos_activos = CursoRealizado.objects.filter(
        activarparaqueseveaenfront=True
    ).order_by('-fechafin')

    return render(request, "cursos.html", {
        "cursos": cursos_activos,
        "perfil": perfil  # <--- IMPORTANTE: Enviamos el perfil
    })


# 💼 EXPERIENCIA LABORAL
def experiencia(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()

    experiencias = ExperienciaLaboral.objects.filter(
        activarparaqueseveaenfront=True
    ).order_by('-fechainiciogestion')

    return render(request, "experiencia.html", {
        "experiencias": experiencias,
        "perfil": perfil
    })


# 🏅 RECONOCIMIENTOS
def reconocimientos(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()

    reconocimientos = Reconocimiento.objects.filter(
        activarparaqueseveaenfront=True
    ).order_by('-fechareconocimiento')

    return render(request, "reconocimientos.html", {
        "reconocimientos": reconocimientos,
        "perfil": perfil
    })


# 🧰 PRODUCTOS LABORALES
def productos_laborales(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()

    productos = ProductoLaboral.objects.filter(
        activarparaqueseveaenfront=True
    ).order_by('-fechaproducto')

    return render(request, "productos_laborales.html", {
        "productos_laborales": productos,
        "perfil": perfil
    })


# 📚 PRODUCTOS ACADÉMICOS
def productos_academicos(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()

    productos = ProductoAcademico.objects.filter(
        activarparaqueseveaenfront=True
    ).order_by('-id')

    return render(request, "productos_academicos.html", {
        "productos_academicos": productos,
        "perfil": perfil
    })


# 🏷️ VENTA GARAGE
def garage(request):
    # Aquí ya lo tenías bien, lo mantengo igual
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    
    items = VentaGarage.objects.filter(
        activarparaqueseveaenfront=True
    ).order_by('valordelbien')

    return render(request, "ventagarage.html", {
        "garage_items": items,
        "perfil": perfil
    })