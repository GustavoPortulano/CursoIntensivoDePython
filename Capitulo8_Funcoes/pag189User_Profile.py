print("\n25 de agosto de 2026. Terça-feria. Madrugada fria.")
print("Página 189 - Usando argumentos nomeados arbitrários.")

def build_profile(first, last, **user_info):
    """Constrói um dicionário """
    """Uso de dois asteristicos"""
    """O parâmetro arbitrário deve ser o último"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value 
    return profile
"""Nome do dicionário: user_profile. A ele é atribuida a função buid_profile."""
user_profile = build_profile('albert','eisntein',location='princeton',field='physics')
"""Para imprimir o dicionário, usar o nome a ele atrubuido."""
print(user_profile)