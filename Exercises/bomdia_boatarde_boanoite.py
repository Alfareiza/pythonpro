from datetime import datetime
time = datetime.now()
def calcula_sauacao(time):
    if 0 < time < 12:
        return f'Bom dia - {time}:'
    elif 12 >= time < 18:
        return f'Boa tarde - {time}:'
    else:
        return f'Boa Noite - {time}:'

print(calcula_sauacao(time.hour),time.minute)