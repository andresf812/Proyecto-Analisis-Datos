# limpieza.py
def limpiar_texto(valor):
    if isinstance(valor, str):
        return (
            valor.strip()
            .lower()
            .replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
            .replace("ñ", "n")
        )
    return valor

def normalizar_dataset(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("á", "a")
        .str.replace("é", "e")
        .str.replace("í", "i")
        .str.replace("ó", "o")
        .str.replace("ú", "u")
        .str.replace("ñ", "n")
    )
    df = df.applymap(limpiar_texto)

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace(' ', '_')

    return df
