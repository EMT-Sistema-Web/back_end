from datetime import timezone
from django.shortcuts import render

def valid_date(self):
        if self.tipo == 'aluguel' and self.data_fim:
            if self.end_date < timezone.now():
                self.valid = False  # Se a data fim for no passado, o contrato é inválido
                self.save()

def valid_contract(self):
    if not self.cliente or not self.maquina:
        self.valido = False
    self.validar_data()  # Verifica a data de expiração
    self.save()
    
def __str__(self):
        return f"Contrato {self.tipo} - Cliente: {self.cliente.nome} - Máquina: {self.maquina.nome}"

