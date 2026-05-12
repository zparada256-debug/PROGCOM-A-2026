import tkinter as tk
from tkinter import font as tkfont
import random

# ─── Datos del juego ───────────────────────────────────────────────────────────
NOMBRES = {1: "Piedra", 2: "Papel", 3: "Tijera"}
ICONOS  = {1: "✊", 2: "✋", 3: "✌️"}
BEATS   = {1: 3, 2: 1, 3: 2}   # clave GANA a valor
MAX_RONDAS = 3

class Juego:
    def __init__(self):
        self.v_jugador = 0
        self.v_maquina = 0
        self.empates   = 0
        self.ronda     = 1
        self.terminado = False

    def jugar(self, eleccion):
        if self.terminado:
            return None
        maquina = random.randint(1, 3)
        if eleccion == maquina:
            resultado = "tie"
            self.empates += 1
        elif BEATS[eleccion] == maquina:
            resultado = "win"
            self.v_jugador += 1
        else:
            resultado = "lose"
            self.v_maquina += 1
        self.ronda += 1
        if self.ronda > MAX_RONDAS:
            self.terminado = True
        return eleccion, maquina, resultado

    def ganador_final(self):
        if self.v_jugador > self.v_maquina:
            return "win"
        elif self.v_maquina > self.v_jugador:
            return "lose"
        return "tie"

    def reset(self):
        self.__init__()


# ─── Colores ───────────────────────────────────────────────────────────────────
BG      = "#1e1e2e"   # fondo principal (oscuro tipo VS Code)
SURFACE = "#2a2a3d"   # superficies / cards
BORDER  = "#3d3d5c"
TEXT    = "#cdd6f4"
MUTED   = "#7f849c"

WIN_BG  = "#1e3a2f";  WIN_FG  = "#a6e3a1"
LOSE_BG = "#3a1e1e";  LOSE_FG = "#f38ba8"
TIE_BG  = "#1e2a3a";  TIE_FG  = "#89b4fa"

BTN_HOVER = "#3d3d5c"
BTN_PRESS = "#534ab7"


