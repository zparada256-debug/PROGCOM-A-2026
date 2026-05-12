"""
=============================================================
  CALCULADORA DE ÍNDICES CLÍNICOS - INGENIERÍA BIOMÉDICA
  Godlike Quest Two - GQ3
=============================================================
  Índices incluidos:
    1. IMC  - Índice de Masa Corporal
    2. PAM  - Presión Arterial Media
=============================================================
"""


# ─────────────────────────────────────────────
#  FUNCIONES DE CÁLCULO
# ─────────────────────────────────────────────

def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """
    Calcula el Índice de Masa Corporal.
    Fórmula: IMC = peso (kg) / altura² (m)
    """
    if altura_m <= 0:
        raise ValueError("La altura debe ser mayor a 0.")
    if peso_kg <= 0:
        raise ValueError("El peso debe ser mayor a 0.")
    return peso_kg / (altura_m ** 2)


def clasificar_imc(imc: float) -> str:
    """Clasifica el IMC según los criterios de la OMS."""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    elif imc < 35.0:
        return "Obesidad grado I"
    elif imc < 40.0:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III (mórbida)"


def calcular_pam(sistolica: float, diastolica: float) -> float:
    """
    Calcula la Presión Arterial Media.
    Fórmula: PAM = diastólica + (1/3) × (sistólica - diastólica)
    Equivalente a: PAM = (sistólica + 2 × diastólica) / 3
    """
    if sistolica <= 0 or diastolica <= 0:
        raise ValueError("Los valores de presión deben ser mayores a 0.")
    if sistolica <= diastolica:
        raise ValueError("La presión sistólica debe ser mayor que la diastólica.")
    return diastolica + (1 / 3) * (sistolica - diastolica)


def clasificar_pam(pam: float) -> str:
    """Clasifica la PAM según rangos clínicos estándar."""
    if pam < 70:
        return "⚠️  PAM baja — Riesgo de hipoperfusión tisular"
    elif pam <= 100:
        return "✅  PAM normal — Perfusión adecuada"
    else:
        return "⚠️  PAM elevada — Riesgo de hipertensión / daño vascular"


# ─────────────────────────────────────────────
#  FUNCIONES DE ENTRADA (con validación)
# ─────────────────────────────────────────────

def pedir_float(mensaje: str, minimo: float = 0.0) -> float:
    """Solicita un número flotante al usuario con validación básica."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= minimo:
                print(f"  ✗ El valor debe ser mayor a {minimo}. Intente de nuevo.\n")
            else:
                return valor
        except ValueError:
            print("  ✗ Entrada inválida. Ingrese un número válido.\n")


# ─────────────────────────────────────────────
#  MÓDULOS DE CADA ÍNDICE
# ─────────────────────────────────────────────

def modulo_imc():
    print("\n" + "─" * 45)
    print("  📊  ÍNDICE DE MASA CORPORAL (IMC)")
    print("─" * 45)
    print("  Fórmula: IMC = peso(kg) / altura²(m)\n")

    peso   = pedir_float("  Ingrese su peso en kilogramos  : ")
    altura = pedir_float("  Ingrese su altura en metros    : ")

    imc           = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)

    print("\n  ──── RESULTADO ────")
    print(f"  IMC             : {imc:.2f} kg/m²")
    print(f"  Clasificación   : {clasificacion}")
    print("\n  Rangos OMS:")
    print("    < 18.5   → Bajo peso")
    print("    18.5–24.9 → Peso normal")
    print("    25.0–29.9 → Sobrepeso")
    print("    30.0–34.9 → Obesidad grado I")
    print("    35.0–39.9 → Obesidad grado II")
    print("    ≥ 40.0   → Obesidad grado III")


def modulo_pam():
    print("\n" + "─" * 45)
    print("  💉  PRESIÓN ARTERIAL MEDIA (PAM)")
    print("─" * 45)
    print("  Fórmula: PAM = DBP + (1/3)(SBP - DBP)\n")

    sistolica  = pedir_float("  Presión sistólica  (mmHg) : ")
    diastolica = pedir_float("  Presión diastólica (mmHg) : ")

    # Validar que sistólica > diastólica
    while sistolica <= diastolica:
        print("  ✗ La presión sistólica debe ser mayor que la diastólica.\n")
        sistolica  = pedir_float("  Presión sistólica  (mmHg) : ")
        diastolica = pedir_float("  Presión diastólica (mmHg) : ")

    pam           = calcular_pam(sistolica, diastolica)
    clasificacion = clasificar_pam(pam)

    print("\n  ──── RESULTADO ────")
    print(f"  PAM             : {pam:.2f} mmHg")
    print(f"  Interpretación  : {clasificacion}")
    print("\n  Rangos clínicos:")
    print("    < 70 mmHg    → PAM baja")
    print("    70–100 mmHg  → PAM normal")
    print("    > 100 mmHg   → PAM elevada")


# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def mostrar_menu():
    print("\n" + "=" * 45)
    print("  🏥  CALCULADORA CLÍNICA BIOMÉDICA  🏥")
    print("=" * 45)
    print("  Seleccione el índice a calcular:\n")
    print("    [1]  IMC  - Índice de Masa Corporal")
    print("    [2]  PAM  - Presión Arterial Media")
    print("    [3]  Calcular ambos")
    print("    [0]  Salir")
    print("─" * 45)


def main():
    print("\n  Bienvenido a la Calculadora de Índices Clínicos")
    print("  Ingeniería Biomédica — GQ3\n")

    while True:
        mostrar_menu()
        opcion = input("  Opción: ").strip()

        if opcion == "1":
            modulo_imc()
        elif opcion == "2":
            modulo_pam()
        elif opcion == "3":
            modulo_imc()
            modulo_pam()
        elif opcion == "0":
            print("\n  👋 ¡Hasta luego! Programa finalizado.\n")
            break
        else:
            print("\n  ✗ Opción no válida. Intente de nuevo.")

        input("\n  Presione Enter para continuar...")


# ─────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    main()
