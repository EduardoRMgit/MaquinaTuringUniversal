{
    "Estados": ["q0", "q1", "qf"],
    "Entrada": ["0", "1"],
    "Cinta": [["0"], ["1"], ["_"]],
    "Inicial": "q0",
    "Blanco": "_",
    "Finales": ["qf"],
    "Transiciones": [
                    ["q0", ["0"], "q1", ["1"], "R"],
                    ["q1", ["1"], "q0", ["0"], "R"],
                    ["q1", ["_"], "qf", ["_"], "R"]
    ]
}