# ─── Ventana principal ─────────────────────────────────────────────────────────
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Piedra · Papel · Tijera")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.geometry("520x620")

        self.juego = Juego()
        self._build_ui()
        self._actualizar_marcador()

    # ── Construcción de la UI ──────────────────────────────────────────────────
    def _build_ui(self):
        pad = dict(padx=20, pady=8)

        # Título
        tk.Label(self, text="Piedra · Papel · Tijera",
                 bg=BG, fg=TEXT, font=("Segoe UI", 18, "bold")).pack(pady=(24, 4))

        # Info de ronda
        self.lbl_ronda = tk.Label(self, text="", bg=BG, fg=MUTED,
                                  font=("Segoe UI", 11))
        self.lbl_ronda.pack()

        # Marcador
        marc_frame = tk.Frame(self, bg=BG)
        marc_frame.pack(pady=14)
        self.lbl_marc_j = self._score_card(marc_frame, "Tú", "0")
        self.lbl_marc_e = self._score_card(marc_frame, "Empates", "0")
        self.lbl_marc_m = self._score_card(marc_frame, "Máquina", "0")

        # Arena (iconos grandes)
        arena = tk.Frame(self, bg=SURFACE, padx=30, pady=18)
        arena.pack(fill="x", padx=20, pady=4)

        self.lbl_icono_j = tk.Label(arena, text="❓", bg=SURFACE, fg=TEXT,
                                    font=("Segoe UI Emoji", 42))
        self.lbl_icono_j.grid(row=0, column=0, padx=20)
        tk.Label(arena, text="VS", bg=SURFACE, fg=MUTED,
                 font=("Segoe UI", 13)).grid(row=0, column=1)
        self.lbl_icono_m = tk.Label(arena, text="❓", bg=SURFACE, fg=TEXT,
                                    font=("Segoe UI Emoji", 42))
        self.lbl_icono_m.grid(row=0, column=2, padx=20)

        tk.Label(arena, text="Tú", bg=SURFACE, fg=MUTED,
                 font=("Segoe UI", 10)).grid(row=1, column=0)
        tk.Label(arena, text="Máquina", bg=SURFACE, fg=MUTED,
                 font=("Segoe UI", 10)).grid(row=1, column=2)

        # Mensaje resultado
        self.lbl_resultado = tk.Label(self, text="", bg=BG, fg=TEXT,
                                      font=("Segoe UI", 13, "bold"), pady=6)
        self.lbl_resultado.pack(fill="x", padx=20)

        # Botones de elección
        btn_frame = tk.Frame(self, bg=BG)
        btn_frame.pack(pady=10)
        for codigo, (nombre, icono) in enumerate(
                zip(["Piedra", "Papel", "Tijera"],
                    ["✊", "✋", "✌️"]), start=1):
            self._boton_eleccion(btn_frame, icono, nombre, codigo)

        # Historial
        tk.Label(self, text="Historial", bg=BG, fg=MUTED,
                 font=("Segoe UI", 10)).pack(anchor="w", padx=24, pady=(10, 2))

        hist_frame = tk.Frame(self, bg=SURFACE, padx=10, pady=6)
        hist_frame.pack(fill="x", padx=20)
        self.historial_frame = hist_frame

        # Botón nueva partida
        btn_reset = tk.Button(self, text="Nueva partida", bg=SURFACE, fg=TEXT,
                              font=("Segoe UI", 11), relief="flat", cursor="hand2",
                              activebackground=BTN_PRESS, activeforeground="#fff",
                              bd=0, padx=16, pady=8,
                              command=self._reset)
        btn_reset.pack(pady=14)

    def _score_card(self, parent, label, valor):
        f = tk.Frame(parent, bg=SURFACE, padx=22, pady=10)
        f.pack(side="left", padx=8)
        tk.Label(f, text=label, bg=SURFACE, fg=MUTED,
                 font=("Segoe UI", 10)).pack()
        lbl = tk.Label(f, text=valor, bg=SURFACE, fg=TEXT,
                       font=("Segoe UI", 22, "bold"))
        lbl.pack()
        return lbl

    def _boton_eleccion(self, parent, icono, nombre, codigo):
        frame = tk.Frame(parent, bg=SURFACE, padx=18, pady=14, cursor="hand2")
        frame.pack(side="left", padx=8)

        tk.Label(frame, text=icono, bg=SURFACE, fg=TEXT,
                 font=("Segoe UI Emoji", 32)).pack()
        tk.Label(frame, text=nombre, bg=SURFACE, fg=MUTED,
                 font=("Segoe UI", 10)).pack()

        frame.bind("<Button-1>", lambda e, c=codigo: self._jugar(c))
        for w in frame.winfo_children():
            w.bind("<Button-1>", lambda e, c=codigo: self._jugar(c))

        frame.bind("<Enter>", lambda e, f=frame: f.config(bg=BTN_HOVER) or
                   [w.config(bg=BTN_HOVER) for w in f.winfo_children()])
        frame.bind("<Leave>", lambda e, f=frame: f.config(bg=SURFACE) or
                   [w.config(bg=SURFACE) for w in f.winfo_children()])

    # ── Lógica ─────────────────────────────────────────────────────────────────
    def _jugar(self, eleccion):
        res = self.juego.jugar(eleccion)
        if res is None:
            return
        yo, maq, resultado = res

        self.lbl_icono_j.config(text=ICONOS[yo])
        self.lbl_icono_m.config(text=ICONOS[maq])
        self._actualizar_marcador()

        if resultado == "win":
            msg = f"¡Ganaste!  {NOMBRES[yo]} vence a {NOMBRES[maq]}"
            self.lbl_resultado.config(text=msg, bg=WIN_BG, fg=WIN_FG)
        elif resultado == "lose":
            msg = f"Perdiste.  {NOMBRES[maq]} vence a {NOMBRES[yo]}"
            self.lbl_resultado.config(text=msg, bg=LOSE_BG, fg=LOSE_FG)
        else:
            msg = f"¡Empate!  Ambos eligieron {NOMBRES[yo]}"
            self.lbl_resultado.config(text=msg, bg=TIE_BG, fg=TIE_FG)

        self._agregar_historial(self.juego.ronda - 1, yo, maq, resultado)

        if self.juego.terminado:
            self._mostrar_final()

    def _actualizar_marcador(self):
        j = self.juego
        self.lbl_marc_j.config(text=str(j.v_jugador))
        self.lbl_marc_e.config(text=str(j.empates))
        self.lbl_marc_m.config(text=str(j.v_maquina))
        ronda_actual = min(j.ronda, MAX_RONDAS)
        self.lbl_ronda.config(
            text=f"Ronda {ronda_actual} de {MAX_RONDAS}" if not j.terminado
            else "Partida terminada")

    def _agregar_historial(self, n_ronda, yo, maq, resultado):
        oc = {"win": "Ganaste", "lose": "Perdiste", "tie": "Empate"}
        fg = {"win": WIN_FG, "lose": LOSE_FG, "tie": TIE_FG}
        row = tk.Frame(self.historial_frame, bg=SURFACE)
        row.pack(fill="x", pady=1)
        tk.Label(row, text=f"Ronda {n_ronda}:  {ICONOS[yo]} vs {ICONOS[maq]}",
                 bg=SURFACE, fg=TEXT, font=("Segoe UI", 10)).pack(side="left")
        tk.Label(row, text=oc[resultado],
                 bg=SURFACE, fg=fg[resultado],
                 font=("Segoe UI", 10, "bold")).pack(side="right")

    def _mostrar_final(self):
        gf = self.juego.ganador_final()
        if gf == "win":
            msg = f"GANASTE LA PARTIDA  {self.juego.v_jugador}-{self.juego.v_maquina}"
            bg, fg = WIN_BG, WIN_FG
        elif gf == "lose":
            msg = f"La máquina ganó  {self.juego.v_maquina}-{self.juego.v_jugador}"
            bg, fg = LOSE_BG, LOSE_FG
        else:
            msg = f"Partida empatada  {self.juego.v_jugador}-{self.juego.v_maquina}"
            bg, fg = TIE_BG, TIE_FG
        self.lbl_resultado.config(text=msg, bg=bg, fg=fg,
                                  font=("Segoe UI", 14, "bold"))

    def _reset(self):
        self.juego.reset()
        self.lbl_icono_j.config(text="❓")
        self.lbl_icono_m.config(text="❓")
        self.lbl_resultado.config(text="", bg=BG, font=("Segoe UI", 13, "bold"))
        for w in self.historial_frame.winfo_children():
            w.destroy()
        self._actualizar_marcador()


# ─── Arrancar ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = App()
    app.mainloop()
