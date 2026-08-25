print("\n25 de agosto de 2026. Terça-feira. Tarde quente.")
print("8.13 - Perfil do usuário: Comece com uma cópia de user_profile.py, da página 210. " \
"\nCrie um perfil seu chamadndo build_profile(), usando seu primeiro nome e sobrenome," \
"\nalém de três outros pares chave-valor que o descrevam.")

def user_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile

print("Perfil do usuário:")
perfil_usuario = user_profile('leto','atreides',planeta_sede='caladan',
                                casa='atreides',titulo_nobresa='duque')
print(perfil_usuario)
print("\n")
