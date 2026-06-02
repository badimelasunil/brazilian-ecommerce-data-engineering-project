
# IN cleaned_customers.py CSV FILE HAVING SHORT_CUT STATE NAMES
# SO WE CAN CREATE SEPERETE state_lookup table  save to cleaned_data folder
#ONCE SEE CUSTOMER CSV FILE YOU CAN UNDERSTAND 

import pandas as pd

# State mapping dictionary
state_mapping = {
    "SP": "Sao Paulo",
    "RJ": "Rio de Janeiro",
    "MG": "Minas Gerais",
    "PR": "Parana",
    "RS": "Rio Grande do Sul",
    "SC": "Santa Catarina",
    "BA": "Bahia",
    "GO": "Goias",
    "ES": "Espirito Santo",
    "DF": "Distrito Federal",
    "PE": "Pernambuco",
    "CE": "Ceara",
    "PA": "Para",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "RN": "Rio Grande do Norte",
    "PB": "Paraiba",
    "AL": "Alagoas",
    "PI": "Piaui",
    "MA": "Maranhao",
    "SE": "Sergipe",
    "TO": "Tocantins",
    "RO": "Rondonia",
    "AM": "Amazonas",
    "AP": "Amapa",
    "AC": "Acre",
    "RR": "Roraima"
}

# Create lookup DataFrame
state_lookup = pd.DataFrame(
    list(state_mapping.items()),
    columns=["state_code", "state_name"]
)

# Print table
print(state_lookup)

# Save CSV
state_lookup.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\lookup_tables\state_lookup.csv",
    index=False
)

print("Lookup table created successfully!")



# py create_state_lookup.py
