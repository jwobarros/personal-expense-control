from re import sub

def snake_case(text):
    """
    Converte uma string para snake case.
    """
    # Remove espaços em branco, hífens e sublinhares no início e no final da string
    text = text.strip().strip('-').strip('_')
    
    # Substitui caracteres especiais por sublinhares
    text = sub(r'[^a-zA-Z0-9]+', '_', text)
    
    # Substitui letras maiúsculas por minúsculas (exceto a primeira letra)
    text = sub(r'([a-z0-9])([A-Z])', r'\1_\2', text).lower()
    
    return text