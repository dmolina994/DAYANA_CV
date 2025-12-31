from django.shortcuts import render
from .models import (
    DatosPersonales,
    ExperienciaLaboral,
    CursoRealizado,
    VentaGarage,
    Reconocimiento,
    ProductoAcademico,
    ProductoLaboral
)

def get_active_profile():
    return DatosPersonales.objects.filter(perfilactivo=1).first()

# ---------- HOME ----------
def home(request):
    perfil = get_active_profile()
    context = {
        'perfil': perfil,
        'resumen_exp': ExperienciaLaboral.objects.filter(idperfilconqueestaactivo=perfil)[:3],
        'resumen_cursos': CursoRealizado.objects.filter(idperfilconqueestaactivo=perfil)[:3],
        'resumen_garage': VentaGarage.objects.filter(idperfilconqueestaactivo=perfil)[:5],
        'resumen_rec': Reconocimiento.objects.filter(idperfilconqueestaactivo=perfil)[:3],
        'resumen_acad': ProductoAcademico.objects.filter(idperfilconqueestaactivo=perfil)[:3],
        'resumen_lab': ProductoLaboral.objects.filter(idperfilconqueestaactivo=perfil)[:3],
    }
    return render(request, 'home.html', context)

# ---------- EXPERIENCIA ----------
def experiencia(request):
    perfil = get_active_profile()
    experiencias = ExperienciaLaboral.objects.filter(
        idperfilconqueestaactivo=perfil,
        activarparaqueseveaenfront=True
    )
    return render(request, 'experiencia.html', {
        'experiencias': experiencias,
        'perfil': perfil
    })

# ---------- PRODUCTOS ACADÉMICOS ----------
def productos_academicos(request):
    perfil = get_active_profile()
    productos_academicos = ProductoAcademico.objects.filter(
        idperfilconqueestaactivo=perfil,
        activarparaqueseveaenfront=True
    )
    return render(request, 'productos_academicos.html', {
        'productos_academicos': productos_academicos,
        'perfil': perfil
    })

# ---------- PRODUCTOS LABORALES ----------
def productos_laborales(request):
    perfil = get_active_profile()
    productos_laborales = ProductoLaboral.objects.filter(
        idperfilconqueestaactivo=perfil,
        activarparaqueseveaenfront=True
    ).order_by('-fechaproducto')
    return render(request, 'productos_laborales.html', {
        'productos_laborales': productos_laborales,
        'perfil': perfil
    })

# ---------- CURSOS ----------
def cursos(request):
    perfil = get_active_profile()
    cursos = CursoRealizado.objects.filter(
        idperfilconqueestaactivo=perfil,
        activarparaqueseveaenfront=True
    )
    return render(request, 'cursos.html', {
        'cursos': cursos,
        'perfil': perfil
    })

# ---------- RECONOCIMIENTOS ----------
def reconocimientos(request):
    perfil = get_active_profile()
    reconocimientos = Reconocimiento.objects.filter(
        idperfilconqueestaactivo=perfil,
        activarparaqueseveaenfront=True
    ).order_by('-fechareconocimiento')
    return render(request, 'reconocimientos.html', {
        'reconocimientos': reconocimientos,
        'perfil': perfil
    })

# ---------- GARAGE ----------
def garage(request):
    perfil = get_active_profile()
    ventas_garage = VentaGarage.objects.filter(
        idperfilconqueestaactivo=perfil,
        activarparaqueseveaenfront=True
    )
    return render(request, 'garage.html', {
        'ventas_garage': ventas_garage,
        'perfil': perfil
    })
